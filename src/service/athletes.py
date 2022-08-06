from urllib.request import urlopen
from urllib.error import HTTPError
from xml.dom import EMPTY_NAMESPACE
from bs4 import BeautifulSoup 
import json
import unidecode

def main():
    clubs = getClubsIds()
    jsonData = []

    for club in clubs :
        print(club['Name'])
        page  = getAthletesFromClub(club['Id'])
        pages = [
            getTableWithAthlets(page[0]),
            getTableWithAthlets(page[1])
        ]
        athletes = []
        for page in pages :
            for row in page:
                athletes.append(extractDataFromTrow(row))
        jsonData.append(
            {
                "Team" : club['Name'],
                "Athletes" : athletes
            }
        )
    print(jsonData)
    

def getAthletesFromClub(clubId):    
    soupPageOne = webSiteContent(f'https://www.cbf.com.br/futebol-brasileiro/atletas/campeonato-brasileiro-serie-a/2022/{clubId}')

    soupPageTwo = webSiteContent(f'https://www.cbf.com.br/futebol-brasileiro/atletas/campeonato-brasileiro-serie-a/2022/{clubId}?atleta=&page=2')

    return [soupPageOne, soupPageTwo]

def extractDataFromTrow(trow):
    a = trow.find_all('a')
    id      = a[0]['href'].split('/')[5].split('?')[0]
    Nome    = a[0].get_text().split('\n')[1].split('\r')[0].lstrip()
    Apelido = a[1].get_text().split('\n')[1].split('\r')[0].lstrip()
    print('\n\n\n')
    print({
        "id"      : id,
        "Nome"    : Nome,
        "Apelido" : Apelido
    })
    return {
        "id"      : id,
        "Nome"    : Nome,
        "Apelido" : Apelido
    }
    

def getTableWithAthlets(soup):
    table = soup.find('table')
    tbody = table.find('tbody')
    trs   = tbody.find_all('tr')
    return trs

def webSiteContent(url):
    try :
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except HTTPError as e:
        print(e)
    return None

def getClubsIds():
    fileJSON = open('./clubs-ids.json','r').read()
    content = json.loads(fileJSON)
    return content

if __name__ == "__main__":
    main()