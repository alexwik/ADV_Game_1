import random
import time
Loop = 1
End = False
while True:
    if End == True:
        Stop = input("Do you want to quit? y/n: ")
        if Stop =='y':
            quit("Bye")
    name = input("What is your name: ")
    print("You wake up in a cavern without memory of how you got there")
    time.sleep(1)
    print("")
    print("You see several structures in front of you")
    time.sleep(1)
    print("")
    choice1 = input("Do you investigate the structures? y/n: ")

    if choice1 =='y':
        print("")
        time.sleep(1)
        print("You walk towards the structures")
        print("")
        time.sleep(1)
        print("You are infront of the nearest structure")
        print("")
        time.sleep(1)
        print("You see something that looks like a door")
        print("")
        time.sleep(1)
        path2 = input("Do you want to open the door? y/n: ")
        if path2 =='y':
            print("")
            time.sleep(1)
            print("You open the door")
    if choice1 =='n':
        print("")
        time.sleep(1)
        print("You decide to stay away from the structures")
        print("")
        time.sleep(1)
        print("Do you want to look around the cavern?")
        print("")
        time.sleep(1)
        path1 = input("y/n: ")
        if path1 =='y':
            print("")
            time.sleep(1)
            print("You look around the cavern")
        if path1 =='n':
            print("")
            time.sleep(1)
            print("You gain the paranoid trait")
            print("")
            time.sleep(1)
            print("You decide to stay where you are")
            print("")
            time.sleep(1)
            print("Do you want to look around your safe space?")
            print("")
            Paranoid = input("y/n: ")
            if Paranoid =='y':
                time.sleep(1)
                print("You look around your safe space")
                print("")
                time.sleep(1)
                print("You find a carrot")
                time.sleep(1)
                print("")
                print("Do you want to look around the cavern now?")
                print("")
                time.sleep(1)
                Paranoid1 = input("y/n: ")
                if Paranoid1 =='y':
                    print("You lose the trait paranoid")
                    print("")
                    time.sleep(1)
                    print("You look around the cavern")
                if Paranoid1 =='n':
                    print("You just sit in your safe space eating carrots")
            if Paranoid =='n':
                print("You gain the insane trait")
                print("")
                time.sleep(2)
                print("Because you are insane you lose track of time and die of starvation")
                print("")
                time.sleep(1)
                print("Crazy Bastard")
                print("")
                time.sleep(2)
                print("---------------------------------------")
                End = True
                continue
            
