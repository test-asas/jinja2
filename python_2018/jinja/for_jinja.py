#外部のテンプレートファイルパターン
from jinja2 import Template, Environment, FileSystemLoader

#'テンプレートファイル配置ディレクトリのルート
env = Environment(loader=FileSystemLoader('.'))
#'sample.tpl'はテンプレートファイル.テンプレート化しているっぽい
tpl = env.get_template('for_jinja.tpl')

foods = []
foods.append({'name':u'ラーメン', 'price':400})
foods.append({'name':u'焼き飯',   'price':500})
foods.append({'name':u'天津飯',   'price':600})
print(foods)

disp_text = tpl.render({'shop':u'悟空軒', 'foods':foods})
print(disp_text)