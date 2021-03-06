import json
import requests
from zabbix.api  import ZabbixAPI as ZA #zabbixのpythonモジュール

def ZA_func():
    url = 'http://192.168.46.220/zabbix/api_jsonrpc.php'
    user = 'Admin'
    pwd = 'zabbix'

    #baseの情報
    zapi = ZA(url=url, user=user, password=pwd)

    #ホスト一覧
    res1= zapi.host.get()
    #グループ一覧
    res2= zapi.hostgroup.get()
    #ホストインターフェース情報一覧
    res3= zapi.hostinterface.get()

    res1_dump=json.dumps(res1, indent=2) #pythonオブジェクトをjsonに変換
    #ホスト一覧
    print(res1)
    print('------------------------------host------------------------------\n'
          +res1_dump)
    print('''
    
    
    ''')

    res2_dump=json.dumps(res2, indent=2) #pythonオブジェクトをjsonに変換
    #グループ一覧
    print(res2)
    print('------------------------------group------------------------------\n'
          +res2_dump)
    print('''
    
    
    ''')

    res3_dump=json.dumps(res3, indent=2)
    #インターフェース情報
    print(res3)
    print('------------------------------interface------------------------------\n'
          +res3_dump)

    #情報はここにある https://www.zabbix.com/documentation/3.0/manual/api/reference/hostinterface/get


def SL_func():
    url = 'https://hooks.slack.com/services/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'
    #slack通知するユーザ名(任意)
    user = 'インフォメーション'
    #slackで通知するメッセージ内容
    message = 'テストです'
    payload = {'text': message, 'username': user}

    #slack_post
    res_mes = requests.post(url, data=json.dumps(payload))


ZA_func()
#SL_func()
