with open("data/onegin.txt", encoding="utf-8") as file:
    onegin = file.read()

VOWELS = "аеёиоуыэюя"

letters = ""
for char in onegin.lower():
    if "" <= char < "я" or char == "ё":
        letters += char

letters = letters[:20000]
print(f"колво взятых букв: {len(letters)}")

# деление на гласные и согласные
kinds = ""
for char in letters:
    if char in VOWELS:
        kinds += "Г"
    else:
        kinds += "С"

print(f"НАЧАЛО СТРОКИ: {kinds[:40]}")

transitions = {"ГГ": 0, "ГС": 0, "СГ": 0, "СС": 0}

# kinds = kinds[:20]

# элегантное решение:
for i in range(len(kinds) - 1):
    pair = kinds[i] + kinds[i + 1]
    transitions[pair] += 1
    print(pair, transitions[pair])
    print(kinds[i:])
    print()
print(transitions)

# count - ОШИБАЕТСЯ! (недосчитывает пары в случае "СССС", например)
# transitions["ГГ"] = kinds.count("ГГ")
# transitions["ГС"] = kinds.count("ГС")
# transitions["СГ"] = kinds.count("СГ")
# transitions["СС"] = kinds.count("СС")

print("Переходы:")
print(transitions)

print("Hello world")