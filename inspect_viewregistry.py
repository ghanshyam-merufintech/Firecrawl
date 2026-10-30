import re
import json

with open("d:/Firecrawl/raw/test_hgc/viewRegistry.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

print("viewRegistry length:", len(text))

# Let's search for view definitions, ids, labels, routes, components
# Often structured as array of objects or object with keys
view_ids = re.findall(r'id:\s*["\']([a-zA-Z0-9_\-]+)["\']', text)
print(f"Total IDs found: {len(view_ids)}")

labels = re.findall(r'label:\s*["\']([^"\']+)["\']', text)
print(f"Total labels found: {len(labels)}")
print("Sample labels:", labels[:30])

titles = re.findall(r'title:\s*["\']([^"\']+)["\']', text)
print(f"Total titles found: {len(titles)}")
print("Sample titles:", titles[:30])

# Dynamic imports in viewRegistry
matches = re.findall(r'import\s*\(\s*["\']([^"\']+)["\']\s*\)', text)
print(f"\nDynamic imports in viewRegistry ({len(matches)}):")
for m in sorted(set(matches)):
    print(m)

