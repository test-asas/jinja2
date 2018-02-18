import textfsm
import csv

with open('show interface_gi3.txt') as f:
    interface_text = f.read()

with open('cisco_ios_show_interfaces.template') as f:
    table = textfsm.TextFSM(f)
    result = table.ParseText(interface_text)

print(result)