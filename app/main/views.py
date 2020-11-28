from flask import render_template,request,redirect,url_for
from . import main
# from ..requests import get_movies,get_movie,search_movie
# from .forms import ReviewForm
# from ..models import Article,News

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title='News source'
    return render_template('index.html',title=title)



