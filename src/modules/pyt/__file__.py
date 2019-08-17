import os

f = open("demo_file.txt", "rt")

print(f.read())
print(f.read(5))
print(f.readline())

for x in f.read():
    print("---->")
    print(x.lower())

f.close()


f = open("demo_file2.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demo_file2.txt", "r")
print(f.read())


f = open("demo_file3.txt", "w")
f.write("oops! I have deleted the content!")
f.close()

f = open("demo_file3.txt", "r")
print(f.read())
f.close()

if os.path.exists("demo_file.txt"):
    os.remove("demo_file.txt")
else:
    print("The file does not exist")
