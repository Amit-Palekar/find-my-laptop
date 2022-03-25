import requests
from bs4 import BeautifulSoup

img_urls = []
def get_craigslist_data(url, params):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.find_all('a', class_= 'result-image')
    
    assert len(posts) == 120 #to double check I got 120 (elements/page)
    img_url = 'https://images.craigslist.org/{}_1200x900.jpg' # <--- for high resolution images
    # img_url = 'https://images.craigslist.org/{}_300x300.jpg'
    for i, (a_img, a_title) in enumerate(zip(soup\
                               .select('.result-row a.result-image.gallery[data-ids]'),
                              soup.select('.result-row a.result-title')), 1):
        img_links = []

        # create a dictionary to store (postID, imageLinks)        
        d = {}
        
        # default dict setup
        d.setdefault(a_title['id'],[])
        
        # for each postID get img links
        for data_id in [s.split(':')[1] for s in a_img['data-ids'].split(',')]:
            # store img links
            img_links.append(img_url.format(data_id))
        
        # append postID and list of img links
        d[a_title['id']].append(img_links)
        img_urls.append(d)        

        print(d[a_title['id']])
        
        # print(f"Item {i} url: {posts[i].attrs['href']}")
        # item_url = posts[i].attrs['href']

        # item_resp = requests.get(item_url)
        # item_soup = BeautifulSoup(item_resp.text, 'html.parser')
        # print(item_soup)
        # item_images = item_soup.find_all('*', class_= 'thumb')
        # print(item_images[0])
        if i == 10:
            break
        



serial_truth = 'FVFZ7345L414'

crg_url = 'https://sfbay.craigslist.org/search/moraga-ca/sss?lat=37.81846319511331&lon=-122.07321166992189&query=macbook%20pro&search_distance=17'

get_craigslist_data(crg_url, None)
