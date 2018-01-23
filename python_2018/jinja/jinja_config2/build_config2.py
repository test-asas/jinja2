from jinja2 import Template, Environment, FileSystemLoader

#'テンプレートファイル配置ディレクトリのルート
FSL = FileSystemLoader('.')
env = Environment(loader=FSL)

#'sample.tpl'はテンプレートファイル.テンプレート化しているっぽい
template = env.get_template('template2')

#必要なインタフェース分rangeを記載
scl = range(1,11)
#dictをまとめるリスト
li = []
keys = ('id', 'intf_ip', 'loop_ip')
iden_k = 'id'
intf_k = 'intf_ip'
loop_k = 'loop_ip'
host = 'RT-A'
snmp_ip = '10.0.0.220'

for iden in scl:
    iden_v = str(iden)
    intf_v = '172.16.' + str(iden) + '.1'
    loop_v = '192.168.0.' + str(iden)
    iden_dict = {} #forのサイクルの中で空dictを定義する必要がある
    iden_dict[iden_k] = iden_v #iden_dictにkey iden_k、vaule iden_vを追加
    iden_dict[intf_k] = intf_v #iden_dictにkey intf_k、vaule intf_vを追加
    iden_dict[loop_k] = loop_v #iden_dictにkey loop_k、vaule loop_vを追加
    li.append(iden_dict) #リストにiden_dictを追加。この状態でjinjaテンプレートの変数値として利用可能になる
print(li)

#template内の変数値にdataの内容を出力
output = template.render({'hostname': host, 'li': li, 'snmp_ip':snmp_ip })
#print(output)
f = open('RT-A.txt', 'w')
f.write(output)
f.close()