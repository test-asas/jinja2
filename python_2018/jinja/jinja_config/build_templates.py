from jinja2 import Template, Environment, FileSystemLoader
import csv

# テンプレートファイル格納場所の環境設定
FSL = FileSystemLoader('.')
env = Environment(loader=FSL)


template = env.get_template('config_template.txt')

f = open('inventory.csv', 'rt') #カレントディレクトリにある「example.csv」をオープン
r = csv.DictReader(f) #オブジェクトを読み込む
for i in r:
    print(i)
    output = template.render(i)
    config_filename = i['hostname'] + '-config' #コンフィグファイル名の定義
    ff = open(config_filename, 'w') #出力されたコンフィグをファイルとして保存
    ff.write(output)
    ff.close()
    #print(output)
f.close()
