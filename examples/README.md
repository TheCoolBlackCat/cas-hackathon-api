# Examples using the API in Python

## Install dependencies
```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
```

## `simple.py`

A simple command line app that prints a list of articles and some details of a single article to the console.

```bash
venv/bin/python simple.py
```

## `app.py`

UI built with `tkinter` displaying a list of the articles and allows the user to navigate to display each article.

```bash
venv/bin/python app.py
```

## `nlp.py`

Fetches a single article and performs some really simple Natural Language Processing using the `nltk` library, listing the most common words used in the article.

```bash
venv/bin/python nlp.py
```
