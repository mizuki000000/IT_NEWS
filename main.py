import feedparser
rss_url ="https://rss.itmedia.co.jp/rss/2.0/ait.xml"
feed =feedparser.parse(rss_url)
for entry in feed.entries[:5]:
    print(f"タイトル:{entry.title}")
    print(f"タイトル:{entry.published}")
    print(f"タイトル:{entry.link}")
    print("-"*60)