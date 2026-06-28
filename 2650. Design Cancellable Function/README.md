# Cancellable Generator

## Problem
Sometimes you have a long-running task represented by a generator that yields promises. Implement a function `cancellable(generator)` that returns:

- A `cancel` function
- A `promise`

The function should:

- Resume the generator whenever a yielded promise resolves.
- Throw rejected promise errors back into the generator.
- If `cancel()` is called before completion, throw `"Cancelled"` into the generator.
- Resolve or reject the returned promise based on the generator's final outcome.

---

## Approach
- Keep a `cancelled` flag.
- Create a recursive `step()` function to process generator execution.
- If cancelled:
  - Throw `"Cancelled"` into the generator.
- If generator finishes:
  - Resolve with the returned value.
- Otherwise:
  - Wait for the yielded promise.
  - On success, pass the resolved value back using `generator.next(value)`.
  - On failure, throw the error back using `generator.throw(error)`.

---

## Constraints:

- cancelledAt == null or 0 <= cancelledAt <= 1000
- generatorFunction returns a generator object

---
