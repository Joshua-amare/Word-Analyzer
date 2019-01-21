def random_headers():
    import desktopAgents
    from random import choice
    return {'User-Agent': choice(desktopAgents.desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

def urlopen(url):
    import urllib.request
    r = urllib.request.Request(url, headers=random_headers())
    response = urllib.request.urlopen(r)
    html= response.read()
    return html

def grabtext(html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text
