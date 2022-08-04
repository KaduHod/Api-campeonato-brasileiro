from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_site_html(url):
    try :
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except HTTPError as e:
        print(e)
        return None
def writeFile(str, file):
    with open(file,'w') as f:
        f.write(str)

def getTabelaClassificacao(page):
    table = page.find("table", class_= "name")
    return table

def getTimes(tabela):
    times = tabela.findAll('div', class_='visible-lg')
    for time in times :
        print(time.get_text())
    return times
    

if __name__ == "__main__":
    html = get_site_html("https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/")
    print(html)
    print("\n\n\n\n\n\n\n")
    tabela = getTabelaClassificacao(html)
    times = getTimes(tabela)
    # print(times)
    
    
        
    