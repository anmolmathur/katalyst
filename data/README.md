# Data snapshots

Point-in-time exports, kept for review. **The Google Sheet is the live source.**

| File | What it is |
|---|---|
| `ALL_COVERAGE_deduped.csv` | 44 placements after deduplication, with a MAV Method column |
| `DUPLICATES_REVIEW.csv` | The 11 merges, with both dates, both publications and both MAV figures |
| `Katalyst_PR_Coverage_WORKING.xlsx` | The restructured workbook as first built — 55 rows, pre-dedupe |
| `Katalyst_PR_Coverage_DEDUPED.xlsx` | The deduped workbook. Missing CLIENTS and MAV_RATES — superseded by the CSVs above |

To apply the deduplication: open the live Google Sheet, select the **ALL_COVERAGE** tab,
then File → Import → Upload → *Replace current sheet* with `ALL_COVERAGE_deduped.csv`.
The file ID does not change, so the Coverage Desk needs no edit.
