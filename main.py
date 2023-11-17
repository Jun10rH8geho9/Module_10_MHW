from collections import UserDict

# Батьківський клас
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    # Клас де зберігаємо ім'я 
class Name(Field):
    pass
    # Клас де зберігаємо номер телефону 
class Phone(Field):
    def __init__(self, value):
        # Проходмо валідацію. Якщо  номер не цифри або довжина менше 10
        if not str(value).isdigit() or len(str(value)) != 10:
            raise ValueError("Телефон повинен мати 10 знаків та не мати букв")
        super().__init__(value)
        # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів. Відповідає за логіку додавання/видалення/редагування
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        # Додадємо номер
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        # Знаходимо номер
    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i
        return None
        # Видаляємо номер
    def remove_phone(self, phone):
        self.phones = [i for i in self.phones if i.value != phone]
        # Редагуємо номер
    def edit_phone(self, old_phone, new_phone):
        found = False
        for i in self.phones:
            if i.value == old_phone:
                i.value = new_phone
                found = True
        if not found:
            raise ValueError(f"Телефонний номер {old_phone} не знайдено")

    def __str__(self):
        return f"Ім'я контакта: {self.name.value}, телефони: {'; '.join(i.value for i in self.phones)}"
    
    # Клас для зберігання та управління записами. Містить логіку пошуку за записами до цього класу
class AddressBook(UserDict):
    # Додадємо номер
    def add_record(self, record):
        self.data[record.name.value] = record
    # Знаходимо номер
    def find(self, name):
        return self.data.get(name, None)
    # Видаляємо номер
    def delete(self, name):
        if name in self.data:
            del self.data[name]