# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self.next:
            return str(self.val)
        return "{}->{}".format(self.val, self.next)


def get_value(list_node):
    """
    Returns the number represented by the ListNode.

    Arg -
        list_node - ListNode,
    """
    if not list_node.next:
        return str(list_node.val)
    return get_value(list_node.next) + str(list_node.val)


def create_list_node(num, next_node=None):
    """
    Args -
        Recursively creates a reversed ListNode from a number.
        Used for testing purpose.

        num - int
        next_node - ListNode (None for the first time.)
    """
    if not num:
        return next_node

    list_node = ListNode(val=(num % 10), next=next_node)
    num = num // 10
    return create_list_node(num, list_node)


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Link to problem: https://leetcode.com/problems/add-two-numbers/

        Problem statement:
            You are given two non-empty linked lists representing two
            non-negative integers. The digits are stored in reverse
            order and each of their nodes contain a single digit. Add
            the two numbers and return it as a linked list.

            You may assume the two numbers do not contain any leading
            zero, except the number 0 itself.

        Example:
            Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
            Output: 7 -> 0 -> 8
            Explanation: 342 + 465 = 807.

        Args -
            l1 - ListNode, first number
            l2 - ListNode, second number

        Pseudocode -
            1. Get numeric value of l1 and l2.
            2. Add them together, convert to string.
            3. Return a reversed ListNode representation of the sum.

        Returns -
            sum_node - ListNode, the sum
        """
        l1_value = int(get_value(l1))
        l2_value = int(get_value(l2))
        value_sum = str(l1_value + l2_value)  # 807
        next_node = ListNode(val=int(value_sum[0]))
        for digit in value_sum[1:]:
            new_list_node = ListNode(val=int(digit), next=next_node)
            next_node = new_list_node
        return next_node
