import re

with open("d:/Firecrawl/raw/test_hgc/index.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Let's search for any imports or string literals with ".js"
matches = re.findall(r'import\s*\(\s*["\']([^"\']+)["\']\s*\)', text)
print("Dynamic imports:", len(matches))
for m in sorted(set(matches)):
    print(m)

# Let's search for strings with "/assets/" or ".js"
js_matches = re.findall(r'["\']([^"\']*\.js)["\']', text)
print("\nJS files:", len(js_matches))
for m in sorted(set(js_matches)):
    print(m)

# Let's search for lazy components or paths
lazy_matches = re.findall(r'[a-zA-Z0-9_$]+\s*=\s*(?:lazy|React\.lazy)\s*\(\s*\(\)\s*=>\s*import\s*\(\s*["\']([^"\']+)["\']\s*\)', text)
print("\nLazy matches:", len(lazy_matches))
for m in lazy_matches:
    print(m)
