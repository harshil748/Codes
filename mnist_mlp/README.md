# MNIST Handwritten Digit Recognition (MLP)

This project trains a Multi-Layer Perceptron (Artificial Neural Network) to classify handwritten digits (0–9) from the MNIST dataset.

## Features

- Load MNIST via `tf.keras.datasets` or from raw IDX gzip files downloaded with `kagglehub`.
- Preprocessing: normalization (0–1) and flattening of 28x28 images.
- Configurable hidden layer architecture + optional dropout.
- Training with Adam optimizer and categorical crossentropy.
- Plots of training loss & accuracy.
- Confusion matrix & classification report.
- Example grids of correctly and incorrectly classified images.
- Simple hyperparameter exploration mode.

## Installation

Create (optional) virtual environment then install requirements:

```bash
pip install -r requirements.txt
```

TensorFlow may leverage hardware acceleration depending on your local setup.

## Using Kaggle Version of Dataset

```python
import kagglehub
path = kagglehub.dataset_download("hojjatk/mnist-dataset")
print(path)
```

Then pass the resulting path to the script with `--kaggle-dir <path>`.
The folder must contain the four gzip files:

- `train-images-idx3-ubyte.gz`
- `train-labels-idx1-ubyte.gz`
- `t10k-images-idx3-ubyte.gz`
- `t10k-labels-idx1-ubyte.gz`

If omitted, the script will fall back to the built-in Keras MNIST loader.

## Running Training

Basic run (default architecture 256-128):

```bash
python train_mnist_mlp.py --epochs 10 --batch-size 128
```

With custom architecture & dropout:

```bash
python train_mnist_mlp.py --hidden 512 256 128 --dropout 0.2 --epochs 15
```

Using Kaggle dataset:

```bash
python train_mnist_mlp.py --kaggle-dir /path/to/kaggle/mnist --epochs 10
```

Hyperparameter exploration (tests a few presets):

```bash
python train_mnist_mlp.py --explore --epochs 8
```

Outputs are written under `outputs/<layer_config>/` including:

- `training_curves.png`
- `confusion_matrix.png`
- `classification_report.txt`
- `correct_examples.png` / `incorrect_examples.png`
- `model_summary.txt`

## Discussion of Design Choices

- **Depth & Width:** More/larger layers can increase capacity, improving accuracy up to a point, but may overfit and increase training time. Typical sweet spot for MNIST MLPs: 1–3 hidden layers with 128–512 units.
- **Activation (ReLU):** Chosen for efficient gradient propagation; avoids vanishing gradients common with sigmoids on deeper nets.
- **Output (Softmax):** Produces probability distribution over 10 digit classes.
- **Loss (Categorical Crossentropy):** Standard for multi-class classification with one-hot labels.
- **Optimizer (Adam):** Adaptive learning rate, generally converges faster than vanilla SGD on this task.
- **Normalization:** Scaling pixel values to [0,1] stabilizes and speeds up training.
- **Dropout:** Regularization option to mitigate overfitting (try 0.1–0.3 if validation accuracy lags behind training accuracy).
- **Batch Size:** 64–256 commonly works; larger batches may slightly reduce generalization but speed up iterations.

## Potential Extensions

- Add early stopping & learning rate scheduling.
- Add L2 weight decay.
- Compare with convolutional neural network (CNN) baseline.
- Implement k-fold cross validation.
- Save best model (checkpoint) and support reload/inference script.

## License

Educational use.
