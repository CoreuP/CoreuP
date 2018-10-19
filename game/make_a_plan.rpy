label quest_make_a_plan_help:
    player "{i}[quest_make_a_plan.help]{/i}"
    if quest_make_a_plan.finished:
        player "{i}There is nothing more that can be done about this in the current version of the game{/i}"
    jump wait

#phase 0
label quest_make_a_plan_start:
    $quest_make_a_plan.active = True
    $quest_make_a_plan.req_clock = 9
    $quest_make_a_plan.clock_mode = "exactly"
    $quest_make_a_plan.help = "Now that we have the plans for the station, we need to make a plan how to rescue Lana."
    return

#phase 1
label quest_make_a_plan_advance_to_talk_mom:
    $quest_make_a_plan.reset()
    $quest_make_a_plan.advance_phase()
    $quest_make_a_plan.mom_location = "vr_room"
    $quest_make_a_plan.location = "vr_room"
    $talk_with_mom.add_topic("Talk about Earth", "quest_make_a_plan_talk_mom", quest_make_a_plan, 1)
    $quest_make_a_plan.help = "Mom was pretty angry... maybe I should try and talk to her when she is relaxed."
    $global_events.rebecca_bedroom = True
    return

#phase 2
label quest_make_a_plan_advance_to_sleep:
    $quest_make_a_plan.reset()
    $quest_make_a_plan.advance_phase()
    $quest_make_a_plan.req_clock = 3
    $quest_make_a_plan.clock_mode = "at_most"
    $quest_make_a_plan.help = "Mom didn't let me finish so I'm still super horny..."
    return

#phase 3
label quest_make_a_plan_advance_to_morning:
    $quest_make_a_plan.reset()
    $quest_make_a_plan.advance_phase()
    $quest_make_a_plan.req_clock = 9
    $quest_make_a_plan.clock_mode = "exactly"
    $quest_make_a_plan.help = "I definitely saw something in the corridors outside. I better tell the others."
    return

#phase 4
label quest_make_a_plan_advance_to_start_training:
    $quest_make_a_plan.reset()
    $quest_make_a_plan.advance_phase()
    $quest_make_a_plan.req_clock = 15
    $quest_make_a_plan.clock_mode = "exactly"
    $quest_make_a_plan.help = "Rebecca said that we should begin training and I think she might be right - we could definitely use some exercise."
    return

#phase 5
label quest_make_a_plan_advance_to_talk_mom_beds:
    $quest_make_a_plan.reset()
    $quest_make_a_plan.advance_phase()
    $quest_make_a_plan.req_clock = 22
    $quest_make_a_plan.clock_mode = "at_least"
    $quest_make_a_plan.location = "shared_beds"
    $quest_make_a_plan.mom_location = "shared_beds"
    $quest_make_a_plan.help = "I should talk with mom and ask her to be more understanding with Rebecca. I'd better do it in the evening when she's alone."
    return

#phase 6
label quest_make_a_plan_advance_to_next_training:
    $quest_make_a_plan.reset()
    $quest_make_a_plan.advance_phase()
    $quest_make_a_plan.req_clock = 15
    $quest_make_a_plan.clock_mode = "exactly"
    $quest_make_a_plan.help = "Mom agreed to stop reminding Rebecca that she lost Lana, so I guess the trainings can continue as planned."
    return

#phase 7
label quest_make_a_plan_advance_to_make_hack:
    $quest_make_a_plan.reset()
    $quest_make_a_plan.advance_phase()
    $quest_make_a_plan.location = "bedroom"
    $quest_make_a_plan.req_clock = 22
    $quest_make_a_plan.clock_mode = "at_least"
    $quest_make_a_plan.help = "Rebecca said she will make the hack for the cameras, I guess she will tell us when she's ready."
    return

#phase 8
label quest_make_a_plan_advance_to_breakfast:
    $quest_make_a_plan.reset()
    $quest_make_a_plan.advance_phase()
    $quest_make_a_plan.req_clock = 9
    $quest_make_a_plan.clock_mode = "exactly"
    $quest_make_a_plan.help = "Rebecca managed to hack the cameras, so we are ready to execute our plan."
    return

#phase 9
label quest_make_a_plan_advance_to_setup_game:
    $quest_make_a_plan.reset()
    $quest_make_a_plan.advance_phase()
    $quest_make_a_plan.location = "vr_room"
    $quest_make_a_plan.rebecca_location = "vr_room"
    $quest_make_a_plan.req_efficiency = 100
    $quest_make_a_plan.req_energy = 1000
    $talk_with_rebecca.remove_topic_by_txt("Play another game")
    $talk_with_rebecca.add_topic("Setup VR room", "quest_make_a_plan_setup_game", quest_make_a_plan, 9)
    $quest_make_a_plan.help = "Once we have 1000 kWh of energy and the panels operate at 100\% I should talk with Rebecca to set up the VR room."
    return

#phase 0
label quest_make_a_plan_discuss:
    hide screen station_rooms

    scene mess_hall_mom_rebecca_1 #done

    player "Now that we have the plans..."
    mom "First things first! We agreed that once we have those, we will cut the connection with Earth, right?"
    rebecca "Amelia, this might not be such a good idea..."

    scene mess_hall_mom_rebecca_4 #mom angry

    mom "No, no, no - you said that once we have the plans, the whole deal with Earth is off!"
    mom "Do you want those perverts down there to watch us and make us do things?"
    rebecca "You think I like having my ass spanked? Well... I don't!"
    rebecca flirting "... Not that much anyway."
    rebecca "But cutting them off means that if the rescue goes south, we can't get help from anyone!"
    player "I think you're right..."
    if (global_events.greg_threesome):
        mom angry "Oh, Mr. 'I-had-a-threesome-with-my-mom' thinks we should keep having sex, so some horny people can watch?"
    else:
        mom angry "Oh, Mr. 'I-spied-on-my-mom-while-she-had-her-pussy-licked' has something to say?"
    mom angry "What a surprise!"
    rebecca "You are overreacting! Why is it such a problem? Nobody got hurt."
    rebecca happy "Well... except for my ass, but I don't mind..."
    mom "That's true, but still... I don't like being spied."
    mom "You know what? You two can sleep in the bedroom and have those perverts peep on you... doing whatever it is you will do..."
    mom "But I won't be a part in that!"

    scene mess_hall_mom_rebecca_1 #done

    rebecca "Fine. Now let's discuss how we are going to help Lana!"
    player "I went thorough the plans... and I can't see how we can breach their section..."
    rebecca "We won't."
    mom "But how are we going to get to Lana then?"
    rebecca "We will swap her for Susan."
    player "What?"
    mom "Swap her?"
    rebecca "We will lure Susan out, incapacitate her, kidnap her and exchange her for Lana."
    mom "You want to bring that thing here?"
    rebecca "It's the only way..."
    call quest_make_a_plan_advance_to_talk_mom from _call_quest_make_a_plan_advance_to_talk_mom
    jump advance_time

#phase 1
label quest_make_a_plan_talk_mom:
    hide screen station_rooms
    player "{i}It might not be safe to talk here with all the people watching us on Earth...{/i}"
    player "Mom... do you want some sunscreen?"

    scene beach_mom_8 #mom angry done

    mom angry "Are you kidding me?"
    player "I think the sun is set to a higher setting than it is {i}on Earth{/i} and I wouldn't want to {i}see{/i} you getting sunburned..."
    mom "Oh... right..."

    scene beach_mom_9 #mom calm done

    player "I wanted to talk with you about... you know..."
    player "About the {i}benefits{/i} and energy {i}costs{/i} of running this room."
    mom "Hmmm..."

    scene beach_mom_10 #mom calm done

    mom "I've told you already - this is exactly what I don't like in this room! The cost is too high!"
    player "But if we manage to use it wisely, we can probably afford it."
    mom "And what happens if you stay here too much? You'll get burned!"
    player "That's what I mean - we can't give up on having the sunscreen, just because it's messy..."
    mom "Maybe you're right... a little sunscreen doesn't hurt anybody..."

    scene beach_mom_11 #mom topless done

    player "Turn around."
    mom flirting "Why? Don't you like what you see?"
    player "No... I mean yes... I mean of course I like it!"

    scene beach_mom_12 #mom topless back done

    mom flirting "You know... sometimes I turn on the monitor for this room and check what is going on in here?"
    player "You do?"
    mom flirting "Did you know there are cameras in here?"
    player "I'm not surprised - this room has some really sophisticated equipment so..."

    scene beach_mom_13 #mom topless player hands on back done

    mom flirting "Oh, I like that!"
    mom flirting "So... sometimes I see some pretty interesting stuff..."

    scene beach_mom_14 #mom topless player hands on ass done

    player "You do?"
    mom flirting "Yes... I've even seen things that I wouldn't know that existed!"
    mom flirting "I mean... are you really that into feet?"

    scene beach_mom_15 #mom topless show feet done

    player "..."
    mom flirting "Oh, wow!"
    mom flirting "You don't have to answer that!"

    scene beach_mom_16 #mom topless kneeling flirty done

    mom flirting "I can see that you {i}really{/i} like them!"
    mom flirting "Anyway, as I have told you, I didn't even know this was a thing!"
    mom flirting "And if this is what you like... I guess I can't say no."

    scene beach_mom_17 #mom topless fj done

    player "Oh, that's hot!"
    mom flirting "I find it quite exciting as well!"
    mom flirting "Let me make myself comfortable..."

    scene beach_mom_fj animated:
        "beach_mom_18" with dissolve
        pause 0.8
        "beach_mom_19" with dissolve
        pause 0.8
        repeat

    pause

    scene beach_mom_20 #mom topless standing done

    mom flirting "Unfortunately I think I had enough sun for today... you can stay if you like."
    player "But mom..."
    mom "See you later!"
    call quest_make_a_plan_advance_to_sleep from _call_quest_make_a_plan_advance_to_sleep
    jump advance_time

#phase 2
label quest_make_a_plan_sleep:
    hide screen station_rooms

    scene blank #done

    player "{i}Shit! Mom didn't let me cum so that chip in my head will probably connect with the cameras again...{/i}"

    scene corridor_1 #done

    player "{i}There we go...{/i}"

    scene corridor_2 #done

    player "..."

    scene corridor_3 #done

    player "{i}Damn...{/i}"

    scene elevator_1

    player "{i}Hmmm...{/i}"
    player "{i}Wasn't this door closed when mom stole Rebecca's suit and ran out of power?{/i}"

    scene corridor_2 #done

    player "{i}Won't this end?{/i}"

    scene corridor_3
    scene corridor_3_run animated with dissolve:
        "corridor_3"
        pause 0.5
        "corridor_3_figure" with dissolve
        pause 0.5
        "corridor_3" with dissolve

    pause

    player "{i}What was that? I think I saw something move!{/i}"
    player "{i}I need to warn the others!{/i}"
    player "..."
    player "{i}So... how do I wake up?{/i}"
    player "..."
    player "{i}I guess I'll have to wait till morning...{/i}"

    scene blank #done

    pause

    call quest_make_a_plan_advance_to_morning from _call_quest_make_a_plan_advance_to_morning
    jump morning

#phase 3
label quest_make_a_plan_morning:
    hide screen station_rooms

    player "I need to tell you something... I connected to the cameras last night and saw something move in the corridors."
    mom "You 'connected'? What did you two... you know what... I don't even want to know!"
    rebecca "We did nothing! I swear!"
    player "Yeah mom, it was because at the beach you didn't..."
    rebecca happy "This gets interesting! What did you not do, Amelia?"
    mom "It's none of your business!"
    rebecca flirting "Ohhh, poor boy... Is this why you were so horny in the morning?"
    mom "I thought you did 'nothing'?"
    rebecca flirting "Well yes - yesterday we didn't do anything, but this morning..."
    rebecca flirting "Rrrr..."
    mom "I'm gonna puke..."
    player "Will you listen to me - I saw someone moving through the corridors!"
    rebecca "So what? It was probably that android... what was it's name..."
    mom "Susan?"
    player "I don't think it was her..."
    rebecca "It doesn't matter! Look, we need to act quickly if we want to save Lana!"
    mom sad "If we {i}can{/i} save her..."
    player "Mom, I don't think Jack will let anything bad to happen to her."
    rebecca "...don't think about that now - we need to start training."
    rebecca "Meet me at the beach at 3 PM."
    player "The beach? What about the cameras?"
    rebecca "Leave that to me. They will experience 'technical difficulties' during that time."
    mom "I don't think I need to..."
    rebecca "Everyone!"
    call quest_make_a_plan_advance_to_start_training from _call_quest_make_a_plan_advance_to_start_training
    jump advance_time

#phase 4
label quest_make_a_plan_start_training:
    hide screen station_rooms

    if (player_location != "vr_room"):
        player "Shit! It's 3 PM already! I need to go to the VR room for the training."
    else:
        player "It's 3 PM and still no one is here..."

    scene beach_training_1 #done

    player "{i}OK, mom is here, but Rebecca is still missing...{/i}"
    mom "So we are both here and guess whose ass is still late!"

    scene beach_training_2 #rebecca walking

    rebecca happy "{i}Hot{/i} ass. Right, Greg?"
    player "Don't start, please!"
    rebecca "You are right - we have a much more important task at hand."

    scene beach_training_3 #rebecca mom sitting

    mom "What do you have in mind?"
    rebecca "First we need to stretch. We don't want to risk an injury..."

    scene beach_training_4 #rebecca stretching

    mom "Fair enough."

    scene beach_training_5 #mom stretching

    player "{i}Wow...{/i}"
    rebecca flirting "Greg, don't just stand there - help your mom!"

    scene beach_training_6 #mom greg stretching

    rebecca "I want to show you some moves that might save your lives if you get in close quarter combat with Susan."

    scene beach_training_7 #rebecca fight moves

    $renpy.pause()

    scene beach_training_8 #rebecca fight moves

    $renpy.pause()

    scene beach_training_9 #rebecca fight moves

    mom "It didn't help you much when that thing got Lana..."

    scene beach_training_10 #rebecca standing angry

    rebecca angry "I didn't expect her to be a fucking robot! I thought I got her with the flamethrower!"
    rebecca "And on top of that, this is just in case you ever get into a fight with it. If everything goes according to plan, it will never come to that."
    mom "I think we are done here..."
    rebecca "Same time tomorrow?"
    mom "Whatever."
    call quest_make_a_plan_advance_to_talk_mom_beds from _call_quest_make_a_plan_advance_to_talk_mom_beds
    jump advance_time

#phase 5
label quest_make_a_plan_talk_mom_beds:
    hide screen station_rooms

    scene door_2
    player "So... let's talk with mom"
    mom "{i}Oh, yes! Oh, that's so good!{/i}"
    player "What the... Is she... let's take a peek!"

    scene shared_beds_mom_3 #mom vibrator

    mom "That's it! Yes!"
    mom "Oh yes!"

    scene shared_beds_mom_4 #mom vibrator

    mom "Oh, I love that on my clit!"

    scene shared_beds_mom_vibrator animated:
        "shared_beds_mom_5" with dissolve #mom vibrator
        pause 0.8
        "shared_beds_mom_6" with dissolve #mom vibrator
        pause 0.8
        repeat

    pause

    player "{i}She has found Lana's vibrator!{/i}"
    player "{i}Oh, that's hot!{/i}"

    scene shared_beds_mom_vibrator_2 animated:
        "shared_beds_mom_7" with dissolve #mom vibrator
        pause 0.8
        "shared_beds_mom_8" with dissolve #mom vibrator
        pause 0.8
        repeat

    pause

    mom "I'm cumming!"
    player "Wow!"

    scene shared_beds_mom_10 #mom standing surprised

    mom "Greg!"
    mom embarassed "What are you doing here?"
    player "I wanted to talk to you..."

    scene shared_beds_mom_11 #mom standing embarassed

    mom embarassed "How long have you been here?"
    player "It doesn't matter. Look..."
    mom embarassed "Please go away."

    player "No!"
    mom "No?"
    player "Why should I? Because you are embarrassed of what just happened?"
    mom "Well... yes!"
    player "Good! Because this is just how Rebecca feels every time you remind her that Lana is missing because she could not protect her."
    player "Please, stop doing that - it's hard enough for her!"

    scene shared_beds_mom_12 #mom standing

    mom "I didn't think about that... you are right."
    player "And also for our deal with Earth, please can you be more supportive?"
    mom "What do you mean?"
    player "I mean that we might need their help again and it's not wise to cut the connection."
    player "Rebecca sees this, I see this, why can't you?"

    scene shared_beds_mom_13 #mom sitting sad

    mom "I just feel bad about what we need to do in order to get their help."
    player "I understand that, but maybe the equipment in the bedroom is helping us not to loose our minds."
    player "We have been locked here for [day] days and if it wasn't... helping us relieve some pressure, we could go insane."
    mom "Maybe Rebecca is right - Earth rules shouldn't apply to us."
    player "She has spent most of her life stuck in space so she probably knows what she's talking about."

    scene shared_beds_mom_14 #mom standing kiss

    mom happy "Thank you!"

    scene shared_beds_mom_15 #mom standing happy

    player "Can I count on you not to piss her off every chance you get?"
    mom happy "I promise!"

    call quest_make_a_plan_advance_to_next_training from _call_quest_make_a_plan_advance_to_next_training
    jump advance_time

#phase 6
label quest_make_a_plan_next_training:
    hide screen station_rooms

    if (player_location != "vr_room"):
        player "Shit! It's 3 PM already! I need to go to the VR room for the training."
    else:
        player "It's 3 PM and still no one is here..."

        scene beach_training_11 # Rebecca, mom walking in distance done

        player "Oh, there they are!"

    scene beach_training_12 # Rebecca, mom standing done

    player "Are we good?"
    mom "Yes."
    rebecca "Your mom and I had a... talk and I think we can proceed with the trainings."
    player "A... talk?"
    mom "Yes."
    rebecca fliting "Anyway, let's start with some stretching!"

    scene beach_training_5 # done

    rebecca happy "Enjoying the view?"
    player "Definitely!"
    rebecca "Don't just stand there! Help your mom!"

    scene beach_training_6_a # done
    $renpy.pause()
    scene beach_training_6 # done

    rebecca "Amelia, care to show us some moves?"

    scene beach_training_13 # mom fight moves done
    $renpy.pause()
    scene beach_training_14 # mom fight moves done

    rebecca "Pretty good!"

    scene beach_training_12 # as above

    mom happy "I studied martial arts when I was younger."
    player "Really?"
    rebecca happy "And I always thought you we some geek scientist!"
    mom happy "Care for a sparring?"

    scene beach_training_15 # Rebecca mom facing done
    $renpy.pause()
    scene beach_training_16 # Rebecca hit mom done

    mom angry "Hey! It wasn't fair!"
    rebecca happy "You think that thing will fight fair?"
    mom "Alright then!"

    scene beach_training_17 # Mom try hit rebecca done
    $renpy.pause()
    scene beach_training_18 # Mom try hit rebecca done
    $renpy.pause()
    scene beach_training_20 # Rebecca push mom done
    $renpy.pause()
    scene beach_training_21 # Rebecca sitting on mom done

    rebecca happy "You've lost!"
    mom "Mphhmp!"
    rebecca happy "I can't hear you!"
    mom "Mphhmp!"

    scene beach_training_22 # Rebecca standing done

    mom "Let's hope it won't come to hand-to-hand combat... I suck pretty bad at that..."
    rebecca "You were pretty good actually, but I've spent most of my life doing that, so it wasn't actually fair."
    player "{i}They seem to get along pretty well... That's good!{/i}"

    scene beach_training_12 # as above done

    player "So, what's the plan?"
    rebecca "Right... We've talked about it and your mom thinks it's best if you stay here and let us capture that thing."
    player "No! I won't let you risk your life while I sit here!"
    mom "Greg, please! I need to know that you are safe!"
    rebecca "And we will need your... eyes on the station."
    player "No!"
    mom "Greg, sit down and listen!"

    scene beach_training_23 # all sitting done

    mom "We will go out, one of us will be the bait, the other will plant a proximity EMP charge."
    rebecca "Don't worry - I will be the bait!"
    mom "I will go out with the chameleon suit and hack the cameras from here to the elevator so they will stream a loop."
    mom "Then I'll go in the armory and take an EMP charge, and plant it."
    rebecca "I will make an ordinary suit that looks just as mine and will go to the elevator room..."
    player "And the cameras won't spot you because they will be playing the loop."
    mom "Exactly!"
    rebecca "Once I'm there, your mom will restore the elevator camera back to operation and they will see me."
    rebecca "For all they know, my suit had went out of power and I had lost my cloak."
    player "They will send the cyborg..."
    mom "And it will trigger the EMP charge, render it inoperable and we will capture it."
    player "What if something goes wrong?"
    rebecca "Then your mom will return here and lock the door."

    scene beach_training_24 # mom surprised to rebecca done

    mom "What? No!"
    rebecca "Amelia, listen to me! You need to get back here, lock the door and pray that Earth will come to their senses and finally decide to act!"
    rebecca "There are no bots roaming through the station, no attempts to hack the door... something is wrong with M.A.L."
    mom "Yeah - it went crazy and killed the whole crew!"
    rebecca "We are still alive, so I don't think that's what happened..."

    scene beach_training_23 # as above done

    mom "Maybe Jack doesn't want it to kill us?"
    rebecca "He doesn't give a shit about us - I can promise you that!"
    rebecca "Megan had a chance to kill Greg and escape, but she didn't. Instead she put that weird chip inside his head. Why?"
    player "I don't know..."
    rebecca "Exactly - we don't know what happened, but it just doesn't make any sense!"
    rebecca "Promise me that you will get back here. I need to know Greg won't fall into their hands and you will take care of him!"
    mom "... I promise."
    rebecca "Good! Let's get started then! I will start making the hack for the cameras."

    call quest_make_a_plan_advance_to_make_hack from _call_quest_make_a_plan_advance_to_make_hack
    jump advance_time

#phase 7
label quest_make_a_plan_make_hack:
    hide screen station_rooms

    scene bedroom_rebecca_5 #rebecca laying bed done

    rebecca "Good! You are here!"
    player "Why?"
    rebecca happy "I think I finished the hack!"
    player "You think?"
    rebecca "I'm pretty sure it will work, but I need to test it first."
    rebecca flirting "That's why I need you!"
    player "I think I know where this is going..."

    scene bedroom_rebecca_6 #rebecca undressing done

    rebecca flirting "I bet you do!"
    rebecca flirting "Drop your pants!"

    scene bedroom_rebecca_7 #rebecca naked done

    rebecca flirting "Come closer..."

    scene bedroom_rebecca_8 #rebecca hj done

    player "I love your hands on my dick!"
    rebecca "What else do you love?"

    scene bedroom_rebecca_9 #rebecca bj lick done

    rebecca flirting "Do you love my tongue on your dick as well?"
    player "Oh yes!"
    player "But I love your mouth more!"

    scene bedroom_rebecca_10 #rebecca bj deep done

    rebecca flirting "..."

    scene bedroom_rebecca_bj animated:
        "bedroom_rebecca_11" with dissolve
        pause 0.8
        "bedroom_rebecca_10" with dissolve
        pause 0.8
        repeat

    pause

    scene bedroom_rebecca_12 #rebecca looking greg

    rebecca flirting "Aren't you ready?"
    player "Maybe, but I like watching you sucking my dick."
    rebecca flirting "This is a test, remember? So please try connecting to your mom's bedroom and I'll go there to hack the camera."

    scene blank

    $renpy.pause()

    scene shared_beds_mom_17 #mom vibrator

    player "I'm connected, but..."
    rebecca "What?"
    player "I don't think it will be a good time for you to go there..."

    scene shared_beds_mom_18 #mom vibrator

    rebecca "Why?"
    player "She's not sleeping..."
    rebecca "She's not?"
    player "No..."

    scene shared_beds_mom_21_a

    scene shared_beds_mom_vibrator_3 animated:
        "shared_beds_mom_21" with dissolve
        pause 0.8
        "shared_beds_mom_21_a" with dissolve
        pause 0.8
        repeat

    rebecca "Are you sure?"
    player "Believe me, I'm absolutely sure she's not!"
    rebecca "What is she doing then?"
    player "She's... playing... with the vibrator..."
    rebecca happy "I must hurry then if I want to catch her in the act!"

    scene bedroom_bed_1 #bedroom from bed pov

    player "{i}She had put the suit on and left...{/i}"
    player "{i}This should be interesting...{/i}"

    scene blank

    pause

    scene shared_beds_mom_22

    scene shared_beds_mom_vibrator_3 animated:
        "shared_beds_mom_22_a" with dissolve
        pause 0.8
        "shared_beds_mom_22" with dissolve
        pause 0.8
        repeat

    pause

    player "{i}I think I heard the door opening...{/i}"

    scene shared_beds_mom_22

    scene shared_beds_mom_23 with dissolve #rebecca appear done

    scene shared_beds_mom_24 with dissolve #rebecca suit visible done

    scene shared_beds_mom_25 with dissolve #rebecca visible done

    rebecca flirting "Well, well, well... What do we have here?"

    scene shared_beds_mom_26 #mom surprised

    mom "Rebecca! What are you doing here?"
    rebecca flirting "Me? What are {i}you{/i} doing with Lana's vibrator?"
    mom "I was just..."

    scene shared_beds_mom_27 #rebecca joining

    rebecca flirting "You don't need to stop just because of me!"
    rebecca flirting "I like to watch!"

    scene shared_beds_mom_28 #mom showing rebecca

    mom flirting "You do? Are you going to just watch or...?"
    rebecca flirting "At least in the beginning."

    scene shared_beds_mom_29 #mom masturbating done

    mom flirting "I think I like being watched... Did you know that Greg saw me using the vibrator earlier?"
    rebecca flirting "No..."

    scene shared_beds_mom_30 #rebecca looking at camera done

    rebecca flirting "He didn't tell me that!"
    rebecca flirting "Does the fantasy of him watching you turns you on?"
    mom "... yes..."
    rebecca flirting "Too bad that he's in the bedroom and can't see you playing with your pussy."

    scene shared_beds_mom_31 #rebecca standing reaching for camera done

    rebecca flirting "I just need to do something and then I may join you!"

    scene shared_beds_cam_1

    $renpy.pause()

    scene bedroom_bed_1 #as above

    player "{i}Shit! She hacked the camera!{/i}"
    player "{i}I'd better try to get some sleep...{/i}"
    scene blank
    player "{i}zzzz{/i}"

    call quest_make_a_plan_advance_to_breakfast from _call_quest_make_a_plan_advance_to_breakfast
    jump morning

#phase 8
label quest_make_a_plan_brakfast:
    hide screen station_rooms
    player "We are ready, let's go!"
    mom "Are we?"
    player "Yes - the hack is working, so..."
    mom "What hack?"
    player "You didn't tell her?"
    rebecca smiling "No."
    mom "Tell me what?"
    rebecca smiling "I made the hack and tested it yesterday on the camera in your room."
    mom angry "And Greg was watching?"
    player "I didn't see much - just the beginning."

    scene mess_hall_mom_rebecca_4 #done

    mom angry "And this somehow makes it better?"
    mom "Rebecca, you could've warned me at least..."
    rebecca flirting "You were busy."
    player "The important thing is that the hack is working and we can save Lana."

    scene mess_hall_mom_rebecca_1 #done

    rebecca "About that..."
    rebecca "We should make sure if this plan fails, Earth will help us."
    mom "You are not suggesting..."
    rebecca "I am. We need to make one last 'show' before we attempt to catch Susan."
    mom "OK, as long at it's the 'last' show, we can do that..."
    rebecca "Fine, we will need a full battery and maximum capacity of the panels. Meet me at the beach when you are ready."

    call quest_make_a_plan_advance_to_setup_game from _call_quest_make_a_plan_advance_to_setup_game
    jump advance_time

#phase 9
label quest_make_a_plan_setup_game:
    hide screen station_rooms
    player "We are ready!"
    rebecca "Nice! I will go get your mom. Meet us in the engineering room."
    hide screen day_time
    hide screen energy

    scene life_support_mom_rebecca_2

    player "Wow! Where did you get those clothes?"
    rebecca flirting "Do you like them?"
    mom flirting "We figured that some roleplay would persuade Earth to help us if the kidnapping doesn't go as planned."
    player "So that's what the extra energy was for..."
    player "I can't wait to see what you've got under those clothes!"
    mom "Greg!"
    rebecca flirting "Play your cards right and you will!"
    player "Cards?"
    mom "Ready for some Black Jack?"
    player "With both of you?"
    rebecca flirting "Can't you handle both of us?"
    if (global_events.greg_threesome):
        mom flirting "I think you already had..."
    rebecca flirting "The room is ready Let's go!"
    menu:
        "Play the game":
            jump game_mom_rebecca_bj_start
        "Skip the game":
            jump quest_make_a_plan_execute_plan

label quest_make_a_plan_execute_plan:
    $quest_make_a_plan.finished = True
    scene blank
    player "..."
    scene corridor_1
    player "OK, I'm connected!"
    rebecca "Amelia, let's go!"
    scene corridor_2
    player "{i}So the plan was for mom to put on the suit and hack the cameras and then Rebecca would go to the armory and pick up an EMP proximity charge.{i}"
    player "{i}She will plant the charge near Megan's section and then move back a bit.{/i}"
    scene corridor_3
    player "{i}Rebecca will be wearing an ordinary suit that looks like her chameleon suit and once everything is set, mom will restore the feed from the camera.{/i}"
    player "{i}It will appear as if the suit has ran out of power, Megan will send Susan to capture her and on her way to Rebecca's position, she will set off the charge.{/i}"
    scene corridor_2
    player "{i}Then mom and Rebecca will bring the disabled cyborg to our section and we will exchange her for Lana.{/i}"
    player "{i}But if the cameras are hacked, how will I see if something goes wrong...{/i}"
    scene corridor_1_sis
    player "What the... Lana?"
    player "She's right in front of our door! Maybe she has escaped by her own!"
    player "I need to let her in and warn the others!"
    scene door_2
    player "What was the code..."
    player "4-2-9-9"
    scene corridor_1_sis_2
    player "Lana! What are you..."
    sis sad "I'm sorry..."
    scene corridor_1_sis_3
    pause 0.5
    scene blank with fade

    jump captured_wake_up
