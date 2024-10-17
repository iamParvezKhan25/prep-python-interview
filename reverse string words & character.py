def reverse_words(string):
    words = []
    current_word = ""
    for char in string:
        if char == " ":
            words.append(current_word)
            current_word = ""
        else:
            current_word += char

    words.append(current_word)

    reversed_string = ""
    for i in range(len(words) - 1, -1, -1):
        reversed_string += words[i] + " "

    return reversed_string.strip()


def reversed_sentance(sentance):
    temp_str = ""
    for i in sentance:
        temp_str = i + temp_str
    return temp_str


sentance = "I LOVE INDIA"
print("senance: ", sentance)

print("reverce string :", reversed_sentance(sentance))
print("reverce words :", reverse_words(sentance))
