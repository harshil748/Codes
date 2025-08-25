import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate dataset (y = 3x + 5 + noise)
np.random.seed(42)
X = np.linspace(0, 10, 100)
y = 3 * X + 5 + np.random.randn(100) * 2

# Initialize parameters
w, b = 0.0, 0.0
alpha = 0.01
epochs = 100


def compute_gradients(X, y, w, b):
    n = len(X)
    y_pred = w * X + b
    dw = (-2 / n) * np.sum(X * (y - y_pred))
    db = (-2 / n) * np.sum(y - y_pred)
    return dw, db


# Step 2: Batch Gradient Descent
loss_bgd = []
w_bgd, b_bgd = 0.0, 0.0

for epoch in range(epochs):
    dw, db = compute_gradients(X, y, w_bgd, b_bgd)
    w_bgd -= alpha * dw
    b_bgd -= alpha * db
    y_pred = w_bgd * X + b_bgd
    loss = np.mean((y - y_pred) ** 2)
    loss_bgd.append(loss)

# Step 3: Stochastic Gradient Descent
loss_sgd = []
w_sgd, b_sgd = 0.0, 0.0

for epoch in range(epochs):
    for i in range(len(X)):
        xi, yi = X[i], y[i]
        y_pred = w_sgd * xi + b_sgd
        dw = -2 * xi * (yi - y_pred)
        db = -2 * (yi - y_pred)
        w_sgd -= alpha * dw
        b_sgd -= alpha * db
    y_pred_all = w_sgd * X + b_sgd
    loss = np.mean((y - y_pred_all) ** 2)
    loss_sgd.append(loss)

# Step 4: Compare Loss Curves
plt.plot(range(epochs), loss_bgd, label="Batch GD")
plt.plot(range(epochs), loss_sgd, label="Stochastic GD")
plt.xlabel("Epochs")
plt.ylabel("MSE Loss")
plt.legend()
plt.show()

print(f"Final Weights (BGD): w={w_bgd:.2f}, b={b_bgd:.2f}")
print(f"Final Weights (SGD): w={w_sgd:.2f}, b={b_sgd:.2f}")
