# ADR 0004: Use Alembic for Database Migrations

- Status: Accepted
- Date: 2026-09-04

## Context

WealthOS uses PostgreSQL as its primary database. As the application
evolves, the database schema will change through new tables, columns,
indexes, constraints, and relationships.

These changes need to be version-controlled, repeatable, and deployable
across development, testing, and production environments.

## Decision

We will use **Alembic** for database schema migrations.

All intentional database schema changes will be represented by
version-controlled Alembic migration files.

The application will not modify the production database schema
automatically at runtime.

## Consequences

### Positive

- Database changes are version-controlled.
- Migrations can be applied consistently across environments.
- Schema history is auditable.
- Alembic integrates well with SQLAlchemy.

### Negative

- Developers must create and review migrations when the schema changes.
- Migration history requires maintenance as the project grows.

## Alternatives Considered

- Manual SQL scripts
- Automatic schema creation from application models

These were rejected because WealthOS requires controlled, repeatable,
and auditable database schema evolution.