LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(ch, alphabet):
    # Shift the character by 13 positions within the given alphabet
    if ch in alphabet:
        pos = alphabet.index(ch)
        new_pos = (pos + 13) % 26
        return alphabet[new_pos]
    else:
        return ch


def rot13(text):
    # Apply ROT13 transformation to the given text
    result = ""
    for ch in text:
        if ch in LOWER_ALPHABETS:
            result = result + shiftCharacter(ch, LOWER_ALPHABETS)
        elif ch in UPPER_ALPHABETS:
            result = result + shiftCharacter(ch, UPPER_ALPHABETS)
        else:
            result = result + ch
    return result


def writeFile(filename, content):
    # Write the content to a file in UTF-8 encoding
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(content)