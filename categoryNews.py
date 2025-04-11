import requests
from bs4 import BeautifulSoup
import json

def fetch_news(url, keyword):
    print(f"🔍 Fetching {keyword.title()} news from {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []

    for a_tag in soup.find_all("a", href=True):
        title = a_tag.get_text(strip=True)
        link = a_tag["href"]

        if not title or len(title.split()) < 3:
            continue

        if not link.startswith("http"):
            if "indiatimes" in url:
                link = "https://timesofindia.indiatimes.com" + link
            elif "indianexpress" in url:
                link = "https://indianexpress.com" + link
            elif "hindustantimes" in url:
                link = "https://www.hindustantimes.com" + link

        articles.append({
            "title": title,
            "link": link
        })

    return articles



def save_news_by_category(category, urls):
    all_articles = []

    for url in urls:
        articles = fetch_news(url, category)
        all_articles.extend(articles)

    file_name = f"data\\{category.lower()}_news.json"
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(all_articles, f, indent=4, ensure_ascii=False)

    print(f"Saved {len(all_articles)} {category.title()} articles to {file_name}")

categories = {
    "technology": [
        "https://timesofindia.indiatimes.com/technology",
        "https://www.hindustantimes.com/technology-news",
        "https://indianexpress.com/section/technology/"
    ],
    "politics": [
        "https://timesofindia.indiatimes.com/india",
        "https://www.hindustantimes.com/india-news",
        "https://indianexpress.com/section/political-pulse/"
    ],
    "articles": [
        "https://timesofindia.indiatimes.com/blogs",
        "https://www.hindustantimes.com/opinion",
        "https://indianexpress.com/section/opinion/"
    ]
}

for category, sources in categories.items():
    save_news_by_category(category, sources)
