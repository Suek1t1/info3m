# learn1.py

import dataset1
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np 


def main():
    # --- 演習1.7: データセットの読み込み ---
    df = dataset1.load_dataset('ex1.tsv')

    # --- 演習1.8: 線形回帰モデルの準備 ---
    model = linear_model.LinearRegression()
    # print(model)


    # --- 演習1.9: フィッティング ---
    X = df[['観測点']]
    y = df['観測値']

    x_train = X[:16]
    x_test = X[16:]
    y_train = y[:16]
    y_test = y[16:]

    print('訓練データの観測点数:\n', len(x_train))
    print('訓練データの観測値数:\n', len(y_train))

    model.fit(x_train, y_train)
    print('回帰係数:', model.coef_)
    print('切片:', model.intercept_)

    # --- 演習1.10: テスト用データセットに対する予測 ---
    y_pred = model.predict(x_test)
    print('テストデータの観測値:\n', y_test.values)
    print('テストデータの予測値:\n', y_pred)

    # --- 演習1.11: モデルの可視化 ---
    plt.scatter(x_train, y_train, color='blue', label='訓練データ')
    plt.plot(x_train, model.predict(x_train), color='red', label='回帰直線')
    plt.xlabel('観測点')
    plt.ylabel('観測値')
    plt.legend()
    plt.show()
    plt.savefig('week3-4/exercises4/ex1.10.png')
main()