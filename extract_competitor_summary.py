import os
import re

competitors = [
    "salesforce", "hubspot", "zoho-crm", "freshsales", "pipedrive", 
    "close", "gohighlevel", "activecampaign", "copper", "insightly", 
    "bitrix24", "nutshell", "keap", "less-annoying-crm", "pipeline-crm"
]

data = {}
for comp in competitors:
    path = f"d:/Firecrawl/teardowns/us/{comp}.md"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            entry_match = re.search(r'Entry Tier:\s*([^\n]+)', content)
            mid_match = re.search(r'Mid.*?Tier:\s*([^\n]+)', content)
            free_match = re.search(r'Free Tier Available:\s*([^\n]+)', content)
            traps = re.findall(r'(\d+\.\s*\*\*[^*]+\*\*:[^\n]+)', content)
            data[comp] = {
                "entry": entry_match.group(1).strip() if entry_match else "N/A",
                "mid": mid_match.group(1).strip() if mid_match else "N/A",
                "free": free_match.group(1).strip() if free_match else "N/A",
                "traps": traps[:3]
            }

print(f"Loaded {len(data)} competitor profiles:")
for k, v in data.items():
    print(f"\n{k.upper()}: Entry={v['entry']} | Mid={v['mid']} | Free={v['free']}")
    for t in v['traps']:
        print(f"  - {t}")

