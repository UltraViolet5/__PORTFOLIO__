import os
txt_word_input = "podaj słowo do zgadniecia :  "
txt_letter_input = "zgadnij litere :  "
place =[]

def read_word(text,word=None):
    while word == None:
        word = input(text)

    return word


def read_letter(letter = ""):
    while letter == "":
        letter = input(txt_letter_input)

    return letter[0]


def number_of_letter(letter):
    number_of = len(letter)
    return number_of


def place_for_letter(len_word):
    place_for = len_word * "_|"
    print(place_for)
    return place_for


def show_index_of_letter(word):
    
    guesses_and_letter = []
    guesses = []
    
    letter = read_letter()
        
    for index in range(len(word)):
        
        if word[index] == letter:
            guesses.append(index)
    print(guesses)
    guesses_and_letter.append(guesses)
    guesses_and_letter.append(letter)
    
                
    return guesses_and_letter

            
def choise_input_metod():
    print("1: wprowadź słowo do odganiecia")
    print("2: zgaduj")
    print("3: wyjscie")
    x = None
    choise_list = [1, 2, 3]
    while x is None:
        choise_input = int(input("wybierz 1,2,3 :"))
        if choise_list.__contains__(choise_input):
            x = 1
        else:
            x = None
    print(choise_input)
    return choise_input


def input_word_to_guess():
    word = None
    while word == None:
        word = read_word(txt_word_input)
        return word

def play (word,number_of_letter):
    # ilość liter razy 3 daje ilośc podejsć
    i=0
    number_of_lives = 2*number_of_letter
    
    list_word = display_place_for_letter(word)
    place = list_word[0]
    while i <= number_of_lives :
        
        
        print("liczba podejs to " , number_of_lives  )
        print("tyle znich wykorzystałeś  =>",i*"X")
        print("                                  ")
        print("                                  ")
        i+=1
        indexes_and_letter = show_index_of_letter(word)
        # number_of_indexes = len(indexes_and_letter[0])
        os.system("cls || clear")
        #znajdz i wyswietl odgadniete litery
        guessed_letter_tupla = show_guessed_letter(list_word[1],indexes_and_letter[1],place)
        print(guessed_letter_tupla)
        
        
        if list_word_to_string(list_word):
            i = number_of_lives+1
            print("zgadłeś!!!")
            input()
            os.system("cls || clear")
            main()

    
def list_word_to_string(list_word):
    
    return list_word[0]==list_word[1]
   



def display_place_for_letter(word):
    place_for_letter_and_listword=[]
    os.system("cls || clear")
    length = len(word)
    place = list(length*"_")
    list_word=list(word)
    print(place)
    place_for_letter_and_listword.append(place)
    place_for_letter_and_listword.append(list_word)
    return place_for_letter_and_listword


def show_guessed_letter (list_word,letter,place):
    
    for index in range(len(list_word)):
        if list_word[index] == letter:
            place[index] = letter
        

    # print(place)
    # place_tupla=tuple(place)
    # print(place_tupla)
     
    return place
        





   
# def display_guessed_letter (word,indexes_or_letter,number_of_indexes):
    
    
#     


#     while i<=number_of_indexes:
#          i+=1
#          palce[i] = indexes
#          print(palce)




# def counter():
#     i = 0
#     i += 1
#     return i


# def start_bool2(arg):
#     if arg == None:
#         return False
#     elif arg:
#         return True


# def counter_bool():
#     counter()
#     if counter() == 1:
#         return False
#     else:
#         return True


# def swich(var):

#     # if var == None:
#     #     logic_counter = False
#     # else:
#     #     logic_counter = True
#     # return logic_counter
#     return not var == None


# def if_statement(word):
#     if word == "":
#         print("musisz najpierw wpisać słowo")
        
#     else:
#         place_for_letter(number_of_letter(var))
#         play(var, number_of_letter(read_word(txt_word_input)))
#         print("else")


# def if_mini_statement(swich,var):
#     if swich:
#         print("zgaduj!!")
#         main(2,var)
#     else:
#         main(1,var)

#def show_place_for_letter(word):
    # list_of_index_and_place = []
    #place = place_for_letter(number_of_letter(word))
    # index_list = show_index_of_letter(word)
    # list_of_index_and_place.append(place)
    # list_of_index_and_place.append(index_list)
    # return index_list



def make_menu(choice,correct_word=""):
    
    if choice == 1:
        correct_word = input_word_to_guess()
        make_menu(2,correct_word)     
    elif choice == 2:
        if correct_word == "":
            print("musisz najpierw wpisać słowo")
            make_menu(1)
        else:
            os.system("cls || clear")  
            #show_place_for_letter(correct_word)
            play(correct_word,number_of_letter(correct_word))   
    elif choice== 3:
        exit()




def main():
     
    choice = choise_input_metod()
    make_menu(choice)
    


    # if option == 1:
    #     guess_correct = start_bool()
    #     swicher = swich(guess_correct)
    #     if_mini_statement(swicher,guess_correct)

    # elif option == 2:
    #     if_statement(guess_correct)

    # elif option == 3:
    #     exit()
    # else:
    #     pass


main()
