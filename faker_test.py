from faker import Faker
fake = Faker()

name_list = []

for name in range(5):
    name_list.append(fake.name())

print(name_list)