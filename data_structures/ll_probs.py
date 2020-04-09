from singly_linked_list import *

def printlist(list):
    for i in range(0,list.count()):
        print(list.get(i))

def main():
    colors = SingleLinkedList()
    colors.push("Red")
    colors.push("Blue")
    colors.push("Green")
    colors.push("Yellow")
    colors.push("Orange")
    colors.push("Gold")

    reverse_sll(colors)
    printlist(colors)

def reverse_sll(list):
    prev, cur = list.begin, list.begin.next
    while cur is not None:
        next = cur.next
        
        cur.next = list.begin
        prev.next = next
        list.begin = cur

        cur = next
        
if __name__ == '__main__':
    main()

