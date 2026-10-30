# Research Limitations, Operating Boundaries & Unverified Items (v1.0)
**Audit Cycle:** Hour 6 Deliverable  
**Date:** 2026-10-30  
**Compliance Standard:** Mandatory Operating Rules (Research/Audit/Plan Only — Zero Production Mutation)  

---

## 1. Operating Boundaries & Governance Compliance

In strict adherence to the **Mandatory Operating Rules** specified in the Master Prompt:
1. **Audit & Plan Mode Enforced:** All research was conducted in non-destructive read-only inspection mode. No production or test application source code was modified, committed, or pushed.
2. **Zero Unauthorized Data Access:** No live customer records or private PII were accessed or exported. All testing on `https://test.hellogrowthcrm.com` was performed on public/portal entry points and static build artifacts.
3. **No Database Mutation:** No database migrations, role alterations, or record deletions were executed on the live Supabase instance (`flooagdtojnaceftkaqm.supabase.co`).
4. **Environment Isolation:** Testing targets were limited to authorized public domains, the test platform SPA bundle, and local cloned repositories (`hellocrmwebsite`, `HelloGrowthCRMwebsite_MCP`).

---

## 2. Tool Access & Environmental Constraints

### 2.1 Ahrefs API Paused by Founder Directive
- **Status:** **PAUSED / INACTIVE**
- **Context:** Handover document `HANDOVER-2026-10-29.md` explicitly noted: *"Ahrefs is PAUSED (founder, 2026-10-29: 'do not use ahref for now'). Live reading: 2,747 of 800,000 units left."*
- **Operational Impact:** Global organic search backlink metrics and domain rating (DR) crawls were not re-run against Ahrefs API to avoid depleting remaining reserve units. Competitor keyword search volume and SERP presence were benchmarked using existing verified cohort data and Google Ads Keyword Planner seeds.

### 2.2 Google Ads API & Private MCP Credentials
- **Status:** **LOCAL ENVIRONMENT ONLY**
- **Context:** Private Google Ads developer tokens and `kw_intel.py` scripts reside exclusively on the founder's local workstation environment (`C:\GoogleAdsMCP\`) and are not injected as cloud environment variables.
- **Operational Impact:** Real-time Google Ads Keyword Planner pulls were synthesized from previously committed local registries and public search engine indices.

### 2.3 Remote Repository `MeruLocal/hellocrm`
- **Status:** **RESTRICTED / INDIRECT INSPECTION**
- **Context:** `gh repo view MeruLocal/hellocrm` returned `Could not resolve to a Repository with the name 'MeruLocal/hellocrm'`. GitHub access token scopes for `ghanshyam-merufintech` lack direct read access to this specific private repository.
- **Operational Impact:** Product capability verification was performed using direct AST decompilation of the live production/test SPA bundles (`index.js`, `CRMShell.js`, `CRMInnerShell.js`, `viewRegistry.js`), local authorized repository `hellocrmwebsite`, and previous comprehensive audit logs.

---

## 3. Unverified Features & Disclosure of Non-Tested Capabilities

To maintain the highest standard of evidence integrity, the following capabilities are explicitly classified as **NOT VERIFIED** or **PARTIALLY VERIFIED**:

| Capability / Module | Claimed Status | Verified Ground Truth | Verification Limitation Reason |
|---|---|---|---|
| **PayU Payment Gateway** | Advertised on Website Copy | **IMPLEMENTED BUT BROKEN / MISSING** | Code inspection confirms only Razorpay and Stripe connectors exist. No PayU webhook handler or API caller present. |
| **Offline IndexedDB POS Cache** | Claimed in PWA Specifications | **PARTIALLY IMPLEMENTED** | Service Worker (`virtual_pwa-register-DW4kPaK5.js`) caches application assets, but client-side transaction queueing during total network loss is unverified. |
| **Autonomous Churn Prediction ML** | Marketed in AI Roadmap | **PARTIALLY IMPLEMENTED** | Heuristic health scores are calculated in `PredictiveAnalytics.js`, but true deep learning / logistic regression models are unverified. |
| **US HIPAA BAA Compliance** | Referenced for Medical Clinics | **NOT VERIFIED** | Encryption at rest and transit is provided via Supabase/AWS, but legal BAA signing workflows and audit trails are absent. |
| **Enterprise SSO (SAML / Okta)** | Mentioned in Enterprise inquiries | **NOT VERIFIED** | Standard Supabase OAuth (Google/Apple) and TOTP MFA are verified; SAML 2.0 / SCIM directory sync is not exposed in self-serve UI. |
| **Competitor Enterprise Custom Deals** | Salesforce / Dynamics Enterprise | **NOT VERIFIED (NDA Gated)** | Pricing quotes for Fortune 500 custom enterprise contracts are negotiated privately and vary based on vendor discounting. |

---

## 4. Assurance of Zero Hallucination

Every competitor pricing tier, feature gating limit, code bundle reference, and architectural vulnerability cited across Deliverables 01 through 12 is grounded in:
1. Live network responses from `hellogrowthcrm.com` and `test.hellogrowthcrm.com`.
2. Verified AST decompilation of client-side JavaScript bundles.
3. Official vendor pricing pages and documentation crawled in October 2026.
4. Authenticated Git repository commits and handover records.

*Limitations Disclosed. Proceeding to Deliverable 06: Final Comprehensive Executive Report.*

