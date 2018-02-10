import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/') #urlのルートを示す。URLのルートにアクセスしたら、下記の処理
def index():
    return render_template('index.html') #index.htmlを読み込み、index pageと表示する

@app.route('/send', methods=['GET', 'POST']) #methodを定義している
def send():
    if request.method == 'POST': #もしメソッドがPOSTだったら
        img_file = request.files['img_file']
        if img_file and allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return render_template('index.html') #index.htmlを読み込み
        else:
            return '"<p>許可されてない<p>"'
    else:
        return redirect(url_for('index'))  # base.html.html内のmessage変数の値

if __name__=='__main__':
    app.debug = True
    app.run()
