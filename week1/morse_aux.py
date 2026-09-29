morse_dict = {
    'A': '.-',
    'B': '-...', 
    'C': '-.-.', 
    'D': '-..', 
    'E': '.', 
    'F': '..-.', 
    'G': '--.', 
    'H': '....', 
    'I': '..', 
    'J': '.---', 
    'K': '-.-.', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.', 
    'O': '---', 
    'P': '.--.', 
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-', 
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-', 
    'Y': '-.--', 
    'Z': '--..', 
    '1' : '.----', 
    '2' : '..---', 
    '3' : '...--', 
    '4' : '....-', 
    '5' : '.....', 
    '6' : '-....', 
    '7' : '--...', 
    '8' : '---..', 
    '9' : '----.', 
    '0' : '-----' 
}

our_text = "ALPHA"

morse_text = []

for letter in our_text:
    print(f"Наша буква: {letter}, Морзе: {morse_dict[letter]}")
    morse_text.append(morse_dict[letter])

final_text = " ".join(morse_text)
print(final_text)

def text_to_morse():
    our_input = input("введите тектс (англ): \n")
    our_input = our_input.upper()
    morse_text = []

    for letter in our_input:
        try:
            morse_text.append(morse_dict[letter])
        except:
            print("вводи нормально")
            return

    final_text = " ".join(morse_text)
    print(f"текстс в морзе: {final_text}")

    return final_text