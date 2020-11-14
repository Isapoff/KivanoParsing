import csv
import requests
import datetime
from bs4 import BeautifulSoup

def get_html(url):
    res = requests.get(url)
    return res.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find('div', class_= 'pager-wrap').find_all('li', class_= 'last')[-1]
    total_pages = pages.find('a').get('href').split('=')[1]
    return int(total_pages)

def write_csv(data):
    with open('telefon.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['photo']])



def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    ads = soup.find('div', class_='list-view').find_all('div', class_= 'item product_listbox oh')

    for ad in ads:    
        try:
            title = ad.find('div', class_= 'listbox_title oh').find('strong').text
        except:
            title = ''
        try:
            price = ad.find('div', class_= 'listbox_price text-center').text.strip()
        except:
            price = ''
        try:
            photo =  'https://www.kivano.kg' + ad.find('div', class_= 'listbox_img pull-left').find('a').get('href')
        except:
            photo = ''
        data = {'title': title, 'price': price, 'photo': photo}
        
        write_csv(data)



def main():
    url = 'https://www.kivano.kg/mobilnye-telefony?page=1'
    base_url = 'https://www.kivano.kg/mobilnye-telefony?'
    page_part = 'page='

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages + 1):
        url_gen = base_url + page_part + str(i) 
        html = get_html(url_gen)
        get_page_data(html)
        





if __name__ == '__main__':
    main()






    





 