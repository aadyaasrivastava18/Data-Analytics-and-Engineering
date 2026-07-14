# ACID Properties

## What is ACID?

ACID is a set of database properties that ensure reliable and consistent transactions.

---

## Atomicity

Either the entire transaction succeeds or nothing happens.

Example:

Money is debited only if it is also credited.

---

## Consistency

The database always remains in a valid state after a transaction.

---

## Isolation

Multiple transactions do not interfere with one another.

---

## Durability

Once a transaction is committed, it remains saved even if the system crashes.

---

## Real Business Example

When paying online, money should never disappear because of a server crash.

ACID ensures transaction reliability.

---

## Key Takeaways

- Atomicity → All or Nothing.
- Consistency → Valid State.
- Isolation → Independent Transactions.
- Durability → Permanent Storage.
