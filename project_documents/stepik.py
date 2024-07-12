from dataclasses import dataclass
from dataclasses import field
from random import choice

def choice():
    hobbies = ["спорт", "чтение", "йога", "спорт", "музыка", "танцы", "путешествия", "кино",
               "фотография", "музыка", "танцы", "йога", "рисование", "кулинария", "танцы",
               "садоводство", "йога", "спорт", "велоспорт", "шахматы", "йога",
               "танцы", "путешествия", "рыбалка", "походы", "спорт",
               "кулинария", "плавание", "танцы", "музыка",
               "спорт", "йога"]
    return choice(hobbies)

@dataclass
class Person:
    first_name: str
    last_name: str
    hobbies: str = field(default_factory=set)


import random
import string
from dataclasses import dataclass, field

alphabet = string.ascii_uppercase + string.digits


def generate_guid():
    guid = ''.join(random.choices(alphabet, k=15))
    return guid


@dataclass(order=True)
class Student:
    sort_index: int = field(init=False, repr=False)
    first_name: str
    last_name: str
    guid: str = field(default_factory=generate_guid, repr=False, init=False)
    email: str = field(init=False)
    tuition: int = field(repr=False, default=0)


    def __post_init__(self):
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@uni.edu'
        self.sort_index = (self.tuition, self.last_name, self.first_name)


jane = Student('Jane', 'Lee', 30000)
assert jane.tuition == 30000
assert len(jane.guid) == 15
print(jane)
print('*'*30)
julia = Student('Julia', 'Doe')
assert julia.tuition == 0
assert len(julia.guid) == 15
print(julia)

jane = Student('Jane', 'Lee', 30000)
julia = Student('Julia', 'Doe', 10000)
jake = Student('Jake', 'Langdon', 20000)
joy = Student('Joy', 'Smith', 15000)
print(*sorted([jane, julia, jake, joy]), sep='\n')