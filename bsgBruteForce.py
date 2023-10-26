import itertools

def generate_passwords(length, characters, repeat):
    if repeat:
        passwords = itertools.product(characters, repeat=length)
    else:
        passwords = itertools.permutations(characters, length)

    with open('passwords.txt', 'w') as f:
        for password in passwords:
            password = ''.join(password) # Konsola şifreyi yazdırmak için yaptım
            print(password)  # Konsola şifreyi yazdırmak için yaptım
            f.write(''.join(password) + '\n')

length = int(input("Lütfen şifre uzunluğunu girin: "))
characters = input("Lütfen şifrede kullanılacak karakterleri girin: ")
repeat = input("Tekrarlanan karakterlere izin verilsin mi? (E/H): ").lower() == 'e'

generate_passwords(length, characters, repeat)
