with open("data/onegin.txt", encoding="utf-8") as file:
    onegin = file.read()

print(type(onegin))
print(f"колво символов: {len(onegin)}")

lines = onegin.split('\n')
print(f"колво строк: {len(lines)}")

words = onegin.split()
print(f"колво слов: {len(words)}")

print(f"первые 300 символов:")
print({onegin[:300]})

print("Hello world")