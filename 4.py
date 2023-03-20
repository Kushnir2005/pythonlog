n = int(input("Podaj ilość liczb w ciągu: "))  # wczytanie ilości liczb w ciągu
negative_count = 0  # inicjalizacja liczby ujemnych liczb

for i in range(n):
    x = int(input("Podaj kolejną liczbę: "))  # wczytanie kolejnej liczby z ciągu
    if x < 0:  # sprawdzenie, czy liczba jest ujemna
        negative_count += 1  # zwiększenie liczby ujemnych liczb

print("Ilość liczb ujemnych w ciągu:", negative_count)  # wyświetlenie liczby ujemnych liczb
