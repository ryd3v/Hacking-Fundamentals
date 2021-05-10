# Program: Study app for Windows
# Author: Ryan
# Original creation date: 2021-05-10
# Version: 1
# Updated:
# pip install win10toast
#!/usr/bin/env python3
import random
import time
import subprocess as s
from win10toast import ToastNotifier

def countdown(mins, secs=0):
    t = (mins*60) + secs
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

print("Let's Study!"),
print("The topics are:\n"),
study_topics = ["Cryptography[1]", "Basic Knowledge[2]", "Reverse Engineering[3]", "Network Security[4]", "Exploitation[5]", "Forensics[6]"]

for topic in study_topics:
    print(topic)
    print()
question = input("Select topic: ")

if question == "1":
    Cryptography = []
    with open("crypt.txt", "r") as f:
        Cryptography = f.readlines()
        print("How about?:", random.choice(Cryptography)),

elif question == "2":
    Basic = []
    with open("basic.txt", "r") as f:
        Basic = f.readlines()
        print("How about?:", random.choice(Basic)),

elif question == "3":
    Reverse = []
    with open("re.txt", "r") as f:
        Reverse = f.readlines()
        print("How about?:", random.choice(Reverse)),

elif question == "4":
    Network = []
    with open("network.txt", "r") as f:
        Network = f.readlines()
        print("How about?:", random.choice(Network)),

elif question == "5":
    Exploit = []
    with open("exploitation.txt", "r") as f:
        Exploit = f.readlines()
        print("How about?:", random.choice(Exploit)),

elif question == "6":
    Forensics = []
    with open("forensics.txt", "r") as f:
        Forensics = f.readlines()
        print("How about?:", random.choice(Forensics)),

else:
    print("Topic entered not in the list!")
    print("Goodbye")
    exit()

input("Press Enter to Start timer")
countdown(30),

toaster = ToastNotifier()
toaster.show_toast("Finished!", "Well done, have a Great Day!",
threaded=True,
icon_path=None, duration=4)  # 4 seconds
