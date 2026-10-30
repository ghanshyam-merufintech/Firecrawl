import re
import json

with open("d:/Firecrawl/raw/test_hgc/viewRegistry.js", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Match lazy dynamic imports
imports = re.findall(r'import\s*\(\s*["\']\./([^"\']+)["\']\s*\)', text)
clean_imports = sorted(list(set(imports)))

print(f"Total Unique View Components: {len(clean_imports)}")

# Group by vertical/domain prefixes
categories = {
    "Core CRM & Sales": [],
    "Omnichannel & Communications": [],
    "AI & Automations": [],
    "Commerce, Billing & Invoicing": [],
    "Field Sales & Visits": [],
    "Customer Support & Portals": [],
    "HR, Payroll & Recruitment": [],
    "Manufacturing & Inventory": [],
    "Real Estate": [],
    "Healthcare & Clinic": [],
    "Education & Coaching": [],
    "CA, Tax & Accounting": [],
    "Travel & Hospitality": [],
    "Retail & POS": [],
    "Freight, Logistics & Export": [],
    "Fitness & Beauty / Salon": [],
    "Event Management": [],
    "Pharma & DCR": [],
    "Agency & Services": [],
    "Admin, Security & Settings": [],
    "Other Verticals": []
}

for comp in clean_imports:
    name = comp.split("-")[0]
    assigned = False
    
    if any(k in name for k in ["Ca", "Tax", "Filing"]):
        categories["CA, Tax & Accounting"].append(name)
        assigned = True
    elif any(k in name for k in ["Edu", "Student", "Admission", "Exam", "Assessment"]):
        categories["Education & Coaching"].append(name)
        assigned = True
    elif any(k in name for k in ["Clinic", "Doctor", "Patient", "Prescription"]):
        categories["Healthcare & Clinic"].append(name)
        assigned = True
    elif any(k in name for k in ["RE", "RealEstate", "Property", "SiteVisit"]):
        categories["Real Estate"].append(name)
        assigned = True
    elif any(k in name for k in ["Travel", "Trip", "Itinerary", "Hotel"]):
        categories["Travel & Hospitality"].append(name)
        assigned = True
    elif any(k in name for k in ["Retail", "POS", "Ecom", "AbandonedCart", "Shopify"]):
        categories["Retail & POS"].append(name)
        assigned = True
    elif any(k in name for k in ["Mfg", "Production", "Boq", "Quality", "Part", "Drawings"]):
        categories["Manufacturing & Inventory"].append(name)
        assigned = True
    elif any(k in name for k in ["Freight", "Consignment", "Fleet", "Driver", "Export", "Shipment", "Dispatch"]):
        categories["Freight, Logistics & Export"].append(name)
        assigned = True
    elif any(k in name for k in ["Gym", "Beauty", "Salon"]):
        categories["Fitness & Beauty / Salon"].append(name)
        assigned = True
    elif any(k in name for k in ["Event", "Exhibition"]):
        categories["Event Management"].append(name)
        assigned = True
    elif any(k in name for k in ["Pharma", "Dcr"]):
        categories["Pharma & DCR"].append(name)
        assigned = True
    elif any(k in name for k in ["Agency", "Retainer"]):
        categories["Agency & Services"].append(name)
        assigned = True
    elif any(k in name for k in ["HR", "Payroll", "Recruitment", "Employee", "Compensation", "TimeCard", "Attendance"]):
        categories["HR, Payroll & Recruitment"].append(name)
        assigned = True
    elif any(k in name for k in ["Field", "Visit", "Map"]):
        categories["Field Sales & Visits"].append(name)
        assigned = True
    elif any(k in name for k in ["WhatsApp", "Email", "SMS", "Call", "Dialer", "Inbox", "Broadcast", "Cadence", "Superfone", "ZohoVoice"]):
        categories["Omnichannel & Communications"].append(name)
        assigned = True
    elif any(k in name for k in ["AI", "Predictive", "Autonomous", "Agent", "ConversationIntelligence"]):
        categories["AI & Automations"].append(name)
        assigned = True
    elif any(k in name for k in ["Billing", "Invoice", "Payment", "Quote", "Proposal", "Expense", "RateContract", "Payout"]):
        categories["Commerce, Billing & Invoicing"].append(name)
        assigned = True
    elif any(k in name for k in ["Support", "Ticket", "Portal", "SLA", "ClientApproval", "Review", "NPS", "Customer"]):
        categories["Customer Support & Portals"].append(name)
        assigned = True
    elif any(k in name for k in ["Deal", "Lead", "Contact", "Pipeline", "Sales", "RepToday", "Activity", "Task"]):
        categories["Core CRM & Sales"].append(name)
        assigned = True
    elif any(k in name for k in ["Setting", "Security", "Admin", "User", "Role", "Team", "Trash", "Audit", "Notification"]):
        categories["Admin, Security & Settings"].append(name)
        assigned = True
    
    if not assigned:
        categories["Other Verticals"].append(name)

with open("d:/Firecrawl/raw/test_hgc/categorized_views.json", "w", encoding="utf-8") as f:
    json.dump(categories, f, indent=2)

for cat, items in categories.items():
    print(f"{cat}: {len(items)} components")

