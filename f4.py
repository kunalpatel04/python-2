subject = ("Python for Data Science", 301)

try:
    subject[1] = 999  
except TypeError as e:
    print("Tuple is immutable! Error:", e)

subject = (subject[0], 999)

print("Updated tuple:", subject)
