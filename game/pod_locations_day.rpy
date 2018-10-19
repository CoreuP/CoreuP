label pod_morning_shower:
    call hide_pod_screens from _call_hide_pod_screens_34
    if (global_events.pod_woman == "rebecca"):
        jump pod_morning_shower_rebecca
    else:
        jump pod_morning_shower_mom

label pod_morning_shower_rebecca:
    scene pod_rebecca_shower_3

    pause 2

    scene pod_rebecca_shower_4

    pause 2

    scene pod_rebecca_shower_5

    pause 2

    scene pod_rebecca_shower_6

    rebecca flirting "Oh, you are up!"
    rebecca flirting "Something on your mind?"

    menu:
        "Have sex":
            jump pod_morning_shower_rebecca_sex
        "Have a shower yourself":
            jump pod_morning_shower_rebecca_greg

label pod_morning_shower_rebecca_sex:
    $pod_had_sex += 1
    player "Guess..."

    scene pod_rebecca_shower_9

    rebecca flirting "I know that look... so what's it gonna be?"

    menu:
        "Blowjob":
            jump pod_shower_rebecca_bj
        "Sex":
            jump pod_shower_rebecca_sex

label pod_morning_shower_rebecca_greg:
    player "I think I'll get a shower myself."
    rebecca "Oh... OK. I thought you might want to have some fun, but..."

    scene pod_rebecca_shower_7

    rebecca flirting "Mmmm... I like looking at you!"
    player "You do?"
    rebecca flirting "Of course I do!"

    scene pod_rebecca_shower_8

    rebecca flirting "Are you sure you don't want to have some fun?"
    player "Maybe later."
    rebecca "As you wish."

    $pod_player.add_stress(-30)

    jump pod_advance_time

label pod_morning_shower_mom:
    scene pod_mom_shower_3

    pause 2

    scene pod_mom_shower_4

    pause 2

    scene pod_mom_shower_5

    pause 2

    player "'Morning mom!"

    scene pod_mom_shower_5_a

    mom happy "Oh, hi Greg!"
    mom happy "I thought I'd take a shower before you got up, in case you wanted to take one too."

    menu:
        "Ask for sex":
            jump pod_morning_shower_mom_sex
        "Just take a shower":
            jump pod_morning_shower_mom_greg

label pod_morning_shower_mom_sex:
    $pod_had_sex += 1
    player "We could've taken one together..."
    mom flirting "Oh yeah? And how do you suppose that would end?"
    player "We'd probably have to take another one after that to clean ourselves up..."
    mom flirting "After what?"

    menu:
        "Ask for a blowjob":
            jump pod_morning_shower_mom_bj
        "Ask for sex":
            jump pod_morning_shower_mom_sex_2

label pod_morning_shower_mom_bj:
    player "After you suck my dick."
    mom flirting "Greg! Is this a proper way to talk to your mother?"
    player "I've been watching you during the night... you do far worse things than talking dirty."
    mom flirting "I'd better get on my knees then..."

    scene pod_mom_shower_9

    mom flirting "Mmmm, I like it when you are so hard!"

    scene pod_mom_shower_hj animated:
        "pod_mom_shower_9" with dissolve
        pause 0.8
        "pod_mom_shower_10" with dissolve
        pause 0.8
        repeat

    pause 2

    player "Are you going to just jerk me off, or are you going to suck it?"
    mom flirting "Greg! It's not like it doesn't turn me on when you talk like that, but still..."
    player "You have your son's dick in your hands and you are concerned about the way I talk?"
    mom flirting "..."

    scene pod_mom_shower_12

    player "That's it!"
    player "Take it all in your mouth!"

    scene pod_mom_shower_bj animated:
        "pod_mom_shower_12" with dissolve
        pause 0.8
        "pod_mom_shower_11" with dissolve
        pause 0.8
        repeat

    pause 2

    player "I said take it all!"

    scene pod_mom_shower_12_a

    mom flirting "I'm trying to, but it won't fit!"
    player "Who told you to stop?"
    mom flirting "Sorry!"

    scene pod_mom_shower_bj animated:
        "pod_mom_shower_12" with dissolve
        pause 0.8
        "pod_mom_shower_11" with dissolve
        pause 0.8
        repeat

    pause 2

    player "That's so good!"
    player "Don't stop!"

    menu:
        "Cum on her tits":
            jump pod_morning_shower_mom_cum
        "Don't cum":
            jump pod_morning_shower_mom_dont_cum

label pod_morning_shower_mom_sex_2:
    player "After I stick it in you."
    mom flirting "You liked it in my ass, didn't you?"
    player "Of course I did! It was so tight! Did you ever had anyone there before me?"
    mom flirting "Come on, Greg! Is that a question you should ask your mother? Besides, it hurts if I'm not horny enough. You should stick it in my pussy first."

    scene pod_mom_shower_22

    mom flirting "Oh, just like that!"
    mom flirting "It's so good feeling your hard dick drilling my pussy!"

    scene pod_mom_shower_23

    mom flirting "Oh, it's so deep! Please go slowly!"

    scene pod_mom_shower_pussy animated:
        "pod_mom_shower_23" with dissolve
        pause 0.9
        "pod_mom_shower_24" with dissolve
        pause 0.9
        repeat

    pause 2

    player "You are so wet!"
    mom flirting "And the shower had nothing to do with it! It's your dick that makes me so wet!"
    mom flirting "Do you enjoy looking at my ass?"
    player "Who wouldn't!"
    mom flirting "Fuck me faster!"

    scene pod_mom_shower_pussy animated:
        "pod_mom_shower_23" with dissolve
        pause 0.6
        "pod_mom_shower_24" with dissolve
        pause 0.6
        repeat

    pause 2

    mom flirting "Oh yeah! Just like that!"
    player "You enjoy being fucked from behind, don't you?"
    mom flirting "Yes! Taking me like I'm some kind of a whore is so turning me on!"
    mom flirting "Do you want to put your finger in my ass?"
    player "My finger? No, I have other plans for your ass!"

    scene pod_mom_shower_18

    mom flirting "Oh, it's so big! It's ripping my hole apart!"
    player "You didn't complain about it the last time!"
    mom flirting "Who's complaining?"

    scene pod_mom_shower_anal animated:
        "pod_mom_shower_18" with dissolve
        pause 0.6
        "pod_mom_shower_19" with dissolve
        pause 0.6
        repeat

    pause 2

    mom flirting "Oh yes! I can't believe how good this feels!"
    player "You are a slut, do you know that?"
    mom flirting "Yes, I am! I'm having my son's cock in my ass and I'm loving it!"
    mom flirting "I can't believe we didn't do it sooner! I was a fool to think it's wrong!"

    menu:
        "Cum":
            jump pod_morning_shower_mom_cum
        "Don't cum":
            jump pod_morning_shower_mom_dont_cum_anal

label pod_morning_shower_mom_dont_cum_anal:
    scene pod_mom_shower_20

    player "I shouldn't..."
    mom flirting "Come on, please! Don't you want to fill my ass with your hot cum?"
    player "I do, but I have a job to do. You know that with M.A.L. out of the game, I need to find a solution before what's in the hanger breaks loose..."
    mom flirting "I know, but I also know that my ass wants your dick! See!"

    scene pod_mom_shower_21

    mom flirting "I think you might have damaged me... I can't close my asshole..."
    player "Then maybe we need to find something to put inside?"
    mom flirting "That's actually not a bad idea..."

    $pod_player.add_arousal(50)

    jump pod_advance_time

label pod_morning_shower_mom_cum:
    player "I'm gonna cum!"

    scene pod_mom_shower_14

    mom flirting "Oh yes! Cum all over me!"

    scene pod_mom_shower_pre_cum animated:
        "pod_mom_shower_14" with dissolve
        pause 0.8
        "pod_mom_shower_13" with dissolve
        pause 0.8
        repeat

    pause 3

    scene white with dissolve

    pause 0.5

    scene pod_mom_shower_15 with dissolve

    pause 0.9

    scene white with dissolve

    scene pod_mom_shower_16 with dissolve

    pause 2

    scene pod_mom_shower_17

    mom flirting "Mmmm! I love the taste of your cum!"
    player "Is this a proper way to talk to your son?"
    mom flirting "I don't care! It's tasty!"

    $pod_player.add_arousal(-50)
    $pod_player.add_stress(-40)

    jump pod_advance_time

label pod_morning_shower_mom_dont_cum:
    scene pod_mom_shower_14

    player "I shouldn't..."
    mom flirting "Please! I want to taste it!"
    player "Haha! Is this a proper way to talk to your son?"
    mom flirting "Please Greg! I will get you aroused again! Just let me have your cum now!"
    player "No, mom! The sooner we get this done, the sooner we will be free."

    $pod_player.add_arousal(30)

    jump pod_advance_time

label pod_morning_shower_mom_greg:
    player "I think I'll get a shower myself."
    mom "Oh... OK. I thought you might want to have some fun, but..."

    scene pod_mom_shower_7

    mom flirting "Mmmm... I like looking at you!"
    player "You do?"
    mom flirting "Of course I do!"

    scene pod_mom_shower_8

    mom flirting "Are you sure you don't want to have some fun?"
    player "Maybe later."
    mom "As you wish."

    $pod_player.add_stress(-30)

    jump pod_advance_time

label pod_day:
    call hide_pod_screens from _call_hide_pod_screens_35
    $location = "pod"
    if (global_events.pod_woman == "rebecca"):
        scene pod_rebecca_1
    else:
        scene pod_mom_4
    jump pod_wait

label bedroom_day:
    call hide_pod_screens from _call_hide_pod_screens_36
    $location = "bedroom"
    $bedroom2_talk.advance_phase()

    scene bedroom2_tiara_1

    tiara happy "Hi Greg!"
    player "Hi!"
    tiara happy "Something on your mind?"
    if (bedroom2_talk.phase == 1):
        jump bedroom_day_1
    elif (bedroom2_talk.phase == 2):
        jump bedroom_day_2
    elif (bedroom2_talk.phase == 3):
        jump bedroom_day_3
    else:
        jump bedroom_day_4

label bedroom_day_1:
    player "I wanted to ask you about Rebecca... you served with her in the military, right? Was she as... wild back then as she is now?"
    tiara happy "Oh, you have no idea!"
    tiara happy "She was known as 'lieutenant deep throat' amongst the guys in our unit."
    tiara happy "I think this was one of the reasons Jack left her. That and your mother's sweet tits."
    player "Hey!"

    scene bedroom2_tiara_1_a

    tiara flirting "Oh come on! Stop acting like she's some kind of a saint. We both know that she's just a slut waiting for an excuse to fuck her son. Actually you both should thank Megan for giving her that excuse."
    player "Thank her? She is responsible for the mess we are in!"
    tiara "Not necessarily. If Rebecca had chosen to complete her mission instead of saving Lana, she could've neutralized M.A.L. and Megan."
    player "By killing all of us?"
    tiara "I've seen the plans for her operation. The risk that it would come to that was minimal. Anyway, it's pointless to guess what could've happened. Let's live in the present and not worry about the past."
    player "It's almost time for dinner..."
    tiara "OK, see you there."

    jump pod_advance_time

label bedroom_day_2:
    player "I wanted to know what do you think about Megan?"
    tiara happy "Megan? I think she is the only one, that can give me what I desire most."
    player "And what is that?"
    tiara "A new life. One that doesn't involve the military."
    player "What? I thought you liked working for them?"
    tiara "Shooting at people just because they want a fair pay for their work is not my idea of a good time. We are no longer a military force, because there is no one to fight with. We are mercenaries for hire."

    scene bedroom2_tiara_1_a

    tiara flirting "The only thing I like about that job is what we get to do between the missions. But if I get what Megan has promised me this will be nothing compared to what I would be able to afford."
    player "And what exactly is that?"
    tiara happy "A queen's life. One of the parts in the equation you are solving is for me to be a queen on a small island in the Pacific."
    tiara flirting "With half naked men ready to fulfil my desires..."
    player "Sound fun..."
    tiara flirting "Oh, it will be!"

    jump pod_advance_time

label bedroom_day_3:
    player "How's Lana?"
    tiara happy "Why don't you ask her yourself?"
    player "I... I'm not sure I want to..."
    tiara "Hey, it's not really her fault. She's doesn't have the strongest will around here. All her life she was ordered around either by Jack or by Susan."
    player "That's the thing - I can't believe she managed to manipulate us into actually helping Megan..."
    tiara happy "Why? Rebecca thought of her as her daughter, for your mom she was just a little girl and for you..."

    scene bedroom2_tiara_1_a

    tiara flirting "Well... you were so focused to getting in her pants, that you chose to ignore all signs if it would mean that you can stick your dick in her."
    tiara happy "If anyone is to blame for your situation, it's you."
    player "Hey, I'm not the one that put that fucking chip in my head! And I didn't shoot myself to end up locked here!"
    tiara happy "Indeed! You just wanted to fuck Megan and then you wanted to 'save' Lana without first asking yourself how was she 'captured'. Come on, you know I'm right!"
    player "None of this matters now... Let's just get the job done..."

    jump pod_advance_time

label bedroom_day_4:
    player "No, just checking what you are doing."
    tiara "Nothing much. Waiting for you to finish your job and get us all out of here."

    jump pod_advance_time

label bunk_day:
    call hide_pod_screens from _call_hide_pod_screens_37
    $location = "bunk"

    scene bedroom_1

    player "{i}Hmmm... no one is here...{i}"

    jump pod_wait

label dining_day:
    call hide_pod_screens from _call_hide_pod_screens_38
    $location = "dining"

    scene dining_1

    player "{i}No one is here yet. Makes sense since it's not dinnertime yet.{/i}"

    jump pod_wait

label outpost_day:
    call hide_pod_screens from _call_hide_pod_screens_39
    $location = "outpost"
    $outpost_talk.advance_phase()

    scene outpost_lana_talk_1

    sis "Hi Greg!"

    if (outpost_talk.phase == 1):
        jump outpost_day_1
    elif (outpost_talk.phase == 2):
        jump outpost_day_2
    elif (outpost_talk.phase == 3):
        jump outpost_day_3
    else:
        jump outpost_day_4

label outpost_day_1:
    sis "How's solving the equation going?"
    player "Fine, I guess..."
    player "By the way, where do you want Jack's machine to take you?"

    scene outpost_lana_talk_2

    sis "Susan said that..."
    player "Susan? I'm not asking about Susan, I'm asking about you. What do {i}you{/i} want?"
    sis "...I want to be with Susan. I've lied, manipulated and even hurt you just to achieve that and the truth is this is the only thing I want."
    player "But you were together... kind of..."
    sis "I know! But Megan is so obsessed with getting her flesh and bone daughter back, that she wouldn't accept anything less than that."
    player "That's stupid..."

    scene outpost_lana_talk_3

    sis "I know! I mean I love her the way she is, why can't Megan?"
    player "I don't know..."
    sis sad "..."
    player "..."
    player "Bye, Lana."
    sis sad "Bye, Greg."

    jump pod_advance_time

label outpost_day_2:
    player "How is Susan?"
    sis sad "The same as yesterday, which was the same as the day before..."
    player "Look, Rebecca didn't mean to..."

    scene outpost_lana_talk_2

    sis "She did, but that's not the point. This shouldn't have happened! We should be able to reboot the hardware, but for some reason we can't."
    player "By the way, I was wondering, how will the time travel work out for her? I mean she is... her biological body is dead, right?"
    sis "Megan seems to think it would be fine. Actually from what I know, that's the bulk of the equation - finding a place where she can transfer her mind to a healthy Susan's body."

    scene outpost_lana_talk_3

    sis "Tiara, mom, you even me - we are just details to that. Once the machine is ready, we can pretty much go wherever we like and be whoever we like."
    player "Sounds like fun."
    sis happy "Yeah, what did you wish for? A harem?"
    player "Actually I haven't thought about it... I guess I just want me and mom to be safe."
    sis "Me too. Bye Greg."
    player "Bye Lana."

    jump pod_advance_time

label outpost_day_3:
    player "How's Jack's work on the time machine progressing?"
    sis "He spends all his day locked up in there."
    sis "I don't even see him anymore... not that I want to."
    player "What I don't get is why do you let him treat you like that!"

    scene outpost_lana_talk_2

    sis sad "It's complicated..."
    player "No, Lana, it's really not! If I were you, I would've killed the bastard."
    sis "And then we would all be stuck here."
    sis "He's the only one able to finish it and get us out of here. I've talked with Tiara and she thinks she knows what's in the hangar. She says that if she's correct about that, we are in a lot of trouble."
    player "And what do you think?"

    scene outpost_lana_talk_3

    sis "Do you have some way of manipulating the equation, so that we don't see him wherever we go?"
    player "No. When I'm connected to M.A.L. it uses my brain's capacity, but I have no influence on the process."
    player "By the way, I thought he also has one of those chips in his head. How come we don't make any progress if I'm not connected?"
    sis "He's... his work on the machine itself is just as important as the equation. We can't go anywhere before it's finished."
    player "Yeah, I guess you are right. Bye."
    sis "Bye, Greg."

    jump pod_advance_time

label outpost_day_4:
    sis "Do you want to talk about something?"
    player "No, just checking on you."
    sis happy "Thank you!"
    player "Bye, Lana."
    sis "Bye, Greg."

    jump pod_wait

label lab_day:
    call hide_pod_screens from _call_hide_pod_screens_40
    $location = "lab"

    if (quest_final.phase >= 3):
        scene lab_no_susan_1

        player "{i}Nothing to do here...{/i}"

    else:
        scene door_1

        player "{i}Megan said we are not allowed in the lab...{/i}"

    jump pod_wait

label armory_day:
    call hide_pod_screens from _call_hide_pod_screens_41
    $location = "armory"
    if (quest_final.phase >= 3):
        scene armory_4

        player "{i}Poor bastard...{/i}"
    else:
        $armory_talk.advance_phase()

        scene door_armory_1

        if (armory_talk.phase == 1):
            player "{i}Hmmm...{/i}"
            player "{i}That's weird... what's in this room?{/i}"
            player "{i}It's not the lab, it's not the machine...{/i}"
        elif (quest_released.phase >= 4):
            player "{i}This must be the armory where they keep Rebecca suit.{/i}"
            player "{i}I need to get in there!{/i}"
        else:
            player "{i}Still locked...{/i}"

    jump pod_wait

label machine_day:
    call hide_pod_screens from _call_hide_pod_screens_42
    $location = "machine"

    if (quest_final.phase >= 3):
        scene machine_1

        player "{i}No one here too...{/i}"

    else:
        scene machine_jack_1

        jack angry "Get the fuck out of here!"
        player "I just wanted to..."
        jack angry "I don't care what you wanted. Get out!"

        scene door_1

        player "{i}What an asshole!{/i}"

    jump pod_wait
