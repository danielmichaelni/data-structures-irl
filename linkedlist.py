"""
Implementation of the Linked List data structure
"""

class LinkedListNode():
  def __init__(self, value = None, next = None):
    self.value = value
    self.next = next
  def __repr__(self):
    if self.next is None:
      return str(self.value)
    return str(self.value) + '->' + repr(self.next)

def get_linked_list_length(head):
  length = 0
  tmp = head
  while tmp != None:
    length += 1
    tmp = tmp.next
  return length

def append_to_start(head, value):
  return LinkedListNode(value, head)

def append_to_end(head, value):
  node = LinkedListNode(value)
  if head == None:
    return node
  tmp = head
  while tmp.next != None:
    tmp = tmp.next
  tmp.next = node
  return head

def remove_from_linked_list(head, value):
  if head == None:
    return None
  if head.value == value:
    return head.next
  tmp = head
  while tmp.next != None:
    if tmp.next == value:
      tmp.next = tmp.next.next
      return head
    tmp = tmp.next
  return head

if __name__ == '__main__':
  a = LinkedListNode(1)
  print('creating a linked list node with value 1: ' + str(a))
  b = append_to_start(a, 2)
  print('appending the value 2 to the beginning: ' + str(b))
  c = append_to_end(b, 3)
  print('appending the value 3 to the end: ' + str(c))
  d = remove_from_linked_list(c, 2)
  print('removing the value 2: ' + str(d))
  print('length of resulting linked list: ' + str(get_linked_list_length(d)))
