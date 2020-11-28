# Encrypt this!
# You want to create secret messages which can be deciphered by the Decipher
#this! kata. Here are the conditions:

# - Your message is a string containing space separated words.
# - You need to encrypt each word in the message using the following rules:
# - The first letter needs to be converted to its ASCII code.
# - The second letter needs to be switched with the last letter

# Keepin' it simple: There are no special characters in input.

# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

def encrypt_this(text):
    """
    >>> encrypt_this('Hello')
    '72olle'

    >>> encrypt_this('good')
    '103doo'

    >>> encrypt_this('hello world')
    '104olle 119drlo'

    >>> encrypt_this('hello world')
    '104olle 119drlo'

    >>> encrypt_this('A wise old owl lived in an oak')
    '65 119esi 111dl 111lw 108dvei 105n 97n 111ka'
    """
    words = text.split()
    encrypted_words = []

    for word in words:
        splitted_text = [letter for letter in word]
        encrypted_text = splitted_text

        encrypted_text[0] = str(ord(encrypted_text[0]))

        if len(splitted_text) >= 3:
            encrypted_text[1], encrypted_text[-1] = encrypted_text[-1], encrypted_text[1]

        encrypted_words.append(''.join(encrypted_text))

    return ' '.join(encrypted_words)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
