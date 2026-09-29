file = open("sandbox/notes.txt", "w", encoding="utf-8")
file.write("первая строкааа ЧТО СЮДА НАПИСАТЬ??? \n")
file.write("Вторая строка ЧОООООООО???!?!?!?! \n")
file.close()

file = open("sandbox/notes.txt", "a", encoding="utf-8")
file.write("новая строка - дополняем файл \n")
file.close()

file = open("sandbox/notes.txt", "r", encoding="utf-8")
text = file.read()
file.close
print(text)
print(f"кол-во символов {len(text)}")



print("Hello world")