# Smart News Digest Generator

**Automated news digest via RSS, summarization, and email delivery.**

## Features
- Fetches articles from multiple RSS feeds daily
- Naive summarization (split-and-take) of article snippets
- Deduplication and storage in SQLite
- Sends a plain-text email digest via Gmail App Password

## Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/smart_news_digest.git
   cd smart_news_digest

2. **Install dependencies**:

pip install -r requirements.txt

3. **Configure**:

Rename config.example.yaml to config.yaml.

Fill in your RSS feed URLs and Gmail app password.

4. **Initialize & run**:

python main.py