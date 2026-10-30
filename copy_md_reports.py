import shutil
import os

base_in = "d:/Firecrawl"
base_out = "d:/Firecrawl/research/hellogrowth-competitive-audit"

shutil.copyfile(f"{base_in}/03_Functional_and_Industry_Gaps.md", f"{base_out}/INDUSTRY_GAPS.md")
shutil.copyfile(f"{base_in}/04_UI_UX_AI_Technical_Gaps.md", f"{base_out}/UI_UX_AUDIT.md")
shutil.copyfile(f"{base_in}/05_Prioritized_Implementation_Backlog.md", f"{base_out}/IMPLEMENTATION_BACKLOG.md")
shutil.copyfile(f"{base_in}/06_Final_Executive_Report.md", f"{base_out}/FINAL_RESEARCH_REPORT.md")

print("Copied primary markdown reports to hellogrowth-competitive-audit directory.")

