import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

x = re.findall("ai", txt)
print(x)

x = re.findall("Portugal", txt)
print(x)


x = re.search(r"\s", txt)

print("The first position:", x.start())

x = re.search("Portugal", txt)
print(x)

x = re.split(r"\s", txt)
print(x)

x = re.sub(r"\s", "9", txt)
print(x)

x = re.search(r"\bS\w+", txt)
print(x.span())

x = re.search(r"\bS\w+", txt)
print(x.group())
