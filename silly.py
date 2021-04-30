import random
import words
import datetime 
import time
import threading
import schedule

# section 1

def silly_string(nouns, verbs, names, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    # Add a while loop here.
    while index < len(template):
        if template[index : index + 8] == '{{noun}}':
            output.append(random.choice(nouns))
            index += 8
        elif template[index : index + 8] == '{{verb}}':
            output.append(random.choice(verbs))
            index += 8
        elif template[index : index + 8] == '{{name}}':
            output.append(names)
            index += 8
        else:
            output.append(template[index])
            index += 1
    return "".join(output)      
    # After the loop has finished, join the output and return it.


if __name__ == '__main__':
    def myFunction():
        print(silly_string(words.nouns, words.verbs, words.names,
        words.templates))


# section 2
        
# This function is to prompt user to set their timer for when 
# they want to receive these random messages
def clock():
    print("Please enter your increment: \n")
    selection = input("second\n" 
    "minute\n" 
    "hour\n" 
    "day\n").lower()
    if selection == "second":
        second() 
    elif selection == "minute":
        min()
    elif selection == "hour":
        hour()
    else:
        print("Please enter the correct increment")
        clock()



# this is the function that gets called when user wants to receive messages every seconds
def second():
    for i in range(60):
        print(i)       # this only prints the seconds the user can enter. Only for user visibilty 
    t = input("Please enter your time in seconds: ") # issue - if user enters wrong iteration, program crashes. Need fixing.
    schedule.every(int(t)).seconds.do(myFunction)   # It's the same issue for the other time options as they are the same set up.
    while True:
        schedule.run_pending()
        time.sleep(1)


# this is the function that gets called when user wants to receive messages every minute
def min():
    for i in range(60):
        print(i)     # this only prints the minutess the user can enter. Only for user visibility
    t = input("Please enter your time in minute: ")
    schedule.every(int(t)).minutes.do(myFunction)
    while True:
        schedule.run_pending()
        time.sleep(1)


# this is the function that gets called when user wants to receive messages every hour
def hour():
    for i in range(24):
        print(i)     # this only prints the hours the user can enter. Only for user visibilty
    t = input("Please enter your time in hours: ")
    schedule.every(int(t)).hours.do(myFunction)
    while True:
        schedule.run_pending()
        time.sleep(1)


# section 3: This is where I try to build the random option, but it's not working yet.

def rand_second():
    n = 0
    t = random.randint(0, 10)
    schedule.every(int(t)).seconds.do(myFunction)
    while n < 1:
        schedule.run_pending()
        n += 1
        if n == 1:
            break
        
   
    #time.sleep()
        #schedule.CancelJob


def rand_s():
   
    t = random.randint(0, 10)
    schedule.every(int(t)).seconds.do(rand_second)
    
    #while True:
    schedule.run_pending()
        #time.sleep(1)
            
        

def rand_min():
    myFunction()
    return schedule.CancelJob

def rand_m():
    t = random.randint(0, 30)
    schedule.every(int(t)).seconds.do(rand_min)
    while True:
        schedule.run_pending()
        time.sleep(1)
        

def rand_day():
    t = random.randint(0, 23)
    schedule.every(int(t)).hours.do(myFunction)
    while True:
        schedule.run_pending()
        time.sleep(1)

def rand_inc():
    while True:
        rand_list = [rand_s, rand_m]
        random.choice(rand_list)()
    

#rand_s()
#rand_second()
#rand_inc()
clock()




# todo: 
# 0- App name for now is SAM(send automatic message)-- 
# 1- how user stops or cancels an increment job or a cycle.
# 2- add a random increment function: whether it chooses a different increment after each job or...
# the random func selects an increment randomly and stays on it? I like the former better 
