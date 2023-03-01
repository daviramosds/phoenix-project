import webbrowser
from urllib import parse

def test():
    print('test command')


def google_search(text):  # say google search {search}
    web_encode = parse.quote(text)
    webbrowser.open(f"https://www.google.com/search?q={web_encode}")
    print(f'google searching {text}')
