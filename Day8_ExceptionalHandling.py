
# try:
#     a=int(input("Enter Number:"))
#     b=7/a
#     print(b)
# except Exception as e:
#     print(f"Exception Occurred {e}")
# else:
#     print("Loop Ended")
try:
    d = {"name": "Ali"}
    print(d["age"])
except KeyError:
    print("Key not found")
except Exception:
    print("Some error")