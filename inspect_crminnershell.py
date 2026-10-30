import re

with open("d:/Firecrawl/raw/test_hgc/CRMInnerShell.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

print("File length:", len(text))
matches = re.findall(r'import\s*\(\s*["\']([^"\']+)["\']\s*\)', text)
print("Dynamic imports in CRMInnerShell:", len(matches))
for m in sorted(set(matches)):
    print(m)

routes = re.findall(r'path:\s*["\']([^"\']+)["\']', text)
print("\nRoutes in CRMInnerShell:", len(routes))
for r in sorted(set(routes)):
    print(r)

# Let's search for sidebar menu items, navigation labels, module keys
nav_labels = re.findall(r'label:\s*["\']([^"\']+)["\']', text)
print("\nLabels:", len(nav_labels))
for l in sorted(set(nav_labels)):
    print(l)

