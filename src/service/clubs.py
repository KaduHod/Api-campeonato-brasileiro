from urllib.request import urlopen
from urllib.error import HTTPError
from xml.dom import EMPTY_NAMESPACE
from bs4 import BeautifulSoup 
import json
import unidecode

def webSiteContent(url):
        try :
            html = urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except HTTPError as e:
            print(e)
        return None

def getFormWithSelect(page):
    selectClubs = page.find(id="clubs")
    return selectClubs

def getOptions(select):
    options = select.findChildren('option', recursive=False)
    return options
    
def getClubsIds(options):
    clubs = []
    for index, soup in enumerate(options):
        if(index == 0):
            continue
        valueBrute = soup['value']
        id = getIdInValue(valueBrute)
        team  = soup.get_text()
        clubs.append({
            "Name" : unidecode.unidecode(team),
            "Id" : id
        })
    return clubs

def getIdInValue(str):
    return str.split('/')[7]

def writeJsonFile(info):
    with open("./clubs-ids.json", 'w') as clubs:
        clubs.write(json.dumps(info))

def main():
    page = webSiteContent("https://www.cbf.com.br/futebol-brasileiro/atletas/campeonato-brasileiro-serie-a/2022/")
    selectClubs = getFormWithSelect(page)
    options = getOptions(selectClubs)
    clubs = getClubsIds(options)
    return clubs

if __name__ == "__main__":
    clubs = main()
    writeJsonFile(clubs)