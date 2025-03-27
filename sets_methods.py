s={1,5,32,54,5,5,"Harry"}
print(s,type(s))
s.add(566)#adds 566 to the set
print(s,type(s)) 
s.remove(1)#removes 1 from the set
print(s,type(s)) 
s.pop()#removes an arbitrary element from the set
print(s,type(s))
s.clear()#clears the set
print(s,type(s))
s1={1,45,6}
s2={7,8,1,78}
print(s1.union(s2))#prints the union of the two sets
print(s1.intersection(s2))#prints the intersection of the two sets  