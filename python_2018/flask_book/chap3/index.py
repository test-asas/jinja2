from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #urlのルートを示す。URLのルートにアクセスしたら、下記の処理
def index():
    return render_template('index.html', message='index page') #index.htmlを読み込み、index pageと表示する

@app.route('/hello/') #ルート以下の階層で/hello/にアクセスしたら、下記の処理
def hello():
    return render_template('hello.html', message='hello world!') #hello.htmlを読み込み、hello world!と表示する


if __name__=='__main__':
    app.debug = True
    app.run()