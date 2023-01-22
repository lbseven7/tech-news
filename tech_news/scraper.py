import requests
import time
# import parsel


# Requisito 1
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


# Requisito 2
def scrape_updates(html_content):
    pass


# Requisito 3
def scrape_next_page_link(html_content):
    pass


# Requisito 4
def scrape_news(html_content):
    pass


# Requisito 5
def get_tech_news(amount):
    pass
