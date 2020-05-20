import requests

'''
TESTE:
    >>> <Response [200]>
'''

def teste():
    r = requests.get('http://google.com')
    print(r)

if __name__ == "__main__":
    teste()