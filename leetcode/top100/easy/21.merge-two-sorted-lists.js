var mergeTwoLists = function (list1, list2) {
  let targetNode = null;
  let newNode;

  while (list1 !== null || list2 !== null) {
    let firstVal;
    if (list1 !== null && list2 !== null) {
      // 둘 다 null이 아님
      firstVal = Math.min(list1.val, list2.val);
      if (list1.val === list2.val) {
        newNode = new ListNode(firstVal, new ListNode(firstVal));
        list1 = list1.next;
        list2 = list2.next;
      } else {
        newNode = new ListNode(firstVal);
        if (list1.val === firstVal) {
          list1 = list1.next;
        } else {
          list2 = list2.next;
        }
      }
    } else {
      // 둘 중 하나가 null
      firstVal = list1 !== null ? list1.val : list2.val;
      newNode = new ListNode(firstVal);
      if (list1) {
        list1 = list1.next;
      } else {
        list2 = list2.next;
      }
    }

    if (targetNode === null) {
      targetNode = newNode;
      continue;
    }
    let currentNode = targetNode;
    while (currentNode.next !== null) {
      currentNode = currentNode.next;
    }
    currentNode.next = newNode;
  }
  return targetNode === null ? list1 : targetNode;
};

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

ListNode.prototype.val = function () {
  return this.val;
};
ListNode.prototype.next = function () {
  return this.next;
};

function mackInsertNode(list) {
  let singleLinkedList = new ListNode();
  let lastNode = singleLinkedList;

  list.forEach((insert) => {
    lastNode.val = insert;
    lastNode.next = new ListNode();
    lastNode = lastNode.next;
  });

  return singleLinkedList;
}

let list1 = mackInsertNode([1, 2, 4]);
let list2 = mackInsertNode([1, 3, 4]);

const result = mergeTwoLists(list1, list2);
console.log(result);
