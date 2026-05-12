import datasets

X, Y = datasets.load_nonlinear_example1()
ex_X = datasets.polynomial2_features(X)
print("ex_X:")
print(ex_X)
print("Y:") 
print(Y)

'''
X, Y = datasets.load_nonlinear_example1()
ex_X = datasets.polynomial2_features(X)

import regression
model = regression.LinearRegression()
model.fit(ex_X, Y)
pred = model.predict(ex_X,Y)
print(model.theta)
print(model.predict(ex_X))
print(model.score(ex_X, Y))
'''
