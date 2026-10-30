import re

with open("d:/Firecrawl/raw/test_hgc/appWebhooks.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

events = re.findall(r'["\']([a-zA-Z0-9_\.]+\.[a-zA-Z0-9_\.]+)["\']', text)
print("Webhook events found:", len(events))
for ev in sorted(set(events)):
    print(ev)

