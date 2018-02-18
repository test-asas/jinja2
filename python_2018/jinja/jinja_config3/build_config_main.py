from jinja2 import Template, Environment, FileSystemLoader
import inv

#'テンプレートファイル配置ディレクトリのルート
FSL = FileSystemLoader('.')
env = Environment(loader=FSL)

#'sample.tpl'はテンプレートファイル.テンプレート化しているっぽい
template = env.get_template('template2')

#dictをまとめるリスト
li = []

for iden,intf,loop in zip(inv.iden_v,inv.intf_v,inv.loop_v):
    iden_dict = {}
    iden_dict[inv.iden_k] = iden #iden_dictにkey iden_k、vaule iden_vを追加
    iden_dict[inv.intf_k] = intf #iden_dictにkey intf_k、vaule intf_vを追加
    iden_dict[inv.loop_k] = loop #iden_dictにkey loop_k、vaule loop_vを追加
    li.append(iden_dict) #リストにiden_dictを追加。この状態でjinjaテンプレートの変数値として利用可能になる

print (li)
#template内の変数値にdataの内容を出力
output = template.render({'hostname': inv.host, 'li': li, 'snmp_ip':inv.snmp_ip })
#print(output)
f = open('RT-A.txt', 'w')
f.write(output)
f.close()