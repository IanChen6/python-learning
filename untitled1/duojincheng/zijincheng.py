# coding: utf-8
import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])#nslookup解析域名
# print('Exit code:', r)

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx \n python.org \n exit\n')
# print(output.decode('utf-8'))
print('Exit code:', p.returncode)