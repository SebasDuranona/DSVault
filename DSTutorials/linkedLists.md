# Linked Lists
Linked lists are linear data structures consisting of nodes where each node points to the next node in the sequence. Linked lists are highly versatile and come in several forms, including singly linked lists, doubly linked lists, and circular linked lists. In this article, we will explore these variations and get an overview of how they are implemented in Python.
## Singly Linked Lists
A singly linked list is the most basic type of linked list. Each node in a singly linked list contains two components: data and a reference (or pointer) to the next node.
### Implementation in Python:
```
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
```
**Overview:**
- First, you create a linked list by instantiating a ***'SinglyLinkedList'*** object.
- Then, you add elements to it by creating ***'Node'*** objects and linking them together using the **'next'** pointers.

## Doubly Linked Lists
A doubly linked list extends the singly linked list by adding a reference to the previous node in each node. This bidirectional linkage makes it easier to traverse the list in both directions.
### Implementation in Python:
```
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
```
**Overview:**
- Just like with singly linked lists, you create a ***'DoublyLinkedList'*** object and add elements to it by creating ***'Node'*** objects.
- In addition to the **'next'** pointer linking each element to the next, you link each element to the previous one using the **'prev'** pointer.
