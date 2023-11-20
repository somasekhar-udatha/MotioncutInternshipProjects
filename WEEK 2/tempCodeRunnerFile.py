def leftpath():
    print("you chose left path,you discover a hidden lake with a mysterious aura.")
    print("choices:\n1.Swim across the lake\n2.Follow the path around the lake")
    quest11 = int(input())
    if quest11 == 1:
        swim_across()
    else:
        continue_on_your_own()

def swim_across():
    print("you chose to swim across the lake, you encounter friendly water spirits.")
    print("choices:\n1.Accept their guidance.\n2.Politely decline and continue on your own.")
    quest111 = int(input())
    if quest111 == 1:
        accept_guidance()
    else:
        continue_on_your_own()
def accept_guidance():
    print("you chose to accepth their guidance,The water spirits guide you to a magical portal.")
    print("choices:\n1.enter the portal\n2.thank the spirits and continue your journey")
    quest1111 = int(input())
    if quest1111 == 1:
        enter_portal()
    else:
        continue_on_your_own()
def enter_portal():
    print("The portal transports you to the heart of the forest, where you find the ancient treasure.")

def continue_on_your_own():
    print("you chose to continue on your own,You find a hidden path leading to a troll bridge.")
    print("choices:\n1.Attempt to cross the bridge.\n2.Find another way around.")
    quest12 = int(input())
    if quest12 == 1:
        cross_bridge()
    else:
        rightpath()
def cross_bridge():
    print("you chose to cross the troll bridge,The troll demands a toll.")
    print("choices:\n1.Pay the toll.\n2.Try to outsmart the troll.")
    quest121 = int(input())
    if quest121 == 1:
        print("you paid toll and cross the bridge and theres nothing there")
    else:
        rightpath()
    

def rightpath():
    print(" you encounter a fierce dragon.")
    print("choices:\n1.Convince the dragon you mean no harm.\n2.Fight the dragon.")
    quest2 = int(input())
    if quest2 == 1:
        convince_dragon()
    else:
        fight_dragon()
def convince_dragon():
    print("The dragon, impressed by your bravery, allows you to pass safely.")
def fight_dragon():
    print("you are fighting dragon")
    print("choices:\n1.use your sword\n2.attempt to escape ")
    quest21 = int(input())
    if quest21 == 1:
        use_sword()
    else:
        escape()
def use_sword():
    print("If you choose to fight, you defeat the dragon and proceed and you find a hidden tunnel that leads to the treasure.")
    print("you found the tresure and you win the game")
def escape():
    print("the dragon catches you and you die")




print("Welcome to the Text-based adventure game")
print("-----------------------------------------------------")
print("GAME INTRODUCTION: ")
print("You, the brave adventurer, find yourself standing at the edge of the Enchanted Forest. Legends speak of hidden treasures and dangerous creatures lurking within its depths. Your quest is to navigate through the forest, make crucial decisions, and ultimately uncover the long-lost treasure guarded by ancient magic.")
print()
print("You start your journey at the forest entrance with only a map and a rusty sword.")
print()
print("s you venture into the forest, you come across a fork in the road.")
print("you have to choose between theese 2 choices")
print("1.Take the left path\n2.Take the right path")
quest1 = int(input())
if quest1 == 1:
    leftpath()
else:
    rightpath()

