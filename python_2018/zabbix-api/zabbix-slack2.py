import json
import requests
from zabbix.api  import ZabbixAPI as ZA #zabbixのpythonモジュール

#zabbixの管理ホスト情報取得
def ZA_func():
    url = 'http://192.168.46.220/zabbix/api_jsonrpc.php'
    user = 'Admin'
    pwd = 'zabbix'

    #baseの情報
    zapi = ZA(url=url, user=user, password=pwd)

    #ホスト一覧
    res1= zapi.host.get()
    #ホストインターフェース情報一覧
    res3= zapi.hostinterface.get()

    #ホスト一覧
    #print('------------------------------host------------------------------\n')
    hostdict={} #この空dictにforで抽出したidとホスト名のマッピングを格納
    for i in res1:
            hostdict.update({i['hostid']:i['host']}) #hostlistにkey hostの値を追加
    #print(hostdict)
    #print('\n\n')


    #インターフェース情報
    intfdict={} #この空dictにforで抽出したidとipアドレスのマッピングを格納
    for i in res3:
            intfdict.update({i['hostid']:i['ip']}) #hostlistにkey hostの値を追加
    #print(intfdict)
    #print('\n\n')


    #hostdictとintfdictのkeyの値同じだったら、host名とIPの組み合わせを作る
    hostip=[] #host名とIPを格納を空リスト
    listnum=0 #for文でlistの中を指定する際に使う
    #host名が格納された辞書のkeyとIPが格納された辞書のkeyが同一
    if hostdict.keys() == intfdict.keys():
        #host名が格納した辞書のvalueをfor
        for i in hostdict.values():
            #host名が格納した辞書のvalueを空リストに追加。host名毎にリストは分ける
            hostip.append([i])
            #print(hostip)
        #IPが格納された辞書のvalueをfor
        for x in intfdict.values():
            #IPが格納した辞書のvalueを先ほどhost名を追加リストに追加これにより[[host1name,host1ip], [host2name,host2name]
            #というlistが作成される。
            hostip[listnum].append(x)
            #listnumに1を追加することで、次のforの際は別のvalueを追加できる
            listnum = listnum+1
            #print(hostip)

    f = open('zabbix.txt', 'w')  # invというファイル名でカレントディレクトリに保存
    f.write(str(hostip))
    f.close()

    #return
    return hostip

#zabbixの管理ホスト情報に変更があったらslackで通知
def SL_func(zavalue):
    li = [['Zabbix server', '127.0.0.1'], ['R1', '10.0.0.100']]
    #print(zavalue)
    if li != zavalue:
        for i in zavalue:
            if i[1] == '10.0.0.100':
                inv = {"CSR1000v": {"hosts": [i[1]], "vars": {"ansible_ssh_pass": "cisco", "ansible_ssh_user": "cisco", "enable_pass": "cisco"}}}

        f = open('csr1000v-inv', 'w')  # invというファイル名でカレントディレクトリに保存
        f.write(str(inv))
        f.close()
        #slackAPI用URL
        url = 'https://hooks.slack.com/services/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'
        #slack通知するユーザ名(任意)
        user = 'zabbixインフォメーション'
        #slackで通知するメッセージ内容
        message = 'zabbixの登録ホストに変更が発生しました。\nインベントリファイルを作成しました。'
        payload = {'text': message, 'username': user}
        #slack_post
        res_mes = requests.post(url, data=json.dumps(payload))

ZA_func()
SL_func(ZA_func())
