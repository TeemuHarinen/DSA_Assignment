
class Node:
    # Initialize empty node
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Linked List class consists of nodes that are linked to each other with pointers
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Append data to end of linked list
    def append(self, data):
        
        currNode = self.head
        while currNode is not None:
            if currNode.data == data:
                return
            currNode = currNode.next
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)



    def search(self, data):
        temp = self.head
        # Check if data is in linked list 
        # 1) If list is empty, return false
        if temp is None:
            print("List is empty")
            return False
        # 2) If data is in list, return true
        while temp != None:
            if temp.data == data:
                return True
            temp = temp.next
        # 3) If data is not in list, return false
        return False

    def delete(self, data):
        temp = self.head
        if temp is None:
            print("List is empty")
            return 
        if temp.data == data:
            self.head = temp.next
            return
        while temp.next != None:
            if temp.next.data == data:
                # Set pointer to next nodes next node
                temp.next = temp.next.next
                return
            # Move to next node
            temp = temp.next

    def print(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return 
        while temp != None:
            print(temp.data, end="")
            if (temp.next != None):
                print(" -> ", end="")
            temp = temp.next
        print()


class HashLinear:
    def __init__(self, M):
        self.MAX = M
        # Create an array of linked lists the size of M
        self.arr = [LinkedList() for _ in range(M)]

    #Hashing with string fold method
    def get_hash(self, data):
        sum = 0
        data = str(data)
        for i in range(len(data)):
            sum += int((ord(data[i])**2))
    
        return sum % (self.MAX)

    def insert(self, data):
        slot = self.get_hash(data)
        # Call append function from linked list class
        self.arr[slot].append(data)

    def search(self, data):
        slot = self.get_hash(data)
        # Call search function from linked list class
        return self.arr[slot].search(data)

    def delete(self, data):
        slot = self.get_hash(data)
        # Call delete function from linked list class
        self.arr[slot].delete(data)

    def print(self):
        for i in range(self.MAX):
            if (self.arr[i].head == None):
                pass
            else:
                print("Slot", i, end=": ")
                # Call print function from linked list class
                self.arr[i].print()
        print()


if __name__ == "__main__":
    table = HashLinear(3)
    table.insert(12)
    table.print()
    table.insert("hashtable")
    table.print()
    table.insert(1234)
    table.print()
    table.insert(4328989)
    table.print()
    table.insert("BM40A1500")
    table.print()
    table.insert(-12456)
    table.print()
    table.insert("aaaabbbbcccc")
    table.print()
    print(table.search(-12456))
    print(table.search("hashtable"))
    print(table.search(1235))
    table.delete("BM40A1500")
    table.delete(1234)
    table.delete("aaaabbbbcccc")
    table.print()