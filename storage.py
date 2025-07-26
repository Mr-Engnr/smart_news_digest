# storage.py
import sqlite3

DB_NAME = 'articles.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            title     TEXT,
            link      TEXT UNIQUE,
            summary   TEXT,
            published TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_article(article):
    """
    Expects article dict with keys: title, link, summary, published.
    """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute('''
            INSERT OR IGNORE INTO articles 
              (title, link, summary, published)
            VALUES (?, ?, ?, ?)
        ''', (
            article['title'],
            article['link'],
            article.get('summary', ''),
            article.get('published', '')
        ))
        conn.commit()
    except Exception as e:
        print("DB insert error:", e)
    conn.close()

def get_all_articles():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT title, summary, link, published 
          FROM articles 
         ORDER BY id DESC
    ''')
    rows = c.fetchall()
    conn.close()
    return rows
