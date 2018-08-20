def bla():
    import urllib.request

    url = 'http://bit.ly/carregarPy2'
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/7.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, './teste2.py')

    ### Em nova celula....
    import teste2 as t
    t.foi()

if __name__ == "__main__":
    print("Hello World!")
