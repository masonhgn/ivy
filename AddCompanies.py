from jobs.models import Company
from ScrapeCompanies import fetch_companies
test_list = fetch_companies(10)
for companyName in test_list:
    if Company.objects.filter(name=companyName) == None:
        Company.objects.create(name=companyName,logo_url=test_list[companyName],url='')