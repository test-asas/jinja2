import textfsm
import csv

with open('show ip int bri.txt') as f:
    interface_text = f.read()

with open('cisco_ios_show_ip_int_brief.template') as f:
    table = textfsm.TextFSM(f)
    result = table.ParseText(interface_text)

print(result)