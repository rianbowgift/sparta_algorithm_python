class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


node = Node(3)

first_node = Node(4)
node.next = first_node

# print(node.next.data)


class LinkedList:
    def __init__(self,data):
        self.head = Node(data)


    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
            print("현재 데이터는 = ", cur.data)
        cur.next = Node(data)
    def print_all(self):

        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linkedList = LinkedList(3)
linkedList.append(4)
linkedList.append(5)
linkedList.print_all()



