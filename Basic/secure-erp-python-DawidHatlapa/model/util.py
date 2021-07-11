import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    characters = []
    for i in range(number_of_small_letters):
        characters.append(random.choice(string.ascii_lowercase))
    for i in range(number_of_capital_letters):
        characters.append(random.choice(string.ascii_uppercase))
    for i in range(number_of_digits):
        characters.append(random.choice(string.digits))
    for i in range(number_of_special_chars):
        characters.append(random.choice(allowed_special_chars))
    random.shuffle(characters)

    return ''.join(characters)
