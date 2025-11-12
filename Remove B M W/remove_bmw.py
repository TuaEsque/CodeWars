# https://www.codewars.com/kata/59de795c289ef9197f000c48

def remove_bmw(string):
    if type(string) != str:
        raise TypeError("This program only works for text.")

    bmw = ["b", "m", "w", "B", "M", "W"]
    return "".join([l for l in list(string) if l not in bmw])