import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import json

url = "https://lenta.ru"

user = UserAgent()
headers = {"User-Agent": user.random}

response = requests.get(url + "/parts/news", headers)
soup = BeautifulSoup(response.text, "lxml")

news_panel = soup.find("div", class_="parts-page")

news_dict = {
    "title": None,
    "link": None,
    "date": None,
    "tag": None,
    "author": None
}

news_list = []


def append_news(n: int):
    for i in range(n):
        news = news_panel.find_all("li", class_="parts-page__item")[i]
        link = url + news.find("a", class_="card-full-news _parts-news").get("href")
        html = requests.get(link, headers)
        soup_ = BeautifulSoup(html.text, "lxml")

        news_dict = {
            "title": soup_.find("h1", class_="topic-body__titles").find("span").text,
            "link": link,
            "date": link[22:32].replace("/", "-"),
            "tag": soup_.find("a", class_="topic-header__item topic-header__rubric").text,
            "author": soup_.find("span", class_="topic-authors__name").text
        }

        news_list.append(news_dict)
        print(news_dict)


# запись в json файл
def write_to_json():
    with open("data/news.json", "w", encoding="utf-8") as f:
        json.dump(news_list, f, ensure_ascii=False, indent=2)


def main():
    count_news = 10
    append_news(count_news)
    write_to_json()


if __name__ == "__main__":
    main()
