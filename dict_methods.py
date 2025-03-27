marks={
    "Harry":100,
    "Ram":89,
    "Koshish":90,
    0:"Harry"
}
print(marks.items())#prints all the items in the dictionary
print(marks.keys())#prints all the keys in the dictionary
print(marks.values())#prints all the values in the dictionary
marks.update({"Harry":99,"Apeak":100  })#updates the value of the key "Harry" to 99
print(marks) 
print(marks.get("Harry"))#prints the value of the key "Harry" #it gives none if the key is not present
print(marks["Harry"])#it gives an error if the key is not present