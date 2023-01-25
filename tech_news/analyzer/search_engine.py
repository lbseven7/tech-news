# from typing import List, Tuple
from tech_news.database import search_news
from datetime import datetime


# Requisito 6


def search_by_title(title):
    """Seu código deve vir aqui"""
    def pega_lista(query):
        todas_as_noticias = search_news(query)
        noticia_por_titulo = []

        for noticia in todas_as_noticias:
            noticia_por_titulo.append((noticia["title"], noticia["url"]))

        return noticia_por_titulo
    return pega_lista({"title": {"$regex": title, "$options": "i"}})


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        noticia_por_data = []
        date = datetime.fromisoformat(date).strftime('%d/%m/%Y')
        for new in search_news({"timestamp": {"$regex": date}}):
            noticia_por_data.append((new["title"], new["url"]))
        return noticia_por_data
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    noticia_por_tag = []
    for new in search_news({"tags": {"$regex": tag, "$options": "i"}}):
        noticia_por_tag.append((new["title"], new["url"]))
    return noticia_por_tag


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
