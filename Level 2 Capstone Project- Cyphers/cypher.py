# From char to ascii
def to_ascii(char):
    return ord(char)


# From ascii to char
def to_text(int):
    return chr(int)


# Caesar list
def caesar(string):
    char_list = list(string)
    cypher_list = []
    # Run through chars to encode each
    for c in char_list:
        curr = to_ascii(c)
        # Lowercase letters
        if 97 <= curr <= 122:
            mod = (curr - 4) % 26
            new_ascii = mod + 97
            char = to_text(new_ascii)
            cypher_list.append(char)
        # Uppercase letters
        elif 65 <= curr <= 90:
            mod = (curr + 2) % 26
            new_ascii = mod + 65
            char = to_text(new_ascii)
            cypher_list.append(char)
        else:
            # Non-letters
            cypher_list.append(c)
    cypher = ''.join(cypher_list)
    return cypher


test = caesar("It's a new car!")
print(test)
