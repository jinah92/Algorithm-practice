## 문제

Given the head of a linked list, remove the nth node from the end of the list and return its head.

## example 1

```code
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

## example 2

```code
Input: head = [1], n = 1
Output: []
```

## example 3

```code
Input: head = [1,2], n = 1
Output: [1]
```

## constraints

- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz