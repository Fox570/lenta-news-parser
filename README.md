# 📰 Lenta.ru News Parser

This is a simple Python-based web scraper that collects the latest news articles from [Lenta.ru](https://lenta.ru) and saves them to a JSON file.

## 🔧 Technologies Used

- `requests` — for making HTTP requests
- `BeautifulSoup` — for HTML parsing
- `fake-useragent` — to generate a random User-Agent
- `lxml` — fast HTML/XML parsing

## ✨ Features

- Collects the latest **N news articles** (default: 10)
- Saves the data to `data/news.json`
- Extracts the following fields:
  - Title
  - URL
  - Date
  - Tag (category)
  - Author

## 🚀 How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
