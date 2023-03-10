import pandas as pd
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 '
                  'Safari/537.36 '
}

details = []


# First step
def request_to_url(num):
    url = f'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{num}'
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


# Second step
def process_get_data(soup):
    elements = soup.find_all('td', attrs={'class': 'data-table__cell'})

    for index in range(0, len(elements), 6):
        rank = elements[index].find('span', attrs={'class': 'data-table__value'}).text
        major = elements[index + 1].find('span', attrs={'class': 'data-table__value'}).text
        degree_type = elements[index + 2].find('span', attrs={'class': 'data-table__value'}).text
        early_career_pay = elements[index + 3].find('span', attrs={'class': 'data-table__value'}).text
        mid_career_pay = elements[index + 4].find('span', attrs={'class': 'data-table__value'}).text
        high_meaning = elements[index + 5].find('span', attrs={'class': 'data-table__value'}).text

        payscale_details = {
            'Rank': rank,
            'Major': major,
            'Degree_type': degree_type,
            'Early_career_pay': early_career_pay,
            'Mid_career_pay': mid_career_pay,
            'High_meaning': high_meaning,
        }
        details.append(payscale_details)


# Third step
def out_put(data):
    df = pd.DataFrame(data)
    df.to_csv('Highest paying jobs.csv', index=False)


for i in range(1, 35):
    print(f'Getting page: {i}')
    html = request_to_url(num=i)
    print('Parsing...')
    process_get_data(html)
out_put(details)
print('Saved to csv')


