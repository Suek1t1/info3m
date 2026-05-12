import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# フォント設定
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
try:
    font_prop = font_manager.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()
except:
    pass


# ーーー　演習1.1: 真の関数の定義　ーーー
def true_function(x):
    """真の関数"""
    return np.sin(np.pi * x * 0.8) * 10


# ーーー　演習1.2: 観測点と真値の準備　ーーー
def generate_datasets(samples=20, seed=0):
    """ランダムな観測点と、それに対応する真値を返す"""
    np.random.seed(seed)
    x = np.random.uniform(-1, 1, samples)
    y = true_function(x)
    return x, y


# ーーー　演習1.3: ノイズを加えた観測値の準備（＆DataFrame作成） ーーー
def create_dataframe(samples=20, seed=0):
    """観測点、真値、観測値（ノイズ入り）をまとめたDataFrameを作成して返す"""
    x_samples, y_samples = generate_datasets(samples, seed)
    
    # ノイズの生成
    np.random.seed(seed) 
    noise_raw = np.random.normal(loc=0.0, scale=np.sqrt(2.0), size=samples)
    noise = noise_raw * 0.5
    
    # DataFrameの作成
    df = pd.DataFrame({
        '観測点': x_samples, 
        '真値': y_samples,
        '観測値': y_samples + noise
    })
    
    return df


# ーーー　演習1.4: データセットのファイル出力　ーーー
def save_dataset(df, filename='ex1.tsv'):
    """DataFrameをTSV形式で保存する"""
    df.to_csv(filename, sep='\t', index=False)


# ーーー　演習1.5: データセットのファイル読み込み　ーーー
def load_dataset(filename='ex1.tsv'):
    """TSVファイルを読み込んでDataFrameとして返す"""
    df_loaded = pd.read_csv(filename, sep='\t')
    return df_loaded 


# ーーー　おまけ：グラフ描画用の関数　ーーー
def plot_dataset(df):
    """データフレームを受け取り、グラフを描画する"""
    x_line = np.linspace(-1, 1, 100)
    y_line = true_function(x_line)

    plt.figure(figsize=(8, 5))
    plt.plot(x_line, y_line, label='True Function')
    plt.scatter(df['観測点'], df['真値'], color='blue', label='真値', marker='o')
    
    # '観測値'列が存在する場合のみ描画
    if '観測値' in df.columns:
        plt.scatter(df['観測点'], df['観測値'], color='red', label='観測値', marker='^')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
