# learn1.py

import dataset1
from sklearn import linear_model

def main():
    # --- 演習1.7: データセットの読み込み ---
    df = dataset1.load_dataset('ex1.tsv')

    # --- 演習1.8: 線形回帰モデルの準備 ---
    model = linear_model.LinearRegression()
    print(model)
