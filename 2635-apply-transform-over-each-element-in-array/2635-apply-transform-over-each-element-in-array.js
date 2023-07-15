/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const values = [];
    for (const i in arr) {
        values.push(fn(arr[i], Number(i)))
    }
    return values;
};