/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map();
    const RESULT_KEY = Symbol('result');

    return function(...args) {
        let currentMap = cache;

        for (let i = 0; i < args.length; i++) {
            const arg = args[i];
            if (!currentMap.has(arg)) {
                currentMap.set(arg, new Map());
            }
            currentMap = currentMap.get(arg);
        }

        if (currentMap.has(RESULT_KEY)) {
            return currentMap.get(RESULT_KEY);
        }

        const result = fn(...args);
        currentMap.set(RESULT_KEY, result);
        return result;
    };
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
