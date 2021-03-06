from jinja2 import Template, Environment, FileSystemLoader

#'テンプレートファイル配置ディレクトリのルート
FSL = FileSystemLoader('.')
env = Environment(loader=FSL)

#'sample.tpl'はテンプレートファイル.テンプレート化しているっぽい
template = env.get_template('template')

#必要なインタフェース分rangeを記載
scl = range(1,3)
#dictをまとめるリストfor mergeの時に勝手に取れる
li = []
keys = ('id', 'intf_ip', 'loop_ip')
iden_k = 'id'
intf_k = 'intf_ip'
loop_k = 'loop_ip'

for iden in scl:
    iden_v = str(iden)
    intf_v = '10.0.' + str(iden) + '.1'
    loop_v = '192.168.0.' + str(iden)
    iden_dict = {} #forのサイクルの中で空dictを定義する必要がある
    iden_dict[iden_k] = iden_v #iden_dictにkey iden_k、vaule iden_vを追加
    iden_dict[intf_k] = intf_v #iden_dictにkey intf_k、vaule intf_vを追加
    iden_dict[loop_k] = loop_v #iden_dictにkey loop_k、vaule loop_vを追加
    print(iden_dict)
    li.append(iden_dict) #リストにiden_dictを追加
print(li)

#template内の変数値にdataの内容を出力
for merge in li:
    output = template.render(merge)
    print(output)
