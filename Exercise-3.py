def hexascii(character):
    characters = [chr(x) for x in range(97,123)]
    hexadecimal= [hex(ord(x)) for x in characters]
    dict_hex = {}
    for each in range(len(characters)):
        dict_hex[characters[each]] = hexadecimal[each]
    print(dict_hex[character])

print("\n\nConvert any character to hexadecimal equivalent of its ASCII!")

user_bool=input("Do you want to enter a new character? (y/n):")

while user_bool!='n':
    user = input("Enter Character:")
    hexascii(user.lower())
    user_bool = input("Do you want to enter a new character? (y/n):")


