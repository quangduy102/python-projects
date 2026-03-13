"""
I will build an application to translate letters with accents to letters without accents
For example, "đ" will be translated to "d", "á" will be translated to "a", "é" will be translated to "e", etc.

"""

letters = input("Nhap chuoi can dich: ")

def translate(letters):
    translate = ""
    for letter in letters:
        if letter == "đ":
            translate += "d"
        elif letter == "á":
            translate += "a"
        elif letter == "é":
            translate += "e"
        elif letter == "í":
            translate += "i"
        elif letter == "ó":
            translate += "o"
        elif letter == "ú":
            translate += "u"
        else:
            translate += letter
    return translate

print(f"Chuoi sau khi dich: {translate(letters)}")