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