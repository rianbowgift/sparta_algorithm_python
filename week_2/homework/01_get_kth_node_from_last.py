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

    def get_kth_node_from_last(self, k):
        size = self.count_all() - k;
        #예를들어 8가지숫자중 뒤에서 2번쨰수를 구해야한다면 8-2=6 앞에서6번쨰 인덱스를 구한다

        return self.get_node(size)

    def count_all(self):
        count=0
        cur = self.head
        while cur is not None:
            count+=1
            cur = cur.next
        return count

    def get_node(self, index):

        node = self.head
        count = 0
        while count < index:
            node = node.next
            count +=1


        return node

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!