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

def getTableName(page):
    table = page.find("table", class_= "name")
    return table

def getTableScore(page):
    table = page.find('table', class_='score')
    return table

def getTimes(tabela):
    times = tabela.findAll('div', class_='visible-lg')
    teams = []
    for time in times :
        teams.append(time.get_text())
    return teams

def getScores(tabela):
    tbody = tabela.find('tbody')
    linhas = tbody.find_all('tr')
    scores = []
    for linha in linhas:
        scores.append(getColunms(linha))
    return scores 
    
def getColunms(trow):
    tds = trow.findAll('td')
    return {
      "Time": None,
      "Pontos ganhos" : tds[0].get_text(),
      "Partidas jogadas" : tds[1].get_text(),
      "Vitórias" : tds[2].get_text(),
      "Empates" : tds[3].get_text(),
      "Derrotas" : tds[4].get_text(),
      "Gols contra"  : tds[5].get_text(),
      "Gols pró" : tds[6].get_text(),
      "Saldo de gols" : tds[7].get_text(),
      "Aproveitamento" : tds[8].get_text(),
    }

def mixData(scores, times):
    tabela_do_brasileirao = []
    for index, score in enumerate(scores):
        score["Time"] = times[index]
        tabela_do_brasileirao.append(score)
    return tabela_do_brasileirao

def main():
    html        = webSiteContent("https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/")
    tabelaName  = getTableName(html)
    tabelaScore = getTableScore(html)
    times       = getTimes(tabelaName)
    scores      = getScores(tabelaScore)
    tabelaBR    = mixData(scores, times)
    return tabelaBR


    
    
    
    
    
    
    
    
    
    
    
        
    