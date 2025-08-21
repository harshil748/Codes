"""
Assignment 1: Implement Logistic Regression or Decision Tree without using scikit-learn
Show how the pruning works in the case of DT and Random forest algorithms.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import math
import random

# ==================== LOGISTIC REGRESSION IMPLEMENTATION ====================


class LogisticRegression:
    def __init__(self, learning_rate=0.01, max_iterations=1000):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        """Sigmoid activation function"""
        z = np.clip(z, -500, 500)  # Prevent overflow
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        """Train the logistic regression model"""
        # Initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Gradient descent
        for i in range(self.max_iterations):
            # Linear model
            linear_model = np.dot(X, self.weights) + self.bias

            # Predictions using sigmoid
            y_predicted = self.sigmoid(linear_model)

            # Compute cost (log loss)
            cost = self.compute_cost(y, y_predicted)

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            if i % 100 == 0:
                print(f"Cost after iteration {i}: {cost}")

    def compute_cost(self, y_true, y_pred):
        """Compute logistic regression cost function"""
        # Avoid log(0) by adding small epsilon
        epsilon = 1e-15
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    def predict(self, X):
        """Make predictions on new data"""
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self.sigmoid(linear_model)
        predictions = [1 if i > 0.5 else 0 for i in y_predicted]
        return np.array(predictions)

    def predict_proba(self, X):
        """Return prediction probabilities"""
        linear_model = np.dot(X, self.weights) + self.bias
        return self.sigmoid(linear_model)


# ==================== DECISION TREE IMPLEMENTATION ====================


class Node:
    def __init__(self):
        self.feature = None
        self.threshold = None
        self.left = None
        self.right = None
        self.value = None
        self.samples = 0


class DecisionTree:
    def __init__(self, max_depth=5, min_samples_split=2, min_samples_leaf=1):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.root = None

    def entropy(self, y):
        """Calculate entropy of a dataset"""
        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))
        return entropy

    def information_gain(self, X_column, y, threshold):
        """Calculate information gain for a split"""
        # Parent entropy
        parent_entropy = self.entropy(y)

        # Split the data
        left_mask = X_column <= threshold
        right_mask = X_column > threshold

        if len(y[left_mask]) == 0 or len(y[right_mask]) == 0:
            return 0

        # Calculate weighted entropy of children
        n = len(y)
        n_left, n_right = len(y[left_mask]), len(y[right_mask])
        entropy_left, entropy_right = self.entropy(y[left_mask]), self.entropy(
            y[right_mask]
        )
        child_entropy = (n_left / n) * entropy_left + (n_right / n) * entropy_right

        # Information gain
        return parent_entropy - child_entropy

    def best_split(self, X, y):
        """Find the best feature and threshold to split on"""
        best_gain = -1
        best_feature = None
        best_threshold = None

        n_features = X.shape[1]

        for feature in range(n_features):
            X_column = X[:, feature]
            thresholds = np.unique(X_column)

            for threshold in thresholds:
                gain = self.information_gain(X_column, y, threshold)

                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold, best_gain

    def build_tree(self, X, y, depth=0):
        """Recursively build the decision tree"""
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        # Stopping criteria
        if (
            depth >= self.max_depth
            or n_labels == 1
            or n_samples < self.min_samples_split
        ):
            leaf_value = self.most_common_label(y)
            node = Node()
            node.value = leaf_value
            node.samples = n_samples
            return node

        # Find best split
        best_feature, best_threshold, best_gain = self.best_split(X, y)

        if best_gain == 0:
            leaf_value = self.most_common_label(y)
            node = Node()
            node.value = leaf_value
            node.samples = n_samples
            return node

        # Create internal node
        node = Node()
        node.feature = best_feature
        node.threshold = best_threshold
        node.samples = n_samples

        # Split the data
        left_mask = X[:, best_feature] <= best_threshold
        right_mask = X[:, best_feature] > threshold

        # Check minimum samples per leaf
        if (
            np.sum(left_mask) < self.min_samples_leaf
            or np.sum(right_mask) < self.min_samples_leaf
        ):
            leaf_value = self.most_common_label(y)
            node.value = leaf_value
            return node

        # Recursively build left and right subtrees
        node.left = self.build_tree(X[left_mask], y[left_mask], depth + 1)
        node.right = self.build_tree(X[right_mask], y[right_mask], depth + 1)

        return node

    def most_common_label(self, y):
        """Return the most common class label"""
        counter = Counter(y)
        return counter.most_common(1)[0][0]

    def fit(self, X, y):
        """Train the decision tree"""
        self.root = self.build_tree(X, y)

    def predict_sample(self, x, node):
        """Predict a single sample"""
        if node.value is not None:
            return node.value

        if x[node.feature] <= node.threshold:
            return self.predict_sample(x, node.left)
        else:
            return self.predict_sample(x, node.right)

    def predict(self, X):
        """Make predictions on multiple samples"""
        return np.array([self.predict_sample(x, self.root) for x in X])

    def prune(self, X_val, y_val):
        """Post-pruning using validation set"""
        self._prune_node(self.root, X_val, y_val)

    def _prune_node(self, node, X_val, y_val):
        """Recursively prune nodes"""
        if node.value is not None:  # Leaf node
            return

        # Recursively prune children
        if node.left:
            self._prune_node(node.left, X_val, y_val)
        if node.right:
            self._prune_node(node.right, X_val, y_val)

        # Calculate accuracy before pruning
        before_accuracy = self._calculate_accuracy(X_val, y_val)

        # Temporarily convert to leaf
        original_left = node.left
        original_right = node.right
        original_feature = node.feature
        original_threshold = node.threshold

        # Convert to leaf with most common class
        mask = (
            X_val[:, node.feature] <= node.threshold
            if node.feature is not None
            else np.ones(len(X_val), dtype=bool)
        )
        relevant_labels = y_val[mask] if len(y_val[mask]) > 0 else y_val
        node.value = self.most_common_label(relevant_labels)
        node.left = None
        node.right = None
        node.feature = None
        node.threshold = None

        # Calculate accuracy after pruning
        after_accuracy = self._calculate_accuracy(X_val, y_val)

        # Keep pruning if accuracy doesn't decrease
        if after_accuracy < before_accuracy:
            # Restore original node
            node.left = original_left
            node.right = original_right
            node.feature = original_feature
            node.threshold = original_threshold
            node.value = None

    def _calculate_accuracy(self, X, y):
        """Calculate accuracy on validation set"""
        predictions = self.predict(X)
        return np.mean(predictions == y)


# ==================== RANDOM FOREST IMPLEMENTATION ====================


class RandomForest:
    def __init__(
        self,
        n_trees=10,
        max_depth=5,
        min_samples_split=2,
        min_samples_leaf=1,
        max_features=None,
    ):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.trees = []

    def bootstrap_sample(self, X, y):
        """Create bootstrap sample"""
        n_samples = X.shape[0]
        indices = np.random.choice(n_samples, size=n_samples, replace=True)
        return X[indices], y[indices]

    def fit(self, X, y):
        """Train random forest"""
        self.trees = []
        n_features = X.shape[1]

        if self.max_features is None:
            self.max_features = int(np.sqrt(n_features))

        for _ in range(self.n_trees):
            # Create bootstrap sample
            X_sample, y_sample = self.bootstrap_sample(X, y)

            # Select random features
            feature_indices = np.random.choice(
                n_features, size=self.max_features, replace=False
            )
            X_sample = X_sample[:, feature_indices]

            # Train decision tree
            tree = DecisionTree(
                max_depth=self.max_depth,
                min_samples_split=self.min_samples_split,
                min_samples_leaf=self.min_samples_leaf,
            )
            tree.fit(X_sample, y_sample)

            # Store tree and its feature indices
            self.trees.append((tree, feature_indices))

    def predict(self, X):
        """Make predictions using majority voting"""
        tree_predictions = []

        for tree, feature_indices in self.trees:
            X_subset = X[:, feature_indices]
            pred = tree.predict(X_subset)
            tree_predictions.append(pred)

        # Majority voting
        tree_predictions = np.array(tree_predictions)
        predictions = []

        for i in range(X.shape[0]):
            votes = tree_predictions[:, i]
            prediction = Counter(votes).most_common(1)[0][0]
            predictions.append(prediction)

        return np.array(predictions)


# ==================== DEMONSTRATION AND TESTING ====================


def generate_sample_data():
    """Generate sample data for testing"""
    np.random.seed(42)

    # Generate linearly separable data
    n_samples = 1000
    X = np.random.randn(n_samples, 2)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)

    return X, y


def demonstrate_pruning():
    """Demonstrate pruning in decision trees"""
    print("=== Decision Tree Pruning Demonstration ===")

    # Generate sample data
    X, y = generate_sample_data()

    # Split data
    split_idx = int(0.7 * len(X))
    X_train, X_val = X[:split_idx], X[split_idx:]
    y_train, y_val = y[:split_idx], y[split_idx:]

    # Train decision tree without pruning
    dt_no_prune = DecisionTree(max_depth=10, min_samples_split=2)
    dt_no_prune.fit(X_train, y_train)

    # Calculate accuracy before pruning
    accuracy_before = np.mean(dt_no_prune.predict(X_val) == y_val)
    print(f"Accuracy before pruning: {accuracy_before:.4f}")

    # Train decision tree with pruning
    dt_with_prune = DecisionTree(max_depth=10, min_samples_split=2)
    dt_with_prune.fit(X_train, y_train)
    dt_with_prune.prune(X_val, y_val)

    # Calculate accuracy after pruning
    accuracy_after = np.mean(dt_with_prune.predict(X_val) == y_val)
    print(f"Accuracy after pruning: {accuracy_after:.4f}")


def main():
    """Main function to demonstrate all implementations"""
    print("Assignment 1: Logistic Regression and Decision Tree Implementation\n")

    # Generate sample data
    X, y = generate_sample_data()

    # Split data into train and test
    split_idx = int(0.8 * len(X))
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]

    print("Dataset shape:", X.shape)
    print("Training samples:", len(X_train))
    print("Test samples:", len(X_test))
    print()

    # ==================== LOGISTIC REGRESSION ====================
    print("=== Logistic Regression ===")
    lr = LogisticRegression(learning_rate=0.1, max_iterations=1000)
    lr.fit(X_train, y_train)

    lr_predictions = lr.predict(X_test)
    lr_accuracy = np.mean(lr_predictions == y_test)
    print(f"Logistic Regression Accuracy: {lr_accuracy:.4f}")
    print()

    # ==================== DECISION TREE ====================
    print("=== Decision Tree ===")
    dt = DecisionTree(max_depth=5, min_samples_split=10, min_samples_leaf=5)
    dt.fit(X_train, y_train)

    dt_predictions = dt.predict(X_test)
    dt_accuracy = np.mean(dt_predictions == y_test)
    print(f"Decision Tree Accuracy: {dt_accuracy:.4f}")
    print()

    # ==================== RANDOM FOREST ====================
    print("=== Random Forest ===")
    rf = RandomForest(n_trees=10, max_depth=5, min_samples_split=10, min_samples_leaf=5)
    rf.fit(X_train, y_train)

    rf_predictions = rf.predict(X_test)
    rf_accuracy = np.mean(rf_predictions == y_test)
    print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
    print()

    # ==================== PRUNING DEMONSTRATION ====================
    demonstrate_pruning()

    # ==================== VISUALIZATION ====================
    plt.figure(figsize=(12, 4))

    # Plot original data
    plt.subplot(1, 3, 1)
    plt.scatter(
        X_test[y_test == 0, 0],
        X_test[y_test == 0, 1],
        c="red",
        label="Class 0",
        alpha=0.7,
    )
    plt.scatter(
        X_test[y_test == 1, 0],
        X_test[y_test == 1, 1],
        c="blue",
        label="Class 1",
        alpha=0.7,
    )
    plt.title("Original Data")
    plt.legend()

    # Plot Logistic Regression predictions
    plt.subplot(1, 3, 2)
    plt.scatter(
        X_test[lr_predictions == 0, 0],
        X_test[lr_predictions == 0, 1],
        c="red",
        label="Predicted 0",
        alpha=0.7,
    )
    plt.scatter(
        X_test[lr_predictions == 1, 0],
        X_test[lr_predictions == 1, 1],
        c="blue",
        label="Predicted 1",
        alpha=0.7,
    )
    plt.title(f"Logistic Regression\nAccuracy: {lr_accuracy:.4f}")
    plt.legend()

    # Plot Decision Tree predictions
    plt.subplot(1, 3, 3)
    plt.scatter(
        X_test[dt_predictions == 0, 0],
        X_test[dt_predictions == 0, 1],
        c="red",
        label="Predicted 0",
        alpha=0.7,
    )
    plt.scatter(
        X_test[dt_predictions == 1, 0],
        X_test[dt_predictions == 1, 1],
        c="blue",
        label="Predicted 1",
        alpha=0.7,
    )
    plt.title(f"Decision Tree\nAccuracy: {dt_accuracy:.4f}")
    plt.legend()

    plt.tight_layout()
    plt.savefig(
        "/Users/harshilpatel/CODE/Major/assignment_01_results.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.show()

    print("\n=== Summary ===")
    print(f"Logistic Regression Accuracy: {lr_accuracy:.4f}")
    print(f"Decision Tree Accuracy: {dt_accuracy:.4f}")
    print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
    print(
        "\nPruning helps prevent overfitting in decision trees by removing nodes that don't improve performance on validation data."
    )


if __name__ == "__main__":
    main()
