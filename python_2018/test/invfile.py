import json
import requests
import ipaddress

def inv_func(comp_va):
    #比較対象となる過去の抽出データ
    hikakudata = ''
    f = open('zabbix.txt', 'r')  # invというファイル名でカレントディレクトリに保存
    for i in f:
        hikakudata = hikakudata + i
    f.close()
    #上記の読み込んだファイルは文字列型なので新規抽出データも合わせる
    str_comp = str(comp_va)
    #CSR1000vのアドレスレンジを定義
    nw_seg = ipaddress.ip_network('10.0.0.0/25')

    #もし、過去の監視対象と現在の監視対象に差分があったら
    if hikakudata != str_comp:
        #現在の監視対象データをファイル保存する
        f = open('zabbix.txt', 'w')  # invというファイル名でカレントディレクトリに保存
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
