import requests

def verificarSite():
    url = 'https://www.pudim.com.br'
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print("\033[33m[!] Você está no site do Pudim! \033[m")
        else:
            print("\033[31m[!] Você NÃO está no site do Pudim! \033[m")
    except:
        print("\033[31m[!] Você NÃO está no site do Pudim! \033[m")
verificarSite()