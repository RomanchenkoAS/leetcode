/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    let x_str = x.toString();

    for (let i = 0; i < Math.floor(x_str.length / 2); i++) {
        if (x_str[i] !== x_str[x_str.length - i - 1]) {
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
