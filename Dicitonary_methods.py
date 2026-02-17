dict={
    "name":"abdullah",
    "surname":"aziz",
    "age":18,
}
print(dict.keys())#Return Keys of the Dictionary
print(dict.values())#Return Values
print(dict.items())#Retrun pair of Keys & values in tuples form
print(dict.get("name"))#to access any Key
dict.update({"city":"Lahore"})#to Add any other key and values
print(dict)
#type casting dict to list
print(list(dict.keys()))
#length of the dictionary
print(len(dict))