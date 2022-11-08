class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):

        node = self.head
        count = 0
        while count < index:
            node = node.next
            count +=1


        return node


    def add_node(self,index,value):
            new_node = Node(value)  # 새로 넣을노드

            if index==0:
                new_node.next = self.head
                self.head = new_node
                return


            node = self.get_node(index-1) # 새로넣을노도의 앞노드
            next_node = node.next # 새로넣을 노드의 뒷노드

            node.next = new_node # 새로넣을노드는 앞노드의 next다.
            new_node.next = next_node # 새로넣을 노드의 다음은 저장해둔 뒷노드다

    def delete_node(self,index):
        if index==0:
            self.head = self.head.next
            return

        node = self.get_node(index - 1)  # 새로넣을노도의 앞노드
        next_node = node.next.next  # 새로넣을 노드의 뒷노드


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0,3)
linked_list.print_all()
linked_list.delete_node(0)
linked_list.print_all()