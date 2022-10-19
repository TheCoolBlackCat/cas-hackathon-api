from ctypes import Array
from datetime import datetime
from hashlib import md5
import json
from pathlib import Path
from pydantic import BaseModel

class NewsItemModel(BaseModel):
    url_hash: str
    title: str
    url: str
    text: str
    author: str
    date: datetime

class NewsItemSummaryModel(BaseModel):
    url_hash: str
    title: str
    url: str
    author: str
    date: datetime


class NewsItem:
    @staticmethod
    def from_json(parsed_json: dict):
        return NewsItem(
            url=parsed_json["url"],
            title=parsed_json["title"],
            text=parsed_json["text"],
            author=parsed_json["author"],
            date=parsed_json["date"]
        )

    def dump_json(self, path: Path):
        with open(path, "w") as f:
            json.dump({
                "url": self.url,
                "title": self.title,
                "text": self.text,
                "author": self.author,
                "date": self.date.isoformat()
            }, f)

    def __init__(self, url: str, title: str, text: str, author: str, date: datetime):
        self.url_hash = md5(url.encode()).hexdigest()
        self.title = title
        self.text = text
        self.url = url
        self.author = author
        self.date = date

        self.image = None
        # self.description = ""
        self.tags = []

    def as_model(self) -> NewsItemModel:
        return NewsItemModel(
            url_hash=self.url_hash,
            title=self.title,
            url=self.url,
            text=self.text,
            author=self.author,
            date=self.date
        )
    
    def as_summary_model(self) -> NewsItemSummaryModel:
        return NewsItemSummaryModel(
            url_hash=self.url_hash,
            title=self.title,
            url=self.url,
            author=self.author,
            date=self.date
        )
