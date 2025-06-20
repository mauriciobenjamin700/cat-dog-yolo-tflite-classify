from glob import glob


cat = glob("data/Cat/*")
dog = glob("data/Dog/*")

print(f"Number of cat images: {len(cat)}")
print(f"Number of dog images: {len(dog)}")