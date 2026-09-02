import requests
#is used to send HTTP requests to websites.
from bs4 import BeautifulSoup
#bs4 allows us to pass in certain paths and patterns to get certain snippets of HTML.


def scrape():
    url = 'https://www.scrapethissite.com/pages/'
    response = requests.get(url) #it is used to open the website and get its content.
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser') #used to read and parse HTML
    title = soup.select_one('h1').text
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href')

    print(title)
    print(text)
    print(link)



if __name__ == '__main__':
    scrape()