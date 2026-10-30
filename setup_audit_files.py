import csv
import shutil

# Copy COMPETITOR_MATRIX.csv and GAP_MASTER_TRACKER.csv
shutil.copyfile("d:/Firecrawl/10_Competitor_Feature_Matrix.csv", "d:/Firecrawl/research/hellogrowth-competitive-audit/COMPETITOR_MATRIX.csv")
shutil.copyfile("d:/Firecrawl/09_Gap_Master_Tracker.csv", "d:/Firecrawl/research/hellogrowth-competitive-audit/GAP_MASTER_TRACKER.csv")

# Create EVIDENCE_REGISTER.csv
evidence_data = [
    ["EVD-INT-001", "Internal", "https://hellogrowthcrm.com", "HTTP/1.1 Probe", "HTTP 200 OK, Cloudflare CDN, Cookie: hgcrm_geo=IN, CSP active", "HIGH", "2026-10-30"],
    ["EVD-INT-002", "Internal", "https://test.hellogrowthcrm.com", "HTTP/1.1 Probe", "HTTP 200 OK, Vite SPA Shell, build version 1793254901284", "HIGH", "2026-10-30"],
    ["EVD-INT-003", "Internal", "index-JdadhMLI.js", "AST Analysis", "60 public, assessment, portal, and Shopify routes", "HIGH", "2026-10-30"],
    ["EVD-INT-004", "Internal", "CRMShell-DFzCAfVT.js", "AST Analysis", "17 lazy auth chunks and 18 top-level routes (/login, /signup, /mfa)", "HIGH", "2026-10-30"],
    ["EVD-INT-005", "Internal", "CRMInnerShell-BIK42-oV.js", "AST Analysis", "42 core operational views and 85 authenticated routes", "HIGH", "2026-10-30"],
    ["EVD-INT-006", "Internal", "viewRegistry-Cj7VM8pO.js", "AST Analysis", "367 unique view components across 33+ specialized business verticals", "HIGH", "2026-10-30"],
    ["EVD-INT-007", "Internal", "freePlanCaps-RFIY9lmq.js", "Bundle Decompilation", "Hardcoded cap: const a=()=>'150 leads'", "HIGH", "2026-10-30"],
    ["EVD-INT-008", "Internal", "tenantFeatureFlags-DOpu3csW.js", "Source Analysis", "Supabase query: s.from('tenant_feature_flags').select('is_enabled')", "HIGH", "2026-10-30"],
    ["EVD-INT-009", "Internal", "integrationScopes-COvQAOgT.js", "Source Analysis", "14 OAuth-style scopes (leads:read/write, deals:read/write, orders:read/write)", "HIGH", "2026-10-30"],
    ["EVD-INT-010", "Internal", "appWebhooks-D0Plx3Jk.js", "Source Analysis", "53 discrete event types (deal.won, whatsapp.message_received, invoice.paid)", "HIGH", "2026-10-30"],
    ["EVD-INT-011", "Internal", "https://mcp.hellogrowthcrm.com", "Live MCP Scan", "Operational knowledge server with 77 tools; unlisted in official registry", "HIGH", "2026-10-30"],
    ["EVD-INT-012", "Internal", "pricing-constants.ts", "File Read", "List price: USD_MONTHLY = 12, USD_ANNUAL = 10, INR_MONTHLY = 899 (+18% GST)", "HIGH", "2026-10-30"],
    ["EVD-INT-013", "Internal", "currency_settings", "Handover U58 Audit", "Open update permissions on currency_settings allowing standard members write access", "HIGH", "2026-10-30"],
    ["EVD-INT-014", "Internal", "PayU Discrepancy", "Handover U54 & Code Scan", "PayU listed on marketing copy; zero gateway integration code present in backend", "HIGH", "2026-10-30"],
    ["EVD-CMP-001", "Competitor", "Salesforce Sales Cloud", "Vendor Pricing / Docs", "Starter ($25) strips workflows; Pro ($100); WhatsApp 3rd-party only; Agentforce $$$", "HIGH", "2026-10-29"],
    ["EVD-CMP-002", "Competitor", "HubSpot Sales Hub", "Vendor Pricing / Docs", "Starter ($20); Pro ($100) + $1,500 onboarding; sequences locked to Pro; contact penalties", "HIGH", "2026-10-29"],
    ["EVD-CMP-003", "Competitor", "Zoho CRM", "Vendor Pricing / Docs", "Standard ($14); Pro ($23); Zia AI locked to Enterprise ($40); Zoho Voice separate", "HIGH", "2026-10-29"],
    ["EVD-CMP-004", "Competitor", "Freshsales", "Vendor Pricing / Docs", "Growth ($15); Pro ($39); sequences on Pro; Freddy AI metered; calls extra", "HIGH", "2026-10-29"],
    ["EVD-CMP-005", "Competitor", "Pipedrive", "Vendor Pricing / Docs", "Essential ($14) disables email sync; Pro ($49); LeadBooster ($32.50) add-on; no WA", "HIGH", "2026-10-29"],
    ["EVD-CMP-006", "Competitor", "Microsoft Dynamics 365", "Vendor Pricing / Docs", "Professional ($65) caps tables at 15; Enterprise ($105); steep partner setup", "HIGH", "2026-10-30"],
    ["EVD-CMP-007", "Competitor", "monday sales CRM", "Vendor Pricing / Docs", "Basic ($12); Pro ($28); strict 3-seat min ($51/mo min); Standard caps 250 automations", "HIGH", "2026-10-30"],
    ["EVD-CMP-008", "Competitor", "Close CRM", "Vendor Pricing / Docs", "Solo ($14); Pro ($49); inside sales focus; lacks quotes, invoices, field sales", "HIGH", "2026-10-29"],
    ["EVD-CMP-009", "Competitor", "GoHighLevel", "Vendor Pricing / Docs", "Starter ($97); Unlimited ($297); Twilio markups add $200-$1,000/mo; weak B2B ERP", "HIGH", "2026-10-29"],
    ["EVD-CMP-010", "Competitor", "Attio CRM", "Vendor Pricing / Docs", "Plus ($35); Pro ($79) locks custom objects; workspace credits meter AI/workflows", "HIGH", "2026-10-30"],
    ["EVD-CMP-011", "Competitor", "LeadSquared", "Vendor Pricing / Docs", "Lite (₹1,250); Super (₹4,500); annual lock-in; strong field GPS; dated UI", "HIGH", "2026-10-30"],
    ["EVD-CMP-012", "Competitor", "Kylas CRM", "Vendor Pricing / Docs", "Flat ₹12,999/mo unlimited users; high entry threshold for <10 reps; lacks proposals", "HIGH", "2026-10-30"],
    ["EVD-CMP-013", "Competitor", "Kommo CRM", "Vendor Pricing / Docs", "Base ($15); Pro ($45); annual commit; strong messenger inbox; lacks B2B quotes/invoices", "HIGH", "2026-10-30"],
    ["EVD-CMP-014", "Competitor", "Bitrix24", "Vendor Pricing / Docs", "Flat 5-50 users; extreme UI bloat (100+ menus); low storage caps; sluggish support", "HIGH", "2026-10-29"]
]

ev_header = ["Evidence ID", "Category", "Source Target", "Verification Method", "Verified Findings / Code Proof", "Confidence Level", "Verification Date"]
with open("d:/Firecrawl/research/hellogrowth-competitive-audit/EVIDENCE_REGISTER.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(ev_header)
    writer.writerows(evidence_data)

print("Generated EVIDENCE_REGISTER.csv and copied matrices.")

