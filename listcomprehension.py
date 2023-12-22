maanden=["January", "February", "March", "April", "May", "June", "July", "August",
"September", "October", "November", "December"]
result_list = [f"{index + 1}: {month[:3].upper()}" for index, month in enumerate(maanden)]

print(result_list)