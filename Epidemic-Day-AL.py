print("Epidemic Day board game by AL '23 \nYou will need the game board that goes with this game!")
def intro():
  print("Hello, I am your narrator for this adventure you will embark on!") 
  print("Today is 2089 and the Earth is being ravaged by deadly pandemics.") 
  print("You are a 7th grader that was on a camping trip, but has been stranded in the forest.")
  print("Your goal is to follow the path and arrive safely in the quariatine.")
  print(" ")
  print("How to play:")
  print("You start with 20 health points, each round you lose 1 health point(HP).")
  print("The objective is to arrive at quarintine(There are 52 spaces).")
  print("Try and avoid the 3 death traps(You die if you land on those spaces).")
  print("Each round you first roll a dice one time. The number you get from a roll determines the amount of spaces you go.")
  print("Then you pick a card. Do whatever the card says.")
  print("Once you've done the actions, deduct 1 HP from your current HP status.")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("If you have any questions email me 23alo@athenian.org, be honest, good luck and have fun! ")
  print("")
  print("Refrences: https://animalsmart.org/species/dogs/dogs-help-reduce-stress , https://www.cdc.gov/rotavirus/about/symptoms.html, https://emojipedia.org/people/ ")
  print("")
  print("")
  print("")
  print("")
  print("")
  
def roll():
  import random
  dice=random.randint(1,6)
  print("")
  print("Move "+ str(dice)+ " spaces forward")
  print("")
  
def sit_cards():
  import random 
  cards=random.randint(1,15)
  if cards==1:
    print("")
    print("You are desperate and hungry.")
    print("You see a basket.")
    print("You open the basket and realize that there are an abundance of clean fruit and a shady bag of hot cheeeetos. 🤠")
    print("...")
    print("As a 7th grader, you decide to consume the hot cheetos.")
    print("...")
    print("Well played... you now have rotavirus. Symptoms you have are: constant diarrhea, vomiting, and fever. This lasted for 5 days")
    print("lose 4 HP💩.")
    print("")
  if cards==2:
    print("")
    print("While walking you hear an intimidating sound behind you.")
    print("You see a van coming towards you.")
    print("The van skids and parks in front of you.")
    print("...")
    print("The driver says to be careful and drops you a box.")
    print("Then the driver drives away 😐")
    print("You open the box and find out that inside there's water, food, and neosporin! Gain 4 HP!")
    print("")
  if cards==3:
    print("")
    print("You feel like your lungs are collapsing.")
    print("You feel like your heart is racing.")
    print("...")
    print("You feel exhausted, and for the last two days you were coughing, fatigued, and had a shortness of breath.")
    print("You suffered cardiovascular bronchitis, lose 6 HP 😮")
    print("")
  if cards==4:
    print("")
    print("You find a jacket!")
    print("It keeps you warm.")
    print("...")
    print("Although it keeps you warm, you begin to start feeling toooo warm.")
    print("You have a fever.")
    print("Soon you realize that you have caught the pandemic, Devil's Fiery, but it was too late")
    print("Devil's Fiery is a virus that is highly contagious and is immune to high body tempratures.")
    print("Forcing your body to raise its body temprature to more than 107 degress Farenheit.") 
    print("Thus, damaging and burning vital organs, such as the brain.")
    print("")
    print("You have unfortunately perished. 😞")
    print("")
  if cards==5:
    print("")
    print("You tripped and fell.")
    print("...")
    print("Lose 2 HP.")
    print("")
  if cards==6:
    print("")
    print("You find a dog.")
    print("Dog follows you.")
    print("...")
    print("🐶")
    print("...")
    print("You pet the dog.")
    print("...")
    print("Playing with pets increase stress reducing hormones like oxytocin, and reduce the production of the stress hormone cortisol.✨")
    print("")
    print("Move 6 spaces forward.")
    print("")
  if cards==7:
    print("")
    print("🌧️")
    print("🌨️")
    print("🌩️")
    print("Weather conditions are terrible...")
    print("You find shelter...")
    print("...")
    print("Can't seem to find a safe place...")
    print("...")
    print("🏠")
    print("You finally find shelter; however, you are shivering, you have a weak pulse and you feel slow.")
    print("")
    print("You are suffering from hypothermia, move back 3 spaces and lose 3 HP")
    print("")
  if cards==8:
    print("")
    print("YOHOHO!")
    print("In the distance, you hear a joyous roar...")
    print("🎅")
    print("You were gifted 8 HP! Happy Holidays!!!")
    print("")
  if cards==9:
    print("")
    print("Last night, you barely slept.")
    print("You feel really sick inside and you really want to sleep.")
    print("But then you find your inner determination and continue to persist onward to the quarantine.💖")
    print("...")
    print("You were going the wrong direction.👍👏👍👏👍👏👍👏👍👏👍👏")
    print("...")
    print("Move back 5 spaces")
    print("")
    print("Jokes aside, sleep is extremely important. Trust me on this one.")
    print("")
  if cards==10:
    print("")
    print("You hear voices in the distance...")
    print("As you're curious you decide to move closer to the voices.")
    print("...")
    print("😃")
    print("YOU FIND YOUR CLASSMATES FROM THE CAMPING TRIP!!!")
    print("...")
    print("You join your class and you all return safely to the quarantine!")
    print("")
    print("Congratulations! You've won!!!🎉🎉🎉")
    print("")
  if cards==11:
    print("")
    print("Out of luck or misfortune, you arrive in the Jungle.")
    print("")
  if cards==12:
    print("")
    print("Out of luck or misfortune, you arrive in the Megalopolis.")
    print("")
  if cards==13:
    print("")
    print("Out of luck or misfortune, you arrive in the Outlands.")
    print("")
  if cards==14:
    print("")
    print("Out of luck or misfortune, you arrive in the Boroughs.")
    print("")
  if cards==15:
    print("")
    print("Roll again and move forward!")
    print("")

intro()
response=0
while response!=(3,4):
  response=int(input("To roll dice {1} To pick cards type in {2} If you die type in {3} If you won type in {4}:  "))
  if response==1:
    roll()
  if response==2:
    sit_cards()
  if response==3:
    for x in range (4):
      print("")
      print("💀😐💀😐💀😐💀😐💀😐💀😐💀😐💀😐💀😐💀😐💀😐Try again?💀😐💀😐💀😐💀😐💀😐💀😐💀😐💀😐💀😐💀😐💀😐💀😐💀")
    break
  if response==4:
    for x in range (4):
      print("")
      print("🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊You're just lucky.🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊🤑🎊")
    break

