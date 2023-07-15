/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const entries = arr.entries();
    const answer = [];
    let entry = entries.next().value;
    while (entry) {
        const condition = fn(entry[1], entry[0])
        if (condition) {
            answer.push(entry[1]);
        }
        entry = entries.next().value;
    }
    return answer;
};