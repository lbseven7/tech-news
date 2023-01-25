# from typing import List, Tuple
from tech_news.database import search_news
# import datetime
# from pymongo import MongoClient


# Requisito 6


def search_by_title(title):
    """Seu código deve vir aqui"""
    def pega_lista(query):
        todas_as_noticias = search_news(query)
        noticias_encontradas = []

        # title = title.lower()
        for noticia in todas_as_noticias:
            noticias_encontradas.append((noticia["title"], noticia["url"]))

        return noticias_encontradas
    return pega_lista({"title": {"$regex": title, "$options": "i"}})


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    # date = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
    # client = MongoClient()
    # db = client.news_database

    # news = list(db.news_collection.find({"timestamp": date}))
    # if not news:
    #     return []

    # return [(new['title'], new['url']) for new in news]


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
