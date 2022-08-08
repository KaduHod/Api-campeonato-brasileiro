from urllib.request import urlopen
from urllib.error import HTTPError
from xml.dom import EMPTY_NAMESPACE
from bs4 import BeautifulSoup 
import json
import unidecode

def main():
    file = open('./athletes.json', 'r').read()
    atletas = json.loads(file)
    dataAll = []
    for atleta in atletas :
        url = f"https://www.cbf.com.br/futebol-brasileiro/atletas/{atleta['id']}?exercicio=2022"
        page = webSiteContent(url)
        print(atleta['nome'])
        dataAll.append(
            {
                'nome' : getName(atleta),
                'apelido' : getApelido(atleta),
                'nascimento' : getDataNascimento(page),
                'clubId' : getClubId(atleta),
                'general-stats' : getGeneralStats(page),
                'rouds-participated' : getMatchs(page)
            }
        )
    print('PRONTO')
    return 1

def getName(athlete):
    return athlete['nome']
def getApelido(athlete):
    return athlete['apelido']
def getDataNascimento(page):
    perfilDetalhado = page.find('ul',class_='perfil-detalhado')
    li = perfilDetalhado.find_all('li')
    return li[1].get_text().split(' ')[1]
def getClubId(athlete):
    return athlete['clubId']
def getGeneralStats(page):
    generalStats = page.find_all('div', class_='dentro-campo__item')
    return {
        "matchs" : generalStats[0].get_text().strip().split("\r")[0],
        "yellow cards" : generalStats[2].get_text().strip().split("\r")[0],
        "red cards" : generalStats[3].get_text().strip().split("\r")[0],
        "goals" : generalStats[1].get_text().strip().split("\r")[0]
    }
def getMatchs(page):
    rodadas = page.find_all('div', class_='rodada')
    rodadasIds = []
    for rodada in rodadas :
        linkJogo = rodada.find('a', class_=['btn','btn-xs','btn-success','m-t-5'])
        rodadaId = linkJogo['href'].split('/')[7]
        rodadasIds.append(rodadaId)
    return rodadasIds

def webSiteContent(url):
    try :
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except HTTPError as e:
        print(e)
    return None

if __name__ == "__main__":
    main()