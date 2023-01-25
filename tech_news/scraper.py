import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup


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
    link = card_noticia.css('h2.entry-title a::attr(href)').getall()
    return link


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
    soup = BeautifulSoup(html_content, 'html.parser')

    url = soup.find('link', {'rel': 'canonical'})['href']

    title = soup.find('h1', class_='entry-title').text.strip()
    timestamp = soup.find('li', class_='meta-date').text.strip()
    writer = soup.find('span', class_='author').text.strip()

    comments_count = soup.find('div', class_='comment-content')
    if comments_count:
        comments_count = int(comments_count.text)
    else:
        comments_count = 0

    summary = soup.find(
        'div', class_='entry-content').find("p").text.strip()

    tags = Selector(text=html_content).css(
        'section.post-tags ul li a::text').getall()

    category = soup.find('span', class_='label').text.strip()

    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'comments_count': comments_count,
        'summary': summary,
        'tags': tags,
        'category': category
    }


# Requisito 5
def get_tech_news(amount):
    pass
