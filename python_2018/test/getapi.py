#mainの関数で各機能の関数を呼び出し、ZabbixAPIからAnsibleAPIを生成する
from zabbix.api import ZabbixAPI as ZA  # zabbixのpythonモジュール
import test.data as dfunc
import test.comparison as cfunc
import test.invfile as ifunc

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

API = host_func() #APIを抽出する関数(上記の関数)

DATA = dfunc.data_func(API) #抽出したAPIから必要データを取り出す関数

COMP = cfunc.comp_func(DATA) #取り出した必要データを掛け合わせ、ファイルに保存する関数

INV = ifunc.inv_func(COMP) #掛け合わせたデータが前回取得したデータと差分があるか確認する関数