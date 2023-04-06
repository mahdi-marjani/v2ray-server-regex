import re
import datetime

with open('input.txt', 'r' , encoding='utf-8') as file:
    text = file.read()




# Add a new line before 'ss://'
text = re.sub(r'[^e](ss://)', r'\n\n\1', text)

# Add a new line before 'vmess://'
text = re.sub(r'(vmess://)', r'\n\n\1', text)

# Add a new line before 'vless://'
text = re.sub(r'(vless://)', r'\n\n\1', text)

# Add a new line before 'trojan://'
text = re.sub(r'(trojan://)', r'\n\n\1', text)



vmess_re  = r'(vmess://.*?)[\s\n]'
vless_re  = r'(vless://.*?)[\s\n]'
trojan_re = r'(trojan://.*?)[\s\n]'
ss_re     = r'[^e](ss://.*?)[\s\n]'

vmess_servers  = re.findall(pattern=vmess_re,string=text)
vless_servers  = re.findall(pattern=vless_re,string=text)
trojan_servers = re.findall(pattern=trojan_re,string=text)
ss_servers     = re.findall(pattern=ss_re,string=text)

vmess_servers  = set(vmess_servers)
vless_servers  = set(vless_servers)
trojan_servers = set(trojan_servers)
ss_servers     = set(ss_servers)

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

with open('output.txt', 'w') as file:
    file.write(f'(time update : {formatted_time})' + '\n\n')
    file.write('vmess servers:' + '\n\n')
    for elem in vmess_servers:
        file.write(str(elem) + '\n')
    file.write('\n' + '-------------------------------------------------' + '\n')
    file.write('vless servers:' + '\n\n')
    for elem in vless_servers:
        file.write(str(elem) + '\n')
    file.write('\n' + '-------------------------------------------------' + '\n')
    file.write('trojan servers:' + '\n\n')
    for elem in trojan_servers:
        file.write(str(elem) + '\n')
    file.write('\n' + '-------------------------------------------------' + '\n')
    file.write('ss servers:' + '\n\n')
    for elem in ss_servers:
        file.write(str(elem) + '\n')
    file.write('\n' + '-------------------------------------------------' + '\n')