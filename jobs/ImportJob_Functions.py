import bs4
from bs4 import BeautifulSoup
import urllib3
import re
import datetime


# job title class tag ends with "topcard__title"
# company class tag starts with "topcard__org-name"

class LinkedInTags:
    title_tag = "topcard__title$"
    company_tag = "^topcard__org-name"


class JobPosting:
    job_title = None
    company = None
    location = None
    employment_type = None

    def __init__(self, job_title: str, company: str, location: str, employment_type: str = None):
        self.job_title = job_title
        self.company = company
        self.location = location
        self.employment_type = employment_type

    def __str__(self):
        return ", ".join([self.job_title, self.company, self.location, self.employment_type])


def get_element_text(element: bs4.ResultSet, debug: bool = False):
    if len(element) == 1:
        result = element[0].string.strip()
        if debug:
            print(result)
        return result
    else:
        raise Exception("Found either 0 or more than 1 matching element")

def get_element_text2(prev_sib_element: bs4.element, debug: bool = False):
    siblings = prev_sib_element.next_siblings

    for sibling in siblings:
        if len(sibling.text.strip()) > 0:
            result = sibling.text.strip()
            if debug:
                print(result)
            return result

    raise Exception("Text not found.")


def get_job_details(job_link: str, debug: bool = False):
    http = urllib3.PoolManager()
    page = http.request("GET", job_link)

    soup = BeautifulSoup(page.data, 'html.parser')

    job_title_element = soup.find_all("h1", class_=re.compile(LinkedInTags.title_tag))
    company_element = soup.find_all("a", class_=re.compile(LinkedInTags.company_tag))
    employment_elder_element = soup.find_all("h3", string=re.compile(".*Employment type.*"))

    title = get_element_text(job_title_element)
    company = get_element_text(company_element)
    location = get_element_text2(company_element[0].parent)
    employment = get_element_text2(employment_elder_element[0])

    JP = JobPosting(title, company, location, employment)
    if debug:
        print(JP)
    return JP


get_job_details(
    "https://www.linkedin.com/jobs/view/3368796517/?alternateChannel=search&refId=2iuTensk5PCFJjxJs%2FuhvA%3D%3D&trackingId=BN9QG6Syxa%2Fry%2FfpetBknA%3D%3D")
