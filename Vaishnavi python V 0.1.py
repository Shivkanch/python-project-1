#!/usr/bin/env python
# coding: utf-8

# In[15]:


def welcoming_bot():    
    #NetTech Welcoming Bot 
    #welcome user 
    print ("welcome to NetTech!")
    #ask user its name 
    username=input("Enter your name here:")
    #greet user
    print ("Hello" ,username)

    #ask user its phone number 
    user_ph_no=input("please enter your your phone number here:")
    #display user phone number
    print("phone number:" ,user_ph_no)


    #ask user its email id
    user_ph_no=input ('please enter your email id here:')
    #display user email id 
    print ('email id:' ,user_ph_no)

    #ask user its preffered course 
    user_ph_no=input ("please enter your preffered course here:")
    #display user preffered course 
    print ("preffered course:" ,user_ph_no)

    #ask user its preffered location 
    user_ph_no=input ("please enter your preffered lacation here:")
    #display user preffered location 
    print ("preffered location" ,user_ph_no)

    user_location=input('Enter your preffered location:')

    if user_location.lower()=='thane':
        print('yes we have classes at Thane')
    else:
        print('sorry we only have classes at Thane')

def chai_bot():    
    #Mumbai's Recommandation chai Bot
    #user welcome
    print('welcome to the city of Garma Garam chai | Amchi Mumbai!')
    #ask user its name 
    user_name=input('please enter your name here:')
    #greet user 
    print('Hello' ,user_name . title())
    #ask user its budget for chai
    user_budget=int(input("please enter your budget for chai here:"))
    #500-->Taj hotel
    if user_budget>=500:
        print('Go to Taj Hotel')
    #100-500-->starbuks
    elif user_budget>=100 and user_budget<500:
        print('Go to starbuks')
    #50-100--> Udipi Hotel 
    elif user_budget>=50 and user_budget<100:
        print('Go To udipi Hotel!')
    #20-50-->Omkar's Cafe 
    elif user_budget>=20 and user_budget<50:
        print("Go To Omkar's Cafe!")
    #5-20--> Tapri
    elif user_budget>=5 and user_budget<20:
        print("Go To Tapri | Better Than Taj Hotel!")
    #5< Go Back to simon!
    else:
        print('Go Back to simon!')

def quize_game():    
    #welcome user 
    print("welcome To India's GK Quize !")
    #ask user its name
    name=input('Enter your name here:')
    #Greet user
    print('Hello' ,name)
    user_1st_question=input("1.who is  national animal:")

    if user_1st_question.lower()=="tiger":
        print('Yes you are correct')
    else:
        print('sorry you are wrong')
    user_2nd_question=input('2.which is national fruit:')

    if user_2nd_question.lower()=='mango':
        print('Yes you are correct')
    else:
        print('sorry you are wrong')
    user_3rd_question=input('3.which is national Flower:')

    if user_3rd_question.lower()=='rose':
        print('Yes you are correct')
    else:
        print('sorry you are wrong')
    user_4th_question=input('what is capital of India:')

    if user_4th_question.lower()=='new delhi':
        print('Yes you are correct')
    else:
        print('sorry you are wrong')
    user_5th_question=input('WHICH PLANET IS KNOWN AS A RED PLANET?:')

    if user_5th_question.lower()=='mars':
        print('Yes you are correct')
    else:
        print('sorry you are wrong')
    user_6th_question=input('what is the largest mammal in the world:')

    if user_6th_question.lower()=='the blue whale':
        print('Yes you are correct')
    else:
        print('sorry you are wrong')
    user_7th_question=input('how many countries are there in world?:')

    if user_7th_question.lower()=='seven':
        print('Yes you are correct')
    else:
        print('sorry you are wrong')
    user_8th_question=input('who painted the mona lisa?:')

    if user_8th_question.lower()=='leonardo da vinci':
        print('Yes you are correct')
    else:
        print('sorry you are wrong')
    user_9th_question=input('What is the chemical symbol of water?:')

    if user_9th_question.lower()=='H2O':
        print('Yes you are correct')
    else:
        print('sorry you are wrong')
    user_10th_question=input('who invited the light bulb?:')

    if user_10th_question.lower()=='Thomas Edison':
        print('Yes you are correct')
    else:
        print('sorry you are wrong')

        

def Airport_Bot():    
    #THANE TO AIRPORT BOT
    #Welcome User 
    print('WELCOME TO TRAVEL RECCOMANDATION BOT (MUMBAI AIRPORT)')
    #ask user its name 
    user_name=input('please enter your name here:')
    #greet user 
    print('Hello',user_name.title())
    #ask user its budget 
    budget=int(input('please enter your budget here:'))
    #500> You can go with ola
    if budget>=500:
        print('you can go by ola')
    #100-500--> You can go by auto
    elif budget>=100 and budget<500:
        print('You can go by auto')
    #50-100--> You can go by bus 
    elif budget>=50 and budget<100:
        print('You can go by bus')
    #10-50--> You can go by train
    elif budget>=10 and budget <50:
        print('You can go by train')
    #10< please stay at home 
    else:
        print('please stay at home')


def catchy_cloths():    
    #MEMORABLE AND CATCHY CLOTHS
    #Welcome user 
    print('Get the best outfit of your life')
    #ask user its name
    user_name=input('please enter your name here:')
    #greet user 
    print('Hello',user_name.title())
    #ask user its budget
    budget=int(input('please enter your budget here:'))
    #5000> you can go to H&M 
    if budget>=5000:
        print('you can go to H&M')
    #1000-5000--> you can go to jogeshwari market
    elif budget>=1000 and budget<5000:
        print('yo can go to jogeshwari market')
    #500-1000--> you can go to zudio 
    elif budget>=500 and budget<1000:
        print('you can go to zudio')
    #100-500--> you can go to local market
    elif budget>=100 and budget<500:
        print('you can go to local market')
    #100< you can wear your leftover cloths
    else:
        print('you can wear your leftover cloths')
    #thank user
    print('thank you be Happy , and be Fashionable')



def heads_tails_game():    
    #Heads & Tails Game 
    #user welcome
    print('Welcome to Heads or Tails Game!')
    #ask user Heads or Tails 
    user_choice=input('please choose Heads or Tails:')
    #display user choice 
    print('you choose' ,user_choice.title())
    #coin toss
    import random 
    if (random.choice('ht'))=='h':
        coin_toss='Heads'
    else:
        coin_toss='Tails'

    #display coin result
    print('coin Result:' ,coin_toss)
    #if user choice is equal to coin toss--> you win!
    if user_choice.lower()==coin_toss.lower():
        print('you win!')
    #else--> you lose!
    else:
        print('you lose!')

def dice_game():    
    #welcome to dice game
    #welcome user
    print('welcome to the dice game')
    #ask user to roll dice
    user_roll=int(input('please enter the number'))
    if user_roll>=1 and user_roll<=6:
        #display user roll
        print('You have choose' ,user_roll)
        #dice rolled
        import random
        dice_rolled=int(random.choice('123456'))
        #display result
        print('dice result' ,dice_rolled)
        if user_roll==dice_rolled:
            print('you win!')
        else:
            print('you lose!')

def Two_dice():    
    #welcome to Two Dice Game
    #welcome user
    print('Welcome to Two Dice Game')
    #ask user for input (1-6)
    user_choice=int(input('please enter a number between 2-12:'))
    if user_choice>=2 and user_choice<=12:
        #display user input
        print('you choose:' ,user_choice)
        #dice toss
        import random
        dice_toss=random.randrange(2,13)
        #display dice result
        print('dice result:' ,dice_toss)
        #if user input is equal to dice result -->you win
        if user_choice==dice_toss:
            print('you win!')
        #else-->you lose
        else:
            print('you lose!')
    else:
        print('invalid input!')


def multiplication_table():    
    #multiplication table
    #welcome user
    print('welcome to the world multiplication!')
    #take 1 number as input from user
    num=int(input('please enter a number here:'))
    #display multiplication table
    for i in range(1,11):
        print(num,'x',i,'=',num*i)

def cube_table():   
    #cube table 
    #welcome user
    print('welcome to the world cube!')
    #take 1 number as input from user
    num=int(input('please enter a number here:'))
    #display cube table
    for i in range(1,11):
        print(i,'cube is',i**3)

def factorial_table():    
    #Factorial table
    #Welcome user
    print('Welcome to the factorial world!')
    #take 1 number as input from user
    user_number=int(input('please enter a number here:'))
    #display factorial table
    fact=1

    for i in range(1,user_number+1):
        fact=fact*i
    print('The factorial of','is',fact)

def fabiconni_table():  
    #Fabiconni table
    #welcome user
    print('welcome to the fabiconni world!')
    #take 1 number as input from user
    user_number=int(input('please enter a number here:'))
    #display fabiconni table 
    num=10
    n1,n2=0,1

    for i in range(2,user_number):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3)




def password_generator():  
    #welcome user
    #password generator
    print('welcome user to generate password:')
    #ask user to number
    user_number=int(input('Enter a number you want for password:'))

    #define variable 
    import random
    charecters='0123456789abcdefgfijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_+}:">?*/'
    password =""
    #create a loop
    for i in range (user_number):
        password=password+(random.choice(charecters))
    #8> sorry please enter a strong password
    if user_number<=8:
        print('sorry please enter a strong password:')
    else:
        print('the password is here:')
    #print the password
    print(password)



def countdown():   
    from countdown import countdown
    #create a countdown of 1 minute and 10
    countdown.coun(mins=1,secs=10)
    #create a countdown of 1 minute
    countdown(1)
    #create a countdown of 10 seconds
    countdown(mins=0,secs=10)

def mind_game():   
    #welcome user
    import time
    #welcome to the mind game
    print('welcome to the mind game:')
    time.sleep(3)

    #ask user to guess number between 1-5000
    print('Guess number between 1-5000!')
    time.sleep(3)

    #ask user to multiply that number by 2
    print('Do multiplication by 2!')
    time.sleep(3)

    import random
    num=0

    for i in range(4):
        #ask user to add 50 in it
        temp_num=random.randrange(1,100)
        num=num+temp_num
        print('Alright! now add' ,temp_num,'in it!')
        time.sleep(3)

    # ask user to divide by 2
    print('Now divide by 2 here:')
    time.sleep(3)

    #ask user to subtract the choosen number from it
    print('Do subtract with your choosen number:')
    time.sleep(3)

    #ask user to answer is here
    time.sleep(3)

    print('yes your answer is' ,num/2)

#importing tkinter library
import tkinter as tk

#creating a main window 
window=tk.Tk()

#change title
window.title('Vaishnavi shinde')

#size
window.geometry('730x500')

#lable
tk.Label(window,text='Python Projects',font=('Helvetica',24)).place(x=270,y=30)
tk.Label(window,text='Made By: Vaishnavi shinde',font=('Helvetica',12)).place(x=290,y=70)

#button
tk.Button(window,text='Multiplication Table',command=multiplication_table).place(x=50,y=130,width=200,height=40)
tk.Button(window,text='Factorial Table',command=factorial_table).place(x=280,y=130,width=200,height=40)
tk.Button(window,text='Fabiconni Table',command=fabiconni_table).place(x=500,y=130,width=200,height=40)
tk.Button(window,text='Mind Game',command=mind_game).place(x=50,y=180,width=200,height=40)
tk.Button(window,text='countdown',command=countdown).place(x=280,y=180,width=200,height=40)
tk.Button(window,text='cube table',command=cube_table).place(x=500,y=180,width=200,height=40)
tk.Button(window,text='Password Generator',command=password_generator).place(x=50,y=230,width=200,height=40)
tk.Button(window,text='Two Dice',command=Two_dice).place(x=280,y=230,width=200,height=40)
tk.Button(window,text='Dice Game',command=dice_game).place(x=500,y=230,width=200,height=40)
tk.Button(window,text='Heads Tails',command=heads_tails_game).place(x=50,y=280,width=200,height=40)
tk.Button(window,text='Catchy Cloths',command=catchy_cloths).place(x=280,y=280,width=200,height=40)
tk.Button(window,text='Airport Bot',command=Airport_Bot).place(x=500,y=280,width=200,height=40)
tk.Button(window,text='Quize Game',command=quize_game).place(x=50,y=330,width=200,height=40)
tk.Button(window,text='Chai Bot',command=chai_bot).place(x=280,y=330,width=200,height=40)
tk.Button(window,text='Welcoming Bot',command=welcoming_bot).place(x=500,y=330,width=200,height=40)




#ye agar nai likhoge toh UI nai dikhega
window.mainloop()




# In[ ]:




