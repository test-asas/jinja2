import xlrd
import sys
import json

#XLS_FILEPATH = '/path/to/host-list.xlsx'

book = xlrd.open_workbook('test.xlsx')  # エクセルファイルからBook作成
sheet = book.sheet_by_name(u"Sheet1")  # Sheet1を指定

hosts = {}  # ホスト一覧を格納する
host_vars = {}  # ホスト毎の属性を格納する

# ここから各行をループします
for row in range(1, sheet.nrows):  # 1からなのは最初のタイトル行をスキップするため
    if sheet.cell(row,0).value:
        group = sheet.cell(row,0).value  # 1列目のグループを取得

    if group not in hosts:
        hosts[group] = {"hosts": []}
    hostname = sheet.cell(row,1).value  # ホスト名取得
    hosts[group]["hosts"].append(hostname)  # ホスト一覧に追加
    print(hosts)

    host_vars[hostname] = {  # ホスト毎の属性に格納
        'ansible_ssh_host': sheet.cell(row,2).value,
        'ansible_ssh_user': sheet.cell(row,3).value,
        }

#if sys.argv[1] == '--list':  # --listが付いているならホスト一覧を
#    print (json.dumps(hosts, sort_keys=True, indent=2))
#else:
#    hostname = sys.argv[2]   # それ以外であれば、当該ホストの属性を表示
#    print (json.dumps(host_vars[hostname], sort_keys=True, indent=2))
