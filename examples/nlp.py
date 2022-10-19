import requests
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def main():
    API_URL = "http://localhost:8000"
    URL_HASH = "aae8123de969670e63d741ba8a10a38a"

    response = requests.get(f"{API_URL}/news/{URL_HASH}")
    data = json.loads(response.content)

    title = data["title"]
    text = data["text"]

    words = word_tokenize(text)

    excluded = set(stopwords.words("english"))
    for punctuation in ".,?!'\"()":
        excluded.add(punctuation)
    filtered_words = [word.lower() for word in words if word not in excluded]

    frequencies = FreqDist(filtered_words)

    print("Article:", title)
    print("Most Common Words:", frequencies.most_common(3))

if __name__ == "__main__":
    main()
