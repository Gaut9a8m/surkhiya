from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.
def home(request):
    newsapi = NewsApiClient(api_key='488ffcf910fb45768a262eb3b3c92e2c')

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(sources = 'google-news-in')
  
    l = top_headlines['articles']
    desc = []
    news = []
    img = []
    pub_date = []
    news_url = []
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        pub_date.append(f['publishedAt'])
        news_url.append(f['url'])
    mylist = zip(news,desc,img,pub_date,news_url)

    return render(request, 'news/home.html' , {'mylist':mylist})
     # /v2/everything
    
    # /v2/sources
    # sources = newsapi.get_sources()

