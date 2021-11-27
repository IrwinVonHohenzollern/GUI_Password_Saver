import string as st
from random import choice, randint


POSSIBLE_SYMBOLS = st.ascii_letters + st.digits + '!?.,@#$%*'


class Password_Generator:
    def __init__(self):
        self.password = ''
        self.generator()

    def generator(self):
        number_of_symbols = randint(10, 20)
        for _ in range(number_of_symbols):
            self.password += choice(POSSIBLE_SYMBOLS)

    def get_password(self):
        return self.password

# password = Password_Generator()
# print(password.password)
# print(password.get_password())
