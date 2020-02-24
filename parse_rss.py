import bs4 as bs
import urllib.request

def get_soup():
    status_page_url = 'https://status.mixer.com/'
    sauce = urllib.request.urlopen(status_page_url).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    return(soup)

def get_status(soup):
    status = soup.find('span', class_='status')
    status = status.text.strip()
    if 'All Systems Operational' in status:
        status_bool = True
    else:
        status_bool = False

    return(status, status_bool)

def get_detailed_status(soup):
    status_detailed  = {}
    statuses = soup.find_all('div', class_='component-inner-container')

    for item in statuses:
        name = item.find('span', class_='name').text.strip()
        status = item.find('span', class_='component-status').text.strip()
        status_detailed.update({name : status})
    return(status_detailed)

def get_last_incident(soup):
    pass


if __name__ == "__main__":
    soup = get_soup()

    print(get_detailed_status(soup))

    status, status_bool = get_status(soup)

    print(f'Current Status - {status}')