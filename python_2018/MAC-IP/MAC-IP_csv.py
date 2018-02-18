import csv
import sys

#python実行時に入力された引数の値を変数に入れる
mac_cisco = sys.argv[1]

#macアドレスから.を消す
mac_none = mac_cisco.replace(".", "")

mac_linux = ':'.join(map(''.join, zip(*[iter(mac_none)]*2)))

#print(mac_linux)

num_lines = len(open('invfile.csv').readlines())

#下記のforで利用する0
#n = 0

#for i in open('invfile.csv').readlines():
#    n += 1
#    if n == num_lines:
#        print('ok')

ID = num_lines+1
IPADDR = '10.0.0.'+str(ID)

ToCSV = [ID, mac_linux, IPADDR]

#print(ToCSV)


x = []

f = open('invfile.csv')


for i in f:
    x.append(i)

f.close()

if x == []:
    with open('invfile.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(ToCSV)

print(x)

if x != []:
    if mac_linux not in x[0]:
        with open('invfile.csv','a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(ToCSV)


