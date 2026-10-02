import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cars.csv")

x = df["mileage"]
y = df["price"]

w = -0.08
b = 28000

predictions = w * x + b

print(x)
print(predictions)


plt.scatter(x, y)
plt.plot(x, predictions)

plt.xlabel("Mileage, km")
plt.ylabel("Price, EUR")
plt.title("Car price vs mileage")

#plt.show()

