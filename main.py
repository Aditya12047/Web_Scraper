import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://example.com"  
response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")


elements = soup.select("selector")


for element in elements:
  
    data = element.get("attribute_name")
    

    print(data)
