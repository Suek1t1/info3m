import importlib
import datasets as datasets
import regression as regression

X, Y = datasets.load_nonlinear_example1()
ex_X = datasets.polynomial2_features(X)
model = regression.RidgeRegression(alpha=10.0)
print(model.alpha)
print(model.fit(ex_X, Y))
print(model.theta)
print(model.score(ex_X, Y))