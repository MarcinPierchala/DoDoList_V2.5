import DoDoList_V25_classes

if __name__=='__main__':

    
    finisher=0
    zadanka=DoDoList_V25_classes.ListDoDo('c:/Python/zadania.pickle')

    print('''WITAJ W PROGRAMIE __LISTA_2_DO__ 
    WYBIERZ MENU : 
    1 : DODAJ NOWE ZADANIE
    2 : SKASUJ NIEPOTRZEBNE ZADANIE
    3 : PRZEGLĄD ZADAŃ
    4 : ZAKOŃCZ PROGRAM
    ''')

    while finisher!=4:

        param=input(' PODAJ NUMER MENU : ')

        if param=='1':
            prior=input('''PODAJ PRIORYTET ZADANIA W SKALI : 
            1 : NAJWAŻNIEJSZE
            2 : WAŻNE
            3 : MAŁO WAŻNE 
            PODAJ TUTAJ : ''')
            opis=input('PODAJ KRÓTKI OPIS ZADANIA : ')
            zadanka.dodaj(prior, opis)

        if param=='2':
            kasuj=input('PODAJ NUMER ZADANIA DO SKASOWANIA : ')
            zadanka.skasuj(kasuj)
            
        if param=='3':
            zadanka.wyswietl()
        
        if param=='4':
            print('\nDZIĘKUJĘ ZA SKORZYSTANIE Z PROGRAMU\n\n           DO WIDZENIA\nMarcin Pierchała\n37361')
            zadanka.save()
            finisher=4
