# Inicjalizacja tablicy dwuwymiarowej
tablica = [[3, 5, 2],
           [7, 1, 9],
           [4, 6, 8]]

# Wyszukiwanie minimalnej wartości w każdym wierszu
for wiersz in tablica:
    min_wartosc = wiersz[0]
    for element in wiersz:
        if element < min_wartosc:
            min_wartosc = element
    if min_wartosc != wiersz[0]:
        index_min_wartosc = wiersz.index(min_wartosc)
        wiersz[0], wiersz[index_min_wartosc] = wiersz[index_min_wartosc], wiersz[0]

# Wyświetlenie tablicy po dokonaniu zamiany
for wiersz in tablica:
    print(wiersz)