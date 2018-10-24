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
