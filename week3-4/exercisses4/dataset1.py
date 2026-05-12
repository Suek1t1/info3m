import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# フォント設定
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
plt.rcParams['font.family'] = font_prop.get_name()


# ーーー　演習1.1: 真の関数の定義　ーーー
def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

# ーーー　演習1.2: 観測点と新地の準備　ーーー
def generate_datasets(samples=20, seed=0):     # デフォルトのサンプル数は20,シードは0
    np.random.seed(seed)
    x = np.random.uniform(-1, 1, samples)
    y = true_function(x)
    return x, y

def true_definition(x):

    x_samples, y_samples = generate_datasets()

    df = pd.DataFrame({'観測点': x_samples, '真の値': y_samples})

    x_line = np.linspace(-1, 1, 100)
    y_line = true_function(x_line)

    plt.figure(figsize=(8, 5))
    plt.plot(x_line, y_line, label='True Function') # 線グラフ
    plt.scatter(df['観測点'], df['真の値'], color='blue', label='真値')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    plt.show()


# ーーー　演習1.3: ノイズを加えた観測値の準備　ーーー
def noise_definition(x):
    x_line = np.linspace(-1, 1, 100)
    y_line = true_function(x_line)
    x_samples, y_samples = generate_datasets()

    np.random.seed(0) # 再現性のためにシードを固定
    noise_raw = np.random.normal(loc=0.0, scale=np.sqrt(2.0), size=20)  # 平均0、分散2の正規分布からノイズを20個生成
    noise = noise_raw * 0.5

    df = pd.DataFrame({'観測点': x_samples, '真の値': y_samples})

    # 真の値にノイズを足して「実際に観測されるデータ」を作る
    df['観測値'] = df['真の値'] + noise

    plt.plot(x_line, y_line, label='True Function')
    plt.scatter(df['観測点'], df['真の値'], color='blue', label='真値', marker='o')       # 真の値
    plt.scatter(df['観測点'], df['観測値'], color='red', label='観測値', marker='^')    # 観測値（ノイズあり）

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    plt.show()


# ーーー　演習1.4: データセットのファイル出力　ーーー
def save_dataset(df):
    df.to_csv('ex1.tsv', sep='\t', index=False)

# ーーー　演習1.5: データセットのファイル読み込み　ーーー
def load_dataset():
    df_loaded = pd.read_csv('ex1.tsv', sep='\t')
    print(df_loaded.head())

