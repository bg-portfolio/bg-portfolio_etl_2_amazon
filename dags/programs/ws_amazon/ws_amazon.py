from utils.amazon_shop import WebDriverContext
from utils.inputs import _inputs, _categories_1, _categories_2
from utils.processing import _page_hopping, _comprehensive_search, _captcha_solver, _save_data
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
from datetime import datetime

# TODO: product details + more


def web_scrape(category_1, category_2, keyword, index, quick_search, scrape):
    options = Options()
    options.add_argument('--incognito')
    options.headless = True
    options.page_load_strategy = 'eager'

    master_list = []  # list of dictionaries for data
    item_url_list = []  # list of item urls for data
    # one of number limits used in number of scrapes. Scrape input is second one
    number_on_site = 1
    page_number = 1  # number used for page hopping
    time = datetime.now().strftime("%y-%m-%d-%H:%M:%S")

    url = category_1[f'{category_2[index]}']

    with WebDriverContext(webdriver.Chrome(ChromeDriverManager().install(), options=options)) as driver:
        _captcha_solver(driver, url)

        print('initializing, please wait.')
        pbar = tqdm(total=scrape)  # load bar 1

        while number_on_site < scrape:  # quick scraping amazon products
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            results = soup.find_all(
                'div', {'data-component-type': 's-search-result'})
            for result in results:
                data_dict = {}
                data_dict['keyword'] = keyword
                data_dict['category'] = category_2[index]
                data_dict['timestamp'] = time
                try:
                    data_dict['name'] = result.find(
                        'span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).text
                except:
                    data_dict['name'] = result.find(
                        'span', {'class': 'a-size-medium a-color-base a-text-normal'}).text
                try:
                    price = result.find('span', {'class': 'a-offscreen'}).text
                    price = price.replace('$', '')
                    price = float(price)
                    data_dict['price_$'] = price
                except:
                    data_dict['price_$'] = float(0)
                try:
                    rating = result.find('span', {'class': 'a-icon-alt'}).text
                    rating = rating.split()
                    rating = float(rating[0])
                    data_dict['rating_out_of_5'] = rating
                except:
                    data_dict['rating_out_of_5'] = 'None'
                data_dict['item_url'] = 'https://www.amazon.com/' + \
                                        result.find(
                                            'a', {'class': 'a-link-normal a-text-normal'})['href']
                item_url_list.append(data_dict['item_url'])
                if data_dict['rating_out_of_5'] == 'None':
                    data_dict['reviews'] = 0
                else:
                    rews = result.find_all('span', {'class': 'a-size-base'})
                    for rew in rews:
                        if len(rew['class']) == 1:
                            number = rew.text
                            number = number.replace(',', '')
                            try:
                                number = int(number)
                                if isinstance(number, int):
                                    data_dict['reviews'] = number
                            except:
                                continue
                master_list.append(data_dict)
                number_on_site += 1
                pbar.update(1)
                if number_on_site > scrape:
                    break
            if number_on_site < scrape:  # page hopping mechanism
                page_number = _page_hopping(page_number, soup, driver)
            else:
                break
        pbar.close()

        if not quick_search:  # determines quick or comprehensive search
            _comprehensive_search(item_url_list, master_list,
                                  0, driver, tqdm, BeautifulSoup)

    return master_list, time


def amazon_scrapper():
    category_2 = _categories_2()
    keyword, index, quick_search, scrape, datatype = _inputs(_categories_2())
    category_1 = _categories_1(keyword)
    master_list, time = web_scrape(category_1, category_2, keyword,
                                   index, quick_search, scrape)
    if datatype == "db":
        from utils.processing import _connect_mongo
        database = _connect_mongo()
    else:
        database = None
    _save_data(database, master_list, keyword, datatype, time)
    print('Done')


if __name__ == '__main__':
    amazon_scrapper()
