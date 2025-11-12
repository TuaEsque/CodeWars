# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    output = []
    for word in sentence.split():
        if len(word) > 4:
            output.append(word[::-1])
        else:
            output.append(word)
    return " ".join(output)

# refactored
def spin_words(sentence):
    return " ".join([word[::-1] if len(word) > 4 else word for word in sentence.split()])