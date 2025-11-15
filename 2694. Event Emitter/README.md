# Design an EventEmitter Class

## Problem Statement
Design an `EventEmitter` class that supports subscribing to events, emitting events, and unsubscribing from specific event listeners.

The interface behaves similarly to Node.js `EventEmitter` or DOM's `EventTarget`, but with simplified rules.

The class must support:

---

## Methods

### 1. **subscribe(eventName, callback)**
- Registers a callback to an event.
- Multiple callbacks can be registered for the same event.
- Callbacks should be executed **in order of subscription**.
- Returns an object containing:

{ unsubscribe: () => undefined }

- Calling `unsubscribe()` removes the callback from that event.

---

### 2. **emit(eventName, args?)**
- Emits the given event.
- `args` is optional and is passed as parameters to each callback.
- Returns:
- An empty array if no listeners exist.
- Otherwise, an array of the callback return values (in correct order).

---

## Example 1

**Input**

actions = ["EventEmitter", "emit", "subscribe", "subscribe", "emit"]

values = [

[],

["firstEvent"],

["firstEvent", "function cb1() { return 5; }"],

["firstEvent", "function cb2() { return 6; }"],

["firstEvent"]

]


**Output**

[

[],

["emitted", []],

["subscribed"],

["subscribed"],

["emitted", [5, 6]]

]


---

## Example 2

**Input**

actions = ["EventEmitter", "subscribe", "emit", "emit"]

values = [

[],

["firstEvent", "function cb1(...args) { return args.join(','); }"],

["firstEvent", [1,2,3]],

["firstEvent", [3,4,6]]

]

**Output**

[

[],

["subscribed"],

["emitted", ["1,2,3"]],

["emitted", ["3,4,6"]]

]


---

## Example 3

**Input**

actions = ["EventEmitter", "subscribe", "emit", "unsubscribe", "emit"]

values = [

[],

["firstEvent", "(...args) => args.join(',')"],

["firstEvent", [1,2,3]],

[0],

["firstEvent", [4,5,6]]

]


**Output**

[

[],

["subscribed"],

["emitted", ["1,2,3"]],

["unsubscribed", 0],

["emitted", []]

]


---

## Example 4

**Input**

actions = ["EventEmitter", "subscribe", "subscribe", "unsubscribe", "emit"]

values = [

[],

["firstEvent", "x => x + 1"],

["firstEvent", "x => x + 2"],

[0],

["firstEvent", [5]]

]


**Output**

[

[],

["subscribed"],

["subscribed"],

["unsubscribed", 0],

["emitted", [7]]

]


---

## Constraints

- 1 <= actions.length <= 10
- values.length == actions.length
- Events can have multiple listeners.
- Unsubscribe is always valid.
- Emit takes 1 or 2 arguments.
- Subscribe takes 2 arguments: event name and callback.

---
