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
# ajuda do Charles Mendes
def scrape_updates(html_content: str) -> list:
    card_noticia = Selector(text=html_content)
    return card_noticia.css('h2.entry-title a::attr(href)').getall()


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
