import requests
from bs4 import BeautifulSoup

URL = "https://grc.ua/vacancies?categories=17"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36',
    'Host': 'grc.ua',
    'Accept': '*/*',
    "Accept-Encoding": "gzip, deflate, br",
    'Connection': 'keep-alive'
    }

def extract_max_page():
    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    last_pages = []
    pagination = soup.find_all('li', {'class': 'page-item'})
    for page in pagination:
        page_text = page.find('a').text
        if page_text.isdigit():  # Проверка, является ли текст целым числом
            last_pages.append(int(page_text))
    return last_pages[-1]+1

def extract_jobs(html):
    title = html.find('a', {'class': 'chakra-link css-137vqne'}).text
    links = html.find('a', {'class': 'chakra-link css-137vqne'})['href']
    link = f"https://grc.ua{links}"
    company = html.find('p', {'class': 'chakra-text css-is0jc4-StyledContactLink'}).text
    town = html.find('p', {'class': 'chakra-text css-1y5cxhh-StyledText'}).text
    return {
        'title': title,
        'company': company,
        'town': town,
        'link': link
    }

def extract_hh_jobs(last_pages):
    jobs = []
    for page in range(1, last_pages):
        print(f'Парсинг страницы {page}')
        resalt = requests.get(f"{URL}&page={page}", headers)
        soup = BeautifulSoup(resalt.text, 'html.parser')
        resalts = soup.find_all('div', {'class': 'css-ax3w0k'})
        for resalt in resalts:
            job = extract_jobs(resalt)
            jobs.append(job)
    return jobs    

def hh_get_jobs():
    max_page = extract_max_page()
    hh_jobs = extract_hh_jobs(max_page) 
    return hh_jobs