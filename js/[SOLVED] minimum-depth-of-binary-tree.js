/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function (root) {
    if (!root) {
        return 0;
    }

    const nodesQueue = [[root, 1]];


    while (nodesQueue.length > 0) {
        const [currentNode, currentDepth] = nodesQueue.shift();

        if (!currentNode.left && !currentNode.right) {
            return currentDepth;
        }

        if (currentNode.left)
            nodesQueue.push([currentNode.left, currentDepth + 1]);
        if (currentNode.right)
            nodesQueue.push([currentNode.right, currentDepth + 1]);
    }

    return 0;
};

// TreeNode constructor
function TreeNode(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
}

// Utility: Convert array to binary tree (level-order)
function buildTreeFromArray(arr) {
    if (!arr.length || arr[0] === null) return null;

    let root = new TreeNode(arr[0]);
    let queue = [root];
    let i = 1;

    while (queue.length > 0 && i < arr.length) {
        let current = queue.shift();

        if (arr[i] != null) {
            current.left = new TreeNode(arr[i]);
            queue.push(current.left);
        }
        i++;

        if (i < arr.length && arr[i] != null) {
            current.right = new TreeNode(arr[i]);
            queue.push(current.right);
        }
        i++;
    }

    return root;
}

// Test cases
const testCases = [
    {
        input: [3, 9, 20, null, null, 15, 7],
        description: 'Balanced tree with depth 2'
    },
    {
        input: [2, null, 3, null, 4, null, 5, null, 6],
        description: 'Skewed tree (right) with depth 5'
    }
];

for (const {input, description} of testCases) {
    const root = buildTreeFromArray(input);
    const result = minDepth(root);
    console.log(`Test: ${description}`);
    console.log(`Input: ${JSON.stringify(input)}`);
    console.log(`Output: ${result}`);
    console.log('------------------------');
}