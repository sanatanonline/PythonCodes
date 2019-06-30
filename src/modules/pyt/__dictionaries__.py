car = {
    "brand": "honda",
    "model": "civic",
    "year": 1984
}
print(car)
print(type(car))

model = car["model"]
print(model)

brand = car.get("brand")
print(brand)

car["year"] = 2018
print(car)

for x in car:
    print(x)
    print(car[x])
    print(type(x))

for x, y in car.items():
    print(x, y)

if "model" in car:
    print("model is mentioned")
else:
    "model is not mentioned"

print(len(car))

car["color"] = "red"
print(car)

car.pop("model")
print(car)
# car.pop("model")
# print(car)

car.clear()
print(car)

car = {
    "brand": "honda",
    "model": "civic",
    "year": 1984
}
copy_car = car.copy()
print(copy_car)
new_car = dict(copy_car)
print(new_car)

another_car = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(another_car)
