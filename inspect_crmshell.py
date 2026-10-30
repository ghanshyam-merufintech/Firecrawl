import re

with open("d:/Firecrawl/raw/test_hgc/CRMShell.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

print("File length:", len(text))
matches = re.findall(r'import\s*\(\s*["\']([^"\']+)["\']\s*\)', text)
print("Dynamic imports in CRMShell:", len(matches))
for m in sorted(set(matches)):
    print(m)

js_files = re.findall(r'["\']([^"\']*\.js)["\']', text)
print("\nJS references in CRMShell:", len(js_files))
for j in sorted(set(js_files)):
    print(j)

# Look for paths or routes
routes = re.findall(r'path:\s*["\']([^"\']+)["\']', text)
print("\nRoutes in CRMShell:", len(routes))
for r in sorted(set(routes)):
    print(r)

