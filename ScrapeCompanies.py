import requests
from bs4 import BeautifulSoup

url = 'https://www.levels.fyi/js/internshipData.json'
response = requests.get(url)
jobs_list = response.json()


def fetch_companies():
    companies = set()
    results = {}
    for i in range(len(jobs_list)):
        if not jobs_list[i]['company'] in companies:
            company = jobs_list[i]
            companies.add(company['company'])
            company_name = company['company']
            logo_link = company['icon']
            results[company_name] = logo_link
    return results



    



