from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news_source
# ,get_movie,search_movie
# from .forms import ReviewForm
# from ..models import Article,News

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    general = get_news_source('general')
    entertainment = get_news_source('entertainment')
    business = get_news_source('business')
    health = get_news_source('health')
    sports = get_news_source('sports')
    science = get_news_source('science')
    technology = get_news_source('technology')
    title='News source'
    return render_template('index.html',title=title,general=general,entertainment=entertainment,business=business,health=health,sports=sports,science=science,technology=technology)



