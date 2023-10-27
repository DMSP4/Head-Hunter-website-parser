import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs/companies"


def extract_max_page():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all('a')
    last_page = int(pages[-2].get_text(strip=True))
    return last_page


def extract_job(html):
    company = html.find("h2", {"class": "fs-body2 mb4"}).find("a").get_text(strip=True)
    #title = html.find("div", {"class": "flex--item fl1 text mb0"}).find("p").get_text(strip=True)
    #location, sfer = html.find("div", {"flex--item fc-black-500 fs-body1"}).get_text(strip=True)
    
    #location_row = html.find("h2", {"class": "mb4"}).find_all("svg").get_text(strip=True)   второй вариант получения инф из одинаковых элементов
    #location = location_row[0]
    #sfer = location_row[1]
    link = "https://stackoverflow.com" + html.find("h2", {"class": "fs-body2 mb4"}).find("a")["href"]
    return {
        "company": company,
        #"title": title,
        #"location": location,
        #"sfer": sfer,
        "link": link
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(1, last_page + 1):
        print(f"Парсинг страницы {page} so")
        resalt = requests.get(f"{URL}?pg={page}")
        soup = BeautifulSoup(resalt.text, "html.parser")
        resalts = soup.find_all("div", {"class": "dismissable-company"})
        for i in resalts:
            job = extract_job(i)
            jobs.append(job)
    print(jobs)
    return jobs
        

       
def so_get_jobs():
    max_page = extract_max_page()
    jobs = extract_jobs(max_page) 
    return jobs

