def hanoi(n, source, target, auxiliary, towers):
    if n == 1:
        disk = towers[source].pop()
        towers[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {towers}")
    else:
        hanoi(n - 1, source, auxiliary, target, towers)
        hanoi(1, source, target, auxiliary, towers)
        hanoi(n - 1, auxiliary, target, source, towers)

def main():
    n = int(input("Введіть кількість дисків: "))
    towers = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {towers}")
    hanoi(n, 'A', 'C', 'B', towers)
    print(f"Кінцевий стан: {towers}")

if __name__ == "__main__":
    main()
