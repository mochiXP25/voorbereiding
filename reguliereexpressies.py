import re

fruit = "apple, banana, avocado, cherry, apricot"
res_fruit = re.findall(r'\ba\w*', fruit)
print(res_fruit)

maanden = "Er zijn 12 maanden in een jaar, 24 uur in een dag."
res_maanden = re.findall(r'\b\d+\b', maanden)
print(res_maanden)

zin3 = "I am walking while singing and eating."
res_zin3 = re.findall(r'\b\w+ing\b', zin3)
print(res_zin3)

alice_zin = "Alice wonders everywhere under the sky."
res_alice_zin = re.findall(r'\b[aeiouAEIOU]\w*\b', alice_zin)
print(res_alice_zin)

email = "Mijn email is voorbeeld@voorbeeld.com en info@test.be."
res_email = re.findall(r'\b[\w\.-]+@[\w\.-]+\b', email)
print(res_email)
