#phase 1
label quest_released_advance_to_voyeur:
    $quest_released.advance_phase()
    $quest_released.time = "NIGHT"
    $location = "pod"
    return

#phase 2
label quest_released_advance_to_shower:
    $quest_released.advance_phase()
    $quest_released.time = "MORNING"
    return

#phase 3
label quest_released_advance_to_count_days:
    $quest_released.advance_phase()
    $quest_released.days_with_no_advance = 0
    $quest_released.time = "MORNING"
    return

#phase 4
label quest_released_advance_to_lana:
    $quest_released.advance_phase()
    $quest_released.days_with_no_advance = -1
    $quest_released.time = "EVENING"
    return

#phase 5
label quest_released_advance_to_morning_megan:
    $quest_released.advance_phase()
    $quest_released.time = "MORNING"
    return

#phase 6
label quest_released_advance_to_check_recordings:
    $quest_released.advance_phase()
    $quest_released.time = "NIGHT"
    $quest_released.arousal = 80
    return

#phase 7
label quest_released_advance_to_morning_camera:
    $quest_released.advance_phase()
    $quest_released.time = "MORNING"
    return

#phase 8
label quest_released_advance_to_talk_tiara:
    $quest_released.advance_phase()
    $quest_released.time = "MORNING"
    return

#phase 9
label quest_released_advance_to_drone_dinner:
    $quest_released.advance_phase()
    $quest_released.time = "EVENING"
    return

#phase 10
label quest_released_advance_to_mount_camera:
    $quest_released.advance_phase()
    $quest_released.time = "EVENING"
    return

#phase 11
label quest_released_advance_to_check_code:
    $quest_released.advance_phase()
    $quest_released.time = "NIGHT"
    return

#phase 12
label quest_released_advance_to_open_armory:
    $quest_released.advance_phase()
    $quest_released.time = "NIGHT"
    return

#phase 13
label quest_released_finish:
    $quest_released.advance_phase()
    call final_start from _call_final_start
    return

label pod_add_shower:
    $global_events.pod_shower = True
    if (global_events.pod_woman == "rebecca"):
        jump pod_add_shower_rebecca
    else:
        jump pod_add_shower_mom

label pod_add_shower_rebecca:
    scene pod_rebecca_bed_1 #rebecca angry on bed looking up

    rebecca angry "Megan! It's been long enough! I want to take a shower {b}now{/b}!"
    rebecca angry "..."
    rebecca angry "Answer me!"
    megan "Enough!"

    scene pod_rebecca_bed_2

    rebecca angry "You said that if we make enough progress, we can have some basic stuff!"
    megan "I'll look into it, but it might be hard to reconfigure the room..."
    rebecca angry "It's a fucking shower, not a space shuttle! How hard can it be?"
    megan angry "Well, guess what! Susan would've done this in a matter of seconds, but you decided to blow an EMP charge next to her!"
    megan angry "So you are stuck with me and I don't think I can make it!"

    scene pod_rebecca_bed_3 #rebecca looking at camera flirting

    rebecca flirting "Greg, you can help solve the equation only when you are horny, correct?"
    player "Yes."
    rebecca flirting "Then prepare for the ride of your life. And when I'm done with you, you won't be able to get it up for days. Let's see how they like that!"
    megan angry "Fine, I'll do it..."

    scene pod_shower_1 #no shower

    pause 1

    scene pod_shower_2 with dissolve #shower

    pause 1

    megan "Happy now?"

    scene pod_rebecca_shower_1 #rebecca going to the shower

    rebecca happy "I am."
    player "Is this VR... like our beach?"
    megan "Something like that. It's not the whole room though, just some parts of it."
    rebecca "As long as I can get cleaned up, I don't care what it is!"
    rebecca happy "Greg, do you mind me taking the shower first?"
    player "Of course not."

    scene pod_rebecca_shower_2 #rebecca showering

    rebecca happy "Oh, that's wonderful!"
    player "Do you want some company?"

    scene pod_rebecca_shower_3

    rebecca happy "Tempting... but not today. It's been so long since I had a shower, that I just want to clean myself!"
    rebecca flirting "But ask me again tomorrow!"

    scene pod_rebecca_shower_4

    pause 2

    scene pod_rebecca_shower_5

    pause 2

    scene pod_rebecca_shower_6 #rebecca naked out

    rebecca happy "Your turn!"

    scene pod_rebecca_shower_7 #camera in shower, rebecca looking

    pause 1

    rebecca flirting "..."
    player "Would you like to join me?"
    rebecca flirting "Is this all you ever think about?"

    scene pod_rebecca_shower_8

    rebecca flirting "No, I won't join you today. But make sure you watch me tonight..."
    player "{i}Hmmm, she never said that before... Something is off...{/i}"

    call quest_released_advance_to_voyeur from _call_quest_released_advance_to_voyeur
    jump pod_advance_time

label pod_add_shower_mom:
    scene pod_mom_bed_1 #mom angry on bed looking up

    mom angry "Megan! It's been long enough! I want to take a shower {b}now{/b}!"
    mom angry "..."
    mom angry "Answer me!"
    megan "Enough!"

    scene pod_mom_bed_2

    mom angry "You said that if we make enough progress, we can have some basic stuff!"
    megan "I'll look into it, but it might be hard to reconfigure the room..."
    mom angry "It's a fucking shower, not a space shuttle! How hard can it be?"
    megan angry "Well, guess what! Susan would've done this in a matter of seconds, but that bitch that came with you decided to blow an EMP charge next to her!"
    megan angry "So you are stuck with me and I don't think I can make it!"

    scene pod_mom_bed_3 #mom looking at camera flirting

    mom flirting "Greg, you can help solve the equation only when you are horny, correct?"
    player "Yes."
    mom flirting "Then prepare for the ride of your life. And when I'm done with you, you won't be able to get it up for days. Let's see how they like that!"
    megan angry "Fine, I'll do it..."

    scene pod_shower_1 #no shower

    pause 1

    scene pod_shower_2 with dissolve #shower

    pause 1

    megan "Happy now?"

    scene pod_mom_shower_1 #mom going to the shower

    mom happy "I am."
    player "Is this VR... like our beach?"
    megan "Something like that. It's not the whole room though, just some parts of it."
    mom "As long as I can get cleaned up, I don't care what it is!"
    mom happy "Greg, do you mind me taking the shower first?"
    player "Of course not."

    scene pod_mom_shower_2 #mom showering

    mom happy "Oh, that's wonderful!"
    player "Do you want some company?"

    scene pod_mom_shower_3

    mom happy "Tempting... but not today. It's been so long since I had a shower, that I just want to clean myself!"
    mom flirting "But ask me again tomorrow!"

    scene pod_mom_shower_4

    pause 2

    scene pod_mom_shower_5

    pause 2

    scene pod_mom_shower_6 #rebecca naked out

    rebecca happy "Your turn!"

    scene pod_mom_shower_7 #camera in shower, rebecca looking

    pause 1

    mom flirting "..."
    player "Would you like to join me?"
    mom flirting "Is this all you ever think about?"

    scene pod_mom_shower_8

    mom flirting "No, I won't join you today. But make sure you watch me tonight..."
    player "{i}Hmmm, she never said that before... Something is off...{/i}"

    call quest_released_advance_to_voyeur from _call_quest_released_advance_to_voyeur_1
    jump pod_advance_time

label quest_released_voyeur:
    if (global_events.pod_woman == "rebecca"):
        jump quest_released_voyeur_rebecca
    else:
        jump quest_released_voyeur_mom

label quest_released_voyeur_rebecca:
    player "{i}Rebecca said to check her out during the night. Let's see why...{/i}"

    scene pod_night_rebecca_1 #done

    rebecca "Greg... Are you sleeping?"
    rebecca "..."
    rebecca "I guess you are. I hope you are watching this. I have a plan how we can get out."

    scene pod_night_rebecca_2 #done

    rebecca "With Susan incapacitated, I doubt M.A.L. has the capacity to monitor us, so hear me out."
    rebecca "They rely solely on you to solve the equation, right? Which means that we are the ones setting the terms."
    rebecca "If you don't make any progress on that for a couple of days, I'm sure Megan will come begging for your cooperation."
    rebecca happy "And then we'll have the upper hand."
    rebecca happy "So have a good night and let's see if we can pull this off."

    call quest_released_advance_to_shower from _call_quest_released_advance_to_shower
    jump pod_advance_time

label quest_released_voyeur_mom:
    player "{i}Mom said to check her out during the night. Let's see why...{/i}"

    scene pod_night_mom_1 #done

    mom "Greg... Are you sleeping?"
    mom "..."
    mom "I guess you are. I hope you are watching this. I have a plan how we can get out."

    scene pod_night_mom_2 #done

    mom "With Susan incapacitated, I doubt M.A.L. has the capacity to monitor us, so hear me out."
    mom "They rely solely on you to solve the equation, right? Which means that we are the ones setting the terms."
    mom "If you don't make any progress on that for a couple of days, I'm sure Megan will come begging for your cooperation."
    mom happy "And then we'll have the upper hand."
    mom happy "So have a good night and let's see if we can pull this off."

    call quest_released_advance_to_shower from _call_quest_released_advance_to_shower_1
    jump pod_advance_time

label quest_released_shower:
    if (global_events.pod_woman == "rebecca"):
        jump quest_released_shower_rebecca
    else:
        jump quest_released_shower_mom

label quest_released_shower_rebecca:
    scene pod_rebecca_shower_2

    player "{i}Rebecca is in the shower already.{/i}"

    scene pod_rebecca_shower_3

    pause 2

    scene pod_rebecca_shower_4

    pause 2

    scene pod_rebecca_shower_5

    pause 2

    player "{i}She said that if we don't make any progress on the equation, Megan might let us out...{/i}"
    player "{i}I guess there is no harm in trying if that's true!{/i}"

    scene pod_rebecca_shower_5_a #closer

    player "Enjoying yourself?"
    rebecca happy "You're up..."
    rebecca flirting "And your dick is up too!"
    player "I guess I just like you too much!"
    rebecca flirting "Oh yeah? Let's see what we can do about that!"

    scene pod_rebecca_shower_9 #rebecca holding dick

    rebecca flirting "So... what did you do tonight?"
    player "Same as usual... spying on you."
    rebecca happy "Oh really? Did you like what you saw?"
    player "I guess we can try it."

    scene pod_rebecca_shower_hj animated:
        "pod_rebecca_shower_9" with dissolve
        pause 0.7
        "pod_rebecca_shower_10" with dissolve
        pause 0.7
        repeat

    pause 3

    rebecca flirting "So... how do you want to do this?"

    menu:
        "Blowjob":
            jump pod_shower_rebecca_bj
        "Sex":
            jump pod_shower_rebecca_sex

label pod_shower_rebecca_bj:
    player "I want a blowjob."
    rebecca flirting "I like having your dick in my mouth!"

    scene pod_rebecca_shower_12

    rebecca flirting "Mmmm!"
    player "Your mouth is amazing!"

    scene pod_rebecca_shower_13

    player "Oh yeah! So deep!"

    scene pod_rebecca_shower_bj animated:
        "pod_rebecca_shower_13" with dissolve
        pause 0.7
        "pod_rebecca_shower_12" with dissolve
        pause 0.7
        repeat

    pause 3

    player "You are amazing!"

    scene pod_rebecca_shower_14 #dick out

    rebecca flirting "Will you give me your cum!"
    player "Yes! Just don't stop!"

    scene pod_rebecca_shower_13

    scene pod_rebecca_shower_bj animated:
        "pod_rebecca_shower_13" with dissolve
        pause 0.5
        "pod_rebecca_shower_12" with dissolve
        pause 0.5
        repeat

    pause 3

    player "I feel it coming!"
    if (quest_released.phase == 2):
        $pod_player.add_arousal(-100)
        $pod_player.add_stress(-100)
        menu:
            "Cum on her face":
                jump pod_rebecca_shower_cum_face
            "Cum in her mouth":
                jump pod_rebecca_shower_cum_mouth
    else:
        menu:
            "Cum on her face":
                jump pod_rebecca_shower_cum_face
            "Cum in her mouth":
                jump pod_rebecca_shower_cum_mouth
            "Don't cum":
                jump pod_rebecca_shower_cum_none

label pod_rebecca_shower_cum_face:
    scene pod_rebecca_shower_14

    rebecca flirting "Oh yeah! I want your cum all over my face!"
    player "Beg for it!"
    rebecca flirting "Please! I need your cum! Please give it to me!"

    scene pod_rebecca_shower_15 with dissolve #cumshot

    pause 1

    scene pod_rebecca_shower_16 with dissolve #cum on rebecca

    pause 2

    scene pod_rebecca_shower_17 #rebecca closeup face

    rebecca flirting "Thank you!"
    player "No, thank you!"
    rebecca flirting "Let's get cleaned up!"


    $pod_player.add_arousal(-30)
    $pod_player.add_stress(-50)

    jump quest_released_shower_end

label pod_rebecca_shower_cum_mouth:
    player "Don't stop! I want to fill your mouth!"

    scene white with dissolve

    pause 0.5

    scene pod_rebecca_shower_13

    pause 0.5

    scene white with dissolve

    pause 0.5

    scene pod_rebecca_shower_13

    pause 0.5

    scene white with dissolve

    pause 1.2

    scene pod_rebecca_shower_13

    pause 2

    scene pod_rebecca_shower_14

    rebecca flirting "Mmmm, that was tasty!"
    player "You swallowed everything!"
    rebecca flirting "Of course I did! I wouldn't waste a drop!"

    $pod_player.add_arousal(-30)
    $pod_player.add_stress(-50)

    jump quest_released_shower_end

label pod_rebecca_shower_cum_none:
    scene pod_rebecca_shower_14

    player "I shouldn't..."
    rebecca flirting "Are you sure you don't want to cover my face with you cum?"
    player "Of course I want to, but if I do that I won't be able to work tonight..."

    $pod_player.add_arousal(20)

    jump quest_released_shower_end

label pod_shower_rebecca_sex:
    player "I want to fuck you!"
    rebecca flirting "Mmmm, the thought of your dick inside my pussy is making me wet..."

    scene pod_rebecca_shower_18

    rebecca flirting "Oh yeah! It's so big!"

    scene pod_rebecca_shower_19

    rebecca flirting "Mmmm... it's so deep..."

    scene pod_rebecca_shower_sex animated:
        "pod_rebecca_shower_19" with dissolve
        pause 0.7
        "pod_rebecca_shower_18" with dissolve
        pause 0.7
        repeat

    pause 3

    player "You are amazing!"
    rebecca flirting "Please just don't stop!"
    player "..."
    rebecca flirting "Don't cum yet! I'm close..."
    rebecca flirting "..."
    rebecca flirting "Yes! I'm cumming! Yes! Yes!"

    scene pod_rebecca_shower_19

    rebecca flirting "Oh yes!"
    player "I love the way your pussy is squeezing my dick when you cum..."
    rebecca flirting "Your turn now!"

    scene pod_rebecca_shower_sex animated:
        "pod_rebecca_shower_19" with dissolve
        pause 0.5
        "pod_rebecca_shower_18" with dissolve
        pause 0.5
        repeat

    pause 3

    player "{i}I feel getting closer...{/i}"
    if (quest_released.phase == 2):
        menu:
            "Don't warn her":
                jump pod_rebecca_shower_cum_pussy
            "Warn her":
                jump pod_rebecca_shower_cum_tits
    else:
        menu:
            "Don't warn her":
                jump pod_rebecca_shower_cum_pussy
            "Warn her":
                jump pod_rebecca_shower_cum_tits
            "Don't cum":
                jump pod_rebecca_shower_cum_none

label pod_rebecca_shower_cum_pussy:
    player "{i}It's too good to pull out!{/i}"

    pause 2

    scene pod_rebecca_shower_19

    scene white with dissolve

    scene pod_rebecca_shower_19 with dissolve

    scene white with dissolve

    scene pod_rebecca_shower_19 with dissolve

    scene white with dissolve

    pause 0.8

    scene pod_rebecca_shower_19 with dissolve

    pause 2

    rebecca flirting "Did you..."
    player "I'm sorry..."
    rebecca flirting "It's OK, I just wanted a taste, that's all! But I guess it's not too late for that."

    scene pod_rebecca_shower_20 #rebecca touching pussy with cum

    rebecca flirting "It's so much!"

    scene pod_rebecca_shower_21 #rebecca lick fingers

    rebecca flirting "Mmmm, tasty!"

    $pod_player.add_arousal(-30)
    $pod_player.add_stress(-50)

    jump quest_released_shower_end

label pod_rebecca_shower_cum_tits:
    player "I'm getting close..."
    rebecca flirting "Wait!"
    rebecca flirting "I want it on my tits!"

    scene pod_rebecca_shower_22 #rebecca hj tits

    rebecca flirting "Mmmm, the thought of your cum on me..."

    scene pod_rebecca_shower_23 #rebecca hj tits

    rebecca flirting "I want to feel your hot cum all over my tits!"

    scene pod_rebecca_shower_tits animated:
        "pod_rebecca_shower_23" with dissolve
        pause 0.7
        "pod_rebecca_shower_22" with dissolve
        pause 0.7
        repeat

    pause 2

    player "Beg for it!"
    rebecca flirting "Please, give it to me!"
    player "Are you ready?"
    rebecca flirting "Yes! Oh, yes!"

    scene pod_rebecca_shower_23

    scene white with dissolve

    scene pod_rebecca_shower_23 with dissolve

    pause 0.7

    scene pod_rebecca_shower_24 #tits with cum

    rebecca flirting "Mmmm, that's so sexy!"
    player "Don't you want a taste?"

    scene pod_rebecca_shower_25 #rebecca lick

    rebecca flirting "Of course I do!"

    $pod_player.add_arousal(-30)
    $pod_player.add_stress(-50)

    jump quest_released_shower_end

label quest_released_shower_mom:
    scene pod_mom_shower_2

    player "{i}Mom is in the shower already.{/i}"

    scene pod_mom_shower_3

    pause 2

    scene pod_mom_shower_4

    pause 2

    scene pod_mom_shower_5

    pause 2

    player "{i}She said that if we don't make any progress on the equation, Megan might let us out...{/i}"
    player "{i}I guess there is no harm in trying if that's true!{/i}"

    scene pod_mom_shower_5_a #closer

    player "Enjoying yourself?"
    mom happy "You're up..."
    mom flirting "And I see that your dick is up too!"
    player "I guess I just like you too much!"
    mom flirting "Oh yeah? Let's see what we can do about that!"

    scene pod_mom_shower_9 #mom holding dick

    mom flirting "So... what did you do tonight?"
    player "Same as usual... spying on you."
    mom happy "Oh really? And what do you think?"
    player "I'd love to try it!"

    scene pod_mom_shower_hj animated:
        "pod_mom_shower_9" with dissolve
        pause 0.7
        "pod_mom_shower_10" with dissolve
        pause 0.7
        repeat

    pause 3

    mom flirting "You are so hard!"
    player "You are the reason for that."
    mom flirting "Oh, yeah? You have seen nothing yet!"

    scene pod_mom_shower_12

    mom flirting "Mmmm! I like the taste of your cock..."
    mom flirting "Let's see how deep it will fit in my mouth!"

    scene pod_mom_shower_11

    mom flirting "Hmph..."

    pause 2

    scene pod_mom_shower_12

    mom flirting "It's huge! I'm sorry Greg... I really wanted the whole of it in my mouth..."
    player "Nothing to apologize for, mom... you are amazing!"
    mom flirting "Oh, that's so sweet!"

    scene pod_mom_shower_bj animated:
        "pod_mom_shower_12" with dissolve
        pause 0.8
        "pod_mom_shower_11" with dissolve
        pause 0.8
        repeat

    pause 2

    player "Your tongue sliding on my cock is so good!"

    scene pod_mom_shower_12

    mom flirting "Don't cum yet!"
    player "I won't..."
    mom flirting "There is something that I wanted to do with you, but I was always afraid to do it..."
    player "Oh yeah? What is that..."

    scene pod_mom_shower_20 #mom laying open ass

    mom flirting "Guess!"
    player "Wow! Really!"
    mom flirting "Just, please be gentle... And start slowly..."

    scene pod_mom_shower_18

    mom flirting "..."
    player "Are you OK?"
    mom flirting "Yes... just... wait for a moment..."
    player "..."
    mom flirting "Is the whole thing in?"
    player "... just the head..."
    mom flirting "What? It feels like it's so deep..."
    mom flirting "..."
    mom flirting "OK, push it deeper."

    scene pod_mom_shower_19

    mom flirting "..."
    player "Am I hurting you?"
    mom flirting "No... It's good... just start slowly..."

    scene pod_mom_shower_anal animated:
        "pod_mom_shower_19" with dissolve
        pause 1
        "pod_mom_shower_18" with dissolve
        pause 1
        repeat

    pause 4

    player "Like that?"
    mom flirting "Just like that..."
    player "Your ass is so tight!"
    mom flirting "I've wanted to do this ever since you stuck your thumb in it..."
    mom flirting "Go faster..."

    scene pod_mom_shower_anal_fast animated:
        "pod_mom_shower_19" with dissolve
        pause 0.6
        "pod_mom_shower_18" with dissolve
        pause 0.6
        repeat

    pause 2.5

    mom flirting "Oh yeah! Do you like it?"
    player "Are you kidding? I love it!"
    mom flirting "Do you want to fill my ass with your cum?"
    player "May I?"
    mom flirting "Not today. I want your cum all over my face and tits!"

    scene pod_mom_shower_14

    scene pod_mom_shower_cum animated:
        "pod_mom_shower_14" with dissolve
        pause 0.6
        "pod_mom_shower_13" with dissolve
        pause 0.6
        repeat

    player "Oh yes! I feel it coming! Do you want it?"
    mom flirting "Please! I need your cum all over me! Please!"

    scene white with dissolve

    pause 0.7

    scene pod_mom_shower_15 with dissolve

    pause 1.2

    scene white with dissolve

    pause 0.7

    scene pod_mom_shower_16

    pause 1.2

    mom flirting "Oh, it's so much!"
    mom flirting "Look what mess you did!"

    scene pod_mom_shower_17

    mom flirting "I love it!"
    player "I love you mom!"
    mom flirting "I love you too, Greg!"
    mom flirting "We should get dressed."

    jump quest_released_shower_end

label quest_released_shower_end:
    if (quest_released.phase == 2):
        $pod_player.add_arousal(-100)
        $pod_player.add_stress(-100)
        call quest_released_advance_to_count_days from _call_quest_released_advance_to_count_days
    jump pod_advance_time


#phase 3
label quest_released_megan:
    if (global_events.pod_woman == "rebecca"):
        jump quest_released_megan_rebecca
    else:
        jump quest_released_megan_mom

label quest_released_megan_rebecca:
    scene pod_megan_1 #megan angry

    megan angry "Greg! We haven't made any progress in solving the equation for [quest_released.days_with_no_advance] days!"
    megan "I know Rebecca isn't particularly attractive..."
    rebecca angry "Excuse me?!?"
    megan "You can have your mom living here if this will help you."
    rebecca angry "Oh, fuck off! We want to get out!"

    scene pod_megan_2 #megan rebecca arguing

    megan "No."
    player "No? How about we just sit on our asses and wait for whoever is in the hangar to break free."
    megan "You can't..."
    rebecca happy "{i}'Can't'{/i}? Enlighten us why is we can't do this?"
    megan "If they get out before we can escape to the parallel universe, it's game over for all of us."

    scene pod_megan_3 #megan looking camera

    player "Then, let's really work together. We just want our freedom. It's not like we can escape or anything!"
    player "Also you know full well, that I'm the only one that can help you achieve that."
    megan "M.A.L. can..."
    player "Cut the bullshit - I know that there is something wrong with M.A.L., so you use all his resources to keep Susan's mind alive."
    rebecca happy "So the way I see it, it's either you letting us free and Greg helping you get to where you want to be, or killing Susan hoping that M.A.L. can get the work done before loosing him too."

    scene pod_megan_1

    megan angry "Or we do nothing and wait for the commandos to storm the station and kill us all."
    player "Exactly!"
    megan angry "..."
    megan angry "Fine!"
    megan "But the laboratory with Susan in it is off limits!"
    rebecca happy "Don't you trust me?"

    scene pod_megan_2

    megan angry "You tried to kill her! Of course I don't trust you!"
    rebecca "Fair enough!"
    megan "Fine! Get dressed and come for breakfast."

    scene black with dissolve

    pause 1

    jump quest_released_breakfast_rebecca

label quest_released_breakfast_rebecca:
    scene outpost_dining_1

    player "Hi!"
    mom happy "Greg! I'm so glad to see you!"
    tiara "Hi Rebecca."
    rebecca "Hi."
    mom "Are you hungry?"
    player "No."
    rebecca "I am!"

    call quest_released_advance_to_lana from _call_quest_released_advance_to_lana

    jump outpost_breakfast

label quest_released_megan_mom:
    scene pod_megan_mom_1 #megan angry

    megan angry "Greg! We haven't made any progress in solving the equation for [quest_released.days_with_no_advance] days!"
    megan "If you are bored with your mom..."
    mom angry "Excuse me?!?"
    megan "You can have Rebecca living here if this will help you."
    mom angry "Oh, fuck off! We want to get out!"

    scene pod_megan_mom_2 #megan rebecca arguing

    megan "No."
    player "No? How about we just sit on our asses and wait for whoever is in the hangar to break free."
    megan "You can't..."
    mom happy "{i}'Can't'{/i}? Enlighten us why is we can't do this?"
    megan "If they get out before we can escape to the parallel universe, it's game over for all of us."

    scene pod_megan_mom_3 #megan looking camera

    player "Then, let's really work together. We just want our freedom. It's not like we can escape or anything!"
    player "Also you know full well, that I'm the only one that can help you achieve that."
    megan "M.A.L. can..."
    player "Cut the bullshit - I know that there is something wrong with M.A.L., so you use all his resources to keep Susan's mind alive."
    mom happy "So the way I see it, it's either you letting us free and Greg helping you get to where you want to be, or killing Susan hoping that M.A.L. can get the work done before loosing him too."

    scene pod_megan_mom_1

    megan angry "Or we do nothing and wait for the commandos to storm the station and kill us all."
    player "Exactly!"
    megan angry "..."
    megan angry "Fine!"
    megan "But the laboratory with Susan in it is off limits!"
    mom happy "Don't you trust us?"

    scene pod_megan_mom_2

    megan angry "The first thing you did when you got here is to detonate an EMP charge! Of course I don't trust you!"
    mom "That was Rebecca!"
    megan "Whatever! Get dressed and come for breakfast."

    scene black with dissolve

    pause 1

    jump quest_released_breakfast_mom

label quest_released_breakfast_mom:
    scene outpost_dining_1

    player "Hi!"
    mom happy "Rebecca! I'm so happy to see you!"
    tiara "Oh, the two love birds together again... Hi Greg."
    rebecca happy "You look hungry?"
    player "I'm not."
    rebecca "I am!"

    call quest_released_advance_to_lana from _call_quest_released_advance_to_lana_1

    jump outpost_breakfast

label outpost_breakfast:
    scene outpost_dining_2 #breakfast

    tiara "Let's eat!"

    scene outpost_dining_3 with dissolve #empty plates

    rebecca happy "Remember when all we had were those terrible protein cookies?"
    mom "..."
    sis sad "But we were happier back then..."
    rebecca angry "I'm not talking to you!"

    scene outpost_dining_4 #some standing

    megan "Let's get back to work!"

    jump pod_advance_time

label outpost_dinner:
    if (quest_released.meets_requirements(9)):
        jump quest_released_drone_dinner
    if (quest_released.meets_requirements(10)):
        jump quest_released_mount_camera

    scene outpost_dining_5 #dinner

    rebecca "Looks delicious!"
    sis "Thanks!"
    rebecca angry "..."
    sis sad "..."
    mom "This is awkward..."
    tiara "Yeah. Let's just eat."

    scene outpost_dining_6 with dissolve #empty plates

    megan "Let's get back to work."

    if (quest_released.meets_requirements(4)):
        scene outpost_dining_4

        sis sad "I want to tell you something..."
        player "What?"
        sis sad "Not here... in my room."
        player "OK, sure."
        jump quest_released_talk_lana

    jump pod_advance_time

label quest_released_talk_lana:
    scene outpost_lana_talk_1

    sis sad "Greg, I'm sorry..."
    player "Save your breath! Why didn't you just ask for help? I would've agreed to do it!"
    sis sad "Dad would punish me if I didn't do as I'm told."
    player "He's an asshole! I wish he had died when we thought he saved us by locking us in that section!"
    sis sad "... Me too..."

    scene outpost_lana_talk_2

    sis "Anyway, how are you feeling?"
    player "Why are you so suddenly concerned about my health?"
    sis "I... you are our only hope of getting out of here. There is something wrong with M.A.L. ..."
    player "I know. And thank you for not lying to me about this."
    sis "What do you mean?"
    player "Not pretending that you care about me."

    scene outpost_lana_talk_3

    sis "No point in doing that anymore, right?"
    player "Yes."
    sis "So? How are you feeling?"
    player "Fine, I guess."
    sis "Did you have time to look around?"
    player "I still don't have access to some parts of this section."
    sis "I know. Believe me, it's for your own good."

    scene outpost_lana_talk_2

    player "And why is that?"
    sis "... Megan is concerned about Susan's safety and I don't think she'd let you in the lab and the other room..."
    player "What about it?"
    sis "There is stuff that might hurt you..."
    player "{i}I bet that's the armory where they keep Rebecca's suit! I need to get in there!{/i}"
    player "Can you open it?"

    scene outpost_lana_talk_3

    sis "Even if I could, I wouldn't let you in there. Believe me, it's safer for you to stay away!"
    player "Why? Because of the chip in my head?"
    sis "... yeah... the chip... there are some devices that emit pretty powerful EMP waves, so you should not get in there!"
    player "{i}Definitely the armory!{/i}"
    player "Is this all you wanted to talk about?"
    sis "Yes... and to tell you that I'm really sorry. I know that doesn't mean much to you, but I just wanted to say it."
    player "Okay. Bye!"

    call quest_released_advance_to_morning_megan from _call_quest_released_advance_to_morning_megan

    jump pod_advance_time

label quest_released_morning_megan:
    if (global_events.pod_woman == "rebecca"):
        jump quest_released_morning_megan_rebecca
    else:
        jump quest_released_morning_megan_mom

label quest_released_morning_megan_rebecca:
    scene pod_megan_4

    megan "Morning!"
    player "Hey! You can't just barge in here!"
    rebecca flirting "Yeah, we could be in the middle of something!"
    megan happy "That's exactly what I wanted to talk about."

    scene pod_megan_5

    megan "We are not making much progress on the equation..."
    megan "My offer still stands. If you want to switch this one with your mom, all you need to do is ask."
    menu:
        "Choose Amelia":
            jump quest_released_morning_megan_choose_mom
        "Stay with Rebecca":
            jump quest_released_morning_megan_dont_switch

label quest_released_morning_megan_choose_mom:
    player "I think I'll prefer to stay with mom..."

    scene pod_megan_6

    megan "I thought you would!"
    megan happy "I'll go get her!"

    scene pod_megan_7 #just rebecca

    player "Look..."
    rebecca "You don't have to say anything... I get it."
    rebecca happy "Hell, if I had to choose between you and Amelia, I'd probably choose her too!"
    player "We cool?"
    rebecca happy "Of course we are, Greg! We can have fun even if I'm not sleeping here!"

    scene pod_megan_8 #megan and mom

    megan "Why are you not dressed yet?"
    rebecca "Fuck off!"
    megan angry "You should reconsider your attitude, girl! Tiara will teach you some manners!"
    rebecca happy "Can't wait for her to try!"
    rebecca flirting "Bye Greg!"

    scene pod_megan_9 #just mom

    mom "I can't believe she went out naked!"
    player "Well... you know her."
    mom happy "Indeed I do!"
    player "Look mom, sorry for choosing Rebecca before..."
    mom "Don't worry about that! I guess you two were planning our escape?"
    player "Yeah, about that..."

    scene pod_megan_10 #mom flirting

    mom flirting "Don't tell me that all you did here was to fuck like rabbits?"
    player "No! We..."
    mom flirting "..."
    player "..."
    mom flirting "Can't say that I blame you - I know how hard it is to resist her."
    player "Exactly!"

    scene pod_megan_9

    mom "Anyway, I don't trust Megan. I think she will screw us the first chance she gets. And I don't trust Lana too."

    jump quest_released_morning_megan_choose_mom_cameras

label quest_released_morning_megan_choose_mom_cameras:

    player "Wait a second..."

    scene pod_desk_1 #done

    player "..."
    player "There! The cameras are hacked, so we can discuss this."

    scene pod_megan_9

    player "I don't trust Lana neither."
    player "Speaking of which, I had a chat with her..."
    mom "And?"
    player "She accidentally mentioned something about one of the locked rooms. I think it's the armory and they have some pretty powerful stuff there."

    scene pod_megan_11

    mom "The question is how can we get inside."
    player "I'll try to access the recordings to see if I can find someone entering the lock code, but I might need your help for that..."
    mom flirting "I thought you might say that!"
    player "Mom, I'll need to be pretty excited when I go to sleep to be able to check the recordings..."
    mom flirting "I'll do my best!"

    $global_events.pod_woman = "mom"

    call quest_released_advance_to_check_recordings from _call_quest_released_advance_to_check_recordings

    jump pod_advance_time

label quest_released_morning_megan_mom:
    scene pod_megan_mom_4

    megan "Morning!"
    player "Hey! You can't just barge in here!"
    mom flirting "Yeah, we could be in the middle of something!"
    megan happy "That's exactly what I wanted to talk about."

    scene pod_megan_mom_5

    megan "We are not making much progress on the equation..."
    megan "My offer still stands. If you want to switch your mom with Rebecca, all you need to do is ask."
    menu:
        "Stay with mom":
            jump quest_released_morning_megan_dont_switch
        "Choose Rebecca":
            jump quest_released_morning_megan_choose_rebecca

label quest_released_morning_megan_choose_rebecca:
    player "Maybe I'll make better progress with Rebecca..."

    scene pod_megan_mom_6

    megan "I thought you would!"
    megan happy "I'll go get her!"

    scene pod_megan_mom_7 #just mom

    player "Look..."
    mom "You don't have to say anything... I get it."
    mom happy "I've been with her, so I know what she can do in the bed!"
    player "Sorry mom... It's just that we've been here for so long..."
    mom happy "Don't worry, Greg! I'm your mom and I love you. Regardless of who you find more attractive."

    scene pod_megan_mom_8 #megan and rebecca

    megan "Why are you not dressed yet?"
    mom "Hey! I'm talking to my son!"
    megan angry "Get dressed and come with me! I have work to do."
    rebecca happy "Work? Oh, you mean trying to figure out how to reboot your daughter?"
    megan angry "..."
    mom "Bye Greg! Love you!"

    scene pod_megan_mom_9 #just rebecca

    rebecca flirting "So you've finally come to your senses?"
    player "Excuse me?"
    rebecca happy "Don't get me wrong, I find your mom extremely sexy, but come on! Choosing her over me?"
    player "Look, she's my mom, I couldn't let her be Tiara's slave..."

    scene pod_megan_mom_10 #rebecca flirting

    rebecca flirting "It sound almost like it had nothing to do with her tight ass..."
    player "How..."
    rebecca flirting "Oh, come on! She told me. It was good, wasn't it?"
    player "Incredible."
    rebecca flirting "She's no virgin there, you know... well, she never had a man fuck her ass, but..."
    player "I get it! Enough!"

    scene pod_megan_mom_9

    rebecca "Anyway, I don't trust Megan. I think she will screw us the first chance she gets. And I'm sorry to say this, but I don't trust Lana too."

    jump quest_released_morning_megan_choose_rebecca_cameras

label quest_released_morning_megan_choose_rebecca_cameras:

    player "Wait a second..."

    scene pod_desk_1 #done

    player "..."
    player "There! The cameras are hacked, so we can discuss this."

    scene pod_megan_mom_9

    player "I don't trust Lana neither."
    player "Speaking of which, I had a chat with her..."
    rebecca "And?"
    player "She accidentally mentioned something about one of the locked rooms. I think it's the armory and they have some pretty powerful stuff there."

    scene pod_megan_mom_11

    rebecca "The question is how can we get inside."
    player "I'll try to access the recordings to see if I can find someone entering the lock code, but I might need your help for that..."
    rebecca flirting "I thought you might say that!"
    player "Rebecca, I'll need to be pretty excited when I go to sleep to be able to check the recordings..."
    rebecca flirting "I'll do my best!"

    $global_events.pod_woman = "rebecca"

    call quest_released_advance_to_check_recordings from _call_quest_released_advance_to_check_recordings_1

    jump pod_advance_time

label quest_released_morning_megan_dont_switch:
    player "No thank you, I'm fine..."
    megan "Really? I thought you'd like to spice it up a bit..."
    if (global_events.pod_woman == "rebecca"):
        rebecca happy "Fuck off, Megan!"
        megan angry "...I'm not done with you, bitch!"

        scene pod_megan_mom_9

        player "Do you think that mom will be safe?"
        rebecca "At least for now. They would not dare hurt her before they get what they want from you."

        jump quest_released_morning_megan_choose_rebecca_cameras

    else:
        mom happy "We have it spicy enough as it is, thank you!"
        megan happy "You overestimate yourself, dear! You think that giving up your ass is enough to compete with Rebecca? Think again!"
        megan happy "From what I hear from Tiara, that bitch is the sluttiest woman in the Solar system."
        player "Anything else you want to share with us? In case you don't... bye!"
        megan happy "I'm actually happy that you chose to stay with your mom. This way I can keep a closer eye on Rebecca. Bye!"

        scene pod_megan_9

        player "Do you think they will hurt her?"
        mom "No. But I think we shouldn't trust Megan... or Lana..."

        jump quest_released_morning_megan_choose_mom_cameras

label quest_released_check_recordings:
    scene blank

    player "{i}Let's see if I can access the recordings to check for the security code on the armory.{/i}"

    if (global_events.pod_woman == "rebecca"):
        scene pod_night_rebecca_1
    else:
        scene pod_night_mom_1

    player "{i}This is our room...{/i}"

    scene bedroom2

    player "{i}Tiara's room... hmmm, I wonder where they are...{/i}"
    player "{i}No time for this now, I should continue looking for the code.{/i}"

    scene lab_susan_1

    player "{i}I wonder why Megan has left the feed from this room...{/i}"

    scene outpost_lana_1

    player "{i}Lana's room...{/i}"

    scene blank with fade

    player "{i}This is useless! There are obviously no cameras overlooking the door. I have to find another way to get it.{/i}"

    call quest_released_advance_to_morning_camera from _call_quest_released_advance_to_morning_camera

    jump pod_advance_time

label quest_released_morning_camera:
    if (global_events.pod_woman == "rebecca"):
        jump quest_released_morning_camera_rebecca
    else:
        jump quest_released_morning_camera_mom

label quest_released_morning_camera_mom:
    scene pod_megan_mom_7

    mom "Any luck?"
    player "No. I can't see what we are looking for..."
    mom sad "Now what?"
    player "We'll have to be creative, that's all! I'll find another way."

    call quest_released_advance_to_talk_tiara from _call_quest_released_advance_to_talk_tiara

    jump pod_advance_time

label quest_released_morning_camera_rebecca:
    scene pod_megan_7

    rebecca "Any luck?"
    player "No. I can't see what we are looking for..."
    rebecca sad "Now what?"
    player "We'll have to be creative, that's all! I'll find another way."

    call quest_released_advance_to_talk_tiara from _call_quest_released_advance_to_talk_tiara_1

    jump pod_advance_time

label quest_released_talk_tiara:
    scene pod_tiara_talk_1

    tiara "Greg, I need your help!"
    player "Isn't anyone on this station familiar with the concept of knocking?"
    tiara "No time for this now! The camera went dark during the night!"
    player "What? Which camera?"

    scene pod_tiara_talk_2

    tiara "This one. It was supposed to monitor the hangar, remember?"
    player "Right. So what's wrong with it?"
    tiara "I was hoping that you would tell me. After the feed went dark, I got out and went to the hangar to retrieve it."
    player "You went out? What did you see?"
    tiara "Nothing. Empty corridors."

    scene pod_tiara_talk_3

    tiara "I was wearing the chameleon suit, so I doubt they saw me too..."
    player "Any idea who are 'they'?"
    tiara "No. But if you can access the drone's storage, there might be clues."
    player "I'll see what I can do."
    tiara "Fine. I have to brief Megan too, can I count on you to check the storage?"
    player "Of course. It concerns the safety of us all."

    if (global_events.pod_woman == "rebecca"):
        jump quest_released_talk_tiara_rebecca
    else:
        jump quest_released_talk_tiara_mom

label quest_released_talk_tiara_mom:
    scene pod_mom_talk_1

    mom "What was this all about?"
    player "Remember that I've told you about someone boarding the station and cutting off the access to the hangar? I helped Tiara and Megan send a surveillance drone there to monitor for chameleon suit signatures."
    mom "Can you do that?"
    player "Well... no. But they think I did. Instead I used the drone's connection to upload Rebecca's camera hack to the system."

    scene pod_mom_talk_2

    mom "So if there is indeed someone wearing a chameleon suit on the station, there is no way we can know about it?"
    player "If there was, the chances are we would be already dead."
    player "Anyway, let's see what happened to this drone..."

    scene pod_desk_2

    player "Hmmm... weird..."
    mom "What?"
    player "The drone is intact, but it's connection was jammed... Let's see what we can get from the storage..."

    scene door_hangar_1

    player "A bit forward..."
    player "..."
    player "Forward..."

    scene door_intruder_1 with dissolve

    player "There!"
    mom "I can't see much..."
    player "That's all we've got. Only one frame and then it went dark."

    scene pod_mom_talk_3

    mom "So, what would we tell Tiara and Megan?"
    player "First of all, we will tell them that this drone is a wreck. I have plans for it. As for the recording... there is no harm in sharing it with them."
    mom "I hope you know what you're doing..."
    player "Me too."

    call quest_released_advance_to_drone_dinner from _call_quest_released_advance_to_drone_dinner

    jump pod_advance_time

label quest_released_talk_tiara_rebecca:
    scene pod_rebecca_talk_1

    rebecca "What was this all about?"
    player "Remember that I've told you about someone boarding the station and cutting off the access to the hangar? I helped Tiara and Megan send a surveillance drone there to monitor for chameleon suit signatures."
    rebecca "Can you do that?"
    player "Well... no. But they think I did. Instead I used the drone's connection to upload your camera hack to the system."

    scene pod_rebecca_talk_2

    rebecca "So if there is indeed someone wearing a chameleon suit on the station, there is no way we can know about it?"
    player "If there was, the chances are we would be already dead."
    player "Anyway, let's see what happened to this drone..."

    scene pod_desk_2

    player "Hmmm... weird..."
    rebecca "What?"
    player "The drone is intact, but it's connection was jammed... Let's see what we can get from the storage..."

    scene door_hangar_1

    player "A bit forward..."
    player "..."
    player "Forward..."

    scene door_intruder_1 with dissolve

    player "There!"
    rebecca "I can't see shit..."
    player "That's all we've got. Only one frame and then it went dark."

    scene pod_rebecca_talk_3

    rebecca "So, what would we tell Tiara and Megan?"
    player "First of all, we will tell them that this drone is a wreck. I have plans for it. As for the recording... there is no harm in sharing it with them."
    rebecca "I hope you know what you're doing..."
    player "Me too."

    call quest_released_advance_to_drone_dinner from _call_quest_released_advance_to_drone_dinner_1

    jump pod_advance_time

label quest_released_drone_dinner:
    scene outpost_dining_7

    tiara "Well... did you learn something useful from the drone?"
    player "Just a couple of things - first of all, that they wrecked it so they are definitely hostile..."
    tiara "Told you!"
    megan "And the other?"
    player "We have an image. Well... not exactly a clear picture of the intruder - just one frame of the recording and it's distorted."

    scene outpost_dining_8

    megan "They don't use chameleon suits? Why?"
    rebecca "It was still an experimental technology, maybe they don't have enough..."
    tiara "Or they don't need one?"
    megan "Can you send me the picture? I want to take a look."
    player "Sure. Do you think you can spend some of M.A.L.'s resources to try and reduce the noise in it?"
    megan "I'll see what I can do."

    scene outpost_dining_7

    player "Also I wanted to talk with you about the machine that Jack is building. Is he close to finishing it? We might not have much time if they decide to storm this section."
    megan "You need to worry about getting the equation solved, I'll worry about having the machine ready on time."
    player "But..."
    megan angry "Enough! Fuck Rebecca, fuck your mom, hell you can even fuck Lana if this will get us any closer to having it solved. Fuck whoever you want! Just get your job done!"
    tiara happy "Even you? Or Susan?"
    megan angry "Fuck off!"

    scene outpost_dining_6

    player "{i}Good! She is so pissed off that she didn't even ask for the camera drone! All I have to do is mount it over the armory door and wait for someone to enter the code. I guess the best time to do that is when everyone is having dinner.{/i}"

    call quest_released_advance_to_mount_camera from _call_quest_released_advance_to_mount_camera

    jump pod_advance_time

label quest_released_mount_camera:
    scene door_armory_1

    player "{i}Let's see... I bet there are some power lines behind that panel, which can power the camera...{i}"
    player "{i}...{/i}"
    player "{i}There! It's done!{/i}"
    tiara "Hey! You know you shouldn't be here!"

    scene door_tiara_1

    player "I was just..."
    tiara "You were just what? Trying to hack the door?"
    player "No."
    tiara happy "I doubt that you could do it anyway! These locks are controlled by M.A.L. and I doubt you would be able to figure them out."
    player "Oh yeah? Why do you need me then?"

    scene door_tiara_2

    tiara flirting "Which reminds me... Megan said that you can fuck whoever you want if this helps you solving the equation, right?"
    player "That's how I remember it too..."
    tiara flirting "So how about we have some fun?"

    menu:
        "Go with her":
            jump quest_released_mount_camera_tiara
        "Refuse":
            jump quest_released_mount_camera_refuse

label quest_released_mount_camera_refuse:
    player "Thanks, but no thanks!"

    scene door_tiara_1

    tiara angry "What? Didn't you like it when we had sex?"
    player "I was a prisoner then. I had no choice!"
    tiara angry "You think you have one now? You deserve everything that has happened to you!"
    tiara "And if I'm correct about what's in the hangar, it will only get worse."

    scene door_armory_1

    player "{i}If she's so worried about Earth's commandoes in the hangar, the sooner I get in the armory, the better...{/i}"

    call quest_released_advance_to_check_code from _call_quest_released_advance_to_check_code

    jump pod_advance_time

label quest_released_mount_camera_tiara:
    player "What do you suggest?"
    tiara flirting "Come and see for yourself..."

    scene bedroom2_tiara_1

    player "So, what do you think is in the hangar?"
    tiara flirting "Stop talking and get your clothes off!"
    player "You'd better watch your tone, missy! Or you might get your ass spanked!"

    scene bedroom2_tiara_2

    tiara flirting "Oh, really? What makes you think I don't want that?"
    player "Didn't you like being the one that gives the spanking?"

    if (global_events.pod_woman == "rebecca"):
        tiara flirting "Well... not so much to be honest. And even though Rebecca is pretty good at spanking, I prefer men's touch, if you know what I mean..."
    else:
        tiara flirting "I've tried it, but I guess I'm submissive type after all... And I'm sorry to say this, but your mom hits like a girl!"

    player "Keep talking like that and you will get yourself in trouble!"

    scene bedroom2_tiara_1

    tiara flirting "You promise?"
    player "So... tell me what's in the hangar."
    tiara flirting "Make me!"
    player "That's it, missy! Drop your pants!"

    scene bedroom2_tiara_3

    player "Last chance..."
    tiara flirting "Do your worst!"

    scene bedroom2_tiara_spank animated:
        "bedroom2_tiara_3" with dissolve
        pause 0.8
        "bedroom2_tiara_4" with dissolve
        pause 0.8
        repeat

    pause 3

    player "So? Ready to talk?"
    tiara flirting "What? You call this spanking?"
    tiara flirting "I've had girls spank me harder than you!"

    scene bedroom2_tiara_spank animated:
        "bedroom2_tiara_3" with dissolve
        pause 0.6
        "bedroom2_tiara_4" with dissolve
        pause 0.6
        repeat

    pause 3

    tiara flirting "That's more like it!"
    tiara flirting "Ouch! It hurts... OK, stop it... I'll talk!"
    player "Stop it? No, no, no... you had your chance! Now you are going to get punished!"

    scene bedroom2_tiara_5

    tiara flirting "Oh! It's too big! Slowly, please!"
    player "Please? I think you are mistaken about who makes the rules here!"

    scene bedroom2_tiara_6

    scene bedroom2_tiara_doggy animated:
        "bedroom2_tiara_6" with dissolve
        pause 0.9
        "bedroom2_tiara_7" with dissolve
        pause 0.9
        repeat

    pause 3

    tiara flirting "Oh yes! Yes!"
    tiara flirting "I can feel it pushing my belly!"
    player "You bitch... you like it, don't you?"
    tiara flirting "Yes! But please, slow down!"
    player "...No."

    scene bedroom2_tiara_doggy animated:
        "bedroom2_tiara_6" with dissolve
        pause 0.6
        "bedroom2_tiara_7" with dissolve
        pause 0.6
        repeat

    pause 3

    tiara flirting "Oh yeah! Fuck me like the bitch I am!"
    player "Turn around!"

    scene bedroom2_tiara_8

    scene bedroom2_tiara_sex animated:
        "bedroom2_tiara_8" with dissolve
        pause 0.7
        "bedroom2_tiara_8_a" with dissolve
        pause 0.7
        repeat

    pause 2

    tiara flirting "You like looking at my tits bounce while you fuck me?"
    player "Of course I do!"
    tiara flirting "What else do you want to do with them?"
    player "I want to cum all over them?"
    tiara flirting "Then what are you waiting for?"

    scene bedroom2_tiara_9

    pause 1

    scene white with dissolve

    pause 1

    scene bedroom2_tiara_10 with dissolve

    tiara flirting "Mmmmm... it's so hot!"
    player "Are you going to tell me now?"

    scene bedroom2_tiara_11 with dissolve

    tiara "...Oh right! The hangar!"
    tiara "I'm not sure, but there were rumors about a new type of shock squad... one that always does the job done, no questions asked..."
    tiara "... because there was no one left to ask them."
    player "If it was them, don't you think they would've already attacked?"
    tiara "Not with M.A.L. still active..."
    player "Do you think if Megan has to choose, she will let M.A.L. defend this section instead of keeping Susan 'alive'?"
    tiara "Not a chance..."
    player "Shit! So I'd better get it solved, right?"
    tiara "You do."
    player "{i}If she's so worried about Earth's commandoes in the hangar, the sooner I get in the armory, the better...{/i}"

    call quest_released_advance_to_check_code from _call_quest_released_advance_to_check_code_1

    jump pod_advance_time

label quest_released_check_code:
    player "{i}OK, let's check if someone entered the armory...{/i}"

    scene door_armory_1

    player "{i}Rewind...{/i}"

    scene door_armory_lana_1

    player "{i}There!{/i}"
    player "{i}OK, I got the code!{/i}"

    scene door_armory_lana_3

    player "{i}But what would Lana want from the armory?{/i}"
    player "{i}Let's see what she takes out...{/i}"
    player "{i}...{/i}"
    player "{i}She sure does take her time in there. Let's move the stream a bit forward.{/i}"

    scene door_armory_lana_2

    player "{i}Hmmm...{/i}"
    player "{i}Nothing? Not the suit, not some weapons...{/i}"
    player "{i}And why would she need those anyway?{/i}"
    player "{i}Next night I'll go and take a look inside while everyone is sleeping!{/i}"

    call quest_released_advance_to_open_armory from _call_quest_released_advance_to_open_armory

    jump pod_advance_time

label quest_released_open_armory:
    player "{i}I shouldn't fall asleep. I need to get in the armory!{/i}"
    player "{i}...{/i}"

    if (global_events.pod_woman == "rebecca"):
        scene pod_rebecca_sleep_1

        player "{i}Rebecca is asleep, I should not wake her up.{/i}"

    else:
        scene pod_mom_sleep_1

        player "{i}Mom is asleep, I don't want to wake her.{/i}"

    scene pod_door_1

    player "{i}There!{/i}"
    player "{i}Let's get dressed and leave.{/i}"

    scene door_armory_1

    player "{i}Noone is around... let's see if I remember the code right...{/i}"
    player "{i}8-3-0-5-1-0{/i}"

    scene armory_1

    player "{i}...{/i}"
    player "{i}This doesn't look like an armory at all!{/i}"

    scene armory_2

    player "{i}This is definitely not an armory! There are some machineries inside...{/i}"

    scene armory_3

    player "{i}Looks like... a kind of pod or something...{/i}"
    player "{i}And there is someone inside it!{/i}"

    scene armory_4

    player "{i}Is that... Jack?! What the fuck is going on here!{/i}"
    player "{i}Then who is in the other pod?{/i}"

    scene armory_5

    player "{i}This is impossible!{/i}"
    player "{i}What the fuck! Why is there a clone of me sitting in that pod!{/i}"

    scene armory_megan_1

    megan angry "What are you doing here!"
    player "What the fuck is this thing? Why did you make a clone of me?"
    megan "A clone? I'm not a bio engineer, Greg... I'm a cybernetics engineer..."
    player "Then what is this? An android like Susan? Why would you make an android of me?"

    scene armory_all_1

    rebecca angry "What's going on here?"
    mom scared "Greg? Are you... What the fuck is this thing inside!"
    player "Megan has made an android that looks like me!"
    sis sad "No, Greg..."
    megan angry "Shut up, Lana!"

    scene armory_all_2

    tiara "You need to tell them. There is no point in keeping it a secret anymore..."
    megan angry "I won't tell them shit! Let them think what they want!"
    rebecca happy "So you won't mind me unplugging this thing?"
    megan scared "No!"
    sis scared "No! Mom! Please!"

    scene armory_all_3

    tiara "Greg... this is not an android..."
    player "Then what is this thing?"
    sis sad "Look, when I shot you... things didn't go exactly as planned..."
    player "What are you saying?"
    megan "The chip in your head short circuited and damaged your brain."

    scene armory_all_2

    player "I feel fine..."
    tiara "That's the thing... This is not an android... You are..."
    mom scared "What?"
    megan "Not exactly. The one standing here is merely a... for lack of a better term... an avatar."
    megan "No complex AI computing center inside his head, just a connection to the person that it hosts."

    scene armory_all_3

    megan "Luckily the part of your brain that got damaged was responsible just for the basic functions like breathing and we could hook you up to a life supporting machine and make this body, so you won't know the difference."
    player "Luckily?"
    megan happy "Yes. The human body is just feeding sensory data to the brain and executing it's commands. A cybernetic body can make this even better!"
    player "Better? I want this fixed! Do you hear me! Fixed!"
    sis sad "Greg, there is nothing we can do... This is why we need you... You have to find a solution to the equation, so we can all go to a place and time where we can be happy."

    scene armory_all_2

    megan "I managed to get the chip in your head working again, but the stress it creates on the remainder of your brain is starting to get me worried."
    player "Is that what happened to Jack? Why is he in one of those pods here too?"
    megan "Yes. He's been using it for too long, hoping that he can work faster if he can access M.A.L.'s resources... unfortunately his brain wasn't prepared for that."
    megan "Before the injury you were doing just fine and showing almost no signs of damage but now..."
    megan "You need to finish solving the equation fast."
    player "How much time do I have left?"
    megan "I don't know yet... Once I get a better estimate, I'll let you know. Now, let's get to sleep..."

    scene blank with fade

    call quest_released_finish from _call_quest_released_finish

    jump pod_advance_time
