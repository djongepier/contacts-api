# Simple script to generate a token to use with the API.

import secrets


def generate_token(length: int) -> str:
    return secrets.token_urlsafe(length)


if __name__ == '__main__':
    length_token = input("What length should the token be?: ")
    token = generate_token(int(length_token))
    print(token)
