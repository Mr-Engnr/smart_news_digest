# fetcher.py
import feedparser

def fetch_articles(rss_urls):
    articles = []
    for url in rss_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            articles.append({
                "title": entry.get("title", "").strip(),
                "link": entry.get("link", "").strip(),
                "summary": entry.get("summary", "").strip(),
                "published": entry.get("published", "").strip()
            })
    return articles
