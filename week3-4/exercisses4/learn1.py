# learn1.py

import dataset1
from sklearn import linear_model


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

main()