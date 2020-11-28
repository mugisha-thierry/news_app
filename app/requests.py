import urllib.request,json
from .models import News,Article

# Getting api key
api_key = None
# Getting the movie base url
base_url = None
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLE_NEWS_URL']

def get_news_source(category):
    """
    Function that gets the json response to our url request
    """
    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

    return news_results 


def process_results(news_list):
    """
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    """
    news_results = []

    for news_item in news_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        url = sources_item.get('url')
        category = sources_item.get('category')

        if id:
            news_object = News(id,name,url,category)
            news_results.append(news_object)

    return news_results        
