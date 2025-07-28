/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    let sortedArr = [...arr];
    
    // Use the built-in sort method and provide a custom compare function
    sortedArr.sort((a, b) => {
        let aValue = fn(a);
        let bValue = fn(b);
        return aValue - bValue;
    });
    return sortedArr;

};
