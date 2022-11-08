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


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum =""
    sum2=""
    cur = linked_list_1.head
    while cur.next is not None:
        sum+=str(cur.data)
        cur = cur.next
    sum+=str(cur.data)
    cur = linked_list_2.head
    while cur.next is not None:
        sum2+=str(cur.data)
        cur = cur.next
    sum2+=str(cur.data)



    return int(sum)+int(sum2)





linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))