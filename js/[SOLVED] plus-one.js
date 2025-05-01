/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
    let lastDigit = digits.at(-1);
    let lastIndex = digits.length - 1;
    if (lastDigit !== 9) {
        digits[lastIndex]++;
        return digits;
    }

    for (let i = lastIndex; i >= 0; i--) {
        if (digits[i] === 9) {
            if (i === 0) {
                digits[i] = 1;
                digits.push(0)
            } else {
                digits[i] = 0;
            }
        } else {
            digits[i]++;
            break;
        }
    }
    return digits;
};

// test function:
d = [5, 4, 3, 2, 1]
console.log("Before:\t", d)
console.log("After:\t", plusOne(d), "\n")

d = [5, 4, 3, 9, 9]
console.log("Before:\t", d)
console.log("After:\t", plusOne(d), "\n")

d = [9, 9, 9, 9, 9]
console.log("Before:\t", d)
console.log("After:\t", plusOne(d), "\n")

d = [9]
console.log("Before:\t", d)
console.log("After:\t", plusOne(d), "\n")

d = [9, 9, 9, 8, 9]
console.log("Before:\t", d)
console.log("After:\t", plusOne(d), "\n")

d = [8, 9, 9, 9]
console.log("Before:\t", d)
console.log("After:\t", plusOne(d), "\n")