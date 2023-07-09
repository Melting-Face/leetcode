/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
const chunk = function (arr, size) {
  let index = 0;
  const result = [];
  while (index < arr.length) {
    result.push(arr.slice(index, index + size));
    index += size;
  }
  return result;
};
