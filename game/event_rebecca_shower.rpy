label rebecca_shower:
    if (global_events.rebecca_bedroom):
        if (quest_make_a_plan.phase == 3):
            jump rebecca_shower_morning
        else:
            jump rebecca_shower_morning_short
    else:
        jump rebecca_shower_noon

label rebecca_shower_noon:
    hide screen station_rooms
    scene door_1
    player "{i}I think Rebecca is in there taking a shower.{/i}"
    menu:
        "Go inside":
            scene shower_rebecca_1
            $renpy.pause()
            scene shower_rebecca_2
            $renpy.pause()
            scene shower_rebecca_3
            rebecca "I'm coming out, please hand me a towel."
            player "{i}She must've seen me walking in the room.{/i}"
            scene shower_rebecca_4
            rebecca "It was so refreshing! Did you enjoy it as much as I did?"
            player "Well... yes."
            rebecca "I'm glad you did!"
            scene shower_rebecca_5
            rebecca "Do you think all the perverts down there enjoyed it too?"
            player "What?"
            rebecca "I know what this room is."
            player "But why do you care about them?"
            rebecca "You are right. I don't care."
            scene shower_rebecca_6
            rebecca flirting "But if they liked it, they would love the show I'd give them if it was me sleeping with you here and not your mom."
            player "We have time..."
            rebecca happy "Oh yeah? Not with your mom around though. I'd love to see her face catching us fucking in her bed, but I don't think it will be productive."
            player "Meaning?"
            rebecca happy "Meaning that we still have to work together if we are to get out of this shitty situation."
            player "I guess you are right..."
            rebecca happy "Now please get out before she starts wondering where is her little boy."
            scene door_1
            $renpy.pause()
            jump advance_time
        "Leave her alone":
            player "{i}I'd better not bother her while in the shower.{/i}"
            jump advance_time

label rebecca_shower_morning:
    hide screen station_rooms
    scene shower_rebecca_morning_1
    scene shower_rebecca_morning animated with dissolve:
        "shower_rebecca_morning_1" with dissolve
        pause 0.8
        "shower_rebecca_morning_2" with dissolve
        pause 0.8
        "shower_rebecca_morning_3" with dissolve
        pause 0.8
        repeat

    $renpy.pause()

    scene shower_rebecca_morning_4 # rebecca towel

    rebecca happy "Oh, did I wake you up?"
    player "What's the time?"
    rebecca "It's 7 o'clock."
    player "Fuck..."
    rebecca "Did you get a good sleep?"
    player "Not at all. I was connected all night."
    rebecca flirting "Does sleeping next to me excite you that much?"
    player "Well..."

    scene shower_rebecca_morning_5 # undress towel

    rebecca flirting "How can I make it up to you?"
    player "I have some ideas..."

    scene shower_rebecca_morning_6 # seductive naked

    rebecca flirting "I think I know what you have in mind."

    scene shower_rebecca_morning_7 # tits closeup

    rebecca flirting "Does it involve sucking my tits?"
    player "It involves sucking, so you are 50\% correct."

    scene shower_rebecca_morning_8 # touching clit

    rebecca flirting "50\% is good enough for me!"
    player "But first you'll have to be punished for keeping me up all night!"
    rebecca flirting "I think I know where this is going..."
    player "Assume the position!"
    rebecca flirting "Yes, master!"

    scene shower_rebecca_morning_spanking animated with dissolve:
        "shower_rebecca_morning_8" with dissolve # rebecca on greg's knees
        pause 0.8
        "shower_rebecca_morning_9" with dissolve # spank
        pause 0.8
        repeat

    $renpy.pause()

    scene shower_rebecca_morning_10 #rebecca red ass

    rebecca flirting "Mmmmm... you slap much better than your mother!"
    player "Now... about that sucking..."

    scene bedroom_rebecca_10
    scene shower_rebecca_morning_bj animated with dissolve:
        "bedroom_rebecca_10" with dissolve # bj
        pause 0.8
        "bedroom_rebecca_11" with dissolve # bj
        pause 0.8
        repeat

    $renpy.pause()

    player "Get on the bed!"

    scene shower_rebecca_morning_15 # doggy

    rebecca flirting "Ohhh, it's so big!"

    scene shower_rebecca_morning_doggy animated with dissolve:
        "shower_rebecca_morning_15" with dissolve
        pause 0.6
        "shower_rebecca_morning_14" with dissolve
        pause 0.6
        repeat

    $renpy.pause()

    player "I'm gonna cum!"

    scene shower_rebecca_morning_16

    pause

    jump advance_time

label rebecca_shower_morning_short:
    hide screen station_rooms
    scene shower_rebecca_morning_1
    scene shower_rebecca_morning animated with dissolve:
        "shower_rebecca_morning_1" with dissolve
        pause 0.8
        "shower_rebecca_morning_2" with dissolve
        pause 0.8
        "shower_rebecca_morning_3" with dissolve
        pause 0.8
        repeat

    $renpy.pause()

    scene shower_rebecca_morning_4 # rebecca towel

    rebecca happy "Look who's up!"
    player "Well, it's 7 o'clock, so..."
    rebecca flirting "I wasn't talking about you."

    scene shower_rebecca_morning_5 # undress towel

    pause

    scene shower_rebecca_morning_6 # seductive naked

    menu:
        "Come here":
            jump rebecca_shower_morning_cont
        "Not now":
            jump advance_time

label rebecca_shower_morning_cont:
    scene bedroom_rebecca_10
    scene shower_rebecca_morning_bj animated with dissolve:
        "bedroom_rebecca_10" with dissolve # bj
        pause 0.8
        "bedroom_rebecca_11" with dissolve # bj
        pause 0.8
        repeat

    pause

    player "Get on the bed!"

    scene shower_rebecca_morning_15 # doggy

    rebecca flirting "Ohhh, it's so big!"

    scene shower_rebecca_morning_doggy animated with dissolve:
        "shower_rebecca_morning_15" with dissolve
        pause 0.6
        "shower_rebecca_morning_14" with dissolve
        pause 0.6
        repeat

    pause

    player "I'm gonna cum!"

    scene shower_rebecca_morning_16

    pause

    jump advance_time
