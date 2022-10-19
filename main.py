from typing import List
from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Required
import uvicorn
from seed import NewsItemModel, NewsItemSummaryModel, seed_data

app = FastAPI(
    title="CAS News API"
)

class NotFoundModel(BaseModel):
    detail: str


class IndexModel(BaseModel):
    message: str

@app.get("/", response_model=IndexModel)
async def root():
    return IndexModel(message="Hello World")


class NewsIndexModel(BaseModel):
    posts: NewsItemModel

@app.get(
    "/news",
    description="This endpoint is used to return all news items",
    response_model=List[NewsItemSummaryModel]
)
async def news(page = 0, limit = 25):
    print("getting all posts")
    print("on page", page)
    return NewsIndexModel(
        posts=[x.as_summary_model() for x in seed_data]
    )

@app.get(
    "/news/{url_hash}",
    description="This endpoint fetches a single news item by its hash",
    response_model=NewsItemModel,
    responses={404: {"model": NotFoundModel}}
)
async def news_item(url_hash: str = Query(default=Required, min_length=32)):
    print("looking up post", url_hash)
    result = filter(lambda x: x.url_hash == url_hash, seed_data)
    result = tuple(result)
    if (len(result) < 1):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="That news item was not found"
        )
    return seed_data[0].as_model()

if __name__ == "__main__":
    uvicorn.run(app)
