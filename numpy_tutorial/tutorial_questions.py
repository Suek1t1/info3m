import numpy as np

#　ベクトル演習の演習
# (1) 5個の要素を持つ列ベクトルを作成
a = np.ones((5, 1))
print("(1)の答え:\n", a)

# (2) 2番目の要素を 3.14 に更新
a[2, 0] = 3.14
print("\n(2)の答え:\n", a)

# (3) ベクトルを複製し、転置して行ベクトルに変換
a_row = a.copy().T
print("\n(3)の答え:\n", a_row)

# (4) 列ベクトルと行ベクトルの内積を求める
dot_product = np.dot(a_row, a)
print("\n(4)の答え:\n", dot_product)

# (5) np.random.randを用いて、10個の要素を持つ列ベクトルを作成
b = np.random.rand(10, 1)
print("\n(5)の答え:\n", b)

# 行列演算の演習行列演算の演習
# (6) 平均10、標準偏差2の正規分布に基づく2行5列の行列を作成
c = np.random.normal(10, 2, (2, 5))
print("(6)の答え:\n", c)

# (7) 2列目の要素を抜き出す
col2 = c[:, 1]
print("\n(7)の答え:\n", col2)

# (8) 3列目と4列目の要素を抜き出す
cols34 = c[:, 2:4]
print("\n(8)の答え:\n", cols34)

# (9) 5行2列の行列を用意し、(6)の行列との積を求める
m2 = np.random.rand(5, 2)
matrix_prod = np.dot(c, m2)
print("\n(9)の答え:\n", matrix_prod)