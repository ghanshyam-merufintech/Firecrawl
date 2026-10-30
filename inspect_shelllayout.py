import re
import json

with open("d:/Firecrawl/raw/test_hgc/CRMShellLayout.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

print("CRMShellLayout length:", len(text))
matches = re.findall(r'import\s*\(\s*["\']([^"\']+)["\']\s*\)', text)
print("Dynamic imports in CRMShellLayout:", len(matches))
for m in sorted(set(matches)):
    print(m)

nav_matches = re.findall(r'["\'](/[^"\']+)["\']', text)
print("\nPaths in CRMShellLayout:", len(nav_matches))
for n in sorted(set(nav_matches)):
    if any(k in n for k in ["admin", "settings", "pipeline", "deals", "leads", "contacts", "tasks", "inbox", "reports"]):
        print(n)

