dict={
    "name":"abdullah",
    "surname":"aziz",
    "age":18,
}
print(type(dict))
print(dict)
print(dict["name"])
dict["name"]="usman"
print(dict)
#null Dictionary
null={}
print(null)
#nested Dictionary
nested_dict={
    "Name":"Abdullah",
    "subject":{
        "chem":83,
        "Bio":76,
    }
}
print(nested_dict)
print(nested_dict["subject"]["chem"])