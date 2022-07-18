import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br/")
except urllib.error.URLError:
    print("\033[31mLamentamos mas o site não está acessível\033[m")
else:
    print("\033[32mO site está acessível!!\033[m")
    print(site.read())
finally:
    print("Obrigado pela sua preferência.")