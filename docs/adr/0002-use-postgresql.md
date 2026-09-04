# ADR 0002: Use PostgreSQL for the Database

- Status: Accepted
- Date: 2026-09-04

## Context

WealthOS will store financial data including transactions, holdings,
portfolio valuations, goals, journal entries, market data, and user
settings.

The database must provide strong consistency, reliable transactions,
precise financial data types, and a solid foundation for future growth.

## Decision

We will use **PostgreSQL** as the primary relational database for WealthOS.

Financial amounts will use PostgreSQL `NUMERIC` types rather than
floating-point types.

The transaction ledger will be treated as the source of truth for
portfolio-related calculations.

## Consequences

### Positive

- Strong transactional consistency.
- Native `NUMERIC` support for precise financial calculations.
- Excellent support for relational data and complex queries.
- Mature ecosystem and tooling.
- Suitable for future analytics and reporting requirements.

### Negative

- Requires database setup and migration management.
- More operational overhead than an embedded database such as SQLite.

## Alternatives Considered

- SQLite
- MySQL

PostgreSQL was selected because financial correctness, transactional
integrity, and long-term scalability are more important than minimizing
initial infrastructure complexity.