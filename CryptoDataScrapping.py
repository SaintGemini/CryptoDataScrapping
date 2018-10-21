from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://finance.yahoo.com/cryptocurrencies'
# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("tr",{"class":"SimpleDataTableRow"})

for container in containers:
    
    #gets company name
    company = container.td.a["title"]
    
    #gets current price
    price_container = container.findAll("span",{"class": "Trsdu(0.3s) "})
    price = price_container[0].text
    
    print(company + " " + "$"+ price)