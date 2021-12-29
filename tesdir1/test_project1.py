import time
my_string = "this program runs slowly"
for letter in my_string:
    print(letter, end = "")
    time.sleep(0.1)
print()
