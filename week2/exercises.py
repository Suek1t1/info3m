import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures

X = np.array([[0.0], [2.0], [3.9], [4.0]])
Y = np.array([4.0, 0.0, 3.0, 2.0])

poly = PolynomialFeatures(degree=2)
X2 = poly.fit_transform(X)
print(X2)

# alphaの値
clf0 = Ridge(alpha=0.0)
clf01 = Ridge(alpha=0.1)
clf05 = Ridge(alpha=0.5)
clf1 = Ridge(alpha=1.0)
clf10 = Ridge(alpha=10.0)

clf0.fit(X2, Y)
clf01.fit(X2, Y)
clf05.fit(X2, Y)
clf1.fit(X2, Y)
clf10.fit(X2, Y)

# 描画
samples_x = np.arange(0, 4.1, 0.1)
samples_x2 = poly.fit_transform(samples_x.reshape(len(samples_x), 1))
samples_y0 = clf0.predict(samples_x2)
samples_y01 = clf01.predict(samples_x2)
samples_y05 = clf05.predict(samples_x2)
samples_y1 = clf1.predict(samples_x2)
samples_y10 = clf10.predict(samples_x2)

plt.plot(samples_x, samples_y0, label='alpha = 0' , color='blue')
plt.plot(samples_x, samples_y01, label='alpha = 0.1' , color='yellow')
plt.plot(samples_x, samples_y05, label='alpha = 0.5' , color='green')
plt.plot(samples_x, samples_y1, label='alpha = 1.0' , color='red')
plt.plot(samples_x, samples_y10, label='alpha = 10.0' , color='cyan')

plt.scatter(X, Y, label='data set')
plt.legend()
plt.show()