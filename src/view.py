# coding: utf-8
# 日本語表示の文字化け防止

from flask import Flask, render_template

# Flask クラスをインスタンス化
app = Flask(__name__)

# --- View側の設定 ---
# ルートディレクトリにアクセスした場合の挙動
@app.route('/')
# def以下がアクセス後の操作
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

# view.py の役割は URL にアクセスが有ればこのファイルが必要というような条件にあったファイルを紐付ける



