import importlib
import datasets
import regression

importlib.reload(regression)

X, Y = datasets.load_linear_example()

model = regression.LinearRegression()
model.fit(X, Y)

print(model.theta)