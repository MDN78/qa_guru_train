import random
from dataclasses import dataclass
from datetime import datetime, timedelta, date
from faker import Faker
from random import randrange

fake = Faker()


@dataclass
class Customer:
    passport_seria: int
    passport_number: int
    first_name: str
    last_name: str
    data_borh: str
    data_vidachi: str
    kem_vidan: str
    podrazdelenie: str

    @classmethod
    def get_passport_seria(cls) -> int:
        return random.randint(4000, 4060)

    @classmethod
    def get_passport_number(cls) -> int:
        return random.randint(500000, 510000)

    @classmethod
    def get_random_string(cls) -> str:
        string = ''
        string_len = random.randint(5, 15)
        for i in range(0, string_len):
            string = string + random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        return string.title()

    @classmethod
    def get_random_long_string(cls) -> str:
        string = ''
        string_len = random.randint(20, 50)
        for i in range(0, string_len):
            string = string + random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя ')
        return string.strip().title()

    @classmethod
    def get_random_podrazdelenie(cls) -> str:
        part_1 = random.randint(100, 999)
        part_2 = random.randint(100, 999)
        return f'{part_1}-{part_2}'

    '''Variant 1 
    def get_random_date() -> str:
        # # Начинаем с первого января 2020 года
        # start_date = datetime(1960, 1, 1)
        # # Ограничиваемся одним годом – до 1 января 2021 года
        # end_date = datetime(2024, 1, 1)
        # random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        # return random_date  # И вуаля, наша случайная дата готова!
    
        random_date = fake.date_between(start_date='-30y', end_date='today')
        return random_date
        
        varian else:
        # d1 = datetime.strptime('1/1/1960 1:30 PM', '%m/%d/%Y %I:%M %p')
        # d2 = datetime.strptime('1/1/2010 2:30 AM', '%m/%d/%Y %I:%M %p')
        # int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        # random_second = randrange(int_delta)
    '''

    @classmethod
    def get_random_date_burn(cls) -> str:
        start_date = date(1900, 1, 1)
        end_date = date(2010, 1, 1)
        return start_date + timedelta(days=randrange((end_date - start_date).days))

    @classmethod
    def get_random_data_vidachi(cls, data_burn: date):
        end_date = datetime.now().date()
        data_with_14_years = data_burn + timedelta(days=14 * 365)
        return data_with_14_years + timedelta(days=randrange((end_date - data_with_14_years).days))

    @classmethod
    def get_customer(cls):
        data_born = cls.get_random_date_burn()
        return Customer(
            passport_number=cls.get_passport_number(),
            passport_seria=cls.get_passport_seria(),
            first_name=cls.get_random_string(),
            last_name=cls.get_random_string(),
            kem_vidan=cls.get_random_long_string(),
            podrazdelenie=cls.get_random_podrazdelenie(),
            data_borh=data_born,
            data_vidachi=cls.get_random_data_vidachi(data_born)
        )


customer = Customer.get_customer()

print(customer)

list_first_name = ['Vasiliy', 'Olga', 'Oleg', 'Stas', 'Jim']

print(random.choice(list_first_name))
