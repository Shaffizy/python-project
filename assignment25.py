def emoji_converter(message):   #code's name is emoji converter
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😞",
        ":|)": "😃"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))
