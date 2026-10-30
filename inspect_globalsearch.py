import re

with open("d:/Firecrawl/raw/test_hgc/GlobalSearchDialog.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Let's search for searchable entities
queries = re.findall(r'from\s*\(\s*["\']([^"\']+)["\']\s*\)', text)
print("Searchable tables / entities:", set(queries))

categories = re.findall(r'["\'](Leads|Contacts|Deals|Tasks|Invoices|Quotes|Orders|Tickets|Products|Activities)["\']', text)
print("Entity categories:", set(categories))

