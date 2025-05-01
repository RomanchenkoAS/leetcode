/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
    let l = 0, r = nums.length - 1;

    while (true) {
        var mid = Math.floor((r - l) / 2) + l;
        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] > target) {
            r = mid;
        } else {
            l = mid;
        }

        if (r - 1 <= l) {
            if (target <= nums[l]) {
                return l;
            } else if (target <= nums[r]) {
                return r;
            } else {
                return r + 1;
            }
        }
    }
};

console.log("\nTest 1: we expect 2");
console.log(searchInsert([1, 3, 5, 6], 5)); // Output: 2

console.log("\nTest 2: we expect 1");
console.log(searchInsert([1, 3, 5, 6], 2)); // Output: 1

console.log("\nTest 3: we expect 4");
console.log(searchInsert([1, 3, 5, 6], 7)); // Output: 4

console.log("\nTest 4: we expect 0");
console.log(searchInsert([1, 3, 5, 6], 0)); // Output: 0

console.log("\nTest 5: we expect 0");
console.log(searchInsert([1], 0)); // Output: 0

console.log("\nTest 6: we expect 1");
console.log(searchInsert([1], 2)); // Output: 1

console.log("\nTest 7: we expect 2");
console.log(searchInsert([1, 2, 4, 6, 9], 3)); // Output: 2

console.log("\nTest 8: we expect 2");
console.log(searchInsert([10, 20, 30, 40], 25)); // Output: 2

console.log("\nTest 9: we expect 1");
console.log(searchInsert([1, 3], 3));