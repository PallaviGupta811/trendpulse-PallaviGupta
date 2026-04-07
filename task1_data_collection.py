import requests
import time
import json
import os
from datetime import datetime

# hackernews api links
top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

# keywords for categories
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# function to find category from title
def find_category(title):
    title = title.lower()
    for cat in categories:
        for word in categories[cat]:
            if word in title:
                return cat
    return None


# step 1: get top story ids
try:
    res = requests.get(top_url, headers=headers)
    ids = res.json()
except:
    print("error getting top stories")
    ids = []

ids = ids[:500]   # take first 500

stories = []
count = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0
}

# step 2: get each story
for story_id in ids:
    print("Fetching story id:", story_id)   # <<< NEW
    try:
        r = requests.get(item_url.format(story_id), headers=headers)
        data = r.json()
    except:
        print("error in story", story_id)
        continue

    if data is None:
        continue

    if "title" not in data:
        continue

    cat = find_category(data["title"])

    # only take if category matches and limit not reached
    if cat is not None and count[cat] < 25:

        story_data = {
            "post_id": data.get("id"),
            "title": data.get("title"),
            "category": cat,
            "score": data.get("score", 0),
            "num_comments": data.get("descendants", 0),
            "author": data.get("by"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        stories.append(story_data)
        count[cat] += 1

    # check if all categories filled
    done = True
    for c in count.values():
        if c < 25:
            done = False

    if done:
        break


# sleep once per category (as asked)
# sleep once per category
for i in range(5):
    print(f"Waiting 2 sec for category {i+1}...")  # optional visual
    time.sleep(2)


# step 3: save file
if not os.path.exists("data"):
    os.makedirs("data")

filename = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(stories, f, indent=4)

print("collected", len(stories), "stories")
print("saved in", filename)