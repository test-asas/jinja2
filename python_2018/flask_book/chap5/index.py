from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/') #urlのルートを示す。URLのルートにアクセスしたら、下記の処理
def index():
    return render_template('index.html') #index.htmlを読み込み、index pageと表示する

@app.route('/send', methods=['GET', 'POST']) #methodを定義している
def send():
    if request.method == 'POST': #もしメソッドがPOSTだったら
        img_file = request.files['img_file']
        img_file.save('./uploads/'+img_file.filename)
        return render_template('index.html') #index.htmlを読み込み
    else:
        return redirect(url_for('index'))  # base.html.html内のmessage変数の値

if __name__=='__main__':
    app.debug = True
    app.run()
