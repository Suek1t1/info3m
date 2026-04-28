import importlib
import week3.datasets as datasets
import week3.regression as regression

importlib.reload(regression)

X, Y = datasets.load_linear_example()

model = regression.LinearRegression()
model.fit(X, Y)

# testing
print(model.theta)          # ver2
print(model.predict(X))     # ver3
print(model.score(X, Y))    # ver4

