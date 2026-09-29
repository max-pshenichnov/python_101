from PIL import Image
from random import randint

path_original = "data/1665_Girl_with_a_Pearl_Earring.jpg"
path_gen = "week2/jpeg_code/output/1665_Girl_with_a_Pearl_Earring_gen.jpg"

img = Image.open(path_original)

for i in range(100):
    q = randint(5, 10) # качество
    k = 10 # дополнительно сохранить каждую k-ую копию
    print(f"Итерация номер {i}")
    img.save(path_gen, quality=q)
    if i % k == 0:
        img.save(f"week2/jpeg_code/output/gradual/{i}_1665_Girl_with_a_Pearl_Earring_gen.jpg", quality=q)
    img = Image.open(path_gen)
    img.load()

print("done!")