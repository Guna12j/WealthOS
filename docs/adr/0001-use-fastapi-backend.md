# ADR 0001: Use FastAPI for the Backend

- Status: Accepted
- Date: 2026-09-04

## Context

WealthOS requires a backend API to manage portfolio data, transactions,
market data, analytics, goals, and authentication.

The backend should be maintainable, well-typed, testable, and suitable
for future deployment.

## Decision

We will use **FastAPI** as the backend web framework.

The backend will use Python 3.13 and will be structured as a modular
application so individual domains can evolve independently.

## Consequences

### Positive

- Strong Python type-hint support.
- Automatic OpenAPI documentation.
- Good support for asynchronous APIs.
- Straightforward automated testing.
- Suitable foundation for modular financial-domain services.

### Negative

- The team must maintain Python backend expertise.
- Additional architecture and validation will be required as the
  application grows.

## Alternatives Considered

- Django
- Flask

FastAPI was selected because its API-first design, typing, automatic
OpenAPI documentation, and testing support fit WealthOS particularly well.