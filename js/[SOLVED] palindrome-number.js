/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    const str = x.toString();
    const mid = Math.floor(str.length / 2);

    for (let i = 0; i < mid; i++) {
        if (str[i] !== str[str.length - 1 - i]) {
            return false;
        }
    }

    return true;
};

console.log("Will check 123")
a = isPalindrome(123)
console.log(a)

console.log("Will check 1234")
a = isPalindrome(1234)
console.log(a)

console.log("Will check 1221")
a = isPalindrome(1221)
console.log(a)
