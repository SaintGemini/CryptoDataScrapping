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
containers = page_soup.findAll("tr",{"class":"simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white) "})


def get_data():
    for container in containers:
        #gets company name
        company = container.td.a["title"]
        #gets current price
        price_container = container.findAll("span",{"class": "Trsdu(0.3s) "})
        price = price_container[0].text
        #gets volume in currency
        volume_container = container.findAll("td", {"class": "Va(m) Ta(end) Pstart(20px) Pend(10px) W(120px) Fz(s)"})
        volume = volume_container[0].text
        #gets percent change
        percent_container = container.findAll("td", {"class" : "Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)"})
        percent = percent_container[2].text
        
        print(company + "    $" + price + "     " + percent + "     Vol: " + volume)
        
get_data()
