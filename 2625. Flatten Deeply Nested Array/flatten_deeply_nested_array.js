/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    const result = [];
    
    for (const item of arr) {
        if (Array.isArray(item) && n > 0) {
            // Recursively flatten with depth reduced by 1
            result.push(...flat(item, n - 1));
        } else {
            // Add non-array items or items when depth is exhausted
            result.push(item);
        }
    }
    
    return result;
};
