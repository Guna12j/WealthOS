# ADR 0003: Financial Data Precision

- Status: Accepted
- Date: 2026-09-04

## Context

WealthOS manages financial values such as transaction amounts,
purchase prices, sell prices, portfolio values, returns, and profit/loss.

Floating-point arithmetic can introduce rounding errors that are
unacceptable for financial calculations.

## Decision

We will use **exact decimal arithmetic** for financial values.

- PostgreSQL: `NUMERIC`
- Python: `Decimal`
- API schemas: explicit decimal-compatible representations
- Monetary values will not use binary floating-point types.

The database precision will initially use `NUMERIC(18,4)` where
appropriate, with higher precision used where the financial domain
requires it.

## Consequences

### Positive

- Deterministic financial calculations.
- No binary floating-point rounding surprises.
- Consistent values between application and database layers.
- Easier auditing and reconciliation.

### Negative

- Decimal arithmetic is slightly more verbose than using `float`.
- Developers must be careful not to introduce floating-point
  conversions at API or calculation boundaries.

## Alternatives Considered

- Python `float`
- PostgreSQL floating-point types

These were rejected because exact financial calculations are a
core requirement of WealthOS.