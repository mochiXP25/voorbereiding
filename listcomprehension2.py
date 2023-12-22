maanden=["January", "February", "March", "April", "May", "June", "July", "August",
"September", "October", "November", "December"]

result_list = [f"{index + 1}: {maand[:3].upper()}" for index, maand in enumerate(maanden) if len(maand) <= 5]


print(result_list)