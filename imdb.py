import requests as req
from bs4 import BeautifulSoup as bs

DATA = {}


def seasonal_fetch(page_id, start, end):
    for i in range(start, end + 1):
        url = f'https://www.imdb.com/title/{page_id}/episodes?season={str(i)}'
        resp = req.get(url)
        if resp.status_code == 200:
            souped(resp.content)
        else:
            print("Request failed!")
            exit(1)


def souped(page):
    soup = bs(page, 'html.parser')
    season_no = soup.find(id='episode_top').get_text()
    season_no = ''.join(season_no.split())
    DATA[season_no] = []
    info = soup.find(class_='list detail eplist')
    info_items = info.find_all('div', class_='list_item')
    for item in info_items:
        ep_name = item.find(itemprop='name').get_text()
        ep_air_date = item.find(class_='airdate').get_text().strip()
        ' '.join(ep_air_date.split())
        ep_rating = item.find(class_='ipl-rating-star__rating').get_text()
        ep_rating_votes = item.find(class_='ipl-rating-star__total-votes').get_text()
        ep_data = {}
        ep_data['name'] = ep_name
        ep_data['airdate'] = ep_air_date
        ep_data['rating'] = ep_rating
        ep_data['votes'] = ep_rating_votes
        DATA[season_no].append(ep_data)
