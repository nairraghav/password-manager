from ciphers.vigenere_cipher import VigenereCipher
from string import (
    ascii_lowercase as string_ascii_lowercase,
    ascii_uppercase as string_ascii_uppercase,
)
from random import choices as random_choices
from json import load as json_load, dump as json_dump
from os.path import (
    expanduser as os_path_expanduser,
    join as os_path_join,
    exists as os_path_exists,
)


class PasswordManager:
    def __init__(self):
        self.allowed_characters = {
            "alphabets_lower": ",".join(string_ascii_lowercase).split(","),
            "alphabets_upper": ",".join(string_ascii_uppercase).split(","),
            "numbers": [str(number) for number in range(10)],
            "symbols": [
                "!",
                "@",
                "#",
                "$",
                "%",
                "&",
                "*",
                "-",
                "_",
                "+",
                "=",
            ],  # can't use comma since it actually exists in the list
        }

        self.file_name = os_path_join(
            os_path_expanduser("~"), ".ron_password_manager"
        )
        if not os_path_exists(self.file_name):
            # generate new random string
            self.secret = self.generate_random_password()
            self.passwords = {}
            self.save_state()
        else:
            with open(self.file_name, "r") as json_file:
                json_output = json_load(json_file)
                self.secret = json_output.get("secret")
                self.passwords = json_output.get("passwords")
        self.vigenere = VigenereCipher(secret=self.secret)

    def get_apps(self):
        return [application for application in self.passwords]

    def get_password(self, application):
        if application in self.passwords:
            return self.vigenere.decrypt(
                encrypted=self.passwords.get(application)
            )
        else:
            raise Exception("Application not in password store")

    def store_password(self, application, password):
        encrypted_password = self.vigenere.encrypt(plain_text=password)
        self.passwords[application] = encrypted_password

    def generate_random_password(
        self,
        length=16,
        alphabet_lower=True,
        alphabet_upper=True,
        number=True,
        symbol=True,
    ):
        if alphabet_lower is alphabet_upper is number is symbol is False:
            print(alphabet_lower)
            print(alphabet_upper)
            print(number)
            print(symbol)
            raise Exception("One of the password options must not be false")

        allowed_characters = []
        if alphabet_lower:
            allowed_characters.extend(
                self.allowed_characters.get("alphabets_lower")
            )
        if alphabet_upper:
            allowed_characters.extend(
                self.allowed_characters.get("alphabets_upper")
            )
        if number:
            allowed_characters.extend(self.allowed_characters.get("numbers"))
        if symbol:
            allowed_characters.extend(self.allowed_characters.get("symbols"))

        return "".join(random_choices(population=allowed_characters, k=length))

    def save_state(self):
        json_object = {"secret": self.secret, "passwords": self.passwords}
        with open(self.file_name, "w") as json_file:
            json_dump(obj=json_object, fp=json_file)
