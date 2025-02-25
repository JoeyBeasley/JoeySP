# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character(_("Commander"))
define m = Character(_("Mechanic"))
define n = Character(_("Navigator"))
define pov = Character("[povname]")
#define a = Character(_("monster.png"))

image bg plain = "plain.jpg"

image bg waterfall = "Waterfall.jpg"

image bg jungle = "Forrest.jpg"

image bg cave = "Cave.jpg"

image bg spacetravel = "spacetravel.jpg"

image meteorite = "meteorite.png"

image meteoriteTop = "meteoritetop.png"

image greenalien = "greenalien.png"

image standardalien = "alien.png"

image meteoritebottom = "meteoritebottom.png"

image bg deck = "Deckbg.jpg"

image grey = "grey.png"



# The game starts here.

label start:
    $ found = 0
    $ mechanicstat = 0
    default mechanicfound = False
    default questionone = False
    default questiontwo = False
    default questionthree = False
    default questionfour = False
    default questionfive = False
    $ navigatorstat = 0
    default navigatorfound = False
    $ commanderstat = 0
    default commanderfound = False
    default mechanicalive = True
    default volcanofood = False
    $ volcanobirds = 0
    default water = False
    default fruit = False
    $ FoodminigameCount = 0
    default navigatorhurt = False
    default youAsked = False
    default sheAsked = False
    default movie = False
    default firsttool = False
    default color = False
    default howlong = False
    $ questions = 0
    $ alreadyAsked = False

    $ cont = 0 #continue variable
    $ arr_keys = ["K_UP", "K_LEFT", "K_DOWN", "K_RIGHT"]
    $ shots = 0
    
    
    default navigatoralive = True
    
    default commanderalive = True

    default part1found = False
    default part2found = False

    default blasterowned = False

    default navigatorJoined = False

    $ lossCount = 0

    $ fruitcount = 0
    $ gun_size = (330 / 2, 384 / 2)
    $ shots = 0
    $ nShot = 0
    $ gun_pos = (0, 0)
    $ gun_opos = (renpy.get_physical_size()[0] / 2 - gun_size[0] / 2, renpy.get_physical_size()[1] - gun_size[1] +  60)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    

    $ povname = renpy.input("Please insert your name", length=32)

    "Welcome aboard [povname]."

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
    play music "GreemaMain.mp3"
    scene bg cave
    menu:

        pov "Where shall I look?"

        #Maybe for her scenario, pay attention to what she syas to distinquish her from imposter
        "Waterfall":
          if part1found:
              pov "I already found the wrench"
              jump junction1
          else:
              jump waterfallintro
        

        

        "Jungle":
          if navigatorfound:
              pov "The navigator is over here"
              jump rightaway
          else:
              jump jungleintro
        
        #"Cave":
         # if commanderfound:
          #    c "Quit fooling around."
           #   jump rightaway
         # else:
          #    jump caveintro

        "Meteor (TESTING ONLY)":
            jump meteor

        "Volcano (TESTING ONLY)":
            jump Volcanominigame

        "Return to ship":
          if part1found and part2found:
            if navigatorhurt:
                jump doctor
            if navigatoralive and mechanicalive:
                jump fixit
            if navigatoralive and not mechanicalive:
                jump ending2
            if not navigatoralive and not mechanicalive:
                jump ending3
            if not navigatoralive and mechanicalive:
                jump fixit
            
              
          else:
            pov "We can't leave yet."
            jump junction1

label fixit:

    show mechanic

    m "Alright! All I gotta do is make some quick adjustments"

    m "Ok boys, time to do your thing"

    hide mechanic

    show themuscle

    c "[povname], you're telling me she talks to her tools?"

    menu:

        "What? It's cute!":
            c "Hmph"
        "I know, weird.":
            c "This is between us"
    hide themuscle

    show mechanic

    m "A one, a two, a skiddly diddly doo!"

    hide mechanic

    "Click on the correct tool needed based on Mily's description"

    "Any mistakes, and she may have to start over."


    jump fixminigame

label fixminigame:

    #click right tool

    while questions < 5:
        $randomizer = renpy.random.randint(1,5) #Replace 3 with the total number of questions.
        if randomizer == 1 and not questionone:
            call question1
        if randomizer == 2 and not questiontwo:
            call question2
        if randomizer == 3 and not questionthree:
            call question3 #And so on for as many questions as you have.
        if randomizer == 4 and not questionfour:
            call question4
        if randomizer == 5 and not questionfive:
            call question5





    if navigatoralive and mechanicalive:
        jump ending1

    if not navigatoralive and mechanicalive:
        jump ending4

label question1:
    m "It appears a few screws are loose"

    menu:
        "{image=wrench.png}":
            m "Wait, that's not right, let me start over!"
            $ questions = 0
            jump fixminigame
        "{image=screwdriver.png}":
            m "That's right!"
            m "Alright...righty tighty...and..."
            m "Fixed!"
            $ questions += 1
            $ questionone = True
            jump fixminigame
        "{image=hammer.png}":
            m "That can't be right"
            $ questions = 0
            jump fixminigame
label question2:
    m "Looks like the battery needs a bit of a boost!"

    menu:
        "{image=cables.png}":
            m "Time to give this ship a little cpr!"
            m "Clear!"
            $ questions += 1
            $ questiontwo = True
            jump fixminigame
        "{image=wrench.png}":
            m "Nope, that won't work"
            m "Come on, gotta concentrate!"
            $ questions = 0
            jump fixminigame
            
        "{image=pliers.png}":
            m "I don't see how that's going to work, but the clamps do remind me of something important!"
            $ questions = 0
            jump fixminigame
label question3:
    m "Aw, some little bolts have gotten lose!"

    menu:
        "{image=screwdriver.png}":
            m "That's great for screwing in...well, screws, but not bolts."
            $ questions = 0
            jump fixminigame
        "{image=hammer.png}":
            m "Wrong tool!"
            m "Sorry Harold H. Hamilton III, but you're gonna have to wait your turn!"
            $ questions = 0
            jump fixminigame
            
        "{image=wrench.png}":
            m "Perfect! Here goes!"
            $ questions += 1
            $ questionthree = True
            jump fixminigame
label question4:
    m "Whoa, we got a few nasty dents I gotta buff in!"

    menu:
        "{image=cables.png}":
            m "Not yet you two!"
            m "Gee, Black Betty and Red Rocket are so impatient sometimes..."
            $ questions = 0
            jump fixminigame
        "{image=hammer.png}":
            m "Come on, Harold, we got some work to do!"
            "Bang! Bang! Bang!"
            m "Heh, always an eager one, isn't he?"
            show themuscle
            c "Mily! Stay focussed!"
            hide themuscle
            m "Sorry boss, I mean, 'sir'!"
            $ questions += 1
            $ questionfour = True
            jump fixminigame

            
        "{image=screwdriver.png}":
            m "Something's not right here..."
            $ questions = 0
            jump fixminigame
label question5:
    m "There's a few broken wires I gotta snip off!"

    menu:
        "{image=screwdriver.png}":
            m "This won't do"
            $ questions = 0
            jump fixminigame
        "{image=cables.png}":
            m "Wait a minute...these two are wires"
            m "Not fit for the job!"
            $ questions = 0
            jump fixminigame
            
        "{image=pliers.png}":
            m "Here goes!"
            "Snip! Snap!"
            $ questions += 1
            $ questionfive = True
            jump fixminigame
            



    


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

    pov "There does not seem to be anything here."

    pov "I see something shiny, maybe that's a part!"

    pov "Wait a minute, what about Mily?"

    menu:

        "Go back":
            jump waterfall

        "Investigate the object":
            pov "Wait, that's not the part we need."
            jump waterfall

label Waterfall3intro:
    scene bg waterfall
    show mechanic

    m "Phew! I thought you left me!"

    m "I should have known you'd come back. While the commander might not agree, I think you're perfect for this mission."

    m "Always looking out for us"

    m "It's been so lonely out out here...with no one to chat with."

    if !alreadyAsked:

        m "Hey, since we've gotten to know each other a bit, why don't we ask some questions to each other along the way?"

        m "You know, to get to know each other more!"

        m "You wanna ask answer something, or do you want to ask me something?"

        menu:
            "I can answer":

                m "Ok then!"

                $ color = renpy.input("What is your favorite color?", length=32)

                m "[color], eh? That's a very lovely one indeed!"

                




                #boolean for who asked

                #string that can be random color for imposter

            "Can I ask you something?":
                m "Fire away!"

                $ youAsked = True

                menu:
                    "Which tool is your favorite?":
                        m "Aw, do I have to pick? They're all my little babies."
                        m "But to be fair, Old Rusty was my very first tool"
                        m "In fact, his nickname is Trusty Rusty!"
                        $ firsttool = True
                        $ alreadyAsked = True
                    "How long have you been with the Space Travel Corps?":
                        m "For five years at this point, I was only in my teens"
                        m "I mainly volunteered helping fix the ships and engines before the commander allowed me to tag along"
                        m "and by that I mean I snuck aboard during one of his missions, he was so mad!"
                        $ howlong = True
                        $ alreadyAsked = True
                    "What is your favorite movie?":
                        m "Oh, definitely the one where that cute little robot falls in love with the other robot!"
                        $ movie = True
                        $ alreadyAsked = True




label Waterfall3:

    menu:

        "Let's search higher":
            if mechanicalive:
                jump WaterfallUpper
            else:
                jump WaterfallUpperBad

        "Let's look ahead":
            #if mechanicalive:
            jump WaterfallLower
            
            #danger there

label WaterfallUpper:



    scene bg waterfall
    show mechanic

    m "the view is lovely and all, but I can't seem to find my tools anywhere."

    m "Wait, down there! I see something shiny! We should go back and head that way!"

    m "It might lead us to finding the tool I need!"

    jump Waterfall3

label WaterfallLower:

    scene bg waterfall
    show mechanic

    m "Gee, it's getting a bit spooky here"

    m "Wait, I hear something!"

    pov "What's that?"

    pov "What to do?"

    menu:

        "I will check":
            "I'm going to investigate"

            "What the heck is that?"

            show monster

            m "Blast it! Hurry!"

            if blasterowned:

                #pow sound

                play sound "blaster.mp3"

                play sound "monsterscream.wav"

                hide monster

                m "That was too close! You were almost a buffet!"

                "We should back on out of here"

                jump WaterfallImposter

            else:
                m "You don't have one?"

                m "Leave it to me!"

                "*chucks hammer at the enemy*"

                m "Yeah! Headshot!"

                "Holy heck, she's brutal!"

                m "Now let's carry on!"

                #picks up screw driver "Good boy, Larry!"

                jump WaterfallImposter

        #REPLACE

        "Let her look":

            m "Are you sure?"

            m "ok...."

            m "Wait!"

            m "HELP-"

            hide mechanic

            "Mily! No!"

            "I...couldn't save her."

            show mechanic

            m "Welp, never doing that again"

            "Mily?! I thought you died"

            m "I would have, until I took my screwdriver and WENT FOR THE EYES!"

            "(I think she has issues...)"
            jump WaterfallImposter

            



        "Go back.":
            jump Waterfall3

label WaterfallImposter:

    show monster

    "Wait, why is there another one?"

    "It's spinning around and around!"

    "(Ooh, I'm getting dizzy)"

    hide monster

    m "[povname], are you ok?"

    show mechanic

    #have a second one

    "Is my head spinning or do we have two mechanics now?"

    "Yeah, [povname], are you ok?"

    m "Wait! Don't listen to her, I'm the real mechanic!"

    "No, I am!"

    "Mily's blaster!"
    
    "It's only got one shot left"

    m "Alright you two, prove to me you're the real mechanic"

    if sheAsked:
        "What is my favorite color?"

        menu:
            "[color]":
                play sound blast
                show mechanic
                m "I knew you could do it, [povname]!"
                m "And what a lovely coinky dink! There's the tool we need!"
                $ part1found = True
                jump junction1
            "(Insert random color generator)":
                play sound blast
                m "Ow!"
                "Oh no! The mechanic is severly wounded!"
                "There's the part! I gotta get us out of here!"

    if youAsked:
        if movie:
            "What is your favorite movie?"
            menu:
                "The one where the cute robots fall in love":
                    play sound blast
                    show mechanic
                    m "I knew you could do it, [povname]!"
                    m "And what a lovely coinky dink! There's the tool we need!"
                    $ part1found = True
                    jump junction1
                "The one with the boy and the giant robot":
                    play sound blast
                    m "Ow!"
                    "Oh no! The mechanic is severly wounded!"
                    "There's the part! I gotta get us out of here!"
                    $ part1found = True
                    jump junction1
        if firsttool:
            "Who was your first tool?"
            menu:
                "Trusty Rusty":
                    play sound blast
                    show mechanic
                    m "I knew you could do it, [povname]!"
                    m "And what a lovely coinky dink! There's the tool we need!"
                    $ part1found = True
                    jump junction1
                "Useful Uter":
                    m "Wait, what kinda name is Uter?"
                    play sound blast
                    m "Ow!"
                    "Oh no! The mechanic is severly wounded!"
                    "There's the part! I gotta get us out of here!"
                    $ part1found = True
                    jump junction1
        if howlong:
            "How many years have you been with the Space Corps?"
            menu:
                "Five years":
                    play sound blast
                    show mechanic
                    m "I knew you could do it, [povname]!"
                    m "And what a lovely coinky dink! There's the tool we need!"
                    $ part1found = True
                    jump junction1
                "Ten years":
                    m "Wait, what kinda name is Uter?"
                    play sound blast
                    m "Ow!"
                    "Oh no! The mechanic is severly wounded!"
                    "There's the part! I gotta get us out of here!"
                    $ part1found = True
                    jump junction1






            


label WaterfallUpperBad:
    "If only I could have saved Mily soon enough."

    "Oh look...Rusty..."

    "Rusty Found..."

    $ part1found = True

    "Guess I'd best head back..."

    jump junction1







label jungleintro:

  play music "jungle.mp3"

  scene bg jungle

  pov "This jungle is huge! Hope my teammates aren't too lost."

  #play soft noise

  play sound "Monstersound2.mp3"

  "What was that sound? Must be some kind of creature"

  "The navigator said he did enjoy seeing wildlife"

  "I find that sound, I might find him"

  #investigate a sound at some point

  jump jungle

label jungle:
    scene bg jungle
    menu:
        #follow monster sound
       "Look to the left":

            jump jungleLeftIntro
        
        #"Check under that rock":
         #   "There's..."

          #  "Nothing to see."

           # jump jungle

       "Was it this way?":
            jump jungleSound
            
            
        


label jungleLeftIntro:
    play sound "quietsound.mp3"

    "Doesn't look like anyone is here"

    "And that sound is getting quieter"

    menu:

        "Go back":
            jump jungle

        "Keep going":
            jump deadend
            

label deadend:

    "No sign of that noise or the navigator anywhere"

    menu:
        "Go back":
            jump jungle



label jungleSound:

    play sound "Monstersound2.mp3"

    "I wonder what that noise was coming from"

    "I must be getting closer"

    
    menu:

        "Higher":
            jump junglesound2

        "Lower":
            jump anotherdeadend

label anotherdeadend:

    "I can't seem to go any further"

    play sound "quietsound.mp3"

    "And that sound is getting further away"

    menu: 
        "Back it up":
            jump jungleSound

label junglesound2:
    
    "There he is!"

    show navigator

    n "Sh! Shhh! Keep your voice down and lay low!"

    n "I have been trying to track down that life form"

    n "It sounds like a Scoriterrordon. Very powerful creature, but I can't be seen by one"

    n "I am deeply allergic to their sting."

    #if you have blaster, you could have used it with mechanic

    n "In all my years of traveling, I can't leave home without my metal detector, my glasses, my map, my telescope, my binocular, my unocular, my trinocular..."

    n "Oh!"

    n "And a spare blaster!"

    n "You seem light on defense, here!"

    "Blaster obtained!"

    $ blasterowned = True

    n "Now remember, only use this in emergencies! We don't want to disturb this planet's ecosystem!"

    n "So, shall we continue our search together?"

  
    n "That's the spirit, young chap!"
    $ navigatorJoined = True
    jump jungleJunction

      

label jungleJunction:

    "I gotta keep searching"

    "There's a fork in the road"

    play sound "Monstersound4.mp3"

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

    show navigator
    n "There's what we were picking up"
    hide navigator
    show monster
    play sound "Monstersound4.mp3"
    n "Whoo [povname]! Look at the size of that beast!"
    n "Aw, and look! He's chewing on that ship part!"
    n "Wait! That's ours!"
    n "He's growling at us!"
    n "Quick! Stun him with the spacebar before he attacks!"
    #hide navigator

        #menu: 
         #   "Blast":

        #$ direction = ""
    call screen forkeys(1)
    if _return == "5":
        play sound "blaster.mp3"
        "POW!"

        hide monster
        play sound "monsterscream.mp3"
        n "That'll show him!"
        n "Now grab that part!"
        $ part2found = True
        n "Let's skedaddle on out of here!"
        hide navigator
        jump junction1

    else:
        "Oh no! The navigator's down!"

        $ navigatorHurt = True

        n "Here...I got the part...the creature dropped it."
            
        $ part2found = True

        show themuscle

        c "This doesn't look good! If we don't get him help soon enough, he could die!"

        c "Hurry up and get the job done, [povname]."

        #minigame where he gets infection fixed

        jump junction1

               




label jungleJunctionRight:
    #if navigatorJoined:
    show navigator
    n "There doesn't seem to be a thing here!"

    n "Come to think of it, there might be something on the other side, let's go back"

    jump jungleJunction        

  




label ending1:
    show mechanic
    m "We made it! All thanks to you!"
    #m "Now let me help you fix the ship"
    hide mechanic
    show navigator   
    n "Spot on, young man!"
    hide navigator
    show themuscle
    c "I must say, I am impressed."
    c "Fine, I guess you've earned your star. Nice work!"
    c "Before we climb aboard, now would be a good time to hit 'Save'."
    hide themuscle

    #implement arrow memory game
    jump arrowNavigatorgame

screen uparrowCommand:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
    
    text "↑"

screen leftarrowCommand:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
    
    text "←"

screen rightarrowCommand:
    frame:
        xpadding 40
        ypadding 20
        xalign 0.5
        yalign 0.5
    
    text "→"

screen forkeys(max_time):

    on "show" action SetVariable("downer", max_time)
    frame:
        xalign 0.5
        yalign 0.0
        hbox:
            timer 0.1 action If(0 < downer, true = SetVariable("downer", downer - 0.1), false = [Hide("forkeys"), Return(direction)] ) repeat True

            bar:
                value AnimatedValue(value=downer, range=max_time, delay= 0.5)
                xalign 0.0
                yalign 0.0
                xmaximum 200

    hbox:
        align (0.5, 0.5)
        vbox:
            textbutton "1 LEFT":            
            # imagebutton:
                #idle "leftarrow.png"
                action SetVariable("direction", direction+"1")
                keysym "K_LEFT"
        vbox:
            textbutton "2 RIGHT":
            # imagebutton:
                #idle "rightarrow.png"
                action SetVariable("direction", direction+"2")
                keysym "K_RIGHT"
        vbox:
            textbutton "3 UP":
            # imagebutton:    
                #idle "uparrow.png"
                action SetVariable("direction", direction+"3")
                keysym "K_UP"
        vbox:
            textbutton "4 DOWN":
            # imagebutton:
                #idle "downarrow.png"
                action SetVariable("direction", direction+"4")
                keysym "K_DOWN"
        vbox:
            textbutton "5 SPACE":
            # imagebutton:
                #idle "downarrow.png"
                action SetVariable("direction", direction+"5")
                keysym "K_SPACE"

default direction = ""
default downer = 0

label arrowNavigatorgame:

    scene bg spacetravel

    play music "jungle.mp3"
    #Boswer inseide story QTE music

    n "Great Vader's Ghost! It's a meteor storm!"

    n "We gotta get through! Quick, type the correct buttons I list! It's our only hope of getting out of here!"
    
    #display keys for a few seconds, if not entered in time, game over
    
    "Up, Left, Down, Right"
    $ direction = ""
    call screen forkeys(3)

    if _return == "3142":
        "You got it right!"
        jump meteor2
       
        
    else:
        jump meteorCrash

label meteor2:

    "Left, Right, Up, Left"
    #"Applebees"
    $ direction = ""
    call screen forkeys(3)
    if _return == "1231":
        "Alright, just a little more and we should be there..."
        jump meteor3

            
    else: 
        jump meteorCrash

label meteor3:    
    "Down, Left, Down, Up"
    $ direction = ""
    call screen forkeys(3)
    if _return == "4143":
        "Phew, we made it!"
        jump meteorDodgeEnding
    else: 
        jump meteorCrash
    
    
    
label meteorDodgeEnding:

    stop music fadeout 1.0

    scene bg deck

    play music "victory.mp3"

    show navigator

    n "See there? I knew we could do it!"

    n "Thanks to you, the ship is in one piece, as are we!"

    hide navigator

    show mechanic

    m "You were amazing out there!"

    m "You truly are the greatest, Rusty would agree!"

    hide mechanic

    show themuscle

    c "You managed to impress me out there, [povname]."

    c "Welcome to the team!"

    c "You're free to fly with us anytime!"

    jump endgame
label endgame:

    "Thanks for playing!"

    return

label meteorCrash:
        #stop the music
        stop music fadeout 1.0
        "Wrong button!"
        "MAYDAY! MAYDAY! MAYDAY!"
        #screen goes black followed by jump sound
        #GAME OVER YEAH!
        #show game over screen

        play sound "gameover.mp3"

        "Continue?"
        menu:
            "Yes":
                jump arrowNavigatorgame
            "No":
                return
        


    #$ game_timer = 20
    
    # Shows the game screen
    #show screen numbers_scr
    
    # The loop will exist untill game screen returns win or lose
   





label ending2:

    show navigator
    n "We found all the parts, wait, where's Mily?"
    hide navigator
    show themuscle
    c "It seems we've lost her"
    c "Repairing the ship will be hard, but it can be done"
    hide themuscle
    jump day2NoMech
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

    jump meteor

label meteor:

    scene bg spacetravel

    m "I can't pick up a thing! It's nearly pitch black out here!"

    "We gotta dodge all this debris"

    "If you see a flaming meteor, fly in the opposite direction with your arrow keys"

    "If there's a big grey meteor, blast it with your spacebar!"

    #make them zoom in

    show meteoriteTop at top
    $ direction = ""
    call screen forkeys(2)
    if _return == "4":
        hide meteoriteTop
        "Nice Move"

    else:
        hide meteoriteTop
        jump crash

    show meteorite at left
    $ direction = ""
    call screen forkeys(2)
    if _return == "2":
        hide meteorite
        "That was close!"

    else:
        hide meteorite
        jump crash

    show grey at center
    $ direction = ""
    call screen forkeys(2)
    if _return == "5":
        hide grey
        "You are the Master Blaster!"

    else:
        hide meteorite
        jump crash

    show meteoritebottom
    $ direction = ""
    call screen forkeys(1)
    if _return == "3":
        hide meteoritebottom 
        "Almost there"

    else:
        hide meteoritebottom 
        jump crash

    show meteorite at right
    $ direction = ""
    call screen forkeys(1)
    if _return == "1":
        hide meteorite
        "We made it!"
        jump meteorDodgeEndingNoNav

    else:
        hide meteorite
        jump crash

    



label crash:

    "Continue?"
    menu:
        "Yes":
            jump meteor
        "No":
            return
    





    # Implement meteor shoot game

      # Before start the game, let's set the timer
    
    #return

label meteorDodgeEndingNoNav:

    show mechanic

    m "In spite of the lack of navigator, we made it!"

    return


label day2NoMech:

    "With our mechanic permanently out of commission, fixing the ship proved to be harder than we thought"

    "So much so that what would be a five minute fix turned into an overnight effort"

    "Night turned into morning and soon enough, I had to find food for my crew"

    jump day2Menuintro

label day2Menuintro:

    "Let's see, the chief loves his meat nice and spicy and the navigator needs his dosage of vitamins"

    "According to my research, some of the food on this planet should be edible"

    jump day2Menu

label day2Menu:

    

    "Where shall I look?"

    menu:

        
        "Volcano":

            if volcanofood:
              "I already found the wrench"
              jump day2Menu
            else:
              jump waterfallintro

        "Cave":

            if water:
                "I found some water"
                jump day2Menu
            else:
                jump Cave

        "Shoreline":

            if fruit:
              "Fruit obtained"
              jump day2Menu
            else:
                jump shoreline         

        "Return to base":
            if FoodminigameCount = 3:
                jump foodEnding

            else:
                "I need to keep looking, even my stomach is growling"
                jump day2Menu

label Volcano:

    "There's the volcano, I can already feel the heat!"

    "If I get too close, I might as well burn up!"

    "Oh! Up there!"

    "I can see some creatures I can hunt for meat."

    "Got my blaster ready!"

    jump Volcanominigame

label Volcanominigame:

    #timer = pygame.time.Clock()

   
    
    call screen targets
   #jump Volcanominigame_end

    #if volcanoBird > 0:
        #volcanofood = true



screen targets:
    $ xx = renpy.random.randint(50, 750)
    $ yy = renpy.random.randint(50, 500)
    text str(nShot) xpos 25 ypos 15
    timer 10.0 action Jump("Volcanominigame_end")
    timer 1.0 action SetScreenVariable("xx", renpy.random.randint(30, 750)) repeat(True)
    timer 1.0 action SetScreenVariable("yy", renpy.random.randint(30, 500)) repeat(True)
    imagebutton idle"greenAlien.png" hover "alienaim.png" action [SetVariable("nShot", (nShot+1))] xanchor 0.5 xpos xx yanchor 0.5 ypos yy
    #make one of green alien with crossfire
    

label Volcanominigame_end:

    #timer = pygame.time.Clock()

   
    
    #call screen targets

    "Let's see..."

    "I shot %(nShot)d targets."

    if nShot > 7:
        "That should be enough for everyone."
    if nShot > 4 and nShot < 7:
        "Not bad, but we may need to split."

    if nShot < 4 and nShot > 0:
        "That's not a lot."

    if nShot == 0:
        "I didn't get any..."
        "If I keep letting my guard down, my team will starve!"


    #if volcanoBird > 0:
        #volcanofood = true

    $ FoodminigameCount += 1
    jump day2Menu

label Cave:

    "My team and I are pretty parched!"

    "Luckily this cave should have some fresh water"

    #make minigame where you catch falling water droplets

label Shoreline:

    "Some fresh fruit should be here, just what the navigator needs for his teeth!"

    #matching minigame

label doctor:

    "The navigator got stung by that beast out there."

    "He doesn't look very good..."

    show themuscle

    c "Here's the first aid kit!"

    c "Now hurry up and cure him!"

    #select the right tool, set background to med box

    #if you succedd, he lives

label FoodEnding:

    show navigator
    n "Well, good news, we got the ship running"

#if fui

    n "Hey, is that fresh hobnanart I smell?"

    hide navigator

    show themuscle

    c "And is that smoked Volcano Buzzard?"

    c "Alright men, let's eat before we take off, traveling on an empty stomach is unwise"

    hide themuscle

    show navigator

    n "Just like the grand expediditon of 2664, I had gone all day without eating,"
    
    n "before long, my stomach was roaring and churning and-"

    hide navigator

    show themuscle

    c "NAVIGATOR!"

    hide themuscle

    show navigator

    n "Well, long story short, I got to see the midair anti gravity physics of my own ejected stomach acid."    


    return
