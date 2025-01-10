#class work
text = input("Enter a text: ")

lower_text = text.lower()
print("Lowercase:", lower_text)

upper_text = text.upper()
print("Uppercase:", upper_text)

capitalized_text = text.capitalize()
print("Capitalized:", capitalized_text)

search_word = input("Enter a word to search for in the text: ")
index = text.find(search_word)

if index != -1:
    print(f"The word '{search_word}' was found at index {index}.")
else:
    print(f"The word '{search_word}' was not found in the text.")
