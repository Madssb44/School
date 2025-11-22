# text based adventure!

# things i want: classes with stats, different paths, randome rolls, equiment,
import time
import random
# Special items
axeOfGortash = 0
ringOfWrath = 0
ringOfRoses = 0 
elfPendent = 0


damage = 0
# Warrior skills 
def swordSlash():
    global lfb
    global power
    global ghp
    global whp
    global ehp
    global dhp
    global damage
    global axeOfGortash
    global ringOfWrath
    global ringOfRoses
    global hp
    damage = -1
    while damage < 0: 
        if power == 10:
            ssdam = 2 + lfb
        if power >= 30: 
            ssdam = 6 + lfb
        if power >= 25:
            ssdam = 5 + lfb
        if power >= 20:
            ssdam = 4 + lfb
        if power >= 15:
            ssdam = 3 + lfb
        if ssdam > 0:
            damage = ssdam + axeOfGortash + ringOfWrath
            hp -= ringOfRoses
            ssdam = 0
            print(f"You deal {damage} damage to your opponent!")
            return damage, hp
            break

def brutalize():
    global energy
    global lfb
    global power
    global ghp
    global whp
    global ehp
    global dhp
    global damage
    global axeOfGortash
    global ringOfRoses
    global ringOfWrath
    global hp
    damage = -1
    while damage < 0:
        if energy >= 3:
            if power == 10:
                bdam = 5 + lfb
            if power >= 30: 
                bdam = 9 + lfb
            if power >= 25:
                bdam = 8 + lfb
            if power >= 20:
                bdam = 7 + lfb
            if power >= 15:
                bdam = 6 + lfb
            if bdam > 0:
                damage = bdam + ringOfWrath + ringOfWrath
                hp -= ringOfRoses
                bdam = 0
                energy -= 3
                print(f"You deal {damage} damage to your opponent!")
                return damage, hp
                break
        if energy < 3:
            print("You feel too exhausted to use this skill...")
            break

def lustForBlood():
    global lfb
    upped = 1
    while upped > 0:
        lfb += 1
        upped -= 1
        if upped == 0:
            return lfb
            break

# Ranger skills


# Mage skills


# Monster stats


# Goblin stats
ghp = 5
gpower = 1

# Wolf stats
whp = 8
wpower = 2

# Elf stats
ehp = 15
epower = 2

# Dragon stats
dhp = 50
dpower = 5

def combatGoblin():
    global hp
    global arm
    global power
    global money
    global swordSlash
    global brutalize
    global lustForBlood
    global ghp
    global gpower
    global damage
    print("Welcome to the combat part of the game!")
    time.sleep(2)
    print("As a warrior You have a few options to choose from each with their own effect!")
    time.sleep(2)
    print("""
    Sword slash: your basic attack! dealing normal damage and always being avaliable!
    
    Brutalize: lets you go into a frenzy of attacks ripping through the enemy!
    The only catch is that it takes a lot of energy 3 to be exact!
    You gain 1 energy each turn that passes and always start combat with 3 energy!
    
    Lust for blood: Lets out your inner bloodlust! giving your attacks + 1 damage for the rest of combat!
    While i can be stacked its also another turn where your enemy can attack you freely so use it carefully!
    """)
    alive = 2
    while alive > 1:
        if hp <= 0:
            alive -= 1
        if ghp <= 0:
            alive -= 1
        else:
            attack = input("What do you do?\n1 = Sword slash\n2 = Brutalize\n3 = Lust for blood\n")
            
            if attack == "1":
                swordSlash()
                ghp -= damage
                hp = hp - gpower - arm
                print("the goblin striks back at you!")
                    
            if attack == "2":
                brutalize()
                ghp -= damage
                hp = hp - gpower - arm
                print("The goblin lashes out at you from the pain slashing you with its dagger!")
                
            if attack == "3":
                lustForBlood()
                hp = hp - gpower - arm
                print("The goblin takes the oppotunity to stab you while you focus!")
        
    if hp <= 0:
        print("looks like even a goblin can take out an adventure huh...")
        time.sleep(2)
        print("Maybe adventuring wasnt for you in the end...")
        time.sleep(2)
        print("GAME OVER")
        exit()
    if ghp <= 0:
        print("Looks like goblins are no problem for you!")
        time.sleep(2)
        print("""
        Time to claim your spoils!
        1 = That goblin must have something it found on the charaige thats worth taking!
        2 = Goblins are dumb no way they know what to take! better search the charaige myself!
        3 = Well An adventure helps people so taking someones stuff doesnt sound like helping... better leave it be!""")
        loot = input("What do you do? (1/2/3)\n")
        if loot == "1":
            print("You search the goblin and find a small pouch with some coins!")
            money += 100 
        if loot == "2":
            print("You search the charaige and find a rugged looking iron chestplate!")
            arm += 1
        if loot == "3":
            print("You start walking along the road again only to be stopped by someone running out of the froest off to the side!")
            time.sleep(2)
            print("Thank you so much for dealing with that goblin! i thought they could get away with all my stuff!")
            time.sleep(2)
            print("Here take this as a reward! i know its not much but i hope it will help!")
            time.sleep(2)
            print("They hand you a large two sided axe, it looks to be made of mithrial much stronger than your steel sword!")
            power += 5
    return hp, arm, power, money

def combatWolf():
    global hp
    global arm
    global power
    global money
    global swordSlash
    global brutalize
    global lustForBlood
    global whp
    global wpower
    global damage
    
    print("!You have entered combat!")
    time.sleep(2)
    print("While the wolf still wakes up compleatly you better make your attack fast!")
    
    alive = 2
    while alive > 1:
        if hp <= 0:
            alive -= 1
        if whp <= 0:
            alive -= 1
        else:
            attack = input("What do you do?\n1 = Sword slash\n2 = Brutalize\n3 = Lust for blood\n")
            
            if attack == "1":
                swordSlash()
                whp -= damage
                hp = hp - wpower - arm
                print("the wolf claws back at you!")
                    
            if attack == "2":
                brutalize()
                whp -= damage
                hp = hp - wpower - arm
                print("The wolf lets out a howl before biting back!")
                
            if attack == "3":
                lustForBlood()
                hp = hp - wpower - arm
                print("The the wolf takes the oppotunity to claw back at you while you gather your power!")
                
    if hp <= 0:
        print("Wolfs really are strong...")
        time.sleep(2)
        print("Maybe adventuring wasnt for you in the end...")
        time.sleep(2)
        print("GAME OVER")
        exit()
    if whp <= 0:
        print("A single wolf was no problem next time bring on the entire pack!")
        time.sleep(2)
        print("""
        Time to claim your spoils!
        1 = That wolf was pretty sturdy! maybe i can use its pelt to make some armor!
        2 = There might be something in the cave worth taking with me!""")
        loot = input("What do you do? (1/2)\n")
        if loot == "1":
            print("You skin the wolf and quickly make a pair of gloves from its sturdy pelt")
            arm += 1 
        if loot == "2":
            print("You look a bit deeper in the cave and hear a little wimper")
            time.sleep(2)
            print("Over in the cornor is a little wolf pup...")
            time.sleep(2)
            wolf = input("Hmm its too young to survive by itself...\nI heard that you can train them if you get them young...\n1 = Im not risking having a wild beast with me!\n2 = One this young cant hurt me so why not try and make a friend!")
            if wolf == "1":
                print("Not wanting to become a midnight snack you kill the young wolf pup...")
                time.sleep(2)
                print("Alright time for some well deserved rest!")
                time.sleep(2)
                print("You head off to sleep!")
                time.sleep(2)
                print("You regain 1 hp while you sleep!")
                print("You wake up feeling well rested and ready for another exciting day!")
                hp += 1
                
            if wolf == "2":
                print("Well i guess theres no one to take care of you now...")
                time.sleep(2)
                print("You hold out a piece of dried meat and after a few minutes the wolf pup slowly comes over and eates it")
                time.sleep(2)
                print("There you go!")
                time.sleep(2)
                print("You set up a litte bowl of water and slowly start petting the wolf while it drinks")
                time.sleep(2)
                print("The wolf pup slowly walks over to you and curls up next to you and goes to sleep")
                time.sleep(2)
                wname = input("Hmm maybe we will become friends! and all firends needs a name\nWhat do you want your wolf to be named? ")
                time.sleep(2)
                print(f"With {wname} laying besides you its about time you get some rest as well!")
                time.sleep(2)
                print(f"The time you spend getting to know {wname} doesn't leave much time to sleep but its better than nothing")
                time.sleep(2)
                print("Besides having a friend for the adventures to come doesn't sound too bad!")
                time.sleep(2)
                print("You go to sleep with your compainon by your side!")
                time.sleep(2)
                print("You wake up the next day a little tired but happy to see your little firend wiggling its tail at you!")
                time.sleep(2)
                print(f"Well time to set out on OUR adventure now {wname}!")
                time.sleep(2)
                print(f"{wname} wiggels its tail and lets out a little woof!")
                time.sleep(2)
                print(f"You can feel it excitement coming from {wname} as i it could understand you!")
                time.sleep(2)
                power += 5
    return hp, arm, power, money, wname
        
    
    
def combatElf():
    global hp
    global arm
    global power
    global money
    global swordSlash
    global brutalize
    global lustForBlood
    global ehp
    global epower
    global ringOfRoses
    global ringOfWrath
    global axeOfGortash
    global elfPendent
    
    alive = 2
    while alive > 1:
        if hp <= 0:
            alive -= 1
        if ehp <= 0:
            alive -= 1
        else:
            attack = input("What do you do?\n1 = Sword slash\n2 = Brutalize\n3 = Lust for blood\n")
            
            if attack == "1":
                swordSlash()
                ehp -= damage
                hp = hp - epower - arm
                print("the elf slashes back at you!")
                    
            if attack == "2":
                brutalize()
                ehp -= damage
                hp = hp - epower - arm
                print("The elf lets out a hiss before striking back!")
                
            if attack == "3":
                lustForBlood()
                hp = hp - epower - arm
                print("The the elf takes the oppotunity to get a good hit in while you gather your power!")
        
        if hp <= 0:
            print("To think that a robber would be your undoing...")
            time.sleep(2)
            print("Maybe adventuring wasnt for you in the end...")
            time.sleep(2)
            print("GAME OVER")
            exit()
        if ehp <= 0:
            print("I almost feel sorry people have to resort to being a robber...")
            time.sleep(2)
            print("But that still doesnt mean that the things he has needs to go to waste!")
            time.sleep(2)
            print("You find a few small things and some coins")
            time.sleep(2)
            money += 1000
            print("You also find a pendent with a picture of a elven woman in it")
            time.sleep(2)
            print("It might belong to someone he knew or might also be stolen...")
            pendent = input("Do you bring it? \n1 = Yes someone might wanna get it back\n2 = Best not to take anything that can link me to this whole thing!")
            if pendent == "1":
                elfPendent = 1
                print("Well best get going before more trouble comes my way")
                return hp, money, elfPendent
                break
            else:
                print("Well best get going before more trouble comes my way")
                return hp, money
                break
            
def combatDragon():
    global hp
    global arm
    global power
    global money
    global swordSlash
    global brutalize
    global lustForBlood
    global dhp
    global dpower
    global ringOfRoses
    global ringOfWrath
    global axeOfGortash
    alive = 2
    while alive > 1:
        if hp <= 0:
          alive -= 1
        if dhp <= 0:
            alive -= 1
        else:
            attack = input("What do you do?\n1 = Sword slash\n2 = Brutalize\n3 = Lust for blood\n")
            
            if attack == "1":
                swordSlash()
                dhp -= damage
                hp = hp - dpower - arm
                print("the elf slashes back at you!")
                        
            if attack == "2":
                brutalize()
                dhp -= damage
                hp = hp - dpower - arm
                print("The elf lets out a hiss before striking back!")
                    
            if attack == "3":
                lustForBlood()
                hp = hp - dpower - arm
                print("The the elf takes the oppotunity to get a good hit in while you gather your power!")
        if hp <= 0:
            print("Well maybe just telling where you find something wasn't such a bad idea after all...")
            time.sleep(2)
            print("GAME OVER")
            exit()
        if dhp <= 0:
            print("After a long fought battle with one of the most mighty creatures know in this world you by some stretch of luck end up walking away alive")
            time.sleep(2)
            print("While the crowd doesn't really know rather to cheer or scream its announced that you will was the victour of the fight")
            time.sleep(2)
            print("A group of guards walk over to you and take you with them leading you outside the city into the forest where they have set up a small camp for you")
            time.sleep(2)
            print("While it doesnt please us we keep our promise...")
            time.sleep(2)
            print("You will be served a meal and have a bed for the night and there will be guards around to keep you safe but in the morning you will be on your own again...")
            time.sleep(2)
            print("Not really knowing what to say to everthing thats happened you eat your meal and get ready to go to bed")
            time.sleep(2)
            print("Now laying in bed you cant help but think back on the journy that brought you here and whats gonna happen next...")
            time.sleep(2)
            print("Thanks you for playing the game!")

def shopping():
    global money
    global power
    global axeOfGortash
    global ringOfWrath
    global ringOfRoses
    global arm
    global hp
    
    while money > 0:
        print("the city is filled with exciting shops so where to start!")
        time.sleep(2)
        store1 = input("What kind of shop are you looking for?\n1 = time to find a new and powerful weapon!\n2 = Hmm some armor wouldn't be a bad idea if im gonna be fighting all the time!\n3 = Some enchanted jewlery could give me the advantage i need!\n4 = I got what i need! time to find somewhere to sleep!")
        if store1 == "1":
            print("You walk around town a bit looking for a blacksmith")
            time.sleep(2)
            print("Not long after you find what looks to be a blacksmith displaying different weaponry!")
            time.sleep(2)
            print("You head inside and is greated by a burly looking man standing over an anvil working on what looks to be a new sword")
            time.sleep(2)
            print("Oii what can i do for you?")
            time.sleep(2)
            blacksmith = input("After talking for a bit and telling him about what you need he shows you a few options\n1 = A sturdy looking 2 handed sword\n2 = A steel kiteshield\n3 = anything more interesting?")
            if blacksmith == "1":
                print("After some haggeling you agree on a prise of 2000 coins")
                time.sleep(2)
                buy = input("Do you buy it? (y/n)\n")
                if buy == "y":
                    if money >= 2000:
                        money -= 2000
                        print("Hope it serves you well! come by anytime for all your smithing needs")
                        time.sleep(2)
                        print("You leave the store")
                        time.sleep(2)
                    if money < 2000:
                        print("Sorry a bit out of my budget for now but ill come back once i make some coin!")
                        time.sleep(2)
                        print("You leave the store")
                if buy == "n":
                    print("I need sometime to think ill come by later")
                    time.sleep(2)
                    print("Alright but you wont find anything better in town i promise you that!")
                    time.sleep(2)
                    print("You leave the store")
                    time.sleep(2)
            if blacksmith == "2":
                print("Well the price for safety is rather expensive now a days... best i can do is 3000 coins")
                time.sleep(2)
                buy = input("Do you buy it? (y/n)\n")
                time.sleep(2)
                if buy == "y":
                    if money >= 3000:
                        print("Pleasure doing buisness with you! may it keep you safe against any beast!")
                        time.sleep(2)
                        money -= 3000
                        arm += 1
                        print("You leave the store")
                        time.sleep(2)
                if buy == "n":
                    print("I need some time to think it over before spending that much...")
                    time.sleep(2)
                    print("The choice is yours ill be here if you are interested later")
                    time.sleep(2)
                    print("You leave the store as the clashing of metal comes back")
                    time.sleep(2)
            if blacksmith == "3":
                print("Well... i happen to have something...")
                time.sleep(1)
                print("Special to say the least...")
                time.sleep(2)
                print("The blacksmith goes out to a back room for a while before returning with what looks to be a battered and beaten axe that looks to be dripping blood from the edge?!")
                time.sleep(3)
                print("This... thing has been the bane of my for almost a year now!")
                time.sleep(2)
                print("Some weird elf looking fellow came by saying he was looking for an axe of the highest quality...")
                time.sleep(2)
                print("So as a proud blacksmith i brought him my finest axe!")
                time.sleep(2)
                print("The handle carved of the Eldertree and blade forged of Celestiolate by none other than myself!")
                time.sleep(2)
                print("My finest work to date! nearly cost me 100.000 coins to make!")
                time.sleep(2)
                print("And that stupid elf took it and said a few words before a big flashing light...")
                time.sleep(2)
                print("And boom... all gone all that was left in his hands was this thing...")
                time.sleep(2)
                print("Worst part is that he looked happy with it... elves are something else i tell you...")
                time.sleep(2)
                print("He ended up paying in full for the thing and letting me keep it... said he wasnt the close combat kinda guy...")
                time.sleep(2)
                print("Since then its been dripping blood all the time and been looking like this...")
                time.sleep(2)
                print("Need to keep the damn thing in a hole outback so it doesnt dirty up the place")
                time.sleep(2)
                print("So how about this... something about this axe isnt normal thats for sure...")
                time.sleep(2)
                print("toss me 500 coins and its yours no questions asked...")
                time.sleep(2)
                buy = input("Do you buy the axe? (y/n)\n")
                if buy == "y":
                    print("acually keep the coin just getting rid of it is worth the 500 coins in it of itself!")
                    time.sleep(2)
                    print("And if you ever meet that elf guy who did this ask him what the hell he did to it!")
                    time.sleep(2)
                    print("With your new axe and a bucket to keep it in for dripping reasons you leave the store")
                    time.sleep(2)
                    axeOfGortash = 1
                if buy == "n":
                    print("Weird elf guy changing an axe to be dripping blood all the time... i think ill stick to my sword...")
                    time.sleep(2)
                    print("Ayy cant blame you...")
                    time.sleep(2)
                    print("you leave the store")
                    time.sleep(2)
        if store1 == "2":
            print("You walk around town for a bit before finding a fine looking armor smith and heading inside to check it out!")
            time.sleep(2)
            print("Its a rather fance looking store but they got armor in all sorts of shapes and sizes!")
            time.sleep(2)
            print("You look around and find a few pieces you find intersting!")
            time.sleep(2)
            print("The first thing that cought your eyes was a pair of platelegs")
            time.sleep(2)
            print("They also have some shoulderguards that could be useful")
            time.sleep(2)
            print("And lastly some chainmail gloves that could come in handy")
            time.sleep(2)
            buy = input("What do you want to buy\n1 = Platelegs\n2 = Shoulderguards\n3 = Chainmail gloves")
            if buy == "1":
                print("You find a pair that fits you well and head to the counter to buy them")
                time.sleep(2)
                print("Greetings sir! looking to become better suited for whats to come i see!")
                time.sleep(2)
                print("And what a fine piece you found! truely fit for someone of your caliber!")
                time.sleep(2)
                print("It will cost you 3000 coins and they are all yours!")
                time.sleep(2)
                buy1 = input("Do you buy them? (y/n)\n")
                if buy1 == "y":
                    if money >= 3000:
                        money -= 3000
                        print("Great! wonderful doing buisness with you sir!")
                        time.sleep(2)
                        print("With your new armor in hand you leave the store!")
                        arm += 1
                    if money < 3000:
                        print("Sorry i dont have the coin for that at the moment...")
                        time.sleep(2)
                        print("You leave the store")
                if buy1 == "n":
                    print("I need to think a bit so ill be back...")
                    time.sleep(2)
                    print ("You leave the store")
                    time.sleep(2)
            if buy == "2":
                print("You find a set that fits well and walk to the counter to buy them")
                time.sleep(2)
                print("Well hello there sir! looking to buy some armor i see!")
                time.sleep(2)
                print("best keep your shoulders safe or you will lose an arm as they say!")
                time.sleep(2)
                print("Alright sir a fine pair such as there will cost you 2500 coins!")
                time.sleep(2)
                buy2 = input("Do you buy them? (y/n)\n")
                if buy2 == "y":
                    if money >= 2500:
                        print("Wonderful! be sure to come back in case you need more armor some day!")
                        time.sleep(2)
                        print("You leave the store")
                        arm += 0.5
                    if money < 2500:
                        print("I dont have the coin for that at the moemnt...")
                        time.sleep(2)
                        print("You leave the store")
                if buy2 == "n":
                    print("Just looking whats around the different stores at the moment...")
                    time.sleep(2)
                    print("You leave the store")
            if buy == "3":
                print("You find a pair of gloves that fits well and head to the counter to buy them")
                time.sleep(2)
                print("Welcome in sir! ready to get hands on i see!")
                time.sleep(2)
                print("A pair of chainmail gloves like that will cost you 500 pr glove!")
                time.sleep(2)
                buy3 = input("Do you buy them? (y/n)\n")
                if buy3 == "y":
                    if money >= 1000:
                        print("There you go sir! have a wonderful day!")
                        money -= 1000
                        time.sleep(2)
                        print("You leave the store")
                        time.sleep(2)
                    if money < 1000:
                        print("Sorry dont have the coin for that right now...")
                        time.sleep(2)
                        print("You leave the store")
                        time.sleep(2)
                if buy3 == "n":
                    print("Just looking at the moment but ill come back if i need anything")
                    time.sleep(2)
                    print("You leave the store")
                    time.sleep(2)
        if store1 == "3":
            print("You look all over town for a place that looks to be selling enchanted jewlery")
            time.sleep(2)
            print("After looking for a while you come across a shady looking house down a side road with a sign saying 'Enchanters emporium'")
            time.sleep(2)
            print("Having found nothing else so far you dicide to take a look")
            time.sleep(2)
            print("You entre and is meet with the smell of herbs... an old lady is sitting in a rocking chair off to the side asleep and some jewlery is laying around on some different tabels across the room")
            time.sleep(2)
            store2 = input("Do you stay and look? (y/n)\n")
            if store2 == "y":
                print("After a second of hesitation you decide to have a look around dispite all the off putting signs")
                time.sleep(2)
                print("You look around at the different tabels seeing if anything peaks your interest")
                time.sleep(2)
                print("There are no signs on anything no discription of the enchantments or anything")
                time.sleep(2)
                print("You find some things that looks to be made for humans... and a lot that arent!")
                time.sleep(2)
                print("You find a weird looking ring that has 3 finger holes, a neckless with a pendent that looks like its some gods symbol and lastly a bracelet made of some weird material...")
                time.sleep(2)
                store3 = input("What do you do?\n1 = bring the ring to the lady and ask what it even is\n2 = bring the neckless to the lady and ask what it is\n3 = bring the bracelet and ask the lady what it is\n4 = This is getitng weirder and weirder! time to leave!")
                if store3 == "1":
                    print("The second you touch the ring you hear a voice coming from right behind you!")
                    time.sleep(2)
                    print("you look behind you to the the old lady standing right behind you looking over your shoulder")
                    time.sleep(2)
                    print("You cant help but wonder how she got there so fast... and without you noticing...")
                    time.sleep(2)
                    print("Ahh the ring of wrath... bound to 3 fingers... 2 materials... and 1 person... interesting choice!")
                    time.sleep(2)
                    print("what do you mean?")
                    time.sleep(2)
                    print("Ahh yes i should explain what it even does!")
                    time.sleep(2)
                    print("The ring of wrath... it binds itself to the wielder once its put on... Then the next weapon you wield and finally your very soul it self hehe")
                    time.sleep(2)
                    print("Wait my soul?! what do you mean with that!")
                    time.sleep(2)
                    print("Well lets just say that you wont be putting your weapon away after putting on this ring...")
                    time.sleep(2)
                    print("But in exchange for all of that it will grant you powers to compensate of course!")
                    time.sleep(2)
                    print("And what would those powers then be?")
                    time.sleep(2)
                    print("Ahh i wont spoil all the fun for you dear! some things in life you have to learn for yourself!")
                    time.sleep(2)
                    hag = input("What do you do?\n1 = Buy the ring... whats the worst that could happen...\n2 = Binding my soul to a ring isnt really in my budget...\n")
                    if hag == "1":
                        print("Well if you have a store and sell things it cant be that bad i guess...")
                        time.sleep(2)
                        print("Im glad to hear that dear! now how do you wanna pay?")
                        time.sleep(2)
                        print("The ring will cost 1000 coins but since you dont need the rest of your fingers soon i can take the other 2 you dont need instead if interested?")
                        time.sleep(2)
                        hag1 = input("1 = i got the coins so lets go with that!\n2 = Well since i dont need them why keep them!\n3 = WAIT WHAT??!? you want my fingers what kind of store is this!!")
                        if hag1 == "1":
                            if money >= 1000:
                                print("Here you go 1000 coins!")
                                time.sleep(2)
                                print("Perfect! make sure to grab your weapon after putting the ring!")
                                time.sleep(2)
                                print("The lady lays a hand on your shoulder and your mind blanks for a second...")
                                time.sleep(2)
                                print("Your back on the main road with the ring in your hand...")
                                time.sleep(2)
                                print("Alright put the ring on grab my weapon and never let go of it! should be simple!")
                                time.sleep(1)
                                print("...")
                                time.sleep(1)
                                print("..")
                                time.sleep(1)
                                print(".")
                                time.sleep(1)
                                print("It does feel like i forgot something tho... where did i even get it from?")
                                time.sleep(2)
                                print("You heear a strange voice in your head saying 'Best of luck dear'")
                                ringOfWrath = 1
                                time.sleep(2)
                                ringOW = input("Do you put it on? (y/n)\n")
                                if ringOW == "y":
                                    print("You put on the ring and feel a slight sting in your chest...")
                                    time.sleep(2)
                                    print("You grab your weapon and for a split second it feels like it molds to your hand")
                                    time.sleep(2)
                                    print("You try to lift a single finger from the handle but its stuck to you...")
                                    time.sleep(2)
                                    print("Well this power must be amazing for this to be my life now...")
                                    time.sleep(2)
                                    print("alright back to shopping!")
                                if ringOW == "n":
                                    print("Hmm maybe i should wait until i find a new weapon before putting it on...")
                                    time.sleep(2)
                                    print("Alright better get back to shopping!")
                        if hag1 == "2":
                            print("Ahh good choice! i couldn't have said it better myself")
                            time.sleep(2)
                            print("Oh but wait how is this whole thing gonna work?")
                            time.sleep(2)
                            print("No need to worry! i just need you to take my hand with the hand and tell me which fingers you dont need...")
                            time.sleep(2)
                            print("She holds out her hand and waits for you...")
                            time.sleep(2)
                            hag2 = input("What do you do?\n1 = Take her hand\n2 = Dont take her hand")
                            if hag2 == "1":
                                print("Okay... i hope you know what you are doing...")
                                time.sleep(2)
                                print("No need to worry this is far from the first time i had to do something like this!")
                                time.sleep(2)
                                print("You reach out and she mumbels a few words you cant hear...")
                                time.sleep(2)
                                print("Alright that should do it!")
                                time.sleep(2)
                                print("She lets go of your hand and you look down to see your hand now only has 3 fingers")
                                time.sleep(2)
                                print("You cant see any sign of a wound or any pysical sign of there ever having been fingers")
                                time.sleep(2)
                                print("Well darling its been a pleasure! i hope you get lots of use out of it!")
                                time.sleep(2)
                                print("Before you can say answer you see a flashing light and you find yourself back on the main road")
                                time.sleep(2)
                                print("You have a weird feeling in your head like you forgot something...")
                                time.sleep(2)
                                print("You look down to see the ring in your hand and the fact that it only has 3 fingers doesnt even seem to bother your mind at all")
                                time.sleep(2)
                                print("All you remember is getting the ring and what it does...")
                                ringOfWrath = 1
                                time.sleep(2)
                                ringOW = input("Do you put it on? (y/n)\n")
                                if ringOW == "y":
                                    print("You put on the ring and feel a slight sting in your chest...")
                                    time.sleep(2)
                                    print("You grab your weapon and for a split second it feels like it molds to your hand")
                                    time.sleep(2)
                                    print("You try to lift a single finger from the handle but its stuck to you...")
                                    time.sleep(2)
                                    print("Well this power must be amazing for this to be my life now...")
                                    time.sleep(2)
                                    print("alright back to shopping!")
                                if ringOW == "n":
                                    print("Hmm maybe i should wait until i find a new weapon before putting it on...")
                                    time.sleep(2)
                                    print("Alright better get back to shopping!")
                            if hag2 == "2":
                                print("Oh dear no need to be so worried i know what im doing!")
                                hag3 = input("What do you do?\n1 = follow along...\n2 = bash her hand away")
                                if hag3 == "1":
                                    print("Okay... i hope you know what you are doing...")
                                    time.sleep(2)
                                    print("No need to worry this is far from the first time i had to do something like this!")
                                    time.sleep(2)
                                    print("You reach out and she mumbels a few words you cant hear...")
                                    time.sleep(2)
                                    print("Alright that should do it!")
                                    time.sleep(2)
                                    print("She lets go of your hand and you look down to see your hand now only has 3 fingers")
                                    time.sleep(2)
                                    print("You cant see any sign of a wound or any pysical sign of there ever having been fingers")
                                    time.sleep(2)
                                    print("Well darling its been a pleasure! i hope you get lots of use out of it!")
                                    time.sleep(2)
                                    print("Before you can say answer you see a flashing light and you find yourself back on the main road")
                                    time.sleep(2)
                                    print("You have a weird feeling in your head like you forgot something...")
                                    time.sleep(2)
                                    print("You look down to see the ring in your hand and the fact that it only has 3 fingers doesnt even seem to bother your mind at all")
                                    time.sleep(2)
                                    print("All you remember is getting the ring and what it does...")
                                    ringOfWrath = 1
                                    time.sleep(2)
                                    ringOW = input("Do you put it on? (y/n)\n")
                                    if ringOW == "y":
                                        print("You put on the ring and feel a slight sting in your chest...")
                                        time.sleep(2)
                                        print("You grab your weapon and for a split second it feels like it molds to your hand")
                                        time.sleep(2)
                                        print("You try to lift a single finger from the handle but its stuck to you...")
                                        time.sleep(2)
                                        print("Well this power must be amazing for this to be my life now...")
                                        time.sleep(2)
                                        print("alright back to shopping!")
                                    if ringOW == "n":
                                        print("Hmm maybe i should wait until i find a new weapon before putting it on...")
                                        time.sleep(2)
                                        print("Alright better get back to shopping!")
                                if hag3 == "2":
                                    print("You bash her hand away as she tires to grab your hand...")
                                    time.sleep(2)
                                    print("You little!...")
                                    time.sleep(2)
                                    print("You see a bright light flash for a second and when you regain your vision your back on the main road...")
                                    time.sleep(2)
                                    print("What was all that about...")
                                    time.sleep(2)
                                    print("You check your pockets to see if you have everything but notice a ring on your finger...")
                                    time.sleep(2)
                                    print("Huh weird... you try to take it off but it seems to be stuck on your finger...")
                                    time.sleep(2)
                                    print("You hear the old ladys voice loudly in your head")
                                    time.sleep(2)
                                    print("Lets hope that teaches you a lesson...")
                                    time.sleep(2)
                                    print("What? hello what do you mean?")
                                    time.sleep(2)
                                    print("You get no answer...")
                                    time.sleep(2)
                                    print("Well whatever that was im glad i got away alive...")
                                    time.sleep(2)
                                    print("Well back to shopping i guess...")
                                    ringOfRoses = 1
                    if hag == "2":
                        print("What a shame! Well be sure to come back if you change your mind!")
                        time.sleep(2)
                        print("you leave the store")
                if store3 == "2":
                    print("The second you touch the neckless you hear a voice right behind you")
                    time.sleep(2)
                    print("Ahh the neckless of life! what a fine choice!")
                    time.sleep(2)
                    print("You turn around to see the old lady standing right behind you")
                    time.sleep(2)
                    print("Oh yeah i was wondering what it was!")
                    time.sleep(2)
                    print("You are always more than welcome to ask!")
                    time.sleep(2)
                    print("Alright it will cost you 1500 coins")
                    time.sleep(2)
                    buy4 = input("Do you buy it? (y/n)")
                    if buy4 == "y":
                        if money >= 1500:
                            print("Perfect dear! see you around")
                            time.sleep(2)
                            print("With the necless now around your neck you leave the store")
                            time.sleep(2)
                            hp += 5
                        if money < 1500:
                            print("i dont have that much coin on my but if i find some ill come back!")
                            time.sleep(2)
                            print("You leave the store")
                            time.sleep(2)
                    if buy4 == "n":
                        print("sorry not at the moment but ill come back if i need it!")
                        time.sleep(2)
                        print("Alright dear!")
                        time.sleep(2)
                        print("you leave the store")
                        time.sleep(2)
                if store3 == "3":
                    print("The second you touch the bracelet you hear a voice coming from behind you")
                    time.sleep(2)
                    print("The bracelet of power i see!")
                    time.sleep(2)
                    print("You turn around and see the old lady standing right behind you")
                    time.sleep(2)
                    print("They are always so like with the new adventures!")
                    time.sleep(2)
                    print("And for the cheap price of 500 coins many get them just to be safe!")
                    time.sleep(2)
                    buy5 = input("Do you buy it? (y/n)")
                    if buy5 == "y":
                        if money >= 500: 
                            print("Alright dear have a wonderful time on your adventures!")
                            time.sleep(2)
                            print("You leave the store with your new eqipment!")
                            time.sleep(2)
                            print("Hmm how come she knew you were and aventrue? you never mentined it to her...")
                            time.sleep(2)
                            print("Well nevermind!")
                            power+= 5
                            time.sleep(2)
                        if money < 500:
                            print("Sorry i dont have coins for that...")
                            time.sleep(2)
                            print("You leave the store")
                    if buy5 == "n":
                        print("Ill have a look around before i buy something but ill come back in case i want it!")
                        time.sleep(2)
                        print("You leave the store")
                        time.sleep(2)
                if store3 == "4":
                    print("Yeah im out of here this is too weird!")
                    time.sleep(2)
                    print("You quickly leave the store and head back to the main road")
                    time.sleep(2)
            if store2 == "n":
                print("this is a bit too weird even for me!")
                time.sleep(2)
                print("You leave the weird store and look back just before turning to the main road to see the sign is gone and the shady looking house not there anymore...")
                time.sleep(2)
            time.sleep(2)
        if store1 == "4":
            return money, power, axeOfGortash, ringOfWrath, ringOfRoses, arm, hp 
            break
            
            
            

print("Greetings adventure!")
time.sleep(2)
print("Welcome to the world of xandarna")

name = input("What do you want your character to be named?\n")
time.sleep(2)

print(f"{name} what a fitting name for a future hero!")
time.sleep(2)

print(f"Alright {name} you are about to go out on a grand journy!")
print("you will come face to face with good, evil and everything that lurks in between!")
time.sleep(2)

print("""
Now every good game needs some way to fight off evil and this is no exception!
You will be a thrown into a vast world filled with lots of adventure!
""")
time.sleep(5)

clas = "w"

if clas == "w":
    hp = 15
    arm = 0
    power = 10
    dex = 5
    wis =  3
    money = 4000
    
#if clas == "r":
#    hp = 10
#    arm = 0
#    power = 5
#    dex = 15
#    wis = 5
#    money = 1000
    
#if clas == "m":
#    hp = 7
#    arm = 0
#    power = 2
#    dex = 7
#   wis = 15
#    money = 1500
    
time.sleep(2)

print("You are about to depart on a grand adventure!\nBut before you head out you need to choose how hard of a adventure you want!\nYou can pick between:\nEasy: A standart adventure and the normal experiance of the game!\nHardcore: Everything is harder! more hp more damage more trouble!\nDeathmode: Not for the faint of heart! you get hardmode but with less stats!")
mode = input("Choose your mode (easy/hard/death)\n")

if mode == "death".lower:
    hp -= 3
    power -= 2
    dex -= 2
    wis -= 2

print(f"Alright time to head out on your own grand adventure!\n{name} may the gods be in your favor!")

time.sleep(3)

print("Its a sunny morning in the land of xandarna!")
time.sleep(2)
print("birds are chirping and the small village you live in has its usual bustling sound...")
time.sleep(2)
print("Today is the day you will be setting out to make a name for yourself!")
time.sleep(2)
print("But in this vast world theres so many things to do!")
time.sleep(2)
print("You have heard of an elven village to the north out past the forest sounds like the perfect adventure to start of with!")

path = 1
if path == 1:
    print("And so the journy begins! The elven village far north.\nYou head out of the village and follow the roads leading towards the north!")
    path1 = input("Not long after you head out you see a charige off the side of the road... looks like something attacked it!\nWhat do you do?\n1 = inspect the caraige\n2 = walk past it. not my problem\n")
    time.sleep(2)
    if path1 == "1":
        print("A real adventure helps everyone in need!")
        time.sleep(2)
        print("After taking a closer look you know what happened here!\nGoblins! its not uncommon around these parts and you have seen it plenty of times in your own village...")
        acc = input("You hear something moving from inside the chairage! you cant quite hear what it is...\nSomeone could be in there and need help! but it might also be a goblin still trying to find things to steal...\nWhat do you do?\n1 = Look inside and see if someone needs help!\n2 = ignore it! those sneaky goblins arent getting me as well!\n")
        time.sleep(2)
        if acc == "1":
            print("You look for where the sound is coming from and find a goblin looking through some remains!\nIf you try to run now its gonna notice you and attack so best to try and get the jump on it!")
            energy = 3
            lfb = 0
            combatGoblin()
        if acc == "2":
            print("Those goblins really are the worst!\nIts a shame i wasn't here earlier when they attacked maybe i could have helped!")
            time.sleep(2)
            print("Trying to walk past all this while thinking about what might have heppened you let your mind slip for a second and don't notice the sound coming from the charige stoped...")
            time.sleep(2)
            print("You feel a sharp pain coming from your lower back and turn around to see the goblin who just stapped you in the back with its dagger")
            time.sleep(2)
            print("Peace was never an option...")
            time.sleep(2)
            hp -= 1
            if hp <= 0:
                print("Your world slowly fades to black...")
                print("GAME OVER")
                exit
            else:
                energy = 3
                lfb = 0
                combatGoblin()
    
    if path1 == "2":
        print("Hmm might be for the best to leave it be it could be an ambush for all i know...")
        time.sleep(2)
        print("You walk past the chariage!")
        time.sleep(2)
    print(f"You have {hp} hp do you wish to continue walking or take a rest?\n1 = Im good whats the worst that could happen!\n2 = Better safe than sorry! time for some rest!")
    rest = input()
    time.sleep(2)
    if rest == "1":
        print("And so the path to glory keeps unfolding!")
        time.sleep(2)
    if rest == "2":
        print("You set up your tent and a nice warm bonfire and get some well deserved rest!")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Huh thats weird... why do i feel so warm?")
        time.sleep(2)
        print("While fast asleep a goblin found its way to your camp and slit your throat while you slept")
        time.sleep(1)
        print("GAME OVER")
        exit
    
print("The path forward is now clearer than ever before!")
time.sleep(2)
print("You make it throught your first eventfull day as an adventure!")
time.sleep(2)
print("It might be time to set up camp tho... energy doesnt last forever! and that fight took quite a bit out of you!")
time.sleep(2)
print("You set up camp! a small bonfire to cook some food over before heading to bed...\nBut you are in the middle of a forest would it be safe to sleep on the ground all night?")
time.sleep(2)
print("You already encountered a goblin earlier and its well known that these woods have wolf's in them as well!\nA goblin suddenly doesnt sound nearly as scary!")
time.sleep(2)
camp = input("Hmm whats gonna be the best choice...\n1 = Sleep on the ground\n2 = find a cave to sleep in")

if camp == "1":
    print("Well everyone in this forest must have heard of how i killed that goblin with ease! even a wolf would know not to mess with me!")
    time.sleep(2)
    print("You head off to bed laying on the forest floor looking up at the sky thinking back on the day and all that happened...")
    time.sleep(2)
    print("You regain 1 hp!")
    hp += 1
if camp == "2":
    print("I saw a cave a short distance back might be best to sleep there to not draw unwanted attention!")
    time.sleep(2)
    print("You make your way back to the cave...")
    time.sleep(2)
    print("You check the cave entrance for signs of animals or other monsters who might have entered and left the cave")
    time.sleep(2)
    print("It looks like there might be some wolf's living in the cave...")
    time.sleep(2)
    print("Theres some foodprints around here leding into the cave so they might have gone to sleep...")
    time.sleep(2)
    cave = input("If they are asleep they would be easy to take out! but if they arent they might attack...\n1 = Head into the cave\n2 = Go back to the camp")
    
    if cave == "1":
        print("The footprints were a bit old so they are most likely asleep best to check it out now!")
        time.sleep(2)
        print("You sneak your way into the cave...")
        time.sleep(2)
        print("While there isnt much light your eyes quickly adjusted to he darkness inside the cave")
        time.sleep(2)
        print("A little further into the save you have some very soft breathing... sounds like something is asleep")
        time.sleep(2)
        print("You take few steps further into the cave...")
        time.sleep(2)
        print("Right there a few meters infront of you!\nYou see a fully grown wolf")
        time.sleep(2)
        print("Its clear that its what you heard earlier!\nThe deep rumbling breath of the sleeping wolf...")
        time.sleep(2)
        print("This cave isnt far from your camp so if it wakes up before you in the morning it might find your camp and attack you before you wake up...")
        time.sleep(2)
        cave1 = input("What do you do?\n1 = Now is the best chance! take out the wolf before it takes out you!\2 = Its dark and there might be more deeper in the cave... best to leave and hope for the best!")
        if cave1 == "1":
            print("Strike while the iron is hot! or the beast is asleep or whatever thay say!")
            time.sleep(2)
            cave2 = input("How do you attack?\n1 = Pick up a big bolder and throw it at the wolf\n2 = Rush over and strike\nLook around and find the best way to attack")
            if cave2 == "1":
                if power >= 6:
                    print("You find a large bolder laying around and throw it at the wolf while its alseep!")
                    time.sleep(2)
                    print("The wolf lets out a squeal and gets up ready to fight back but it took quite the hit from that bolder you threw")
                    time.sleep(2)
                    combatWolf()
                else:
                    print("You find a large bolder and throw it at the wolf but the bolder was a bit too heavy so you miss the wolf")
                    time.sleep(2)
                    print("You end up waking the wolf up and it looks like it wont let you off too easy now...")
                    time.sleep(2)
                    combatWolf()
            if cave2 == "2":
                if dex >= 8:
                    print("You swiftly rush over and strike the wolf!")
                    time.sleep(2)
                    print("The wolf now awake and already half beaten up looks like its ready to fight back")
                    time.sleep(2)
                    combatWolf()
                else:
                    print("You rush over to try and strike it down before it can notice you but the wolf ends up waking up just before you get over to it and dodges your sneak attack")
                    time.sleep(2)
                    print("The wolf gives you a look saying better luck next time and gets ready to attack")
                    time.sleep(2)
                    combatWolf() 
            if cave2 == "3":
                if wis >= 10:
                    print("You look around you and notice a rock above the wolf looks like it could fall any second now!")
                    time.sleep(2)
                    print("You find a small rock and throw it at the rock above the wolf making it fall onto the wolf")
                    time.sleep(2)
                    print("The wolf quickly gets back up but it looks like that falling rock did a number on it already!")
                    time.sleep(2)
                    combatWolf()
                else:
                    print("You walk around the area a bit to find the best way to attack but its too dark to notice the branches on the ground")
                    time.sleep(2)
                    print("You accidently step on a few and the sound wakes up the wolf")
                    time.sleep(2)
                    print("The wolf now looks angrily towards you for disturbing its sleep...")
                    time.sleep(2)
                    combatWolf()
                    
        if cave1 == "2":
            print("You slowly make your way out of the cave and return to your camp")
            time.sleep(2)
            print("But the extra time and the thought of a wolf attacking you in your sleep made it hard to fall asleep...")
            time.sleep(2)
            print("You regain no hp during your sleep")
            time.sleep(2)
            print(2)
            print("You wake up slightly tired but still alive!")
        
        if cave == "2":
            print("You head back to camp and go to sleep")
            time.sleep(2)
            print("You regain 1 hp!")
            hp += 1
            print("You wake up well rested and ready for yet another day!")
            time.sleep(2)

if cave == "2":
    print("You wake up early in the morning to some noice coming just outside your camp")
    time.sleep(2)
    cave3 = input("What do you do?\1 = Ignore it sleep is important\n2 = Grab your weapon and go check it out\n3 = Listen closely without moveing")
    if cave3 == "1":
        print("You try and fall back sleep but quickly get woken up by a wolf pouncing on you!")
        hp -= 5
        combatWolf()
        print("Well with all that taken care of its time to move farward!")
    if cave3 == "2":
        print("You ready your weapon and look around you!")
        time.sleep(2)
        print("And just in time you see a fully grown wolf appere from the forest with a look in its eyes saying you are its morning sncak!")
        time.sleep(2)
        combatWolf()
        print("Well with all that taken care of its time to move farward!")
    if cave3 == "3":
        print("You lay compleatly still listening to what could be moveing")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("You hear a soft growl coming not far off to the side...")
        time.sleep(2)
        print("It must be whatever was in that cave...")
        time.sleep(2)
        print("You grab your weapon and get ready to find out whats making all this fuzz")
        time.sleep(2)
        print("You see a fully grown wolf appere form the woods and it doesn't look like it wants to play fetch!")
        time.sleep(2)
        combatWolf()
        print("Well with all that taken care of its time to move farward!")
        
print("Rested and ready for whats to come you head out for the forest of the elves!")
time.sleep(2)
print("After spending all morning and most of the day in the forest you finally make it to a town!")
time.sleep(2)
print("Teldorana a bustling town known for being a corssroad for many travelers, merchants and adventures alike!")
time.sleep(2)
print("Well you have some coin to spare since you sold all your belongings before heading out so why see if something of use could be found here!")
time.sleep(4)
shopping()
print("After a day of shoping and experincing a bunce of new things you find a place to sleep")
time.sleep(2)
print("In the morning you set out again ready and eqiped for whats to come!")
time.sleep(2)
print("You leave the city behind and continue towards the north")
time.sleep(2)
print("Far out into the distance you finally start to see the elven forest!")
time.sleep(2)
print("While its still more than a days travel away you cant but help to feel excited you made it this far!")
time.sleep(2)
print("A little futher up ahead you see a man standing by the side of the road")
time.sleep(2)
print("He seems to be well dressed and doesnt seem like the type to be a robber so no need to worry about that...")
time.sleep(2)
print("But hes looks like hes trying to get your attention")
time.sleep(2)
print("When you get closer the man calls out to you")
time.sleep(2)
print("Greetings sir! would you be willing to partake in a game?")
time.sleep(2)
print("Just a harmless game of cards!")
time.sleep(2)
print("Sure how do i play?")
time.sleep(2)
print("Here i have a deck of cards with the numbers 1 through 5 i will shuffel them and hold them out face down")
time.sleep(2)
print("You will then call out a number and pick a card if you called out the right number you win otherwhise i win")
time.sleep(2)
print("Simple right? lets give it a try!")
time.sleep(2)
testCards = input("Call out your number 1 through 5\n")
testCardsResault = random.choice(1,2,3,4,5)
if testCards == testCardsResault:
    print(f"You point at a card and he flips it over to reveal a {testCardsResault}! looks like you won")
if testCards != testCardsResault:
    print(f"You point out a card and he filps it over showing a {testCardsResault}... looks like you lost")
print("Alright now you know how to play! how about we raise the stakes a little...")
time.sleep(2)
print("What do you mean?")
time.sleep(2)
print("Well you could bet coins for example! if you win i give you 10 times what you bet back and if i win i get your bet")
time.sleep(2)
cards = input("Do you play? (y/n)")
if cards == "y":
    print("Ahh a man of my liking lets get it going then!")
    while cards == "y":
        time.sleep(2)
        print("and how much are you willing to bet?")
        time.sleep(2)
        bet = input("Enter the amount of coins you want to bet: ")
        print("Perfect let the game begin!")
        time.sleep(2)
        call = input("What number do you call out ")
        print("He shuffels the card and holds them out for you to pick one")
        input("What card do you pick? 1, 2, 3, 4 or 5\n")
        time.sleep(2)
        cardsResault = random.choice(1,2,3,4,5)
        print(f"He flips the card to reveal a {cardsResault}")
        if cards == cardsResault:
            bettot = bet * 10
            money += bettot
            print("Ahh there you go you are a natural at this!")
            time.sleep(2)
            again = input("Do you wanna play again? (y/n)")
            if again == "n":
                break
            if again == "y":
                continue
        if cards != cardsResault:
            print("aww what a same! better luck next time!")
            money -= bet
            if money < 0:
                print("Oh looks like you dont have enough coins...")
                time.sleep(2)
                print("A deal is a deal...")
                time.sleep(2)
                print("You feel a stinging feeling in your chest")
                hp -= 1
                if hp == 0:
                    print("GAME OVER")
                else:
                    time.sleep(2)
                    print("What the hell did you do?")
                    time.sleep(2)
                    print("Well when making a deal with the devil you need to pay one way or another...")
                    time.sleep(2)
                    print("A devil! thats why you standing here luring in people! no way ill keep playing!")
                    break
            again = input("Do you wanna keep playing? (y/n)")
            if again == "y":
                continue
            if again == "n":
                print("I think this is enough for now")
                time.sleep(2)
                print("Alright sir see you around!")
                time.sleep(2)
if cards =="n":
    print("Oh well have a wonderful day then!")

print("You keep going along the road until you are just outside of the elven forest")
time.sleep(2)
print("Its getting pretty late and you dont know whats hiding in the forest so best to rest up now and get ready for the final stretch tomorrow!")
time.sleep(4)
print("You set up camp and rest for the night")
time.sleep(2)
print("The next morning you head out for the final stretch!")
time.sleep(2)
print("The forest is a lot more dense than the once you are used to back home")
time.sleep(2)
print("And you are seeing animal you only heard of in fairytales")
time.sleep(2)
print("after a few hours of walking through the forest you decide to take a rest")
time.sleep(2)
print("You find tree stump to sit down on")
time.sleep(2)
print("You hear some rustling in the woods behind you")
time.sleep(2)
woods = input("What do you do?\n1 = Better check it out what it was\n2 = Might just be a animal no need to worry\n3 = Hmm maybe this is some sort of nest better get moving!")
time.sleep(2)
if woods == "1":
    print("You get back up and walk over towards where the noice was")
    time.sleep(2)
    print("As you get closer to where you heard the sound coming from you notice a shadow moving just to the side of you")
    time.sleep(2)
    print("Not wanting to alert what ever it is you act like you nothing and go back to the stump and sit down")
    time.sleep(2)
    print("Now more alert than before it doesn't take you long to notice something moving around just outside of view")
    time.sleep(2)
    print("And whatever its definetly not an animal thats for sure...")
    time.sleep(2)
    print("It seems to try and find a way to get close to you without getting noiced so it most likely doesn't have the best intentions either...")
    time.sleep(2)
    print("If its something wanting to hurt you it might be best to set up a trap of some kind but that might be hard without it seeing...")
    time.sleep(2)
    print("Or maybe just calling out and letting it know you know its there will be enough to scare it away...")
    time.sleep(2)
    woods1 = input("What do you do?\n1 = Set up a trap\n2 = call out")
    if woods1 == "1":
        print("After taking a look around your surounding you find a place were you will be able to set up something that just might work...")
        time.sleep(2)
        print("After a bit of walking around and trying not to make anything seem out of the ordinary you get the trap set up and place yourself as the bait")
        time.sleep(2)
        print("Still on high alert it doesnt take you long to notice that whatever is after you has started to make a move")
        time.sleep(2)
        print("It sounds like its slowly making its way around you to find a way to approch you without being seen")
        time.sleep(2)
        print("With your trap being set up there its just a waiting game now")
        time.sleep(2)
        print("It doesnt take long before you hear whatever is moving around slowly approching from behind you")
        time.sleep(2)
        print("A few seconds later and you hear your trap go off and something that say something")
        time.sleep(2)
        print("You turn around with your weapon ready for whatever is facing you")
        time.sleep(2)
        print("Standing there already out of your trap is a young elf standing with 2 daggers")
        time.sleep(2)
        print("He yells at you 'You better leave all your stuff and get out of here before you get hurt!'")
        time.sleep(2)
        print("Wait a second no need to get violent! if its food your after i dont mind sharing")
        time.sleep(2)
        print("I said leave your stuff and go!")
        time.sleep(2)
        elf = input("What do you do?\n1 = Leave your things and go\n2 = Get ready for a fight")
        if elf == "1":
            if ringOfWrath == 1:
                print("Okay okay ill go!")
                time.sleep(2)
                print("You leave your things and slowly walk away")
                time.sleep(2)
                print("Your weapon as well!")
                time.sleep(2)
                print("I cant its bound to me so i can't let go of it")
                time.sleep(2)
                print("I said drop it!")
                time.sleep(2)
                print("the elf jumps at you with his daggers going right for your throat")
                time.sleep(2)
                hp -= 2
                combatElf()
            else:    
                print("Easy now! ill go!")
                time.sleep(2)
                print("You leave your bags and belongings and slowly walk away")
                time.sleep(2)
                print("After a little while you had back to check if hes are still there")
                time.sleep(2)
                print("You find all your things almost untouched besides from most of your food being gone")
                time.sleep(2)
                print("Hmm he must have had some bad experiances leaving him to treat people like that...")
                time.sleep(2)
                print("You gather your things and set out for last stretch to the elven city")
                time.sleep(2)
        if elf == "2":
            print("Well if its a fight you are looking for you found the right person!")
            time.sleep(2)
            combatElf()
    if woods1 == "2":
        print("You call out to see if someone answers")
        time.sleep(2)
        print("Nothing... so whatever it was it didnt take off running when they heard you")
        time.sleep(2)
        print("You try again a few times")
        time.sleep(2)
        print("Still no answer but just as you get ready to call out again you feel something pointy against your back")
        time.sleep(2)
        print("You hear a voice right behind you")
        time.sleep(2)
        print("Don't move or your done for!")
        elf1 = input("What do you do? \n1 = Try and attack whatever is holding you there\n2 = Do what they say")
        if elf1 == "1":
            print("You swing your weapon around and try to cut down who ever is holding you but they dodge the strike")
            time.sleep(2)
            print("You see a young looking elf with a pair of daggers and before you can react he jumps at you")
            hp -= 2
            combatElf()
        if elf1 == "2":
            print("They start emptying your pockets and you feel like they are too distracted so you swing your weapon and strike back at them")
            time.sleep(2)
            combatElf()
        
if woods == "2":
    print("With all the animals you saw today you wouldn't be surprised if it was just another")
    time.sleep(2)
    print("A few minutes later you hear a snap somewhere and seconds you feel a stinging from your side")
    time.sleep(2)
    print("You look down to see an arrow stuck in your chest and just inside the forest a young looking elf getting another one ready")
    time.sleep(2)
    print("As he fires the next arrow you are ready for it and charge over to fight back!")
    combatElf()
if woods == "3":
    print("You get your things ready and set off for the last stretch")
    time.sleep(2)
    print("Being in a unknown forest filled with animals and other creatures you don't know might not be the best place to rest up...")
    time.sleep(2)
    
print("After another hour of walking you reach the entrence to the elven city of Lilyandra")
time.sleep(2)
print("Its the most grand looking place you have ever seen")
time.sleep(2)
print("A city build in the middle of a forest")
time.sleep(2)
print("Houses floating the the trees and elves, animals, and other creatures walking with one another")
time.sleep(2)
print("Well nothing to do but experiance the town!")
time.sleep(2)
print("You walk down a road filled with different stands ran by all sorts of beings")
time.sleep(2)
print("Some elvels some humans and some races you havent even heard of")
time.sleep(2)
if axeOfGortash == 1:
    print("Oh hello there stranger! may i ask you a question?")
    time.sleep(2)
    print("Sure no wrong in a question or two")
    time.sleep(2)
    print("That axe you got on with you would that happen to come from Teldorana would it?")
    time.sleep(2)
    print("Well it just might! if i may ask was it you who enchanted it?")
    time.sleep(2)
    print("Ahh yes it was! i was on a mission and happend by a new way to enchant weapons and wanted to test it out")
    time.sleep(2)
    print("Only catch being that most weapons wouldn't be able to handle an enchantment of that caliber")
    time.sleep(2)
    print("When i was passing through the town i took a look at all the blacksmiths and found one that had a weapon i thought might be able to handle the nechantment and right i was")
    time.sleep(2)
    print("About the time i got done with the enchantment my master sendt me a message telling me to rush back here so i didn't have time to explain the the blacksmith")
    time.sleep(2)
    print("But i do hope you have had some good use of the weapon!")
    time.sleep(2)
    print("I sure have!")
    time.sleep(2)
    print("Well im glad to clear up some things then! be sure to let him know if you pass by the town again!")
    time.sleep(2)
    print("I will!")
    time.sleep(1)
    print("And with that the elf waves goodbye and heads off")
    time.sleep(2)
print("walking around you can't help but hear about some sort of memorial thats being held today at the palace")
time.sleep(2)
print("You pass by some food stalls with food from your home town")
time.sleep(2)
print("After having a chat with the owner you find out that they knew your gandparents")
time.sleep(2)
print("They invited you home for a meal and after eating and a lot of talking you head back to town")
time.sleep(2)
print("After making your round you end up in fornt of what looks to be the palace you heard people talk about")
time.sleep(2)
print("Theres already a lot of people flocking to the palace so its must be soon the memorial is being held")
time.sleep(2)
palace = input("Do you go to the memorial?\n1 = Well what better way to experiance a new culture seeing how they do things\n2 = Its been a long day better get some rest")
if palace == "1":
    print("Following the stream of people you walk towards the palace")
    time.sleep(2)
    print("You end up in a line towards what looks like the palace garden")
    time.sleep(2)
    print("You see a bunch of guards padding people down before letting them in")
    time.sleep(2)
    print("When it becomes your turn you are meet with a tall rough looking elven guard")
    time.sleep(2)
    if ringOfWrath == 1:
        print("Hmm soulbinding huh... ill have to lock your axe with magic if you wanna enter!")
        time.sleep(2)
        print("Sure i dont wanna couse any trouble!")
        time.sleep(2)
        print("He mumbels a few words and you see a transparent looking fog cover up your weapon")
        time.sleep(2)
        print("Alright walk on in!")
        time.sleep(2)
        print("You keep following the people around until you reach a big open area with a tomb in the center and a picuter of a young looking elf")
        time.sleep(2)
        if elfPendent == 1:
            print("You reconize the picture on the tomb to the the same as the one in the pendent")
            time.sleep(2)
            print("This might not be the best time to let people know about what happened in the forest...")
            time.sleep(2)
            print("You watch along and go off after the whole thing is over and find a pub you passed by earlier")
            time.sleep(2)
            print("You head off to bed and think about the adventures you have been on so far and whats to come in the future!")
            time.sleep(2)
            print("Thanks for playing the game!")
        if elfPendent == 1:
            print("The guard pads you down and notice the pendent in your pocket and askes what it is")
            time.sleep(2)
            print("You find the pendent and shows it to the guard")
            time.sleep(2)
            print("His face turns from a stern look to almost shock for a second before going back to stern")
            time.sleep(2)
            print("Come with me for a second")
            time.sleep(2)
            print("You start to follow along him but seconds after a group of guards grab you and drags you off")
            time.sleep(2)
            print("Not knowing whats going on you follow along without any resistance")
            time.sleep(2)
            print("They take you to a underground celler")
            time.sleep(2)
            print("A little while later a tall elf waring what looks to funural atire comes into the room")
            time.sleep(2)
            print("Where did you find the pendent...")
            time.sleep(2)
            king = input("What do you say?\n1 = You explain what happened in the forest\n2 = At least tell me whats going on!")
            if king == "1":
                print("He looks intently while you explain what happened and how you came to have the pendent")
                time.sleep(2)
                print("After you explain everything he tells you that hes the king of the elves and that the pendent you have is his")
                time.sleep(2)
                print("The pendent was stolen from him and the whole kingdome have been looking for it")
                time.sleep(2)
                print("You are let free and are given a room in the palace to rest up in and a reward of 100000 coins for bringing it back to the king")
                time.sleep(2)
                print("Now laying in your room you cant help but think back to all thats happened and whats to come in your future adeventures")
                time.sleep(2)
                print("Thanks for playing the game!")
            if king == "2":
                print("The man waves his hand and you hear a heavy thounk before fainting")
                time.sleep(2)
                print("When you wake up you find yourself in a areana filled with elves looking down at you in antisipation")
                time.sleep(2)
                print("You hear a extreamly loud voice annoncing that the one who stole the kings pendent has been found and is now being triled")
                time.sleep(2)
                print("They will be facing a dragon for their disgresions towards the king and if alive by the end be exiled from the city")
                time.sleep(2)
                print("The whole areana erupts in a fix of cheering and screaming and a platform in the middle of the areana starts rasing from beneth the ground")
                time.sleep(2)
                print("As the platform goes higher and higher you start to see what trouble you have landed yourself in...")
                time.sleep(2)
                print("Now standing before you is a fully grown red dragon")
                time.sleep(2)
                print("A magical barrier envelops the areana shielding you the crowd from the dragon and leaving you and the dragon locked in together")
                time.sleep(2)
                combatDragon()
        else:
            print("You see the memorial and the different traditions of the elvels")
            time.sleep(2)
            print("After everthing is over you head back to a pub you passed by earlier on you trip around town")
            time.sleep(2)
            print("You get yourself a room and head to sleep")
            time.sleep(2)
            print("You can't help think back on everything thats happened so far and whats to come!")
            time.sleep(2)
            print("Thanks for playing the game!")
if palace == "2":
    print("You head out to a tavern you passed by earlier and get yourself a room")
    time.sleep(2)
    print("You think back on the journy you have been on already and wonder whats to come in the future!")
    time.sleep(2)
    print("Thanks for playing the game!")
    exit()
