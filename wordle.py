import random
import os
from colorama import Fore
import nltk
os.system('cls')
nltk.download('words')
words = nltk.corpus.words.words()
word_list=[]
os.system('cls')
print("Welcome to Turan's Wordle!")
#wordle_words=['TEETH','SHEEP','CROWN','PLANE','PLAIN','SLEEP','GREEN','BROWN','SAILOR','QUEEN','PANDA','CRUSH','BURST','BLAST','BLUST'
#              ,'HYDRA','PHOBIA','TRAIN','BRAIN','MAGIC','TRAGIC']
for i in words:
    if len(i)==5:
        word_list.append(i.upper())
def func(word_list):
    count=0
    l_list=[]
    target=random.choice(word_list)
    #print(target)
    sum=''
    hints=''
    a=True
    while a:
        sum=''
        hints='' #hints
        while count<=6 and sum!=target: # Changed count<6 to count<=6

            user_input=input(f'Guess {count+1}: ').upper()
            #letter_count(user_input,l_list)
            if user_input not in word_list or len(user_input)!=5:
                print('Not a valid word!')
                count-=1
            else:
                for i in range(5): # Added a for loop to compare each letter
                    if user_input[i]==target[i]:
                        #sum+=user_input[i]
                        hints+= Fore.GREEN + user_input[i] + Fore.RESET
                    elif user_input[i] not in target:
                        #sum+=user_input[i]
                        hints+= Fore.RED + user_input[i] + Fore.RESET
                    else:
                        hints+=Fore.YELLOW + user_input[i] + Fore.RESET

            count+=1
            print(hints)
            hints=''
            store=sum
            sum=''

            if count==6 or store.upper()==target.upper():
                #print('break')
                a=False
                break

    print('Target word is:',target)

x='y'
loop=True
while loop:
    if x=='y':

        func(word_list)
        x=input('again? y/n :')
        os.system('cls')
    else:
        input('press enter to exit')
        loop=False
