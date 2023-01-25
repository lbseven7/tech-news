from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""

    top_5 = []
    lista = find_news()
    lista.sort(key=lambda x: (x["comments_count"], x["title"]), reverse=True)
    for new in lista:
        top_5.append((new["title"], new["url"]))
    return top_5[:5] if len(top_5) >= 5 else top_5 if top_5 else []


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui - Ajuda do Arlisson Nascimento"""
    top_5 = []
    lista = find_news()
    noticias = [new["category"] for new in lista]
    contador_noticias = Counter(noticias).most_common(5)
    contador_noticias.sort(key=lambda x: (-x[1], x[0]))
    for new in contador_noticias:
        top_5.append(new[0])
    return top_5
