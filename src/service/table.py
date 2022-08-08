import sys
from urllib.request import urlopen
from urllib.error import HTTPError
from xml.dom import EMPTY_NAMESPACE
from bs4 import BeautifulSoup
from helpers import wikiTables
import json
import unidecode

def main():
    tabela = wikiTables.mainTables()
    rankwiki = getRowValues(tabela['rank'])
    writeFile(rankwiki)

def writeFile(data):
    with open('./tabela-wiki.json', 'w') as tabela:
        tabela.write(json.dumps(data))
        

def tableHeaders(table):
    tableHeaders = getHeaders(table)
    return tableHeaders

def getRowValues(table):
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')
    rankArr = []
    for index,row in enumerate(rows):
        if index == 0:
            continue
        tds = getTds(row)
        rankArr.append({
            'Team name' : getTeamName(row) ,
            'Points' : tds[2].get_text().strip(),
            'Matchs' : tds[3].get_text().strip(),
            'Wins' : tds[4].get_text().strip(),
            'Draws' : tds[5].get_text().strip(),
            'Losses' : tds[6].get_text().strip(),
            'GP' : tds[7].get_text().strip(),
            'GC' : tds[8].get_text().strip(),
            'SG' : tds[9].get_text().strip(),
            'Aproveitamento' : tds[10].get_text().strip()
        })
    return rankArr

def getTeamName(row):
    a = row.find_all('a')
    return unidecode.unidecode(a[1].get_text().strip())

def getTds(row):
    return row.find_all('td')

def getHeaders(table):
    tbody = table.find('tbody')
    firstTr = tbody.find('tr')
    trows = firstTr.find_all('th')
    headers = []
    for trow in trows:
        title = trow.get_text().strip()
        if(title != "Classificação ou rebaixamento" and title != "M"):
            headers.append(title)
    return headers

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
    return tables['rank']
    
    
if __name__ == "__main__":
    main()