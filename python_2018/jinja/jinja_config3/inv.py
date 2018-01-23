#必要なインタフェース分rangeを記載
scl = range(1,11)

#可変パラメータを下記に変数として格納
host = 'RT-A'
iden_k = 'id' #id key
intf_k = 'intf_ip' #GigabitEthernet ip key
loop_k = 'loop_ip' #Loopback ip key
snmp_ip = '10.0.0.220'

#シーケンスで利用する可変パラメータを下記に変数として格納
iden_v = [] #id vaule
intf_v = [] #GigabitEthernet ip vaule
loop_v = [] #Loopback ip vaule

for iden in scl:
    iden_v.append(str(iden))
    intf_v.append('172.16.' + str(iden) + '.1')
    loop_v.append('192.168.0.' + str(iden))

