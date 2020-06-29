import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

from faker import Faker
from testapp.models import Marks, BasicInfo

obj = Faker()

def call(N=10):
    num = 1
    for i in range(N):
        full_name = obj.name()
        list = full_name.split()
        first = list[0]
        second = list[1]
        ads = obj.address()
        m1 = obj.random_number(digits = 2)
        m2 = obj.random_number(digits=2)
        m3 = obj.random_number(digits=2)
        basic_obj = BasicInfo.objects.get_or_create(first_name = first, last_name = second, roll_no = num )[0]
        mark_obj = Marks.objects.get_or_create(name = basic_obj, address = ads, english_marks = m1, maths_marks = m2, science_marks = m3)[0]
        num += 1


if __name__ == '__main__':
    print('Filling random data')
    call(10)
    print('Filled with fake data')
