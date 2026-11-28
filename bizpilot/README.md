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

The demo shop runs on real, anonymized public data: the order and payment history of one seller from the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (2016–2018, BRL). That history is replayed into a Shopify development store and a Stripe sandbox, so BizPilot reads it through the same APIs a real shop would use. No real money moves.

- Product costs and monthly targets are **assumptions**, labeled as such, because the dataset has no costs.
- The dataset is not stored in this repository; it is downloaded when needed. Credit: Olist. Licence: see the dataset page.
