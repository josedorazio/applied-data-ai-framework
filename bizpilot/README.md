# BizPilot — Business Intelligence & Reporting Automation for SMBs

BizPilot turns scattered sales data into one reliable, tested source of truth, with clear KPIs, a dashboard and automated reporting.

> **Status:** in development.

## The problem

Small and medium-sized businesses often keep their sales in spreadsheets and exports from different systems. As a result:

- someone consolidates the data by hand every week or month;
- the same KPI is calculated differently in different reports;
- basic questions ("which products and customers drive revenue?") take days to answer;
- duplicates, cancellations and missing values quietly distort the numbers.

## What BizPilot will do

1. **Connect** to transaction data from public datasets and client CSV/Excel files.
2. **Validate** schema, types, duplicates and cancellations.
3. **Store** raw and curated data in PostgreSQL.
4. **Model** analytics-ready tables with documented metric definitions.
5. **Report** through a dashboard and scheduled business reports.

## Data

Public data only: [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii), real transactions from a UK online retailer, 2009–2011. Chen, D. (2012), UCI Machine Learning Repository, https://doi.org/10.24432/C5CG6D, licensed CC BY 4.0.
