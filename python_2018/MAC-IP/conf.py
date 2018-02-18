import csv
from jinja2 import Template, Environment, FileSystemLoader
from datetime import datetime


#'テンプレートファイル配置ディレクトリのルート
FSL = FileSystemLoader('.')
env = Environment(loader=FSL)

#dhcpとsshのconfファイルのテンプレート
template_dhcp = env.get_template('dhcp_template')
template_ssh = env.get_template('ssh_template')

#ファイル名に利用する日付
basename = datetime.now().strftime('%Y%m%d-%H%M')

#テンプレートに反映される各変数パラメータ用空リスト
rtnum = []
mgmtip = []
ifmac = []

#インベントリCSVファイルから各変数パラメータを作るため、CSVを読み込む
with open('invfile.csv') as f:
    reader = csv.reader(f) #csvファイルオブジェクトを読み込む
    for row in reader: #csvオブジェクトをrowに入れforする
        rtnum.append(row[0]) #リストに1列目の値を追記
        ifmac.append(row[1]) #リストに2列目の値を追記
        mgmtip.append(row[2]) #リストに3列目の値を追記

#print(rtnum)
#print(ifmac)
#print(mgmtip)

#templateの変数はdict形式だが、それをまとめるリストが必要になるため、ここで作成
li = []

for x, y, z  in zip(rtnum, ifmac, mgmtip): #list3つをそれぞれx,y,zに入れforする
    dict = {} #行ごとにdictが必要になるため、ここで空のdictを作成
    dict['rtnum'] = x #dictにkey rtnum value xを追記
    dict['ifmac'] = y #dictにkey ifmac value yを追記
    dict['mgmtip'] = z #dictにkey mgmtip value zを追記
    li.append(dict) #リストにdictを追加。この状態でjinjaテンプレートの変数値として利用可能になる

#print(li)


#templateからconfファイルを作成。機器台数分confファイルを生成するため、for文を利用する
for merge in li: #変数値のネタとなるリストをmergeに入れfor
    dhcp_output = template_dhcp.render(merge) #forされた値をtemplate_dhcpに入れる
    with open('dhcp_conf'+'_'+basename, 'w') as f: #dhcp_conf_作成時刻というファイル名でconfファイルを作る
        f.write(dhcp_output) #dhcp_outputの内容を書き込む
    ssh_output = template_ssh.render(merge) #forされた値をtemplate_sshに入れる
    with open('ssh_conf_R'+merge['rtnum'], 'w') as f: #ssh_conf_ルータ名というファイル名でconfファイルを作る
        f.write(ssh_output) #ssh_outputの内容を書き込む
