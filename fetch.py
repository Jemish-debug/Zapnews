import requests
from bs4 import BeautifulSoup
import json

def fetchHeadlines():
    # Fetch website content
    url = "https://timesofindia.indiatimes.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract headlines and links
    articles = []
    for figure in soup.find_all("figure"):  # Find all <figure> tags
        caption = figure.find("figcaption")  # Find <figcaption> inside <figure>
        link_tag = figure.find("a", href=True)  # Find <a> inside <figure>

        if caption and link_tag:
            title = caption.get_text(strip=True)  # Extract headline text
            link = link_tag["href"]  # Extract article link

            # Ensure absolute URL
            if link and not link.startswith("http"):
                link = "https://timesofindia.indiatimes.com" + link

            articles.append({"title": title, "link": link})

    # Save to JSON file
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

    print("✅ data.json updated with headlines & links!")
