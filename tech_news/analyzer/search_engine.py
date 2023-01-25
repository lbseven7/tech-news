# from typing import List, Tuple
from tech_news.database import search_news
from datetime import datetime


# Requisito 6


def search_by_title(title):
    """Seu código deve vir aqui"""
    def pega_lista(query):
        todas_as_noticias = search_news(query)
        noticias_encontradas = []

        for noticia in todas_as_noticias:
            noticias_encontradas.append((noticia["title"], noticia["url"]))

        return noticias_encontradas
    return pega_lista({"title": {"$regex": title, "$options": "i"}})


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        noticias_encontradas = []
        date = datetime.fromisoformat(date).strftime('%d/%m/%Y')
        for new in search_news({"timestamp": {"$regex": date}}):
            noticias_encontradas.append((new["title"], new["url"]))
        return noticias_encontradas
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
