items= ["apple","banana","orange","apple","mango"]
unique_items= set()

for i in items:
    if i in unique_items:
        print("duplicate",i)
        break
    else:
        unique_items.add(i)
