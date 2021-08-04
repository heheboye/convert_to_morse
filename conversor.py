# Convert strings of text and numbers to morse.

morse_alphabet = [".- ", "-... ", "-.-. ", "-.. ", ". ", "..-. ", "--. ", ".... ", ".. ", ".--- ", "-.- ", ".-.. ", "-- ", "-. ", "--- ", ".--. ", "--.- ", ".-. ", "... ", "- ", "..- ", "...- ", ".-- ", "-..- ", "-.-- ", "--.. ", ".-.-.- ", "--..-- ", "..--.. ", "-..-. ", "...-.- ", ".---- ", "..--- ", "...-- ", "....- ", "..... ", "-.... ", "--... ", "---.. ", "----. ", "----- ", " "]

# Convert to morse function.
def convert_to_morse(phrase):
    alphabet = 'abcdefghijklmnopqrstuvwxyz.,?/@1234567890 ' # A long string containing all the letters and most used symbols from the alphabet.
    alphabet_list = list(alphabet) # Convert the alphabet from a string into a list to have all the letters separeted in items, each with his respective index.
    morse_version = [] # Empty list where the morse version will end up stored.
    try:
        for letter in list(phrase.lower().strip()): # Each letter from the phrase passed as an argument is converted into a list, lowercased and extra spaces are removed.
            morse_version.append(morse_alphabet[alphabet_list.index(letter)]) # Appends to the morse_version list (letter by letter) from the morse_alphabet list, using the indexes from the phrase letters that's looping from alphabet_list.
        morse_version = "".join(morse_version) # Convert the list into a string again.
        print("Morse translation: " + morse_version)
    except:
        print("Avoid using weird symbols.")

while True:
    print("\nConvert to morse xd.\n")
    print("Type 1 to convert something or 2 to exit.")
    option = int(input("Select an option: "))
    if option == 1:
        entry = input("\nType something: ")
        if entry.isnumeric():
            convert_to_morse(int(entry))
        else:
            convert_to_morse(entry)
    elif option == 2:
        break