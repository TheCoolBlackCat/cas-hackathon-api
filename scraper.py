#
# Adapted from https://github.com/TheCoolBlackCat/html-offline
#


from datetime import datetime
from hashlib import md5
from typing import List
from bs4 import BeautifulSoup
from pathlib import Path
import requests
import json

from NewsItem import NewsItem

BASE_FOLDER = Path("res/")

def scrape_article(url: str) -> NewsItem:
    url_hash = md5(url.encode()).hexdigest()

    soup: BeautifulSoup = None
    path = BASE_FOLDER.joinpath("posts")
    path = path.joinpath(url_hash)
    original_file = path.joinpath("original.html")
    parsed_file = path.joinpath("parsed.json")
    if path.exists():
        try:
            with open(parsed_file, "r") as f:
                json_text = json.load(f)
                return NewsItem.from_json(json_text)
        except json.decoder.JSONDecodeError:
            print("Invalid JSON in", parsed_file)
    else:
        # Fetch page and cache
        path.mkdir(parents=True)
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        with open(original_file, "w") as f:
            f.write(soup.prettify())
        
        text = [line.get_text().strip() for line in soup.select("div.usercontent")]
        date = datetime.strptime(
            soup.select_one("p.blog-header-date").get_text().strip(), # "05 October 2022"
            "%d %B %Y"
        )

        item = NewsItem(
            url=url,
            title=soup.select_one("h1.blog-header-title").get_text().strip(),
            text="\n".join(text),
            author=soup.select_one("p.blog-author-name").get_text().strip(),
            date=date
        )

        item.dump_json(parsed_file)

        return item

def scrape_articles(root_url: str) -> List[NewsItem]:
    response = requests.get(root_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    index_path = BASE_FOLDER.joinpath(Path("index"))
    page_number = soup.select_one("li.active").get_text().strip()

    path = index_path.joinpath(Path(page_number))
    if not path.exists():
        path.mkdir(parents=True)
        with open(path.joinpath("original.html"), "w") as f:
            f.write(soup.prettify())
    
    links = soup.select("a.archive-list-results-item")
    items = []
    for link in links:
        href = link.attrs["href"]
        if href.startswith("/news-and-blogs"):
            # if href.startswith("/"):
            href = "https://www.computingatschool.org.uk" + href
            items.append(scrape_article(href))

    return items
        
