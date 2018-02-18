import textfsm #textfsmをインポート
import csv #CSVにパースした結果を保存

#パース対象ファイルを開く
with open('show inventroy.txt') as f:
    inventory_text = f.read()

#該当するNTC-Templateを開く
with open('cisco_ios_show_inventory.template') as f:
    table = textfsm.TextFSM(f)
    result = table.ParseText(inventory_text)

print(result)

#出力結果をCSVに保存
with open('inventory.csv', 'w', newline='') as f: # Windowsの場合、newline=''が必要
    w = csv.writer(f)
    w.writerow(table.header) #テーブルヘッダーとして、tableの値を利用する
    w.writerow(result[0]) #配列の配列(二次元list)の場合は、writerowsを利用する