import numpy as np

# 行列の作成
a = np.array([[1,2,3], [4,5,6]])
print(a)
print(type(a))
print(a.shape)

#行の参照
print("--- 行の参照 ---")
print(a[0])

#列の参照
print("--- 列の参照 ---")
print(a[:,0])

#スライス指定も可能
print("--- スライス指定 ---")
print(a[0:2])  #行の0から1までを参照

print(a[:,0:2])    #列の0から1までを参照

# 「行列 + 1」は全要素に対する和を実行
print("\n--- 行列 + 1 ---")
print(a + 1)

# *演算子も同様。
print("\n--- 行列 * 2 ---")
print(a * 2)

#行列演算ではない！
print("\n--- 行列 * 行列 ---")
print(a * a)

#転置行列
print("\n--- 転置行列 ---")
print(a.T)

#内積を求めるにはdot関数を使う
print("\n--- 内積 ---")
print(np.dot(a, a.T))

#逆行列
print("\n--- 逆行列 ---")
print(np.linalg.inv(np.dot(a, a.T)))

#ゼロ行列、1行列、対角行列
print("\n--- ゼロ行列、1行列、対角行列 ---")
print(np.zeros((2,3)))

print(np.ones((2,3)))

print(np.eye(3))


#特定範囲内で幅を指定してサンプル点を用意。
#例えば、
# 「y=x**2」のグラフを描画したいとき、
#　定義域「-10〜10の範囲で0.1刻みでサンプル点を用意」みたいなときに便利。
print("\n--- 特定範囲内のサンプル点 ---")
print(np.arange(0, 1, 0.3))

#np.arangeで始点、刻み幅を省略すると0から指定個数の整数を用意。
print("\n--- 指定個数の整数 ---")
print(np.arange(8))

#行列の形を変形できる。
print("\n--- 行列の形を変形 ---")
print(np.reshape(np.arange(6),(2,3)))

#刻み幅はどうでも良いからサンプル数を指定したい場合に便利。
print("\n--- 等間隔なサンプル点 ---")
print(np.linspace(0, 2, 3))

#行列を結合できる。
#縦方向に結合
a = np.array([[1,2,3], [4,5,6]])
b = np.array([[7,8,9], [10,11,12]])
print("\n--- 行列の結合 ---")
print(np.r_[a, b])

#横方向に結合
print("\n--- 横方向に結合 ---")
print(np.c_[a, b])