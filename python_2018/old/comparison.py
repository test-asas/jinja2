#取り出した必要データを掛け合わせ、ファイルに保存する関数
#引数はdata.pyのリターン値
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