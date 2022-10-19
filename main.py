from typing import List
from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Required
import uvicorn
from scraper import scrape_articles
from NewsItem import NewsItem, NewsItemModel, NewsItemSummaryModel

app = FastAPI(
    title="CAS News API"
)
class Data:
    data: List[NewsItem] = None

    @staticmethod
    def get():
        if not Data.data:
            Data.refetch()
        return Data.data

    @staticmethod
    def refetch():
        Data.data = scrape_articles("https://www.computingatschool.org.uk/news-and-blogs")


class NotFoundModel(BaseModel):
    detail: str


class IndexModel(BaseModel):
    message: str

@app.get("/", response_model=IndexModel)
async def root():
    return IndexModel(message="Hello World")


class NewsIndexModel(BaseModel):
    posts: List[NewsItemSummaryModel]
    count: int

@app.get(
    "/news",
    description="This endpoint is used to return all news items",
    response_model=NewsIndexModel
)
async def news(page = 0, limit = 25):
    print("getting all posts")
    print("on page", page)
    posts = [x.as_summary_model() for x in Data.get()]
    return NewsIndexModel(
        posts=posts,
        count=len(posts)
    )

@app.get(
    "/news/{url_hash}",
    description="This endpoint fetches a single news item by its hash",
    response_model=NewsItemModel,
    responses={404: {"model": NotFoundModel}}
)
async def news_item(url_hash: str = Query(default=Required, min_length=32)):
    print("looking up post", url_hash)
    result = filter(lambda x: x.url_hash == url_hash, Data.get())
    result = tuple(result)
    if (len(result) < 1):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="That news item was not found"
        )
    return result[0].as_model()

if __name__ == "__main__":
    # scrape_article("https://www.computingatschool.org.uk/news-and-blogs/2022/october/codeish-the-art-teaching-computing")
    Data.refetch() # Preload data
    uvicorn.run(app)
