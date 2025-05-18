/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    const red = nums.filter(num => num === 0).length;
    const white = nums.filter(num => num === 1).length;
    const blue = nums.filter(num => num === 2).length;

    const sorted = Array(red).fill(0).concat(Array(white)
    .fill(1)).concat(Array(blue).fill(2));

    for (let i = 0; i < nums.length; i++) {
        nums[i] = sorted[i];
    }
};