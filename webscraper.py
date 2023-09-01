import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
#you create a Beautiful Soup object that takes page.content, 
# which is the HTML content you scraped earlier, as its input.
###################################################################
#html.parser makes sure that you use the appropriate parser for HTML content

results = soup.find(id="ResultsContainer")
#find that specific HTML element by its ID:
print(results.prettify())
#you can pick out one element from among the rest of the HTML. 
###################################################################

job_elements = results.find_all("div", class_="card-content")
#returns an iterable containing all the HTML for all the job listings displayed on that page.

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text)
    print(company_element.text)
    print(location_element.text)
    print()
