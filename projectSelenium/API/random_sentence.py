import random
import string


def generate_random_string(length):  # Method for generation sentence used in the test_input_text
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
