define Uknown = Character("Unknown")
define none = Character("...")
define D = Character("*Message*")
define Y = Character("You")
define G = Character("Guide")
define P = Character("passcode")



label start:
    scene bg start
    with fade
    Y "*A message shows up to your desktop*"

    D "“Check the app”"

    Y "*A message on the app appears saying*"

    Uknown "So, you finally found me… That’s good, for starters,"

    Uknown "I’m obligated to explain to you how this whole system works."
    Uknown "I’m going to be sending you guides to help you progress and some questions about you,"
    Uknown "in which you can answer them with a simple Yes or No."
    Y "*He then sends another message saying*"
    Uknown "Let’s test it out."

label Choice:
    default learned = False
    Uknown "Question 1: Do you know your name?"

    menu:
        "Yes":
            jump choices1_a
        "No":
            jump choices1_b

label choices1_a:
    Uknown "Very good"
    $ learned = True
    jump choices1_common

label choices1_b:
    Uknown "Very good"
    jump choices1_common

label choices1_common:
    Uknown "Very good"
    Uknown "Very good"

label flags:
    if learned:
        Uknown "Very good"
    else:
        Uknown "Very good"

label after:
    Uknown "Now that you are somewhat familiar with it,"
    Uknown "go look for a special looking key to get started."
    none "The door that leads out of his bedroom is locked until he finds the key."
    Y "You pick up the key that was inside a drawer."
    none "*The door is now unlocked*"

label Chapter1:
    play music "audio/bmg_the-ambience-room-tone.mp3" fadein 2.0
    scene bg scared
    with fade
    play sound "audio/bmg_seeing-the-painting.mp3"
    none "He sees a mirror-like symbol and the end of it"
    G "Familiar, right?"
    none "After stepping out of the room, a message is sent"
    D "Yes, this is not your house nor mine well,"
    D "I wouldn’t even call it a house to be honest"
    D "Remember, you wanted to live this experience knowing the whole process"
    D "If you look around, you’ll see some paintings."
    D "A specific one of them might be worth looking at…"
    stop music fadeout 1.0
   

label Choice2:
    default learned2 = False
    Uknown "Question 2: Does it make you feel scared?"

    menu:
        "Yes":
            jump choices2_a
        "No":
            jump choices2_b

label choices2_a:
    Uknown "..."
    $ learned2 = True
    jump choices2_common

label choices2_b:
    Uknown "..."
    jump choices2_common

label choices2_common:
    Uknown "..."
    Uknown "..."

label flags2:
    if learned2:
        Uknown "..."
    else:
        Uknown "..."

label sfx:
    play sound "audio/sfx_banging.mp3"
    queue music "audio/next_roar.mp3" fadein 1.0
    none "*BANG BANG BANG*"
    stop music fadeout 1.0

label endofchampter1:
    scene bg kitchen
    with fade
    none "A creature filled with rot in pure agony. It has a gun on his hand."
    show dark shadow
    none "...."
    Uknown "KILL IT"
    hide dark shadow
    none "A shadowy-like figure appears behind him and after three shots, it disappears. "
    G "It would be wise to measure all your shots and know what you are killing"
    G "The basement is where you want to go but it requires a password and I’m afraid that I can’t help you any further than that for now"
    none "The 4 different numbers will be written inside of 4 different rooms"
    none "Each room represents the cycle of life"

    scene bg kids
    none "A kid’s room "

    scene bg teenage
    none "A teenage room"

    scene bg adult
    none "An adult’s room"

    scene bg elder
    none "An elderly’s room "

    scene bg kitchen
    Uknown "Now it's time'"

label Choice3:
    default learned3 = False
    none "*Pass: The cycle of life*"

    menu:
        "8539":
            jump choices3_a
        "3895":
            jump choices3_b

label choices3_a:
    Uknown "Door Unlocked"
    $ learned3 = True
    jump choices3_common

label choices3_b:
    Uknown "Wrong password but the door cracked open"
    jump choices3_common

label choices3_common:
    Uknown "..."
    Uknown "..."

label flags3:
    if learned3:
        Uknown "now enter the basement"
    else:
        Uknown "now enter the basement"

label champter2:
    scene bg prison
    none "..."


label Choice4:
    default learned4 = False
    D "Question 3: Can you hear their screams?"

    menu:
        "Yes":
            jump choices4_a
        "No":
            jump choices4_b

label choices4_a:
    Uknown "*scream*"
    $ learned4 = True
    jump choices4_common

label choices4_b:
    Uknown "*scream*"
    jump choices4_common

label choices4_common:
    Uknown "*scream*"
    Uknown "*scream*"

label flags4:
    if learned4:
        Uknown "*scream*"
    else:
        Uknown "*scream*"

    play sound "audio/sfx_scream.mp3"

label cont3:
    G "Each corner has an enemy to greet you"
    G "You have to find different explosive parts to blow out the main entrance for the next area"

    scene bg shell
    G "after you collected evething you need lets go to the entrance"

    scene bg entrance
    G "Oh look, it's a locked door just next to the blocked entrance"
    G "But the key is no where to be found"
    none "After progressing with the explosion"
    G "Do you hear that?"
    play sound "audio/sfx_roar.mp3"
    Y "..."
    scene bg boss
    G "This is like a demon"
    G "It's on it's knees"
    G "You have to shoot it now"
    
    play sound "audio/sfx_gun.mp3"
    scene bg black

    G "is it over?"
    D "...."
    
label Choice5:
    default learned5 = False
    D "Question 4: “Do you feel pity for him?"

    menu:
        "Yes":
            jump choices5_a
        "No":
            jump choices5_b

label choices5_a:
    D "You didn’t even feel sorry for them!"
    $ learned = True
    jump choices5_common

label choices5_b:
    D "..."
    jump choices5_common

label choices5_common:
    D "...."
    D "...."

label flags5:
    if learned5:
        D "..."
    else:
        D "..."

label epilogue:
    none "The player gets teleported to a dark room with the Guide."
    scene bg you
    G "I always wanted to meet face to face,"
    G "to see how you really look like."
    G "How has your experience been so far? Did you enjoy it? Did you have fun?"
    G "I certainly did."
    G "All these things I had you do in order to progress, pathetic…"
    G "You obeyed me so good, without even questioning me or should I say… you…?"
    G "How did you feel when you were killing them all? Did it feel right?"
    G "You didn’t even feel sorry for them! Are you going to kill me now?"
    G "Yeah, you do that. Why don’t you go on and kill yourself, what about that huh?"
    G "It would be such a hug favor for all of us! Don’t you pull that trigger now you stupid, little man."
    G "I’m gonna ruin your entire existence! Just who do you think you are?!"
    none "Your hand slowly raises to shoot at the Guide"
    play sound "audio/sfx_gun.mp3"
    none "*Gunshot*"
    scene bg black
    none "..."
    scene bg crashed
    none "..."
    none "..."
    scene bg black
    return