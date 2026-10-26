import os
import requests
import feedparser
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI(title="Global Conflict Monitor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FILE = "conflicts_data.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            summary TEXT,
            region TEXT,
            threat_level INTEGER,
            urgency TEXT,
            published_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

RSS_FEEDS = [
    "http://feeds.bbci.co.uk/news/world/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
]

def fetch_news_task():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    for url in RSS_FEEDS:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:
                title = entry.title
                summary = entry.get('summary', '')
                keywords = ["war", "conflict", "military", "missile", "strike", "attack", "gaza", "ukraine", "korea", "china"]
                if any(kw in title.lower() or kw in summary.lower() for kw in keywords):
                    cursor.execute("SELECT id FROM news WHERE title = ?", (title,))
                    if cursor.fetchone() is None:
                        cursor.execute('''
                            INSERT INTO news (title, summary, region, threat_level, urgency)
                            VALUES (?, ?, ?, ?, ?)
                        ''', (title, summary[:120] + "...", "글로벌 분쟁", 78, "경보"))
                        conn.commit()
        except Exception as e:
            print("크롤링 에러:", e)
    conn.close()

@app.get("/api/conflicts/latest")
def get_latest():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM news ORDER BY published_at DESC LIMIT 15")
    rows = cursor.fetchall()
    
    cursor.execute("SELECT AVG(threat_level) as avg_threat FROM news")
    avg_row = cursor.fetchone()
    avg_val = avg_row['avg_threat'] if avg_row and avg_row['avg_threat'] else 65.2
    conn.close()

    return {
        "status": "success",
        "global_threat_index": round(avg_val, 1),
        "data": [dict(r) for r in rows]
    }

@app.post("/api/conflicts/refresh")
def refresh(background_tasks: BackgroundTasks):
    background_tasks.add_task(fetch_news_task)
    return {"status": "ok"}