import matplotlib.pyplot as plt
list = []

entered_num = int(input("Number? : "))
n = entered_num
while n != 1:
    if n % 2 == 0:
        n /= 2
        print(n)
        list.append(n)
    elif n % 2 != 0:
        n = 3 * n + 1
        print(n)
        list.append(n)

plt.plot(list)
plt.show()
