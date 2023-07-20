import requests
from bs4 import BeautifulSoup
import json

def parse_data():
    result = []
    
    for page in range(1, 11):
        url = f'http://quotes.toscrape.com/page/{page}/'
        html_doc = requests.get(url)

        if html_doc.status_code == 200:
            soup = BeautifulSoup(html_doc.content, 'html.parser')

            # quotes_extraction
            quotes = soup.find_all('span', class_='text')
            authors = soup.find_all('small', class_='author')
            tags = soup.find_all('div', class_='tags')

            for i in range(len(quotes)):
                quote_dict = {}
                quote_dict['quote'] = quotes[i].text
                quote_dict['author'] = authors[i].text

                tags_list = []
                tagsforquote = tags[i].find_all('a', class_='tag')
                for tagforquote in tagsforquote:
                    tags_list.append(tagforquote.text)
                quote_dict['tags'] = tags_list

                result.append(quote_dict)

    return result


if __name__ == '__main__':
    quotes_list = parse_data()

    with open('quotes.json', 'w') as quotes_file:
        json.dump(quotes_list, quotes_file, indent=2)