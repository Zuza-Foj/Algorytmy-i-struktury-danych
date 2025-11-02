def is_palindrom(sl):
    if type(sl) != str:
        print("To nie jest słowo!")
    else:
        sl = sl.upper()
        for i in range(len(sl)):
            if sl[i] != sl[len(sl) - i - 1]:                        # -1, żeby indeksy się zgadzały
                return False
            return True

if is_palindrom('kajAk'):
    print('Jest palindromem')
else:
    print('Nie jest palindormem')

if is_palindrom('krowa'):
    print('Jest palindromem')
else:
    print('Nie jest palindormem')
