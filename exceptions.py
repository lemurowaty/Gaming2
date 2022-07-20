from random import randint

# def func():
#     x = int(input("Podaj liczbe"))
#     print(f"Podano wartosc {10//x}")
#
# try:
#     func()
# except ValueError as e:
#     print("Podana wartosc nie jest liczba!")
#     print(e)
# except ZeroDivisionError:
#     print("Wprowadzona wartosc nie moze byc zerem!")

#napisz funkcje ktora sprawdza czy dana wartosc moze byc przekonwertowana na float, wykorzystaj wyjtki

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# x = input("Podaj wartosc")
# print("To jest liczba" if is_float(x) else "to nie jest liczba")

class ArgumentError(Exception):
    pass

#raise ValueError() #rzut wyjatkiem

def wylosuj(lista, ile):
    if type(ile) != int:
        raise ArgumentError("Parametr ile powinien byc typu int")
    if type(lista) != list:
        raise AttributeError("Parametr lista powinien byc lista")
    if ile < 0:
        raise ValueError(f"Wartośc nie powinna być ujemna, otrzymano: {ile}")

    for i in range(ile):
        lista.append(randint(1, 6))

data = []
wylosuj(data, "gfdgfd")
#wylosuj(100, 10)
#wylosuj(data, -1)
print(data)


# try:
#     data = pobierz_z_serwera()
# except ConnectionError:
#     data = wczytaj_z_pliku()
#