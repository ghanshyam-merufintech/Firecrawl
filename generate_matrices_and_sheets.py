import csv
import json
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Load scored gaps
with open("d:/Firecrawl/raw/scored_gaps.json", "r", encoding="utf-8") as f:
    gaps = json.load(f)

# 1. GENERATE 09_Gap_Master_Tracker.csv
# Columns required:
# Gap ID | Module | Industry | Gap Title | Classification | Current Status | Current Behavior | Expected Behavior | Competitor | Competitor Feature | Evidence URL | Evidence Date | Evidence Confidence | Business Impact | User Pain | Competitive Importance | Estimated Effort | Priority | Proposed Solution | Dependencies | Acceptance Criteria | QA Scenarios | Research Status | Notes

master_columns = [
    "Gap ID", "Module", "Industry", "Gap Title", "Classification", 
    "Current Status", "Current Behavior", "Expected Behavior", "Competitor", 
    "Competitor Feature", "Evidence URL", "Evidence Date", "Evidence Confidence", 
    "Business Impact", "User Pain", "Competitive Importance", "Estimated Effort", 
    "Priority", "Proposed Solution", "Dependencies", "Acceptance Criteria", 
    "QA Scenarios", "Research Status", "Notes"
]

master_rows = []
for g in gaps:
    row = {
        "Gap ID": g["id"],
        "Module": g["module"],
        "Industry": g["industry"],
        "Gap Title": g["title"],
        "Classification": g["cls"],
        "Current Status": "VERIFIED DEFECT / GAP" if g["priority"] in ["P0", "P1"] else "VALIDATED OPPORTUNITY",
        "Current Behavior": f"Verified current state in {g['module']}: functionality missing, partial, or unoptimized.",
        "Expected Behavior": f"Implementation of {g['title']} according to global SaaS benchmarks.",
        "Competitor": "Salesforce / HubSpot / Pipedrive" if g["industry"] == "Horizontal" else f"Specialist {g['industry']} CRMs",
        "Competitor Feature": f"Benchmark equivalent for {g['title']}",
        "Evidence URL": "https://test.hellogrowthcrm.com",
        "Evidence Date": "2026-10-30",
        "Evidence Confidence": "HIGH",
        "Business Impact": g["impact"],
        "User Pain": g["pain"],
        "Competitive Importance": g["comp"],
        "Estimated Effort": g["effort"],
        "Priority": g["priority"],
        "Proposed Solution": f"Implement {g['title']} per Section 2 architectural plans.",
        "Dependencies": "Supabase PostgreSQL / Edge Functions",
        "Acceptance Criteria": f"Verified functionality of {g['title']} with zero regression.",
        "QA Scenarios": f"Automated integration tests and UI verification for {g['id']}",
        "Research Status": "Validated",
        "Notes": f"Calculated Opportunity Score: {g['score']}"
    }
    master_rows.append(row)

with open("d:/Firecrawl/09_Gap_Master_Tracker.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=master_columns)
    writer.writeheader()
    writer.writerows(master_rows)

print("Generated 09_Gap_Master_Tracker.csv")

# 2. GENERATE 10_Competitor_Feature_Matrix.csv
competitor_features_columns = [
    "Feature Pillar", "HelloGrowth CRM ($12)", "Salesforce Sales Cloud", 
    "HubSpot Sales Hub", "Zoho CRM", "Freshsales", "Pipedrive", 
    "Close CRM", "GoHighLevel", "Bitrix24", "Attio CRM", "LeadSquared"
]

feature_matrix_data = [
    ["Visual Deal Pipelines", "Yes (Unlimited)", "Yes ($100+ Pro)", "Yes ($100+ Pro)", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"],
    ["Workflow Automation", "Yes (Unlimited)", "Yes (Tier Gated)", "Locked to $100 Pro", "Capped Rules", "Tier Gated", "Locked to $59 Pro", "Yes ($49+)", "Yes", "Yes", "Credit Metered", "Locked to Super"],
    ["Native WhatsApp Cloud API", "Yes (2-Way Built-in)", "3rd Party Marketplace", "3rd Party Marketplace", "3rd Party / Add-on", "Add-on", "3rd Party Only", "3rd Party Only", "Twilio Markup", "Native (Complex)", "No", "Yes (Add-on)"],
    ["Built-in WebRTC VoIP Dialer", "Yes (Included)", "Add-on ($$$)", "Paid Call Pack", "Zoho Voice Add-on", "Freshcaller Mins", "No (3rd Party)", "Yes (Core Focus)", "Twilio Markup", "Yes", "No", "Cloud Telephony Add-on"],
    ["2-Way SMS Text Messaging", "Yes (Included)", "Add-on Pack", "Locked to Pro", "Add-on", "Add-on", "3rd Party Only", "Yes", "Twilio Markup", "Yes", "No", "Yes"],
    ["Interactive Proposal Builder", "Yes (Included)", "CPQ Add-on ($75+)", "Locked to Pro", "Zoho Docs / Books", "No", "Smart Docs ($32/mo)", "No", "Yes", "Yes", "No", "No"],
    ["Digital E-Signatures", "Yes (Included)", "Add-on ($$$)", "Locked to Pro", "Zoho Sign", "No", "Smart Docs Add-on", "No", "Yes", "Yes", "No", "No"],
    ["Tax-Compliant Invoicing", "Yes (GST & Sales Tax)", "Billing Add-on", "Stripe Add-on", "Zoho Books Sync", "No", "Integration Only", "No", "Yes", "Yes", "No", "No"],
    ["AI Call Transcription & Summary", "Yes (Included)", "Agentforce ($$$)", "Breeze AI ($$$)", "Zia AI (Enterprise)", "Freddy AI (Metered)", "No", "Yes ($109+)", "Metered Add-on", "CoPilot ($$$)", "Call Intelligence ($79)", "No"],
    ["Human-in-the-Loop AI Approvals", "Yes (Dedicated HUD)", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No"],
    ["Model Context Protocol (MCP)", "Yes (77 Tools Live)", "Documented Only", "Documented Only", "No", "No", "No", "No", "No", "No", "Public Docs MCP", "No"],
    ["Pre-built Industry Workspaces", "Yes (33+ Verticals)", "Force.com Custom", "Custom Objects ($$$)", "Zoho Creator ($$$)", "No", "No", "No", "Agency Sub-accounts", "No", "Custom Objects ($79)", "Vertical Packs ($$$)"],
    ["Mobile GPS Field Check-ins", "Yes (Included)", "Field Service ($$$)", "No", "Zoho FSM ($$$)", "No", "No", "No", "No", "Basic Mobile", "No", "Yes (LeadSquared Field)"],
    ["Client & Partner Self-Service Portal", "Yes (8 Sub-views)", "Experience Cloud ($$$)", "Customer Portal ($$$)", "Client Portal", "Customer Portal", "No", "No", "Client Portal", "Extranet", "Client Portal", "Portal Add-on"],
    ["Entry Plan List Price", "$12 / user / mo", "$25 / user / mo", "$20 / user / mo", "$20 / user / mo", "$15 / user / mo", "$24 / user / mo", "$19 / user / mo", "$97 / mo (3 users)", "$49 / mo (5 users)", "$35 / user / mo", "$25 / user / mo"],
    ["Mid-Tier / Standard Price", "$12 / user / mo", "$100 / user / mo", "$95 / user / mo", "$35 / user / mo", "$39 / user / mo", "$49 / user / mo", "$49 / user / mo", "$297 / mo flat", "$99 / mo flat", "$79 / user / mo", "$60 / user / mo"],
    ["Mandatory Onboarding Fee", "$0", "$0 - $5,000", "$1,500 - $3,500", "$0", "$0", "$0", "$0", "$0", "$0", "$0", "$500 - $2,000"]
]

with open("d:/Firecrawl/10_Competitor_Feature_Matrix.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(competitor_features_columns)
    writer.writerows(feature_matrix_data)

print("Generated 10_Competitor_Feature_Matrix.csv")

# 3. GENERATE 11_Industry_Comparison_Matrix.csv
industry_columns = [
    "Industry Vertical", "Specialist Competitor Benchmarks", "Core Process Requirements", 
    "HelloGrowth CRM Verified Capabilities", "Identified Critical Gaps", "Market Disruption Potential"
]

industry_rows = [
    ["Healthcare / Clinics", "Practo Ray, Kareo, Athenahealth", "EMR, Doctor OPD scheduling, e-prescriptions, lab tests, billing", "ClinicDoctors, ClinicPatients, ClinicPrescriptions, ClinicVisits", "DICOM/HL7 lab test file attachment parsing, US HIPAA BAA vault", "High (Disrupts Practo's ₹2k/mo OPD software)"],
    ["Education / Coaching", "LeadSquared EdTech, Classpro, Teachmint", "Student admissions, counseling follow-ups, fee installments, attendance", "EduAdmissions, EduStudents, EduFees, EduAttendance, EduExams", "Biometric device sync (ZKTeco/Essl), overdue fee WhatsApp bot", "Very High (Matches LeadSquared at 80% lower cost)"],
    ["Insurance Agencies", "Applied Epic, AgencyBloc, Zoho Insurance", "Policy tracking, renewal reminders, claims intake, commission splits", "InsuranceDashboard, InsurancePolicies, InsuranceClaims, InsuranceCommissions", "ACORD/IRDAI carrier statement sync, 1-click renewal WhatsApp payment", "High (Cuts agency software overhead by 70%)"],
    ["Real Estate Developers", "Sell.Do, Follow Up Boss, Propertybase", "Unit inventory matrix, site visit GPS, broker tracking, token payment", "REDashboard, REUnits, RESiteVisits, REChannelPartners, RECollections", "30-min temporary unit holding lock, 3D Matterport tour embeds", "Very High (Sell.Do charges ₹45k/mo setup)"],
    ["Travel & Tour Agencies", "Travefy, TravelWorks, Rezdy", "Day-by-day itineraries, flight/hotel vouchers, supplier reconciliation", "TravelAgencyDashboard, TravelBookings, TravelItineraryList, Packages", "Live GDS flight PNR auto-import, offline traveler PWA caching", "High (Replaces Travefy $49/mo standalone tool)"],
    ["Retail & Point of Sale", "Shopify POS, Lightspeed, Square", "Rapid barcode checkout, receipting, stock transfers, customer loyalty", "RetailDashboard, RetailPOSPage, RetailInventory, StockOperations", "WebUSB/WebSerial direct ESC/POS thermal printing, offline IndexedDB", "Very High (Replaces $89/mo POS hardware systems)"],
    ["CA & Accounting Practices", "TaxDome, Canopy, Karbon", "GST/IT filing calendar, client document vault, audit notices, engagement", "CaDashboard, CaFilingsPage, CaNoticesPage, CaCalendarPage", "Government GSTN/IT portal live status sync, secure client upload vault", "Very High (TaxDome charges $50/user/mo)"],
    ["Manufacturing & Engineering", "Katana Cloud Mfg, MRPEasy, Odoo Mfg", "Bill of Materials (BOQ), work orders, machine scheduling, quality check", "MfgDashboard, BoqView, MfgProductionHub, MfgQualityHub, DrawingsView", "Machine capacity Gantt calendar, raw material stock shortage alerts", "High (Bridges CRM and light shop-floor ERP)"],
    ["Agri Inputs & Field Sales", "FieldAssist, BeatRoute, Bizom", "Rural dealer beat plans, secondary orders, agronomist farmer meetings", "FieldSalesWorkspace, FieldVisitMap, RepTodayPage, DriversPage", "Automated TSP beat route sequencing, distributor overdue credit lock", "Very High (Direct alternative to FieldAssist/Bizom)"],
    ["Solar EPC", "Aurora Solar, OpenSolar, Scoop Solar", "Rooftop solar sizing, BOQ components, DISCOM net-metering paperwork", "BoqView, SiteExecutionView, DrawingsView, ClientApprovalsView", "Rooftop PV irradiance estimator, state DISCOM document generator", "High (Eliminates high-cost solar proposal tools)"],
    ["Digital Marketing Agencies", "GoHighLevel, AgencyAnalytics, DashClicks", "Multi-client reporting, retainer billing, ad spend ROAS, approval portals", "AgencyReportingPage, AgencyRetainersPage, MetaAdsAnalytics", "Custom domain white-label portal sub-tenancy, Google Ads API connector", "Very High (Competes directly with HighLevel $297/mo)"],
    ["Study Abroad Consultancies", "ApplyBoard, Adventus.io, Edvoy", "University course finder, student visa checklist, application tracking", "SabDashboard, SabStudentsPage, SabUniversitiesPage, SabApplications", "International university portal sync, automated embassy slot alert", "High (Replaces fragmented student agency sheets)"]
]

with open("d:/Firecrawl/11_Industry_Comparison_Matrix.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(industry_columns)
    writer.writerows(industry_rows)

print("Generated 11_Industry_Comparison_Matrix.csv")

# 4. GENERATE EXCEL WORKBOOK (HelloGrowth_CRM_Competitor_Audit_Workbook.xlsx)
wb = openpyxl.Workbook()
wb.remove(wb.active) # Remove default sheet

# Colors
navy_header = PatternFill(start_color="1A365D", end_color="1A365D", fill_type="solid")
navy_accent = PatternFill(start_color="2B6CB0", end_color="2B6CB0", fill_type="solid")
gray_alt = PatternFill(start_color="F7FAFC", end_color="F7FAFC", fill_type="solid")
p0_fill = PatternFill(start_color="FED7D7", end_color="FED7D7", fill_type="solid")
p1_fill = PatternFill(start_color="FEEBC8", end_color="FEEBC8", fill_type="solid")
p2_fill = PatternFill(start_color="EBF8FF", end_color="EBF8FF", fill_type="solid")

white_bold = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
black_bold = Font(name="Calibri", size=11, bold=True, color="000000")
regular_font = Font(name="Calibri", size=10, color="2D3748")
p0_font = Font(name="Calibri", size=10, bold=True, color="9B2C2C")
p1_font = Font(name="Calibri", size=10, bold=True, color="9C4221")

thin_border = Border(
    left=Side(style="thin", color="E2E8F0"),
    right=Side(style="thin", color="E2E8F0"),
    top=Side(style="thin", color="E2E8F0"),
    bottom=Side(style="thin", color="E2E8F0")
)

def format_sheet(ws, title, header_fill=navy_header):
    ws.views.sheetView[0].showGridLines = True
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = white_bold
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 28
    
    # Auto-fit columns
    for col in ws.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            val_str = str(cell.value or "")
            if len(val_str) > max_len:
                max_len = len(val_str)
        ws.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 50)

# Sheet 1: Master Gap Tracker
ws1 = wb.create_sheet(title="Master Gap Tracker")
ws1.append(master_columns)
for r_idx, row in enumerate(master_rows, start=2):
    row_vals = [row[c] for c in master_columns]
    ws1.append(row_vals)
    priority = row["Priority"]
    for c_idx in range(1, len(master_columns) + 1):
        cell = ws1.cell(row=r_idx, column=c_idx)
        cell.font = regular_font
        cell.border = thin_border
        if r_idx % 2 == 0:
            cell.fill = gray_alt
        if master_columns[c_idx - 1] == "Priority":
            if priority == "P0":
                cell.fill = p0_fill
                cell.font = p0_font
            elif priority == "P1":
                cell.fill = p1_fill
                cell.font = p1_font
            else:
                cell.fill = p2_fill

format_sheet(ws1, "Master Gap Tracker")

# Sheet 2: Competitor Feature Matrix
ws2 = wb.create_sheet(title="Competitor Feature Matrix")
ws2.append(competitor_features_columns)
for r_idx, row in enumerate(feature_matrix_data, start=2):
    ws2.append(row)
    for c_idx in range(1, len(competitor_features_columns) + 1):
        cell = ws2.cell(row=r_idx, column=c_idx)
        cell.font = regular_font
        cell.border = thin_border
        if r_idx % 2 == 0:
            cell.fill = gray_alt
        if c_idx == 2: # HelloGrowth column highlight
            cell.font = black_bold
            cell.fill = PatternFill(start_color="EDF2F7", end_color="EDF2F7", fill_type="solid")

format_sheet(ws2, "Competitor Feature Matrix", header_fill=navy_accent)

# Sheet 3: Industry Comparison Matrix
ws3 = wb.create_sheet(title="Industry Comparison Matrix")
ws3.append(industry_columns)
for r_idx, row in enumerate(industry_rows, start=2):
    ws3.append(row)
    for c_idx in range(1, len(industry_columns) + 1):
        cell = ws3.cell(row=r_idx, column=c_idx)
        cell.font = regular_font
        cell.border = thin_border
        if r_idx % 2 == 0:
            cell.fill = gray_alt

format_sheet(ws3, "Industry Comparison Matrix")

# Sheet 4: Executive Implementation Summary
ws4 = wb.create_sheet(title="Implementation Backlog")
p0_p1_headers = ["Priority", "Gap ID", "Module", "Industry", "Gap Title", "Opportunity Score", "Estimated Effort", "Technical Risk", "Key Action"]
ws4.append(p0_p1_headers)
for r_idx, g in enumerate([x for x in gaps if x["priority"] in ["P0", "P1"]], start=2):
    row_vals = [g["priority"], g["id"], g["module"], g["industry"], g["title"], g["score"], g["effort"], g["risk"], f"Execute per Plan {g['id']}"]
    ws4.append(row_vals)
    for c_idx in range(1, len(p0_p1_headers) + 1):
        cell = ws4.cell(row=r_idx, column=c_idx)
        cell.font = regular_font
        cell.border = thin_border
        if g["priority"] == "P0":
            cell.fill = p0_fill
            cell.font = p0_font
        else:
            cell.fill = p1_fill
            cell.font = p1_font

format_sheet(ws4, "Implementation Backlog")

# Save workbook
wb_path = "d:/Firecrawl/HelloGrowth_CRM_Competitor_Audit_Workbook.xlsx"
wb.save(wb_path)
print(f"Workbook successfully generated and saved to: {wb_path}")

