import requests
import json

API_URL = "http://localhost:8000"
URL_HASH = "aae8123de969670e63d741ba8a10a38a"

def main():
    response = requests.get(f"{API_URL}/news")
    data = json.loads(response.content)
    posts = data["posts"]

    for i, post in enumerate(posts):
        print(i+1, post["title"])
    print()


    response = requests.get(f"{API_URL}/news/{URL_HASH}")
    data = json.loads(response.content)

    title = data["title"]
    author = data["author"]
    text = data["text"]

    print("Title:", title)
    print("Author:", author)
    print("-" * 30)
    print(text)

if __name__ == "__main__":
    main()
