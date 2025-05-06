/**
 * Definition for singly-linked list.
 * @param {number} val
 * @param {ListNode|null} next
 */
function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

var seenNodes = new Set()
var lastGoodNode = null

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
    if (!head) {
        return head;
    }
    let currentNode = head;
    while (currentNode.next !== null) {
        if (currentNode.val === currentNode.next.val) {
            // remove next node
            currentNode.next = currentNode.next.next;
        } else {
            currentNode = currentNode.next;
        }
    }
    return head;
};