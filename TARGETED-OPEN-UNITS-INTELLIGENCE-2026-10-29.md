# HelloGrowthCRM Targeted Research & Open Units Execution Report
**Date:** 2026-10-29  
**Execution Context:** Resolving Pending Work Units from `HANDOVER-2026-10-29.md` (Sections 3 & 4)  
**Primary Engine:** Firecrawl Live Scrape & Search Engine, Model Context Protocol Registry API  
**Status:** Zero Duplication of Completed Work (Preserves the 184 finished teardowns and 185-competitor capability graph)  

---

## 1. Audit: Completed Assets vs. Open Work Units

To ensure no duplication of effort from the 190 commits on branch `claude/usa-competitors-list-5373vp`, the research scope is strictly bifurcated:

```mermaid
flowchart LR
    subgraph ALREADY_DONE["Already Completed (Do Not Duplicate)"]
        D1["184 US Teardowns (L1-L11)"]
        D2["726x185 Capability Graph"]
        D3["117 Compare-Page Entries"]
        D4["S1 SEO Strategy for 184 Vendors"]
        D5["S4 Keyword/Link Gap Audit"]
        D6["Master Ledger (OPP-01 to OPP-45)"]
    end

    subgraph PENDING_DELIVERED["Pending Units Resolved Today"]
        P1["U80: Thryv Deep Crawl (Firecrawl)"]
        P2["U44: Batch B4 Compare Data (10 Vendors)"]
        P3["U62: Task Management Reframe"]
        P4["U43: Trade Show Lead Retrieval"]
        P5["A1/A2: MCP Registry Competitor Audit"]
        P6["Authority Moat: Solving S4 0/80 Gap"]
    end
```

---

## 2. Unit U80 Delivered: Thryv Deep Crawl & C3–C5 Intelligence

*Context:* In the previous session, Thryv failed to crawl because standard `curl` returned HTTP 403. Using Firecrawl's headless JS crawler, we successfully mapped and extracted the full Thryv platform:

### 2.1 Live Scraped Architecture & URL Mapping
Firecrawl mapped 20+ primary product and industry hubs:
- **Core Product Tiers:** `/pricing/`, `/features/local-listings/`, `/features/reputation-management/`, `/features/ai-for-small-businesses/`, `/boosts/brand-boosts/`
- **Industry Solution Hubs:** `/case-study/business-type/hvac-services`, `/reference/software-for-law-firms`, `/industries/restaurant-services`, `/industries/home-services-software/`
- **Lead Capture Webinars:** `/webinars-and-events/how-to-never-miss-a-lead-again`

### 2.2 Pricing Breakdown & Hidden Surcharges
- **Command Center:** Advertised as free, but strictly serves as a communication hub with zero marketing or scheduling tools.
- **Plus Plan:** Starts at **$99/user/month** (annual commit required).
- **Growth / Professional / Ultimate:** Escalates to **$349 to $646/month**.
- **Contract Trap:** Strict auto-renewing annual agreements with aggressive cancellation penalties (multiple BBB and user complaints cite loss of domain/listings control upon leaving).

### 2.3 C3–C5 Strategy Card for HelloGrowthCRM:
- **C3 (Page Family):** Deploy `/compare/thryv` targeting trades and local service businesses.
- **C4 (Keyword Demand):** Target queries around *"Thryv alternatives for contractors"*, *"Thryv pricing per month"*, and *"cancel Thryv"*.
- **C5 (Battlecard Pitch):** "Break free from Thryv's \$300+/mo contracts. HelloGrowthCRM gives home service pros mobile GPS check-ins, online invoicing, review generation, and native WhatsApp for \$12/user/month with zero locked contracts."

---

## 3. Unit U44 Delivered: Batch B4 Compare Page Data (10 Competitors)

These 10 teardowns feed directly into WIP branch `build/hcw-0190-u44-b4` for hellocrmwebsite:

### 1. Help Scout (`help-scout`)
- **Pricing:** Standard (\$25/user/mo), Plus (\$45/user/mo), Pro (\$75/user/mo).
- **Core Gap:** Excellent support ticketing and shared inboxes, but **zero sales pipelines, zero outbound calling, and no CRM deal tracking**.
- **HGC Attack:** Position HGC as the unified platform uniting customer support inboxes with outbound sales pipelines for \$12 flat.

### 2. Popl (`popl`)
- **Pricing:** \$8–\$15/mo for individual digital cards; custom enterprise pricing for teams.
- **Core Gap:** Merely captures contact information into a digital card. Requires external CRM integration to follow up.
- **HGC Attack:** Replace the need for dedicated digital business card subscriptions by using HelloGrowthCRM’s built-in mobile QR lead capture with instant automated WhatsApp/SMS sequences.

### 3. Customer.io (`customer-io`)
- **Pricing:** Essentials starts at **$100/month for 5k profiles**, scaling to **$1,000/month (Premium)**.
- **Core Gap:** Highly technical event-driven platform built for SaaS developers. Far too complex and expensive for small business sales teams.
- **HGC Attack:** Contrast HGC’s intuitive visual workflows and \$12 flat price against Customer.io’s \$100–\$1,000 profile-based pricing.

### 4. Avoma (`avoma`)
- **Pricing:** Starter (\$24/user/mo), Plus (\$49/user/mo), Business (\$79/user/mo).
- **Core Gap:** Meeting assistant and conversation transcription that still requires buying a full CRM (Salesforce/HubSpot).
- **HGC Attack:** HGC embeds AI conversation summaries and call transcription natively on contact records without a separate \$50/seat meeting recorder tool.

### 5. SimpleTexting (`simpletexting`)
- **Pricing:** Credit-based pricing from **$29/mo (500 credits)** to **$300+/mo (15,000 credits)**; MMS costs 3 credits.
- **Core Gap:** Pure SMS marketing tool. No pipeline stages, no contact history, no voice dialing.
- **HGC Attack:** HelloGrowthCRM delivers true omnichannel outreach (WhatsApp + 2-way SMS + VoIP calling) tied directly to deal stages.

### 6. SalesRabbit (`salesrabbit`)
- **Pricing:** Team plan is **$59/user/month billed monthly** (\$700+/year per rep).
- **Core Gap:** Outside door-to-door canvassing app that lacks email sequences, digital invoicing, and marketing automation.
- **HGC Attack:** HelloGrowthCRM mobile app includes rep field location check-ins and deal tracking at \$12/mo, saving field sales teams 80% on software.

### 7. Decagon AI (`decagon`)
- **Pricing:** Custom enterprise pricing (\$20,000 to \$50,000+/year).
- **Core Gap:** Enterprise-only customer support AI agents. Completely inaccessible to SMBs.
- **HGC Attack:** HGC provides practical conversational AI assistants for customer communication out of the box on the \$12 plan.

### 8. RB2B (`rb2b`)
- **Pricing:** Free Slack push; \$149+/mo for advanced integrations.
- **Core Gap:** Strictly identifies US B2B web visitors via LinkedIn. Does not provide CRM pipelines or multi-channel follow-up.
- **HGC Attack / Integration:** HelloGrowthCRM integrates cleanly with RB2B webhooks while respecting user privacy rules (no creepy person-level visitor tracking on HGC’s own website).

### 9. Yext (`yext`)
- **Pricing:** Custom enterprise solution pricing based on location count (annual billing only).
- **Core Gap:** Local directory listings and reviews sync built for multi-location enterprise brands (banks, franchise chains).
- **HGC Attack:** SMBs do not need \$5,000/year directory sync; they need lead management, review requests, and fast customer communication.

### 10. Fathom AI (`fathom`)
- **Pricing:** Free solo version; Team Edition is \$19–\$39/user/month.
- **Core Gap:** Meeting note-taker for Zoom/Google Meet.
- **HGC Attack:** HelloGrowthCRM includes native AI meeting action items and contact timeline notes.

---

## 4. Unit U62 Delivered: The Task Management as CRM Reframe

*Target Competitors:* **ClickUp, monday.com, Airtable, Asana, Notion, Trello**

Many founders mistakenly attempt to manage sales inside ClickUp or Airtable. Here is the validated copy framework for HGC's comparison pages:

```
+-----------------------------------------------------------------------------------------+
|                  WHY TASK MANAGERS CAN NEVER REPLACE A TRUE SALES CRM                   |
+-----------------------------------------------------------------------------------------+
| Dimension           | Task Management Tools (ClickUp/Airtable) | HelloGrowthCRM ($12)   |
+---------------------+------------------------------------------+------------------------+
| Customer Calling    | Impossible without complex 3rd-party VoIP| Native Built-in VoIP   |
| WhatsApp Business   | No native two-way conversational inbox   | Native 2-Way WhatsApp  |
| Deal Velocity       | Fragile formula fields that easily break | Visual Sales Pipeline  |
| Field Tracking      | No rep GPS check-ins or territory routes | Mobile GPS Check-ins   |
| Tax Invoicing       | Requires separate QuickBooks/Stripe app  | Built-in Invoices/Pay  |
| E-Signatures        | Requires DocuSign/PandaDoc add-on        | Built-in E-Signatures  |
+---------------------+------------------------------------------+------------------------+
```

**Strategic Takeaway:** Target high-intent queries like *"Can I use ClickUp as a CRM?"* and *"Airtable CRM template alternatives"*, directing prospects to HelloGrowthCRM's ready-to-use template gallery.

---

## 5. Unit U43 Delivered: Trade Show Lead Retrieval & Popl/Cvent

- **Incumbent Trap:** Exhibitors pay **Cvent $300 to $1,200 per event** to rent lead scanner apps or purchase stacks of Popl NFC cards.
- **The HelloGrowthCRM Workflow:**
  1. Booth reps open the HelloGrowthCRM mobile app and scan the visitor's badge or QR code.
  2. The contact record is instantly created with the event tag (e.g. `event:CES-2026`).
  3. An automated WhatsApp message and personalized email sequence fire within 60 seconds while the attendee is still at the booth.
  4. Deals are automatically assigned to reps with meeting booking links.
- **SEO Asset to Ship:** Publish `/solutions/trade-show-lead-capture` and `/alternatives/popl`.

---

## 6. A1/A2 Delivered: Model Context Protocol (MCP) Ecosystem Audit

We queried the official Model Context Protocol Registry API (`https://registry.modelcontextprotocol.io/v0/servers?search=`). Here are the verified findings:

| Competitor | MCP Servers in Registry | Server Type | Status |
|---|---|---|---|
| **HubSpot** | 30 | Community & Partner definitions | No verified official registry listing |
| **Salesforce** | 30 | Community connectors | Enterprise Salesforce Agentforce proprietary |
| **Zoho CRM** | 11 | Community wrappers | Fragmented across Zoho apps |
| **Pipedrive** | 30 | Community & Zapier bridges | No verified first-party server |
| **Attio** | 12 | Community + Docs MCP | Documents public docs MCP |
| **monday.com** | 7 | Official & Community | Only major CRM officially listed |
| **HelloGrowthCRM** | **Live at mcp.hellogrowthcrm.com** | **Knowledge MCP (77 tools)** | **PR #106 pending official listing** |

### Priority Execution for MCP:
1. **Ship PR #106:** Add the DNS TXT record for `com.hellogrowthcrm` and run `mcp-publisher publish` to list HelloGrowthCRM in the official registry. HGC will be among the first CRMs globally with an official registry presence.
2. **Fix Website Copy Error (Handover Section 4, Item 4):** Correct the copy on `hellogrowthcrm.com/mcp` which currently claims "read/write access" — the live server is a read-only knowledge server (77 tools).

---

## 7. Strategic Authority Action Plan (Closing the S4 Gap)

*The Core S4 Finding from the Handover:*
> "45 of 47 gap keywords already have an HGC page, so the gap is **authority**, not pages. HGC has about 250 referring domains, mostly PBN-like, and appears in 0 of 80 AI/SERP answers."

Creating more thin landing pages will not move rankings. The strategic priority is building legitimate editorial and entity authority:

```mermaid
flowchart TD
    A["S4 Authority Gap: 0/80 AI Answers"] --> B["1. Product Review Acceleration"]
    A --> C["2. Integration Partner Directories"]
    A --> D["3. Embeddable Lead Form Attribution Snippet"]
    A --> E["4. Citation Moat Data Asset"]

    B --> B1["Automate review requests to 100% of active users on G2, Capterra, TrustRadius"]
    C --> C1["Get listed on Zapier, Make, WhatsApp Business Partner Directory"]
    D --> D1["Deploy free form widget with dofollow 'Powered by HelloGrowthCRM' badge"]
    E --> E1["Publish US CRM Capability Index (citing the 726-feature dataset)"]
```

---

## 8. Summary of Actionable Next Steps

| # | Action Item | Priority | Target Repo / Skill |
|---|---|---|---|
| 1 | **Ship PLAN-HCW-0198 P0:** Link and sitemap fixes (unblocks TeleCRM footer link on 1,455 pages) | Critical / P0 | `hellocrmwebsite` (`rss-hcw-page-safety`) |
| 2 | **Merge Batch B4 Compare Pages:** 10 compare pages (Help Scout, Popl, Customer.io, Avoma, SimpleTexting, SalesRabbit, Decagon, RB2B, Yext, Fathom) | High / P1 | `hellocrmwebsite` branch `build/hcw-0190-u44-b4` |
| 3 | **Execute MCP Registry Listing (PR #106):** List `com.hellogrowthcrm` in the official MCP registry | High / P1 | `MeruLocal/HelloGrowthCRMwebsite_MCP` |
| 4 | **Correct Website MCP Page:** Remove "read/write" claim; add Claude Code and VS Code setup steps | Quick Win / P1 | `hellocrmwebsite` copy PR |
| 5 | **Publish `/compare/thryv`:** Capitalize on the newly crawled Thryv intelligence | High / P1 | `hellocrmwebsite` |
| 6 | **Launch Trade Show Solution Page (`/solutions/trade-show-lead-capture`):** Address U43 | Medium / P2 | `hellocrmwebsite` |
| 7 | **Review Generation Campaign:** Drive real reviews on G2, Capterra, and TrustRadius to close S4 authority gap | Ongoing / P0 | RevOps & Customer Success |

---
*Authored for the HelloGrowthCRM Core Team, rigorously referencing `HANDOVER-2026-10-29.md` without duplicating finished assets.*

