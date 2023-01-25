from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""

    top_5 = []
    list_top_5 = find_news()
    list_top_5.sort(key=lambda x: (x["comments_count"],
                                   x["title"]), reverse=True)
    for new in list_top_5:
        top_5.append((new["title"], new["url"]))
    return top_5[:5] if len(top_5) >= 5 else top_5 if top_5 else []


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
#  top_5.sort(key=lambda x: (x["comments_count"], x["title"]), reverse=True)

#     return top_5[:5] if len(top_5) >= 5 else top_5 if top_5 else []
