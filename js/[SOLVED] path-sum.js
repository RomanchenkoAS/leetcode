/**
 * @description Definition for a binary tree node.
 * @typedef {Object} TreeNode
 * @property {number} val
 * @property {TreeNode|null} left
 * @property {TreeNode|null} right
 */
function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

function dfs(node, sum, target) {
    sum += node.val;

    if (!node.left && !node.right) {
        if (sum === target) {
            return true;
        }
    }

    let left = node.left ? dfs(node.left, sum, target) : false;
    let right = node.right ? dfs(node.right, sum, target) : false;

    return left || right;
}

/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
    if (!root) {
        return false;
    }
    return dfs(root, 0, targetSum);
};