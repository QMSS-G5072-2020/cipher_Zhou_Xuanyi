from cipher_xz2959 import __version__
from cipher_xz2959 import cipher_xz2959
import string
import random


def random_gen_str(size=100):
    alphabet = string.ascii_letters + ' '
    return ''.join(random.choice(alphabet) for _ in range(size))


def test_version():
    assert __version__ == '0.0.1'


def test_shift():
    assert cipher_xz2959.cipher("hello cipher!", 10) == 'rovvy mszroB!'
    assert cipher_xz2959.cipher("hello cipher!", -2) == 'fcjjm agnfcp!'
    assert cipher_xz2959.cipher("fcjjm agnfcp!", 2) == 'hello cipher!'


def test_encrypt_decrypt():
    for shift in range(-10, 10):
        text = random_gen_str()
        encrypt = cipher_xz2959.cipher(text, shift, True)
        decrypt = cipher_xz2959.cipher(text, -shift, False)
        assert encrypt == decrypt
