import os
import gzip
import argparse
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

# Lazy import TensorFlow to allow help/--info without heavy startup


def lazy_tf_import():
    import tensorflow as tf  # noqa: F401

    return tf


def load_mnist_keras():
    tf = lazy_tf_import()
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    return (x_train, y_train), (x_test, y_test)


def parse_idx_images(filepath: Path) -> np.ndarray:
    with gzip.open(filepath, "rb") as f:
        data = f.read()
    magic = int.from_bytes(data[0:4], "big")
    if magic != 2051:
        raise ValueError(f"Invalid magic number {magic} for images file {filepath}")
    n_images = int.from_bytes(data[4:8], "big")
    n_rows = int.from_bytes(data[8:12], "big")
    n_cols = int.from_bytes(data[12:16], "big")
    images = np.frombuffer(data, dtype=np.uint8, offset=16).reshape(
        n_images, n_rows, n_cols
    )
    return images


def parse_idx_labels(filepath: Path) -> np.ndarray:
    with gzip.open(filepath, "rb") as f:
        data = f.read()
    magic = int.from_bytes(data[0:4], "big")
    if magic != 2049:
        raise ValueError(f"Invalid magic number {magic} for labels file {filepath}")
    n_items = int.from_bytes(data[4:8], "big")
    labels = np.frombuffer(data, dtype=np.uint8, offset=8)
    if labels.shape[0] != n_items:
        raise ValueError("Label count mismatch")
    return labels


def load_mnist_kaggle(kaggle_dir: Path):
    # Expect the four gzip files present in kaggle_dir
    files = {
        "train_images": "train-images-idx3-ubyte.gz",
        "train_labels": "train-labels-idx1-ubyte.gz",
        "test_images": "t10k-images-idx3-ubyte.gz",
        "test_labels": "t10k-labels-idx1-ubyte.gz",
    }
    paths = {k: kaggle_dir / v for k, v in files.items()}
    for p in paths.values():
        if not p.exists():
            raise FileNotFoundError(f"Expected file not found: {p}")
    x_train = parse_idx_images(paths["train_images"])
    y_train = parse_idx_labels(paths["train_labels"])
    x_test = parse_idx_images(paths["test_images"])
    y_test = parse_idx_labels(paths["test_labels"])
    return (x_train, y_train), (x_test, y_test)


def preprocess(x_train, x_test):
    # Normalize to [0,1] and flatten
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0
    n_train = x_train.shape[0]
    n_test = x_test.shape[0]
    x_train = x_train.reshape(n_train, -1)
    x_test = x_test.reshape(n_test, -1)
    return x_train, x_test


def build_mlp(input_dim: int, hidden_layers, dropout=0.0):
    tf = lazy_tf_import()
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=(input_dim,)))
    for units in hidden_layers:
        model.add(tf.keras.layers.Dense(units, activation="relu"))
        if dropout > 0:
            model.add(tf.keras.layers.Dropout(dropout))
    model.add(tf.keras.layers.Dense(10, activation="softmax"))
    return model


def plot_history(history, outdir: Path):
    outdir.mkdir(parents=True, exist_ok=True)
    hist = history.history
    epochs = range(1, len(hist["loss"]) + 1)

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(epochs, hist["loss"], label="train")
    if "val_loss" in hist:
        plt.plot(epochs, hist["val_loss"], label="val")
    plt.title("Loss")
    plt.xlabel("Epoch")
    plt.legend()

    plt.subplot(1, 2, 2)
    acc_key = "accuracy" if "accuracy" in hist else "acc"
    val_acc_key = "val_accuracy" if "val_accuracy" in hist else "val_acc"
    plt.plot(epochs, hist[acc_key], label="train")
    if val_acc_key in hist:
        plt.plot(epochs, hist[val_acc_key], label="val")
    plt.title("Accuracy")
    plt.xlabel("Epoch")
    plt.legend()

    plt.tight_layout()
    plt.savefig(outdir / "training_curves.png", dpi=150)
    plt.close()


def visualize_predictions(model, x_test, y_test, outdir: Path, n=24):
    tf = lazy_tf_import()
    outdir.mkdir(parents=True, exist_ok=True)
    # x_test here is flattened normalized; reshape back
    side = int(np.sqrt(x_test.shape[1]))
    x_images = x_test.reshape(-1, side, side)
    probs = model.predict(x_test, verbose=0)
    preds = probs.argmax(axis=1)

    correct_idx = np.where(preds == y_test)[0]
    incorrect_idx = np.where(preds != y_test)[0]

    def plot_examples(indices, fname):
        sel = np.random.choice(indices, size=min(n, len(indices)), replace=False)
        cols = 6
        rows = int(np.ceil(len(sel) / cols))
        plt.figure(figsize=(cols * 1.5, rows * 1.5))
        for i, idx in enumerate(sel):
            plt.subplot(rows, cols, i + 1)
            plt.imshow(x_images[idx], cmap="gray")
            plt.axis("off")
            plt.title(f"p:{preds[idx]} t:{y_test[idx]}", fontsize=8)
        plt.tight_layout()
        plt.savefig(outdir / fname, dpi=150)
        plt.close()

    if len(correct_idx) > 0:
        plot_examples(correct_idx, "correct_examples.png")
    if len(incorrect_idx) > 0:
        plot_examples(incorrect_idx, "incorrect_examples.png")


def evaluate(model, x_test, y_test, outdir: Path):
    tf = lazy_tf_import()
    outdir.mkdir(parents=True, exist_ok=True)
    probs = model.predict(x_test, verbose=0)
    preds = probs.argmax(axis=1)
    cm = confusion_matrix(y_test, preds)
    report = classification_report(y_test, preds, digits=4)

    with open(outdir / "classification_report.txt", "w") as f:
        f.write(report)

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Confusion Matrix")
    plt.savefig(outdir / "confusion_matrix.png", dpi=150)
    plt.close()
    return report


def main():
    parser = argparse.ArgumentParser(description="Train an MLP on MNIST")
    parser.add_argument(
        "--kaggle-dir",
        type=str,
        default=None,
        help="Path to kagglehub downloaded MNIST gzip files",
    )
    parser.add_argument(
        "--hidden", type=int, nargs="*", default=[256, 128], help="Hidden layer sizes"
    )
    parser.add_argument("--dropout", type=float, default=0.0)
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--output", type=str, default="outputs")
    parser.add_argument("--val-split", type=float, default=0.1)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--explore",
        action="store_true",
        help="Run simple hyperparameter exploration over predefined configs",
    )

    args = parser.parse_args()
    np.random.seed(args.seed)

    if args.kaggle_dir:
        kaggle_dir = Path(args.kaggle_dir)
        (x_train, y_train), (x_test, y_test) = load_mnist_kaggle(kaggle_dir)
    else:
        (x_train, y_train), (x_test, y_test) = load_mnist_keras()

    x_train, x_test = preprocess(x_train, x_test)

    tf = lazy_tf_import()
    y_train_cat = tf.keras.utils.to_categorical(y_train, 10)
    y_test_cat = tf.keras.utils.to_categorical(y_test, 10)

    outdir = Path(args.output)
    outdir.mkdir(exist_ok=True, parents=True)

    def train_and_eval(hidden_layers):
        model = build_mlp(x_train.shape[1], hidden_layers, dropout=args.dropout)
        optimizer = tf.keras.optimizers.Adam(learning_rate=args.lr)
        model.compile(
            optimizer=optimizer, loss="categorical_crossentropy", metrics=["accuracy"]
        )
        history = model.fit(
            x_train,
            y_train_cat,
            validation_split=args.val_split,
            epochs=args.epochs,
            batch_size=args.batch_size,
            verbose=2,
        )
        subdir = outdir / ("_".join(map(str, hidden_layers)))
        subdir.mkdir(exist_ok=True, parents=True)
        plot_history(history, subdir)
        visualize_predictions(model, x_test, y_test, subdir)
        rep = evaluate(model, x_test, y_test, subdir)
        with open(subdir / "model_summary.txt", "w") as f:
            model.summary(print_fn=lambda line: f.write(line + "\n"))
        return model, rep

    if args.explore:
        configs = [args.hidden, [512, 256, 128], [512, 256], [256, 256, 128]]
        summaries = []
        for cfg in configs:
            print(f"\n=== Training config: {cfg} ===")
            _, rep = train_and_eval(cfg)
            summaries.append((cfg, rep.split("\n")[-2]))  # crude overall accuracy line
        with open(outdir / "exploration_summary.txt", "w") as f:
            for cfg, line in summaries:
                f.write(f"{cfg}: {line}\n")
    else:
        train_and_eval(args.hidden)


if __name__ == "__main__":
    main()
