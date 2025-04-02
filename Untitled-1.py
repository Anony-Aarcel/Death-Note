def reverse(s):
    return s[::-1]

def encrypt (s):
    new_s = ''
    for c in s:
        new_s += c + random_letter()

        return reverse(new_s)


if __name__ == '__main__':
    
    try:
        with open(sys.argv[1], 'r') as message_file:
            message = message_file.read()
            encrypted_message = encrypt(message)

        with open(sys.argv[1], 'w') as encrypted_message_file:
            encrypted_message_file.write(encrypted_message)
    except FileNotFoundError:
        print('File not found')
    except IndexError:
        print('Please enter a message file name')