# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character(_("Commander"))
define m = Character(_("Mechanic"))
define n = Character(_("Navigator"))

image bg plain = "plain.jpg"

image bg waterfall = "Waterfall.jpg"

image bg jungle = "Forrest.jpg"

image bg cave = "Cave.jpg"



# The game starts here.

label start:
    $ found = 0
    $ mechanicstat = 0
    default mechanicfound = False
    $ navigatorstat = 0
    default navigatorfound = False
    $ commanderstat = 0
    default commanderfound = False
    default mechanicalive = True
    
    
    default navigatoralive = True
    
    default commanderalive = True

    default part1found = False
    default part2found = False

    default blasterowned = False

    default navigatorJoined = False

    $ lossCount = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    "Your team of space travelers has crash landed on a mysterious planet."

    "As the newly elected pilot, it is your sworn duty to find the parts needed to repair the ship"

    show themuscle

    # These display lines of dialogue.

    c "As much as it pains me to admit, you're our only hope."

   

    c "The team decided to split up to help, but this is a dangerous new locale, we don't know what kind of dangers await us."

    c "You keep an eye out for those parts, but most importantly, make sure nothing happens to our crew."

    c "Remember, first rule of leadership,"

    c "Everything is your fault."

    jump junction1
label junction1:

    menu:

        "Where shall I look?"

        
        "Waterfall":
          if part1found:
              "I already found the wrench"
              jump junction1
          else:
              jump waterfallintro
        

        

        "Jungle":
          if navigatorfound:
              "The navigator is over here"
              jump rightaway
          else:
              jump jungleintro
        
        #"Cave":
         # if commanderfound:
          #    c "Quit fooling around."
           #   jump rightaway
         # else:
          #    jump caveintro

        "Return to ship":
          if part1found and part2found:
            if navigatoralive and mechanicalive:
                jump ending1
            if navigatoralive and !mechanicalive:
                jump ending2
            if !navigatoralive and !mechanicalive:
                jump ending3
            if !navigatoralive and mechanicalive:
                jump ending4
              
          else:
            "We can't leave yet."
            jump junction1



label waterfallintro:

  scene bg waterfall
  
  show mechanic
  m "Oh, there you are!"
  m "Thank goodness you came along, I knew you would help me!"
  m "So, all my parts fell out the ship's window when we crashed, Nebula knows where they could have ended up"
  m "And worst of all, my sweet little wrench, Rusty, is missing!"


label waterfall:

  scene bg waterfall

  menu:

        "What's that over there?":

            jump Waterfall2

        "Follow Mily":

            jump Waterfall3intro

label Waterfall2:
    scene bg waterfall

    "There does not seem to be anything here."

    "I see something shiny, maybe that's a part!"

    "Wait a minute, what about Mily?"

    menu:

        "Go back":
            jump waterfall

        "Investigate the object":
            jump Waterfall4

label Waterfall3intro:
    scene bg waterfall
    show mechanic

    m "Phew! I thought you left me!"

    m "I should have known you'd come back. While the commander might not agree, I think you're perfect for this mission."

    m "Always looking out for us"

label Waterfall3:

    menu:

        "Let's search higher":
            if mechanicalive:
                jump WaterfallUpper
            else:
                jump WaterfallUpperBad

        "Let's look ahead":
            if mechanicalive:
                jump WaterfallLower
            else:
                "Probably best I don't go back there again..."
                jump Waterfall3
            #danger there

label WaterfallUpper:

    scene bg waterfall
    show mechanic

    "She's quite the chatterbox, but it's nice to have someone to chat with."

    m "Wait! Is that?"

    m "Rusty! My beloved!"

    "Rusty Found!"

    $ part1found = True

    m "This is wonderful! I thought I'd never see her again!"

    m "Let's hurry back!"

    m "We found the first part sir!"

    show themuscle

    c "hm, not bad, but we still have a lot of work to get done."

    jump junction1

label WaterfallLower:

    scene bg waterfall
    show mechanic

    m "Gee, it's getting a bit spooky here"

    m "Wait, I hear something!"

    "What's that?"

    "What to do?"

    menu:

        "I will check":
            "I'm going to investigate"

            "What the heck is that?"

            m "Blast it! Hurry!"

            m "That was too close! You were almost a buffet!"

            "We should back on out of here"

            jump Waterfall3

        "Let her look":

            m "Are you sure?"

            m "ok...."

            m "Wait!"

            m "HELP-"

            hide mechanic

            "Mily! No!"

            $ mechanicalive = False
            $ lossCount += 1

            "I...couldn't save her."

            "Guess I should just go the other way"
            jump Waterfall3

            



        "Go back.":
            jump Waterfall3


label WaterfallUpperBad:
    "If only I could have saved Mily soon enough."

    "Oh look...Rusty..."

    "Rusty Found..."

    $ part1found = True

    "Guess I'd best head back..."

    jump junction1







label jungleintro:

  scene bg jungle

  "This jungle is huge! Hope my teammates aren't too lost."

  #investigate a sound at some point

  jump jungle

label jungle:
    scene bg jungle
    menu:

       "Look to the left":

            jump jungleLeftIntro
        
        #"Check under that rock":
         #   "There's..."

          #  "Nothing to see."

           # jump jungle

       "What was that sound?":
            jump jungleSound
            
            
        


label jungleLeftIntro:
    "Looks like there isn't much to see here"

    "Though I can't help but wonder where our navigator is. I have to find him too"

    "And I can't get too lost!"

    "I'm still hearing strange sounds on that other side."

    menu:

        "Go back":
            jump jungle

        "Look deeper":
            jump jungleJunctionLeft

label jungleSound:

    "I wonder what that noise was coming from"

    show navigator

    n "Oh, I knew I was picking up something familiar"

    n "I have been trying to track down other lifeforms"

    #if you have blaster, you could have used it with mechanic

    n "In all my years of traveling, I can't leave home without my metal detector, my glasses, my map, my telescope, my binocular, my unocular, my trinocular..."

    n "Oh!"

    n "And a spare blaster!"

    n "You seem light on defense, here!"

    "Blaster obtained!"

    $ blasterowned = True

    n "Now remember, only use this in emergencies! We don't want to disturb this planet's ecosystem!"

    n "So, shall we continue our search together?"

    menu:

        "You and me!":
            n "That's the spirit, young chap!"
            $ navigatorJoined = True
            jump jungleJunction

        "I shall continue alone.":
            n "Oh, well carry on!"
            jump jungleJunction

label jungleJunction:

    "I gotta keep searching"

    "There's a fork in the road"

    menu:
        "There's that sound again to the left":
            jump jungleJunctionLeft

        "The right route seems more peaceful":
            if navigatoralive:
                jump jungleJunctionRight
            else:
                "I can't go back..."
                jump jungleJunction

label jungleJunctionLeft:
    if navigatorJoined:
        show Navigator
        n "There's what we were picking up"
        n "Whoo! Look at the size of that puppy!"
        n "Aw, and look! He's chewing on that ship part!"
        n "Wait! That's ours!"
        n "He's growling at us!"
        n "Quick! Stun him!"

        menu: 
            "Blast":
                n "That'll show him!"
                n "Now grab that part!"
                $ part2found = True
                n "Let's skedaddle on out of here!"
                jump junction1
    else:
        "I hear it!"
        "What the heck is that thing?"
        "It's got something in its mouth"
        "That's the part I need!"
        "Uh oh! It's charging!"
        menu: 
            "Blast":
                n "That was almost too close!"
                $ part2found = True
                n "I gotta get out of here!"
                jump junction1

label jungleJunctionRight:
    if navigatorJoined:
        show Navigator
        n "There doesn't seem to be a thing here!"

        n "Come to think of it, there might be somethinf on the other side, let's go back"

        jump jungleJunction        

    else:
        "Wait! I see something through the bushes!"
        "Is that...the navigator?"
        "And what's that-"
        "I gotta save him!"
        "That's right, my blaster"
        # return a random float between 0 and 1
        $ randfloat = renpy.random.random()
        if randfloat = 1:
            "Fire Away!"
            n "You Saved Me!"
            n "Let's get out of here"
            n "By the way"
            n "Look what I found!"
            "Part obained"
            $ part2found = True
            n "Let's skedaddle on out of here!"
            jump junction1
        if randfloat = 0:
            "Blast!"
            "I missed..."
            "I couldn't save the navigator"
            $ navigatoralive = False
            jump jungleJunction




label ending1:
    show mechanic
    m "We made it! All thanks to you!"
    m "Now let me help you fix the ship"
    hide mechanic
    show navigator   
    n "Spot on, young man!"
    hide navigator
    show themuscle
    c "I must say, I am impressed."
    c "Fine, I guess you've earned your star. Nice work!"
    return
label ending2:

    show navigator
    n "We found all the parts, wait, where's Mily?"
    hide navigator
    show themuscle
    c "It seems we've lost her"
    c "Repairing the ship will be hard, but it can be done"
    return
label ending3:

   show themuscle
   c "Looks like you and me are the only ones left."
   c "This is what I get for putting you in charge"
   c "You have let down this operation, you're lucky I don't leave you behind on this planet."
   return

label ending4:
    show mechanic
    m "Okie dokie! The ship's all fixed!"
    m "Wait, where's the navigator?"
    hide mechanic
    show themuscle
    c "It seems our little first in command here couldn't keep him out of harm's way."
    hide themuscle
    show mechanic
    m "Aw, I miss hearing his stories"
    m "he was quite eccentric"
    m "Nonetheless, let's get offa this planet and back to base!"





    # This ends the game.

    return
