from faker import Faker



#Фейки
fakerus = Faker('ru_RU')
fake_name = fakerus.first_name()
fake_lastname = fakerus.last_name()
fake_phone = fakerus.phone_number()

fakeeng = Faker()
fake_password = fakeeng.password()
fake_login = fakeeng.user_name()
fake_email = fakeeng.email()
print(fake_name)

#валидные данные
valid_email = 'leroxo7528@goflipa.com'
valid_password = 'QaSwEd1!'

#не валидные данные
invalid_ls = '45665445621'
