a = ["Snehal More", "Parvez Khan", "Gurjeet Singh"]

# Use the sorted function with a custom sorting key to sort by the first name
sorted_a = sorted(a, key=lambda name: name.split()[1])

print(sorted_a)
