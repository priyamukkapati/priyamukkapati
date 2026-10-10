# StreamCommerce

A small local prototype for creator subscriptions and gifting.

## Current implementation

Records purchases in SQLite, uses request IDs to prevent duplicate transactions, rejects conflicting retries, and calculates revenue in integer cents.

## Run

From the repository root, with Python 3.10+:

```bash
python3 projects/streamcommerce/app.py
```

Creator revenue: $6.99

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Limitations

This demo uses an in-memory database. It does not process payments, manage recurring billing, authenticate users, or expose an API. Store('purchases.db') can persist the ledger locally.

## Roadmap

Add a Spring Boot API, PostgreSQL persistence, payment-provider sandbox integration, and authentication before considering event processing or deployment.
