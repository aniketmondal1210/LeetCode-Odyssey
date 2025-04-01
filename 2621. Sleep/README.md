# Sleep Function

A simple asynchronous function that pauses execution for a given number of milliseconds.

## Usage

### Function Definition

```javascript
async function sleep(millis) {
    return new Promise(resolve => setTimeout(resolve, millis));
}
```

### Example Usage

```javascript
let t = Date.now();
sleep(100).then(() => {
    console.log(Date.now() - t); // Should print approximately 100
});
```

## Constraints

- `1 <= millis <= 1000`

## Explanation

This function returns a Promise that resolves after `millis` milliseconds, using `setTimeout`. The function can be used with `await` in an async function or with `.then()` for handling the promise resolution.
