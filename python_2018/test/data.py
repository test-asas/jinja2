#抽出したAPIから必要データを取り出す関数
#引数はgetapi.pyのリターン値
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