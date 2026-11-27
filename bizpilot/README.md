# BizPilot — Data Integration & Reporting Automation for Small Online Shops

BizPilot connects a small online shop's Shopify orders, Stripe payments and Google Sheets costs into one tested database, then reports sales, margin and reconciliation automatically.

> **Status:** in development.

## The problem

> "Every Monday I export orders from Shopify, payments from Stripe and copy my product costs from a spreadsheet, then spend a few hours pasting it all together. I never know my real margin, and sometimes the numbers don't match and I don't know why."

That owner's week, in short:

- data lives in three or four tools, and someone consolidates it by hand;
- real margin is unknown because costs sit in a separate spreadsheet;
- orders and payments don't always match (missing payments, refunds recorded in only one place);
- the same KPI is calculated differently in different reports.

## What BizPilot will do

1. **Connect** to Shopify, Stripe, Google Sheets and CSV/Excel exports.
2. **Validate** schema, types and duplicates; keep rejected rows with their reason.
3. **Store** raw and curated data in PostgreSQL.
4. **Model** sales, margin and order ↔ payment reconciliation with documented metric definitions.
5. **Report** through a shareable dashboard and an automated weekly report.

## Data

All data is **synthetic** and belongs to a fictional demo shop: a Shopify development store, Stripe in test mode and a Google Sheet. No real customers or payments.

The shop's products and order patterns are seeded from [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii), real transactions from a UK online retailer, 2009–2011. Chen, D. (2012), UCI Machine Learning Repository, https://doi.org/10.24432/C5CG6D, licensed CC BY 4.0.
