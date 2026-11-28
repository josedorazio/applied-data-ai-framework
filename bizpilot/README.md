# BizPilot — Data Integration & Reporting Automation for Online Sellers

BizPilot turns an online seller's weekly exports (orders, payments) and cost list into one tested database, then reports sales, margin and payment reconciliation automatically.

> **Status:** in development.

## The problem

> "Every Monday I download my orders and payments exports from the marketplace and paste them into a spreadsheet next to my product costs. It takes hours, I never know my real margin, and sometimes what I sold and what I got paid don't match and I don't know why."

That owner's week, in short:

- data arrives as separate exports, and someone consolidates it by hand;
- real margin is unknown because costs sit in a separate file;
- orders and payments don't always match (missing payments, several payments per order, canceled orders);
- the same KPI is calculated differently in different reports.

## What BizPilot will do

1. **Ingest** CSV exports through a connector, processing only new files.
2. **Store** them as received (Bronze), then validated and normalized (Silver), keeping rejected rows with their reason.
3. **Model** sales, margin and order ↔ payment reconciliation with documented metric definitions (Gold).
4. **Report** through a shareable dashboard and an automated weekly report.
5. **Later:** add a second source (for example Google Sheets, Stripe or Shopify) into the same model.

Every tool used is free.

## Data

Real, anonymized public data: the orders and payments of one seller from the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (2016–2018, BRL), used as that seller's exports.

- Product costs and monthly targets are **assumptions**, labeled as such, because the dataset has no costs.
- The dataset is not stored in this repository; it is downloaded when needed. Credit: Olist. Licence: see the dataset page.
