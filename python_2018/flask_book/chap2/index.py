from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #urlのルートを示す。URLのルートにアクセスしたら、下記の処理
def index():
    return render_template('index.html', message='ちんぽ') #base.html.html内のmessage変数の値

if __name__=='__main__':
    app.debug = True
    app.run()