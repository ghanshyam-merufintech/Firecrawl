import re

with open("d:/Firecrawl/raw/test_hgc/CRMInnerShell.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Let's inspect routes and components mapping
route_components = re.findall(r'path:\s*["\']([^"\']+)["\']\s*,\s*(?:element|Component|lazy):\s*([a-zA-Z0-9_$]+)', text)
print("Route to component bindings:", len(route_components))
for r, c in route_components[:30]:
    print(f"{r} -> {c}")

# Let's search for roles or permission checks
roles = re.findall(r'["\'](admin|super_admin|manager|sales_rep|agent|member|owner|guest|viewer)["\']', text)
print("\nRoles mentioned:", set(roles))

# Let's search for feature flags or capabilities
flags = re.findall(r'["\']([a-zA-Z0-9_]+_(?:enabled|feature|gate|access))["\']', text)
print("\nFeature flags / gates:", set(flags))

