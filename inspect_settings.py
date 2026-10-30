import re

with open("d:/Firecrawl/raw/test_hgc/settingsRegistry.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

print("settingsRegistry length:", len(text))
keys = re.findall(r'["\']([a-zA-Z0-9_\-]+)["\']', text)
settings_keys = [k for k in set(keys) if any(s in k.lower() for s in ["setting", "whatsapp", "email", "sms", "ai", "billing", "webhook", "pipeline", "lead", "deal", "invoice", "currency", "brand", "domain"])]
print(f"Relevant settings keys found: {len(settings_keys)}")
for sk in sorted(settings_keys)[:40]:
    print(sk)

