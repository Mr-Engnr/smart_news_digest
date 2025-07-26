# summarizer.py

def summarize_text(text, sentence_count=2):
    """
    Naive summarizer: split on periods and take the first N sentences.
    """
    cleaned = text.replace("\n", " ").strip()
    if not cleaned:
        return "No content to summarize."

    parts = [s.strip() for s in cleaned.split('.') if s.strip()]
    chosen = parts[:sentence_count]
    summary = '. '.join(chosen)
    if summary and not summary.endswith('.'):
        summary += '.'
    return summary
