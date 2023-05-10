/**
 * @param {number[]} nums
 * @return {boolean}
 */
const increasingTriplet = function(nums) {
  let i = Number.POSITIVE_INFINITY;
  let j = Number.POSITIVE_INFINITY;
  for (const num of nums) {
    switch (true) {
      case num <= i:
        i = num;
        break;
      case num <= j:
        j = num;
        break;
      default:
        return true;
    }
  }
  return false;
};