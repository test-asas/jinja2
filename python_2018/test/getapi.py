#mainの関数で各機能の関数を呼び出し、ZabbixAPIからAnsibleAPIを生成する
from zabbix.api import ZabbixAPI as ZA  # zabbixのpythonモジュール
import json
import requests
import ipaddress
import os


url = 'http://192.168.46.220/zabbix/api_jsonrpc.php'
user = 'Admin'
pwd = 'zabbix'

# baseの情報
zapi = ZA(url=url, user=user, password=pwd)

#APIを抽出する関数
def host_func():
    # ホスト一覧
    hostget = zapi.host.get()
    # ホストインターフェース情報一覧
    intfget = zapi.hostinterface.get()
    #上記hostget,intfgetをreturnする
    return hostget, intfget


#抽出したAPIから必要データを取り出す関数
#引数はhost_funcのリターン値
def data_func(API):
    hostapi = API[0] #API情報からホスト名が含まれる情報を抽出
    intfapi = API[1] #API情報からインターフェース(IP)が含まれる情報を抽出

    #ホスト一覧
    hostdict={} #この空dictにforで抽出したidとホスト名のマッピングを格納
    for i in hostapi:
            hostdict.update({i['hostid']:i['host']}) #hostlistにkey hostの値を追加
    #print(hostdict)
    #print('\n\n')


    #インターフェース情報
    intfdict={} #この空dictにforで抽出したidとipアドレスのマッピングを格納
    for i in intfapi:
            intfdict.update({i['hostid']:i['ip']}) #hostlistにkey hostの値を追加
    #print(intfdict)
    #print('\n\n')

    return hostdict, intfdict #加工したデータをリターン



#取り出した必要データを掛け合わせる
#引数はdata_funcのリターン値
def comp_func(dictdata):
    hostdict = dictdata[0] #API情報からhost名情報を抽出
    intfdisc = dictdata[1] #API情報からインターフェース情報を抽出

    #hostdictとintfdictのkeyの値同じだったら、host名とIPの組み合わせを作る
    hostip=[] #host名とIPを格納を空リスト
    listnum=0 #for文でlistの中を指定する際に使う
    #host名が格納された辞書のkeyとIPが格納された辞書のkeyが同一
    if hostdict.keys() == intfdisc.keys():
        #host名が格納した辞書のvalueをfor
        for hostname in hostdict.values():
            #host名が格納した辞書のvalueを空リストに追加。host名毎にリストは分ける
            hostip.append([hostname])
            #print(hostip)
        #IPが格納された辞書のvalueをfor
        for ipaddr in intfdisc.values():
            #IPが格納した辞書のvalueを先ほどhost名を追加リストに追加これにより[[host1name,host1ip], [host2name,host2name]
            #というlistが作成される。
            hostip[listnum].append(ipaddr)
            #listnumに1を追加することで、次のforの際は別のvalueを追加できる
            listnum = listnum+1
    return hostip


#ansibleのinventoryファイルを生成する
#引数はcomp_funcのリターン値
def inv_func(comp_va):
    #カレントディレクトリ
    directory = os.listdir('.')
    #比較対象となる過去の抽出データ
    # zabbix.txtがカレントディレクトリにあるか確認ある場合は、下記の処理
    if 'zabbix.txt' in directory:
        hikakudata = ''
        f = open('zabbix.txt', 'r')  # zabbix.txtというファイル名でカレントディレクトリに保存
        for i in f:
            hikakudata = hikakudata + i #hikakudataにzabbix.txtの内容を入れる
        f.close()
        str_comp = str(comp_va) #上記の読み込んだファイルは文字列型なので新規抽出データも合わせる
        nw_seg = ipaddress.ip_network('10.0.0.0/25') #CSR1000vのアドレスレンジを定義
        #もし、過去の監視対象と現在の監視対象に差分があったら
        if hikakudata != str_comp:
            #現在の監視対象データをファイル保存する
            f = open('zabbix.txt', 'w')  # zabbix.txtというファイル名で新たにカレントディレクトリに保存
            f.write(str(comp_va))
            f.close()
            #現在の監視対象データをforする
            for ip in comp_va:
            #listの2番目にIP情報があるので、それをipaddressモジュールを用いてipアドレス化
                comp_ip = ipaddress.ip_address(ip[1])
                #もし、今回取得したアドレス情報がnw_segのレンジ内だったら
                if comp_ip in nw_seg:
                    #新たなAnsibleインベントリファイルを作る
                    inv = {"CSR1000v": {"hosts": [ip[1]], "vars": {"ansible_ssh_pass": "cisco", "ansible_ssh_user": "cisco", "enable_pass": "cisco"}}}
            output = json.dumps(inv, sort_keys=True, indent=2)  # jsonに変換
            f = open('csr1000v-inv', 'w')  # invというファイル名でカレントディレクトリに保存
            f.write(output)
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


    if 'zabbix.txt' not in directory:
        f = open('zabbix.txt', 'w')  # invというファイル名でカレントディレクトリに保存
        f.write(str(comp_va))
        f.close()
        nw_seg = ipaddress.ip_network('10.0.0.0/25')
        for ip in comp_va:
            # listの2番目にIP情報があるので、それをipaddressモジュールを用いてipアドレス化
            comp_ip = ipaddress.ip_address(ip[1])
            # もし、今回取得したアドレス情報がnw_segのレンジ内だったら
            if comp_ip in nw_seg:
                # 新たなAnsibleインベントリファイルを作る
                inv = {"CSR1000v": {"hosts": [ip[1]], "vars": {"ansible_ssh_pass": "cisco", "ansible_ssh_user": "cisco",
                                                               "enable_pass": "cisco"}}}
        output = json.dumps(inv, sort_keys=True, indent=2)  # jsonに変換
        f = open('csr1000v-inv', 'w')  # invというファイル名でカレントディレクトリに保存
        f.write(output)
        f.close()
        url = 'https://hooks.slack.com/services/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'
        #slack通知するユーザ名(任意)
        user = 'zabbixインフォメーション'
        #slackで通知するメッセージ内容
        message = 'zabbixの登録ホストファイルを作成しました。\nインベントリファイルを作成しました。'
        payload = {'text': message, 'username': user}
        #slack_post
        res_mes = requests.post(url, data=json.dumps(payload))


API = host_func() #APIを抽出する関数(上記の関数)
DATA = data_func(API) #抽出したAPIから必要データを取り出す関数
COMP = comp_func(DATA) #取り出した必要データを掛け合わせ、ファイルに保存する関数
INV = inv_func(COMP) #掛け合わせたデータが前回取得したデータと差分があるか確認する関数