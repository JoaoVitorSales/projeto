from random import randint
from faker import Faker


fake = Faker('pt-BR')


def rand_ratio():
    return randint(840, 900), randint(473, 573)


def fabric_car():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=2),
        'description': fake.sentence(nb_words=20),
        'date': fake.date_time(),
        'value': fake.random_number(digits=8, fix_len=True),
        'details': fake.sentence(nb_words=150),
        'author': {
            'primary_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'Shop': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/cars' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(fabric_car())
