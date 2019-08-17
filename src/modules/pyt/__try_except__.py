try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

try:
    print("Hello")
except NameError:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

f = open("demofile.txt", "w+")
try:
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    print(type(f))
    f.close()
