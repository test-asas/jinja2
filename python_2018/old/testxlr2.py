import xlrd
import sys
import json

#XLS_FILEPATH = '/path/to/host-list.xlsx'

book = xlrd.open_workbook('test.xlsx')  # エクセルファイルからBook作成
sheet = book.sheet_by_name(u"Sheet1")  # Sheet1を指定

hosts = {}  # ホスト一覧を格納する
host_vars = {}  # ホスト毎の属性を格納する

# ここから各行をループします
for row in range(1, sheet.nrows):  # nrowsは行数を取得。excel2行目からsheet1のデータがあるところまでをforする
    if sheet.cell(row,0).value != '': # rowが空白行でない場合
        group = sheet.cell(row,0).value  # 1列目のセルを取得
    if group not in hosts: #hostsの中に上記グループが含まれていない場合
        hosts[group] = {'hosts': []} # hostsにgroupの値を追加({'web':{'hosts': []})
    hostname = sheet.cell(row,1).value  # 1列目のセルを取得
    hosts[group]["hosts"].append(hostname)  # 'hosts': []の中に取得した1列目の値を入れる

    host_vars[hostname] = {  # ホスト毎の属性に格納
        'ansible_ssh_host': sheet.cell(row,2).value,
        'ansible_ssh_user': sheet.cell(row,3).value,
        }

output = json.dumps(hosts, sort_keys=True, indent=2)
print(output)

f = open('inv','w')
f.write(output)
f.close()
