def firstDuplicate(array):
   closest= set()
   for i in range(len(array)):
       if (array[i] in closest):
           return array[i]
       else:
           closest.add(array[i])
   return -1
            

def firstNotRepeatingCharacter(s):
   arr = []
   arr2 = []
   
   for i in s:
       if i in arr:
           arr2.append(i)
           arr.remove(i)
       else:
           arr.append(i)

   if not arr:
       return '_'
       
   return arr[0]

def rotLeft(a, d):
    roti = d%len(a)
    temp = list(range(len(a)))
    for i in range(len(a)):
        newi = (i + roti)%len(a)
        print (newi)
        temp[i] = a[newi]
        print (temp)
        print (a)
    return temp

#print (rotLeft([1,2,3,4,5],3))

def isisometric(a,b):
   
    if a is None or b is None:
        return False
    if not (len(a) == len(b)):
        return False
    dic = {} 
    for i in range(len(a)):
        c1 = a[i]
        c2 = b[i]
       
        if c1 in dic:
            if dic[c1] != c2:
                return False
        
        else:
            if c2 in dic.values():
                return False
            dic[c1] = c2

    return True
#print(isisometric("foo", "bar"))

def reverseWords(s):
    s = s.split()
    for i in range(len(s)):
    
        temp = s[i]
        sw=s[len(s)-1-i]
        
        s[i] = sw
        s[len(s)-1-i] = temp
        if i - (len(s)-1-i) == 0 or i - (len(s)-1-i) == 1:
            return s

print(reverseWords("sky is blue"))


#binary tree
class BinarySTree(object):
    def __init__(self, root):
        self.value = root
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                
                else:
                    self.left = BinarySTree(value)
                    
            elif value > self.value:
                
                if self.right:
                    self.right.insert(value)
                    
                else:
                    self.right = BinarySTree(value)
                    
            else:
                self.value  = value
            
    #inorder
    def printTree(self):
        if self.value:
            if self.left:
                self.left.printTree()
                
            print(self.value)
        
            if self.right:
                self.right.printTree()
                
    def printpreorder(self):
        if self.value:
            print (self.value)
            if self.left:
                self.left.printpreorder()
            if self.right:
                self.right.printpreorder()
    
    def printpostorder(self):
        if self.value:
            if self.left:
                self.left.printpostorder()
            if self.right:
                self.right.printpostorder()
            print(self.value)
    
    def length(self,size=0):
        size = size+1
        if self.value:
            if self.left:
                size=self.left.length(size)
            if self.right:
                size=self.right.length(size)
        
        return size
    
    def addtotal(self, value=0):
        if self.value:
            value = value + self.value
            if self.left:
                value = self.left.addtotal(value)
            if self.right:
                value = self.right.addtotal(value)
        return value
        
    def maxvalue(self, maxval=float('inf')):
        if self.value:
            maxvalue = self.value
            if self.value < maxval:
                maxval = self.value
            if self.left:
                maxval = self.left.maxvalue(maxval)
            if self.right:
                maxval = self.right.maxvalue(maxval)
                
        return maxval
        
tree = BinarySTree(-5)
tree.insert(-2)
tree.insert(-6)
tree.insert(-8)
tree.insert(-3)
tree.insert(-1)
tree.insert(-40)
tree.insert(-9)
tree.printTree()
print("break")
tree.printpreorder()
print("break")
tree.printpostorder()
print("break")
print(tree.maxvalue())


#linked list
"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        pos = 1
        current = self.head
        while current and pos <= position:
            
        
            if pos == position:
                return current
                
            pos += 1
            current = current.next
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        return None
    
    def insert1(self, new_element, position):
        current = self.head
        pos = 2
        if position == 1:
            new_element.next = current.next
            self.head = new_element
        
        while current and pos <= position-1:
            
            current = current.next
            if pos == position-1:
                new_element.next = current.next
                current.next = new_element
            pos += 1    
            
            
        
        
    
    def insert(self, new_element, position):
        prev = self.head
        current = prev.next
        pos = 2
        if position == 1:
            new_element.next = prev
            self.head = new_element
            return 
        
         
        while current and pos < position:
            pos += 1
            prev = prev.next
            current = current.next
            
            if pos == position:
                prev.next = new_element
                new_element.next = current
                return
            
            
            
            
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        after = current.next
        if current and current.value==value:
            current.next == None
            self.head =after
            
        while after:
            if after.value == value:
                current = after.next
                return
            current = current.next
            after= after.next
        
    
    def visual(self):
        lis = []
        current = self.head
        while current:
            lis.append(current.value)
            current = current.next
        
        print lis
            

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
ll.visual()
# Should also print 3
print ll.get_position(3).value
ll.visual()
# Test insert
ll.insert(e4,3)
ll.visual()
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
ll.visual()
# Should print 2 now
print ll.get_position(1).value
ll.visual()
# Should print 4 now
print ll.get_position(2).value
ll.visual()
# Should print 3 now
print ll.get_position(3).value
