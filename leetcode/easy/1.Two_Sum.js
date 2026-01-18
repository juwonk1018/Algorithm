/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  for (let firstIdx = 0; firstIdx < nums.length; firstIdx++) {
    for (let secondIdx = firstIdx + 1; secondIdx < nums.length; secondIdx++) {
      if (nums[firstIdx] + nums[secondIdx] === target) {
        return [firstIdx, secondIdx];
      }
    }
  }
};
