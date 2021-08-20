from random import choice


def private_key(p):
    user_number = int(input("Pick a private key: "))
    while user_number <= 1 or user_number >= p:
        user_number = int(input("Pick a private key greater than 1 and less than prime key"))
    return user_number


def public_key(p, g, private):
    return (g ** private) % p


def secret(p, public, private):
    return (public ** private) % p


def generate_prime_numbers():
    prime_numbers_list = list()
    for number in range(0, 1000):
        if number > 1:
            for index in range(2, number):
                if number % index == 0:
                    break
                else:
                    prime_numbers_list.append(number)
    p = choice(prime_numbers_list)
    g = choice(prime_numbers_list)
    while p == g:
        g = choice(prime_numbers_list)
    return p, g


if __name__ == '__main__':
    p, g = generate_prime_numbers()
    alice_priv_key = private_key(p)
    bob_priv_key = private_key(p)
    alice_public_key = public_key(p, g, alice_priv_key)
    bob_public_key = public_key(p, g, bob_priv_key)
    alice_calculate_secret_key = secret(p, bob_public_key, alice_priv_key)
    bob_calculate_secret_key = secret(p, alice_public_key, alice_priv_key)
