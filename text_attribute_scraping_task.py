import requests as rq
from bs4 import BeautifulSoup
from bs4 import NavigableString

TUrl = 'https://books.toscrape.com/'

THeader = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

TResp = rq.get(url=TUrl, headers=THeader)

print(TResp.status_code)  # Check if the request was successful

bSoup = BeautifulSoup(TResp.content, 'html.parser')

def removeExtra(itration):
    return list(filter(lambda x: type(x) != NavigableString, itration))

# all_art = books
all_art = bSoup.find_all('article', class_='product_pod')

# print(all_art[0].h3.a.attrs['title'])

def Num_Converter(num_text ) :
    if num_text == 'One' :
        return 1 
    elif num_text == 'Two' :
        return 2
    elif num_text == 'Three' :
        return 3 
    elif num_text == 'Four' :
        return 4
    elif num_text == 'Five' :
        return 5
    else :
        return 0
    
# print(Num_Converter(all_art[0].p.attrs['class'][1]))

# print(all_art[0].h3.nextSibling.nextSibling.p.getText())



def TRP (b) :
    T = b.h3.a.attrs['title']
    R = Num_Converter(b.p.attrs['class'][1])
    P = b.h3.nextSibling.nextSibling.p.getText()
    return {
        'Title' : T ,
        'Rating' : R ,
        'Price' : P
    }


books_data = []

for b in all_art :
    B_TRP = TRP(b)
    books_data.append(B_TRP)

print(books_data)
