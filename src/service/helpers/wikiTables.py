from urllib.request import urlopen
from urllib.error import HTTPError
from xml.dom import EMPTY_NAMESPACE
from bs4 import BeautifulSoup

def webSiteContent(url):
    try :
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except HTTPError as e:
        print(e)
        return None
    
def getTablesHtml(page):
    table = page.find_all('table', class_='wikitable')
    tables = {
        'teams' : table[0],
        'stadiums' : table[1],
        'rank' : table[2],
        'passed rounds' : table[3],
        'performance per round' : table[4],
        'rank goals' : table[5],
        'rank assists' : table[6],
        'rank hat-tricks' :table[7],
        'biggest audiences' : table[8],
        'lowest audiences' : table[9],
        'avarage audiences fo each club' : table[10]
    }
    return tables

def mainTables():
    url = "https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2022_-_S%C3%A9rie_A"
    page = webSiteContent(url)
    return getTablesHtml(page)
    
if __name__ == "__main__":
    mainTables()