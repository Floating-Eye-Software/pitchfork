# Financial and Budgeting Client Notes

First pass based on the local material in `../financial/`.

## Source Inventory

The folder looks like a one-day collection of Canadian household finance reference material:

- Statistics Canada household economic account tables in CSV, database-loading CSV, SDMX XML, and ZIP form.
- Survey of Household Spending PDFs:
  - `62f0026m2020001-eng.pdf`: Survey of Household Spending Modelled Annual Statistics, 2010 to 2017.
  - `62f0026m2021001-eng.pdf`: User Guide for the Survey of Household Spending, 2019.
- `statscan.xlsx`, likely a manual workbook or extracted table bundle. I could not inspect sheet contents locally because `openpyxl` is not installed.

The dataset exports appear centered on household income, consumption, saving, wealth, and household counts. They are not transaction data and should be treated as reference baselines, benchmarks, and category scaffolding.

## StatCan Tables Present

| File | Table | Subject | Frequency / Dates Seen |
| --- | --- | --- | --- |
| `3610010101-eng.csv` | 36-10-0101-01 | Number of households by income quintile and socio-demographic characteristic | Annual, 2017-2021 |
| `3610058701-eng.csv` | 36-10-0587-01 | Income, consumption, and saving by characteristic | Annual, 2017-2021 |
| `3610058801-eng.csv` | 36-10-0588-01 | Income, consumption, and saving for Canada, provinces, and territories | Annual, 2017-2021 |
| `3610066101-eng.csv` | 36-10-0661-01 | Wealth, Canada, regions, and provinces | Quarterly, 2022-04 in local extract |
| `3610066201-eng.csv` | 36-10-0662-01 | Income, consumption, and saving by characteristic | Quarterly, 2022-04 in local extract |
| `3610066301-eng.csv` | 36-10-0663-01 | Income, consumption, and saving by geography | Quarterly, 2022-04 in local extract |
| `3610066401-eng.csv` | 36-10-0664-01 | Wealth indicators by characteristic | Quarterly, 2022-04 in local extract |
| `3610066501-eng.csv` | 36-10-0665-01 | Wealth indicators by geography | Quarterly, 2022-04 in local extract |
| `3610066701-eng.csv` | 36-10-0667-01 | Number of households by income quintile and socio-demographic characteristic | Quarterly, 2021-07 to 2022-04 |

The database-loading CSV files are the easiest ingestion target. They have stable machine-readable columns such as `REF_DATE`, `GEO`, `DGUID`, dimension columns, `UOM`, scalar fields, `VECTOR`, `COORDINATE`, `VALUE`, and status fields.

## Product Shape

The financial client should not start as "another bank app." The available data suggests a household budgeting and planning client that can combine:

- Personal or household ledgers entered by the user.
- Budget categories aligned to real-world household account categories.
- Benchmarks derived from public Canadian household data.
- Scenario planning for income, expenses, saving, debt, and wealth.
- Export or reporting views that preserve provenance and calculation logic.

The StatCan data can support context like "household disposable income," "consumption expenditure," "savings," "financial assets," "mortgage liabilities," "debt to disposable income ratio," and similar high-level concepts. It should not be used to infer an individual user's true circumstances without explicit user-entered data.

## Candidate Domain Model

Core records:

- `Household`: the client-side private planning unit.
- `Account`: bank, credit card, loan, cash, asset, or liability account.
- `Transaction`: dated inflow/outflow, imported or manually entered.
- `BudgetCategory`: user-facing spending or income category.
- `ReferenceCategory`: external classification from StatCan, GIFI, or another taxonomy.
- `BudgetPeriod`: month, quarter, year, or custom household cycle.
- `Plan`: a scenario with assumptions and targets.
- `Benchmark`: public-data comparison value with source metadata.
- `EvidenceRecord`: imported file, statement, receipt, or user attestation.

Important distinction:

- A household budget category is a user experience object.
- A tax/reporting category is a compliance object.
- A public-statistics category is a benchmark object.

These should map to each other where useful, but none should be treated as the canonical truth for all purposes.

## Budgeting Features

Near-term features:

- Category-based monthly and annual budgets.
- Cash-flow forecast from recurring income and bills.
- Household net-worth snapshot.
- Debt ratio and savings-rate views.
- Manual CSV import with review before posting.
- "What changed?" diffs between periods.
- Data-source provenance on every benchmark.

Later features:

- Mapping layer from household categories to GIFI or other chart-of-account taxonomies.
- StatCan benchmark panels by household income quintile.
- Privacy-preserving household comparisons.
- Scenario planning for rent/mortgage changes, food inflation, childcare, vehicle costs, and income interruptions.
- Export packs for accountant review.

## Ingestion Notes

For the StatCan CSVs:

- Prefer `*_databaseLoadingData.csv` for ingestion.
- Preserve all dimension columns; do not collapse them into a single text label too early.
- Normalize `REF_DATE` as either annual or quarterly period, depending on table frequency.
- Store `SCALAR_FACTOR` and `DECIMALS` so values can be rendered correctly.
- Keep `VECTOR` and `COORDINATE` for traceability back to the source table.
- Treat missing `STATUS`, `SYMBOL`, and `TERMINATED` fields as metadata, not numeric zeros.

Potential local staging tables:

- `statcan_table`
- `statcan_observation`
- `statcan_dimension`
- `statcan_dimension_value`
- `statcan_source_file`

## Privacy and Safety

This client will handle sensitive financial data. Baseline requirements:

- Local-first storage by default.
- Explicit user consent for any cloud sync or sharing.
- Encryption at rest for local stores containing real transaction data.
- Separate sample/demo data from real household data.
- No hidden financial advice engine.
- Clear distinction between descriptive budgeting, tax preparation support, and regulated financial advice.
- Exportable raw data and calculation history.

## Fit With Pitchfork / Pancakes

The financial client can share infrastructure ideas with Pancakes without turning household finance into a game economy:

- Household tasks and service credits can be shown separately from money.
- Pancakes credits should not be mixed into taxable or bank balances unless there is a deliberate accounting treatment.
- Pitchfork-style rewards can be symbolic overlays on budget habits, but they should not obscure real debt, cash flow, or obligations.
- A household covenant could have a financial planning view, for example "cook at home four nights this week," but the financial effect should be estimated and optional.

## Open Questions

- Is the target user a household, a small business, a mutual-aid node, or an accountant-facing workflow?
- Should the first client be personal budgeting, small-business bookkeeping, or cooperative ledgering?
- Is Canada the primary jurisdiction?
- Should GIFI support be first-class, or only an export/mapping layer?
- Do we want bank import, manual entry, or synthetic/sample data first?
- Should the system model taxes directly, or prepare clean records for external tax software?

## Recommended First Slice

Build a local-first household budgeting prototype:

1. Import a small sample of transaction-like CSV data.
2. Let the user map rows to budget categories.
3. Show period totals, cash-flow forecast, and net-worth snapshot.
4. Add a read-only benchmark panel backed by the local StatCan tables.
5. Preserve source metadata for every imported observation.

This keeps the first version useful without prematurely claiming accounting, tax, or financial-advice authority.
