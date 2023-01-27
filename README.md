# DSA_Assignment

1. Implementing the Hash Table
1.1 Structure of the hash table
Hash table with linear probing, open hashing, and collision handling. Hash table consists of array with linked lists as elements. Collisions are handled with linked lists, when collision happens, the value is added to the end of the linked list.

1.2 Hash function
Hash table uses string folding as a hash function. In string folding each character in an input is transformed into its ASCII value. Characters ASCII values are summed together (before summing raise to 3rd potency). Using potencies eliminates problem with short input being calculated as small number always. This is mainly the reason I chose this type of hashing method.

1.3 Methods
get_hash(self, data)
Calculates a slot for the data based on the data’s characters ASCII values.

insert(self, data)
Inserts new value to the table. Calls linked list’s function to do the appending. Append works by shifting the nodes pointers based on logic.

search(self, data)
Searches the selected value. Returns True, False or None based on the outcome.

delete(self, data)
Deletes the selected value. Works by shifting the pointers. (Note: When deleting the node the previous node’s pointer needs to be directed to next.next node)

print(self)
Loops through the array of linked lists and prints the contents.

