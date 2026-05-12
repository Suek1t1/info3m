import numpy as np
import datasets
import regression
import matplotlib.pyplot as plt

X, Y = datasets.load_nonlinear_example1()
ex_X = datasets.polynomial2_features(X)
model = regression.LinearRegression()
model.fit(ex_X, Y)

samples = np.arange(0, 4, 0.1)
X_samples = np.c_[np.ones(samples.shape[0]), samples]
ex_X_samples = datasets.polynomial2_features(X_samples)

plt.scatter(X[:,1], Y)
plt.plot(samples, model.predict(ex_X_samples))
plt.show()