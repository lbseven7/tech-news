import requests
import time
from parsel import Selector


# Requisito 1 Ciência da Computação - Aula 3.2 - Raspagem de Dados
# Eli Candido Jr
def fetch(url: str, aguarde: int = 1) -> str:
    headers = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        response = requests.get(url, timeout=aguarde, headers=headers)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2 - Crie a função scrape_updates
# https://blog.betrybe.com/carreira/
# https://blog.betrybe.com/tecnologia/
# https://blog.betrybe.com/desenvolvimento-web/
# https://blog.betrybe.com/javascript/


def scrape_updates(html_content: str) -> list:
    # selector = Selector(html_content)
    card_noticia = Selector(html_content)
    novas_urls = []
    for url in card_noticia.css('.post-outer a::attr(href)').getall():
        if 'button' not in card_noticia.css(
         url).get():
            novas_urls.append(url)
        elif card_noticia.css(url).get() is None:
            return []
    return novas_urls


if __name__ == "__main__":
    page_content = fetch("https://blog.betrybe.com/")
    updates = scrape_updates(page_content)


# Requisito 3
def scrape_next_page_link(html_content):
    sel = Selector(html_content)
    # Use o seletor CSS para selecionar o
    # elemento que contém o link da próxima página
    url_proxima_pagina = sel.css('a.next::attr(href)').get()
    if url_proxima_pagina:
        return url_proxima_pagina
    else:
        return None


# Requisito 4
def scrape_news(html_content):
    pass


# Requisito 5
def get_tech_news(amount):
    pass
