# Python 2.7
# code by Magdalena Kudyba
import sys
import os
import time
import random

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rand_function(): # choosing random question
    a = random.randint(1, 160)
    if a <= 20:
        Question1()
    elif a > 20 and a <= 40:
        Question2()
    elif a > 40 and a <= 60:
        Question3()
    elif a > 60 and a <= 80:
        Question4()
    elif a > 80 and a <= 100:
        Question5()
    elif a > 100 and a <= 120:
        Question6()
    elif a > 120 and a <= 140:
        Question7()
    else:
        Question8()

# names of our files from command line:
and_ = ""
or_ = ""
not_ = ""
impl_ = ""
# declaration of dictionaries for each logical operator
AND = {}
OR = {}
NOT = {}
IMPL = {}

points = 0
max_points = 12


def start(): # we check if arguments from the command line are correct
    counter = 0
    for i in sys.argv[1:]:
        counter += 1
    if counter == 0:
        error()
        sys.exit()
    for arg in sys.argv[1:]:
        if (arg == "--or" or arg == "--and" or arg == "--not" or arg == "--impl"):
            continue
        elif arg == "--info":
            info()
            sys.exit()
        elif arg == "--files":
            files()
            sys.exit()
        elif arg == "and.txt":
            global and_
            and_ = arg
        elif arg == "or.txt":
            global or_
            or_ = arg
        elif arg == "impl.txt":
            global impl_
            impl_ = arg
        elif arg == "not.txt":
            global not_
            not_ = arg
        else:
            error()
            sys.exit()

    if (and_ != "and.txt" or or_ != "or.txt" or impl_ != "impl.txt" or not_ != "not.txt"):
        error()
        sys.exit()

def welcomeInfo():

    while True:
        print("GRA LOGICZNA \n\t 1 jezeli chcesz kontynuowac");
        print("\t 0 aby zakonczyc")
        print("Swoj wybor potwierdz wciskajac klawisz [ENTER] ")
        pressed = raw_input()
        ClearScreen()
        if pressed == '1':
            print("Instrukcja, jak udzielac odpowiedzi:\n\tPrzyklad:")
            print("\t\t0 - NIE")
            print("\t\t1 - TAK")
            print("\t\t2 - NIE WIADOMO")
            print("Wcisniecie cyfry odpowiadajacej danej danej odpowiedzi na pytanie \noraz potwierdzenie swojej decyzji klawiszem [ENTER].\nZaczynamy! :)")
            time.sleep( 5 )
            ClearScreen()
            break
        elif pressed == '0':
            sys.exit()
        else:
            continue

def waitForZero():
     while True:
        print("Wcisnij 0 i [ENTER] aby zakonczyc.")
        pressed = raw_input()
        ClearScreen()
        if pressed == '0':
            sys.exit()
            break
        else:
            continue

def info():
    print("Program akceptuje jako parametry wywolania sciezki do plikow \nz definicjami operatorow logicznych")
    print("Przykladowe poprawne wywolanie programu: \n\tpython game.py sciezka nazwa_pliku ...")
    print("Sciezki do pliku:")
    print("\t--and    KONIUNKCJA")
    print("\t--or     ALTERNATYWA")
    print("\t--not    NEGACJA")
    print("\t--impl   IMPLIKACJA")
    print("Uzyj opcji --files aby uzyskac informacje o formacie plikow \nz definicjami operatorow logicznych.")

def files():
    print("Pliki zawieraja definicje wartosci logicznych dla roznych \nkombinacji dwoch zmiennych logicznych:")
    print("\tKazda linia wyglada nastepujaco:")
    print("\t\tzmienna1 zmienna2 wynik")
    print("Przy czym istotna jest kolejnosc \n(np. w pliku umieszczamy kombinacje zarowno 1 0 jak i 0 1)")
    print("\tPrawda: 1")
    print("\tFalsz: 0")
    print("\tWartosc nieokreslona (ani prawda ani falsz): 2")


def error():
    print("Wystapil blad. Uzyj komendy --info w celu uzyskania dodatkowych informacji")

def userAnswers(correctAnswer):
    while True:
        answer = raw_input()
        if (answer != '1' and answer != '0' and answer != '2'):
            print ("Wystapil blad - mozliwe opcje odpowiedzi to: 0, 1, 2. Prosze sprobowac ponownie.")
            time.sleep(2)
            continue
        else:
            if answer == correctAnswer:
                countPoints()
                print("\nBrawo - poprawna odpowiedz! :)")
                time.sleep(3)
                break
            else:
                print("\nBledna odpowiedz! :(")
                time.sleep(3)
                break


# quiz

def Question1():
    print("1) Posprzatam pokoj i wyjde z psem na spacer. ")
    print("2) Nie posprzatam pokoju lub nie wyjde z psem na spacer. ")
    print("Czy zdanie 2) jest prawidlowym zaprzeczeniem zdania 1)?")
    print("\t0) TAK")
    print("\t1) NIE")
    print("\t2) NIE WIADOMO")

    p = '1' # I will tidy my room
    q = '1' # I will walk my dog
    # the first de Morgan's law: ~(p ^ q) <=> ~p v ~q
    p = '1'
    q = '1'
    correctAnswer = not_function(and_function(p,q))
    userAnswers(correctAnswer)

def Question2():
    print("Aneta powiedziala: \"Jesli w piatek pojde do kina to pojde tez na dyskoteke.\"")
    print("Czy na podstawie jej slow mozemy powiedziec, ze jesli nie pojdzie na dyskoteke \nto pojdzie do kina?")
    print("\t0) NIE")
    print("\t1) TAK")
    print("\t2) NIE WIADOMO")
    #implication - one way only
    p = '2' # we do not know if she is going to cinema
    q = '0' #she isn't going to the disco
    correctAnswer = impl_function(p,q)
    userAnswers(correctAnswer)

def Question3():
    print("\"Jezeli przeczytam podrecznik lub bede chodzil na wyklady \nto bez trudu zdam egzamin.\"")
    print("Czy musze chodzic i na wyklady i przeczytac podrecznik, zeby zdac egzamin?")
    print("\t0) TAK")
    print("\t1) NIE")
    print("\t2) NIE WIADOMO")
    # we need to check if it is necessary to attend lectures as well as reading books to pass the exam
    # example:
    p = '1' # I attend lectures
    q = '0' # I don't read books
    r = '1' # I pass my exam
    correctAnswer = impl_function(or_function(p,q), r)
    userAnswers(correctAnswer)

def Question4():
    print("Jaka wartosc logiczna przyjmuje koniunkcja ponizszych zdan?")
    print("Ziemia bedzie nieruchoma.")
    print("Ludzie w 2100 r. pobuduja osiedla na Marsie.")
    print("\t0) FALSZ")
    print("\t1) PRAWDA ")
    print("\t2) NIE WIADOMO")
    q = '2' # the first one is unknown
    r = '2' # the same what above
    correctAnswer = and_function(q, r)
    userAnswers(correctAnswer)

def Question5():
    print("Co nalezy wstawic w puste miejsce w zdaniu 2) aby zdanie to bylo \n poprawnym zaprzeczeniem zdania 1)?")
    print("1)Mam BMW lub Audi.")
    print("2)Nie mam BMW ___ nie mam Audi.")
    print("\t0) \"i\" ")
    print("\t1) \"lub\"")
    print("\t2) zarowno \"i\" jak i \"lub\" sa poprawne")
    # Second de Morgan's law:
    # ~(p v q ) <=> ~p ^ ~q
    p = '1' # I have bmw
    q = '0' # I don't have audi
    correctAnswer = not_function(or_function(p,q))
   # alternatively:
   # correctAnswer = and_function(not_function(p),not_function(q))
    userAnswers(correctAnswer)

def Question6():
    print("\"Jezeli liczba 60 jest liczba parzysta, to liczba 62 jest ujemna.\" \nTo zdanie jest implikacja dwoch zdan:")
    print("\"Liczba 60 jest liczba parzysta\" oraz \"liczba 62 jest ujemna\".")
    print("Implikacja ta jest:")
    print("\t0) falszywa")
    print("\t1) prawdziwa ")
    print("\t2) nie wiadomo")
    p = '1' # first sentence is correct
    q = '0' # second sentence is not correct
    correctAnswer = impl_function(p, q)
    userAnswers(correctAnswer)

def Question7():
    print("1.\"Berlin jest stolica Niemiec.\" \n2.\"Wszystkie koty sa czarne.\"\n3.\"Nie wiem, czy  umiem jezdzic na rolkach.\"")
    print("X - alternatywa zdan 2. i 3.")
    print("Y - koniunkcja zdan 1. i X")
    print("Z - zaprzeczenie Y\n Jaka wartosc logiczna przyjmuje Z?")
    print("\t0) falsz")
    print("\t1) prawda ")
    print("\t2) nie wiadomo")
    p = '1' # first sentence is correct
    q = '0' # second sentence is not correct
    r = '2' # we do not know
    correctAnswer = not_function(and_function(p, or_function(q,r)))
    userAnswers(correctAnswer)

def Question8():
    print("1.\"Sa wakacje i jade nad morze.\" - powiedziala Ania jadac")
    print("w polowie lutego pociagiem do Sopotu. \nJaka wartosc logiczna przyjmuje zaprzeczenie tego zdania?")
    print("\t0) falsz")
    print("\t1) prawda ")
    print("\t2) nie wiadomo")
    p = '0' # first sentence is correct
    q = '1' # second sentence is not correct
    correctAnswer = not_function(and_function(p, q))
    userAnswers(correctAnswer)

# we use the content of textfiles in dictionaries
# so that we can use it to check if player's answer is correct

def filesToDictionaries():
    with open(impl_, 'r') as file:
        for x in file:
            x = x.strip().replace(" ", "")
            IMPL[x[:2]] = x[2:]
    with open(not_, 'r') as file:
        for x in file:
            x = x.strip().replace(" ", "")
            NOT[x[:1]] = x[1:]
    with open(and_, 'r') as file:
        for x in file:
            x = x.strip().replace(" ", "")
            AND[x[:2]] = x[2:]
    with open(or_, 'r') as file:
        for x in file:
            x = x.strip().replace(" ", "")
            OR[x[:2]] = x[2:]

# Logical functions

def and_function(p, q):
    return AND.get(p + q)

def or_function(p, q):
    return OR.get(p + q)

def not_function(p):
    return NOT.get(p)

def impl_function(p, q):
    return IMPL.get(p + q)

def countPoints():
    global points
    points +=1

def end():
    print "Koniec gry!\n ~~~ Twoj wynik to:", points ," / ", max_points," punktow. ~~~"
    if (points == max_points):
        print ("GRATULACJE!!! \n Udalo Ci sie wygrac, brawo! :) ")
    elif (points > max_points/2):
        print ("Calkiem nie najgorzej! :) ")
    else:
        print ("Moze nastepnym razem bedzie lepiej... :)")
    waitForZero()

def play():
    NumberOfQuestion = 0
    while True:

        rand_function()
        NumberOfQuestion += 1
        ClearScreen()
        if (NumberOfQuestion == max_points):
                  break

# main part
start()
ClearScreen()
welcomeInfo()
filesToDictionaries()
play()
end()
