from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

def naver_keyword(keyword):
    url = "https://search.naver.com/search.naver?where=news&query=" + str(keyword)
    web = requests.get(url).content
    source = BeautifulSoup(web, 'html.parser')

    news_subjects = source.find_all('a', {'class' : '_sp_each_title'}) # ResultSet (리스트와 유사한 형태)
    result = []

    for subject in news_subjects:
        result_subject = subject.get_text()
        result_url = subject.attrs['href']
        result.append((result_subject, result_url))

    return result
