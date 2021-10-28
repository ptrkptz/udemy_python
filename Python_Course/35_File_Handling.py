# r = read, w = write, a = append, x = will create new, but will error if already exists

f = open("test.txt", "w")
f.write("This is some new text2")

f = open("test.txt", "a")
f.write("\nNow we appended.")

f = open("test.txt", "r")
print(f.read())

open("C:/Users/Patrick/Desktop/new_pythonFile.txt", "x")
