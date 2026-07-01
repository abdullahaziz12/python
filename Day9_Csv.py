import csv as cs

with open("firstprogram.csv", "w", newline="") as file:
    w = cs.writer(file)
    w.writerow(["name", "age", "city"])
    w.writerows([                           # list of lists — ek argument
        ["Ali", 20, "Lahore"],
        ["Sara", 22, "Karachi"]
    ])

with open("firstprogram.csv", "r", newline="") as read:
    r = cs.reader(read)
    for data in r:
        print(data)