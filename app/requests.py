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

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results 


def process_results(news_list):
    """
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news sources

    Returns :
        news_results: A list of news objects
    """
    news_results = []

    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        url = news_item.get('url')
        category = news_item.get('category')

        if id:
            news_object = News(id,name,url,category)
            news_results.append(news_object)

    return news_results   



# article functions



def get_news_article(id):
    """
    Function that gets the json response to our url request
    """
    get_article_url = article_url.format(id,api_key)
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_results(article_results_list)

    return article_results 

def process_article(article_list):
    """
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    """
    article_results = []
    source_dictionary = {}

    for article_item in article_list:
        source_id = result ['source']
        source_dictionary['id'] = source_id['id']
        source_dictionary['name'] = source_id['name']
        id = source_dictionary['id']
        name = source_dictionary['name']

        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if urlToImage:
            article_object = Article(id,name,author,title,description,url,urlToImage,publishedAt)
            article_results.append(article_object)

    return article_results       