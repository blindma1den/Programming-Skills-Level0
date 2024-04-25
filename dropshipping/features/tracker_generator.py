
import string
import random

minusculas = string.ascii_lowercase
mayusculas = string.ascii_uppercase
numeros = string.digits
especiales = '!@#$%^&*()-_=+[{]}\|;:\'",<.>/?'


def tracker_generator_fn():
    tracker_list = []

    for _ in range(16):
        type_chosen = random.choice([minusculas, mayusculas, numeros, especiales])
        index = random.randint(0, len(type_chosen)-1)
        character = type_chosen[index]
        tracker_list.append(character)

    tracker_id = ''.join(tracker_list)

    return tracker_id


