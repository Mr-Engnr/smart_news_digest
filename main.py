# main.py
import yaml
from fetch_rss import fetch_articles
from summarizer import summarize_text
from storage import init_db, save_article, get_all_articles
from emailer import send_email
import os

# 1) Load config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

rss_urls = config["feeds"]
email_cfg = config["email"]

# 2) Initialize (and reset) DB
if os.path.exists('articles.db'):
    os.remove('articles.db')       # delete old DB so schema resets cleanly
init_db()

# 3) Fetch articles
raw_articles = fetch_articles(rss_urls)

# 4) Summarize & save
for art in raw_articles:
    art["summary"] = summarize_text(art["summary"])
    save_article(art)

# 5) Build digest text
articles = get_all_articles()
if not articles:
    print("No articles to send.")
    exit()

digest = "📰 Your Daily News Digest\n" + ("="*40) + "\n\n"
for idx, (title, summary, link, published) in enumerate(articles, 1):
    digest += f"{idx}. {title}\n   {published}\n   {summary}\n   Read more: {link}\n\n"

# 6) Send email
send_email(
    subject="🗞️ Daily News Digest",
    body=digest,
    sender=email_cfg["sender"],
    recipient=email_cfg["recipient"],
    password=email_cfg["password"]
)

print("✅ Digest sent!")
