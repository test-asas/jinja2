#外部のテンプレートファイルパターン
from jinja2 import Template, Environment, FileSystemLoader

#'テンプレートファイル配置ディレクトリのルート
env = Environment(loader=FileSystemLoader('.'))
#'sample.tpl'はテンプレートファイル.テンプレート化しているっぽい
template = env.get_template('sample.tpl')
#template内の変数値の定義
data = {'name': 'Kuro', 'lang': 'Python'}
#template内の変数値にdataの内容を出力
disp_text = template.render(data)
print(disp_text)