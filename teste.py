import requests


def teste():
    '''#Teste da funcao
    >>> teste()
    <Response [2]>
    '''
    r = requests.get('http://google.com')
    print(r)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
