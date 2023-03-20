# Inicjalizacja tablicy
tablica = [5, 3, 8, 2, 7]

# Wyszukiwanie minimalnej wartości w tablicy
min_wartosc = tablica[0]  # Założenie, że pierwszy element jest minimalny
for element in tablica:
    if element < min_wartosc:
        min_wartosc = element

# Wyświetlenie minimalnej wartości
print("Minimalna wartość w tablicy to:", min_wartosc)