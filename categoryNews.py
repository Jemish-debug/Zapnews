import requests
from bs4 import BeautifulSoup
import json

def is_article_link(link):
    return "/articleshow/" in link or "/news/" in link or "/article/" in link or "/story/" in link

def fetch_news(url, category):
    print(f"🔍 Fetching {category.title()} from {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []

    for a_tag in soup.find_all("a", href=True):
        title = a_tag.get_text(strip=True)
        link = a_tag["href"]

        if not title or len(title.split()) < 3:
            continue

        # Construct full URL if it's relative
        if not link.startswith("http"):
            if "indiatimes" in url:
                link = "https://timesofindia.indiatimes.com" + link
            elif "indianexpress" in url:
                link = "https://indianexpress.com" + link

        # Filter out non-article pages
        if is_article_link(link):
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

    filename = f"data/{category.lower()}_news.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(all_articles, f, indent=4, ensure_ascii=False)

    print(f"✅ Saved {len(all_articles)} {category.title()} articles to {filename}")


# Category source URLs
categories = {
    "technology": [
        "https://timesofindia.indiatimes.com/technology",
        "https://indianexpress.com/section/technology/"
    ],
    "politics": [
        "https://timesofindia.indiatimes.com/india",
        "https://indianexpress.com/section/political-pulse/"
    ],
    "articles": [
        "https://timesofindia.indiatimes.com/blogs",
        "https://indianexpress.com/section/opinion/"
    ]
}


# Run the fetch and save process
for category, sources in categories.items():
    save_news_by_category(category, sources)
