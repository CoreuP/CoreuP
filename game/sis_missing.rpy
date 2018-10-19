label quest_sis_missing_help:
    player "{i}[quest_sis_missing.help]{/i}"
    if quest_sis_missing.finished:
        player "{i}There is nothing more that can be done about this in the current version of the game{/i}"
    jump wait

#phase 0 auto breakfast
label quest_sis_missing_start:
    $quest_sis_missing.active = True
    $quest_sis_missing.help = ""
    $quest_sis_missing.req_day = day + 2
    $quest_sis_missing.day_mode = "at_least"
    return

#phase 1 terminal
label quest_sis_missing_advance_to_talk_earth:
    $quest_sis_missing.reset()
    $quest_sis_missing.advance_phase()
    $quest_sis_missing.req_clock = 3
    $quest_sis_missing.clock_mode = "at_most"
    $quest_sis_missing.location = "comm"
    $quest_sis_missing.help = "I should talk to Earth and try to make them help us free Lana"
    $global_events.sis = False
    $talk_with_terminal.add_topic("Ask for help", "quest_sis_missing_talk_earth", quest_sis_missing, 1)
    return
    
#phase 2 talk
label quest_sis_missing_advance_to_talk_rebecca:
    $quest_sis_missing.reset()
    $quest_sis_missing.advance_phase()
    $quest_sis_missing.location = "vr_room"
    $quest_sis_missing.rebecca_location = "vr_room"
    $quest_sis_missing.help = "So, the guy from Earth said they are willing to help if we make some money for them... I should talk with Rebecca to see what she thinks about it"
    $talk_with_rebecca.add_topic("Tell her about Earth's request", "quest_sis_missing_talk_rebecca", quest_sis_missing, 2)
    return
    
#phase 3 auto dinner
label quest_sis_missing_advance_to_dinner:
    $quest_sis_missing.reset()
    $quest_sis_missing.advance_phase()
    $quest_sis_missing.req_clock = 12
    $quest_sis_missing.clock_mode = "at_least"
    $quest_sis_missing.help = "Rebecca and I have to talk to mom and explain her about Earth's request"
    return
    
#phase 4 auto mom shower
label quest_sis_missing_advance_to_mom_shower:
    $quest_sis_missing.reset()
    $quest_sis_missing.advance_phase()
    $quest_sis_missing.help = "Mom said that she will think about doing what the guys on Earth want, but I'm worried it might be too late"
    return
    
#phase 5 auto breakfast
label quest_sis_missing_advance_to_talk_breakfast:
    $quest_sis_missing.reset()
    $quest_sis_missing.advance_phase()
    $quest_sis_missing.help = "Whoa! I wonder if what happened this morning has anything to do with our current situation..."
    return
    
#phase 6 terminal
label quest_sis_missing_advance_to_talk_earth_again:
    $quest_sis_missing.reset()
    $quest_sis_missing.advance_phase()
    $quest_sis_missing.location = "comm"
    $quest_sis_missing.req_clock = 3
    $quest_sis_missing.clock_mode = "at_most"
    $quest_sis_missing.help = "Let's check with Earth if what we did in the morning made enough money for them to acquire the plans of the station"
    $talk_with_terminal.add_topic("Ask about the plans", "quest_sis_missing_talk_earth_again", quest_sis_missing, 6)
    return
    
#phase 7 auto breakfast
label quest_sis_missing_advance_to_setup_scene:
    $quest_sis_missing.reset()
    $quest_sis_missing.advance_phase()
    $quest_sis_missing.help = "Rebecca should have already made the clothes - she said that we'll talk at breakfast"
    return
    
#phase 8 auto 11:00
label quest_sis_missing_advance_to_med_bay:
    $quest_sis_missing.reset()
    $quest_sis_missing.advance_phase()
    $quest_sis_missing.req_clock = 11
    $quest_sis_missing.clock_mode = "exactly"
    $quest_sis_missing.help = "Rebecca said to meet her in the Med Bay at 11:00"
    return
    
#phase 9 auto 12:00
label quest_sis_missing_advance_to_lesb_show:
    $quest_sis_missing.reset()
    $quest_sis_missing.advance_phase()
    $quest_sis_missing.req_clock = 12
    $quest_sis_missing.clock_mode = "exactly"
    $quest_sis_missing.help = "The show should start any minute now..."
    return
    
#phase 10 auto dinner
label quest_sis_missing_advance_to_dinner_talk:
    $quest_sis_missing.reset()
    $quest_sis_missing.advance_phase()
    $quest_sis_missing.help = "What happened in the bedroom should make enough money for the guy on Earth to acquire the plans. Let's discus it at dinner."
    return
    
#phase 11 terminal
label quest_sis_missing_advance_to_get_plans:
    $quest_sis_missing.reset()
    $quest_sis_missing.advance_phase()
    $quest_sis_missing.location = "comm"
    $quest_sis_missing.req_clock = 3
    $quest_sis_missing.clock_mode = "at_most"
    $talk_with_terminal.add_topic("Obtain the plans", "quest_sis_missing_get_plans", quest_sis_missing, 11)
    $quest_sis_missing.help = "Next step should be obtaining the plans from Earth."
    return
    
label quest_sis_missing_advance_to_make_plan:
    $quest_sis_missing.reset()
    $quest_sis_missing.advance_phase()
    $quest_sis_missing.finished = True
    $quest_sis_missing.help = "There is nothing more here."
    call quest_make_a_plan_start from _call_quest_make_a_plan_start
    return
        
#phase 0 auto breakfast
label quest_sis_missing_breakfast:
    mom "I want to talk to you about something..."
    sis "What is it?"
    mom "It has been [day] days and I really think we should do something about our situation here."
    rebecca "Finally!"
    player "Mom, we can't escape..."
    mom "I'm not talking about escaping. All I'm saying is that can't just sit here and wait for God knows who to come and rescue us."
    rebecca "We have the suit..."
    mom "And we should use it to our advantage as much as we can!"
    sis "But it's too limited - you can go out there for only a couple of hours and we have only one."
    rebecca happy "I should be the one that goes out!"
    mom angry "I've used it too, I know how it works!"
    rebecca happy "And after that I had to rescue your sorry ass. We are not risking the suit and that's final!"
    mom sad "I guess you are right..."
    rebecca happy "So? Are we doing it or what?"
    sis "Doing what, mom?"
    player "Yeah, we need a plan what you will do once you get outside."
    rebecca "The way I see it, first we need weapons so we can defend ourselves."
    player "Anything else?"
    sis "We only have two hours, we will be lucky if mom manages to find the weapons storage and bring some back."
    rebecca "And on top of that once I get the weapons, my cover will be blown."
    mom "Oh, right - the suit can't make anything you carry invisible too."
    rebecca "So not much left to think about. Let's get the weapons first."
    mom "Is there enough power for you to charge the suit?"
    player "I believe there is!"
    rebecca happy "What are we waiting for then?"
    
    scene life_support_mom_sis_rebecca_1 #all standing around done
    
    rebecca "This brings back memories from the last time I charged the suit..."
    mom "What are you talking about?"
    rebecca flirting "Greg can explain."
    mom angry "Explain what?"
    player "Nothing mom!"
    rebecca flirting "Yeah... nothing."
    
    scene life_support_mom_sis_rebecca_2 #all standing rebecca naked done
    
    mom "Greg, don't look!"
    rebecca flirting "Too late for that, don't you think?"
    sis "How long should we wait?"
    rebecca "Not too long, the suit's power banks are pretty advanced."
    sis "Mom, please find the weapons, get some and come back quickly!"
    sis "Don't take any chances."
    rebecca "Thank you but I think I can take care of myself!"
    mom angry "What is wrong with you? Your daughter is worried about you!"
    rebecca sad "I'm sorry Lana... Of course I won't take any chances - it's not just my life on the line, yours is too."
    sis "Thank you mom!"
    player "I think the suit is ready."
    rebecca "You are right!"
    
    scene life_support_mom_sis_rebecca_1 #all standing around done
    
    rebecca "Once I'm cloaked, open the door and close it as soon as I'm through!"
    player "Take the radio, I'll connect to the cameras and check ahead of you."
    rebecca "I can't carry anything with me - it will blow my cover."
    sis "Right!"
    rebecca happy "Let's do this thing!"
    
    scene life_support_mom_sis_rebecca_4 #rebecca body disappear done
    with dissolve
    
    scene life_support_mom_sis_rebecca_5 #rebecca suit disappear done
    with dissolve
    
    scene life_support_mom_sis_rebecca_6 #rebecca gone done
    with dissolve
    
    rebecca "OK, open the door!"
    player "Done!"
    rebecca "I'm through - close it!"
    player "Closed!"
    sis sad "... I have a bad feeling about this..."
    mom "It will be OK - she is highly trained and Greg can check the cameras."
    player "Mom, it's not that easy... in order for me to connect to the cameras..."
    mom "You have to be... excited... I know..."
    mom "It's fine..."
    sis "Let's go to the bedroom - it will be easier there."
    
    scene bedroom_mom_sis_1 #mom standing sis half naked done
    
    mom "Do I need to be here?"
    sis "You can stay if you like..."
    mom "OK, I'll stay but I won't do anything."
    sis "Get on the bed and close your eyes."

    scene blank
    
    sis flirting "Let's get you naked!"
    sis flirting "Amelia, did Greg took after his father in terms of size?"
    mom happy "What? No, his father was... average at best!"
    mom flirting "He got it from my side of the family."
    sis flirting "Wait, how do you know..."

    scene bedroom_mom_sis_2 #3rd person same as 1 done
    
    player "OK, I'm connected!"
    sis flirting "You little pervert! I haven't even touched you yet!"
    player "I think I'm getting better at this."
    sis flirting "Are you sure it has nothing to do with our little conversation?"
    mom flirting "Lana, you shouldn't look a gift horse in the mouth."
    
    scene bedroom_mom_sis_3 #3rd person sis hold dick done
    
    sis flirting "I'm not going to do anything with his mouth... I'll use mine instead!"
    
    scene bedroom_mom_sis_4 #done
    
    mom "Greg, can you see anything in the corridors outside?"
    player "Oh, right!"
    
    scene corridor_2 #done
    
    sis flirting "I bet he was enjoying the view. I think your son is a voyeur!"
    mom flirting "All men are."
    player "Nothing in the corridor..."
    
    scene outpost_2 #done
    
    player "Nothing in the Megan's part of the station too..."
    
    scene outpost_1 #done
    
    player "That's weird... Where are they?"
    
    scene locker_1 #done
    
    player "I think I found the weapons locker..."
    sis "Is my mom there?"
    player "I don't know... I can't see her."
    sis flirting "Mmmm, keep looking!"
    mom flirting "{i}(whisper) Oh, yeah!{/i}"
    player "{i}Wait! What is mom doing?{/i}"
    
    scene bedroom_mom_sis_5 #3rd person sis bj mom touching done
    
    player "{i}Is she... touching herself?{/i}"
    player "{i}That guy on Earth said that there are virtual cameras everywhere in this room, so it shouldn't be too hard switching the angle...{/i}"
    
    scene bedroom_mom_sis_6 #3rd person mom touching closeup done
    
    sis flirting "Amelia! What are you doing there?"
    mom embarassed "Nothing!"
    
    scene bedroom_mom_sis_7 #done
    
    sis flirting "And why are you naked?"
    mom embarassed "You are naked too!"
    player "Girls, this is not helping!"
    sis angry "What are you doing? You are supposed to be looking for my mother, not looking at yours!"
    
    scene locker_1 #done
    
    player "Sorry!"
    sis flirting "Not that I blame you - your mom looks amazing!"
    
    scene locker_2 #done
    
    player "I think she's there!"
    sis "Did you see her?"
    player "No but one of the weapons moved..."
    
    scene locker_3 #done
    
    player "She is definitely there!"
    sis "Check the corridors on her way back!"
    
    scene corridor_3 #done
    
    $renpy.pause()
    
    scene corridor_2 #done
    
    player "All clear!"
    sis "Hurry, mom..."
    mom flirting "Lana, you have a job to do..."
    sis flirting "Oh, right! Sorry!"
    
    scene corridor_weapon_3 #corridor 3 with floating weapons done
    
    player "She's coming back."
    
    scene corridor_weapon_2 #corridor 2 with floating weapons done
    
    player "Almost here..."
    
    scene corridor_weapons_susan_2 #same as above with susan in BG done
    
    player "Shit!"
    player "It's Megan's daughter!"
    sis "I have to help mom!"
    mom "Lana, wait!"
    
    scene corridor_sis_1 #corridor 1 with sis naked done
    
    player "Lana got out!"
    
    scene corridor_rebecca_sis_susan_1 #corridor 2 with weapons floating sis running susan BG done
    
    sis "Mom! Look out! She is behind you!"
    
    scene corridor_rebecca_sis_susan_2 #same with rebecca appearing done
    with dissolve
    
    scene corridor_rebecca_sis_susan_3 #same with suit visible done
    with dissolve
    
    scene corridor_rebecca_sis_susan_4 #same with rebecca visible done
    with dissolve
    
    rebecca angry "Stop! I'll shoot!"
    susan happy "Be my guest!"
    
    scene corridor_rebecca_sis_susan_5 #weapons fire? done
    
    $renpy.pause()
    
    scene corridor_rebecca_sis_susan_6 #android in place of susan done
    
    sis scared "What the fuck is that!"
    rebecca scared "Lana, get back!"
    sis scared "Mom, hurry!"
    
    scene corridor_rebecca_sis_susan_7 #android hit rebecca done
    
    $renpy.pause()
    
    scene corridor_rebecca_sis_susan_8 #android got sis, rebecca unconscious done
    
    susan happy "You are coming with me!"
    sis scared "Mom! Help me! Mom!"
    
    player "She took Lana!"
    
    scene bedroom_mom_6 #mom point away done
    
    mom "Meet me at the section entrance!"
    
    scene bedroom_mom_7 #bedroom empty done
    
    player "{i}Wait! Lana went out to help Rebecca and I could still feel someone playing with my dick! It was either mom or I must've imagined it...{/i}"
    player "{i}No time for this now, I need to get to the section door.{/i}"

    scene life_support_mom_rebecca_1 #mom naked rebecca sitting done
    
    mom angry "What the fuck happened! Where is Lana?"
    player "Mom it wasn't her fault!"
    rebecca sad "A cyborg!"
    mom scared "A cyborg?"
    player "I saw her too! But I thought she was human - Megan was referring to her as her daughter."
    rebecca sad "I've told you - Megan was working in the cybernetic department. In her twisted mind that cyborg might be her daughter..."
    mom angry "We need to get Lana out of there!"
    rebecca sad "But how?"
    player "We'll think of something."
    call quest_sis_missing_advance_to_talk_earth from _call_quest_sis_missing_advance_to_talk_earth
    jump advance_time
    
label quest_sis_missing_talk_earth:
    hide screen station_rooms
    player "This is Greg, come in!"
    male "Hi Greg, What's up?"
    player "They've got Lana..."
    male "What? Wait... Lana was the young one, your sister?"
    player "Yes."
    male "Who's got her?"
    player "M.A.L. ... and the others..."
    male "What others?"
    player "There are other people on the station... You don't know, do you?"
    male "No... Do you know who they are?"
    player "I'm pretty sure one of them is Jack."
    male "Your dad?"
    player "My step dad... and Lana's father."
    male "Who else?"
    player "There is a woman named Megan..."
    male "Big boobs, nice ass, red hair?"
    player "You know her?"
    male "I've told you - I saw the profiles of all the women on the station. She was working in the cybernetics unit, developing some sort of humanoid robots or something, right?"
    player "She succeeded in that - the one that captured Lana was a cyborg."
    male "A cyborg? You mean a fusion between a living organism and a robot?"
    player "I don't know... She looked alive but then Rebecca fired on her and her skin was gone, revealing a robot inside."
    male "Rebecca... is this the other chick, who's with you on the station?"
    player "Yes."
    male "And what do you expect me to do about it?"
    player "Help us free Lana."
    male "No. It's too risky!"
    player "We have to try!"
    male "It's too risky for us. What if M.A.L. takes this as an attack on the station and fires the nukes?"
    player "We just need the plans for the station, so we can get to where they are keeping her."
    male "Good luck with that! The station's plans are classified. Even I don't have access to them."
    player "But you must know someone, who can access them?"
    male "I do, but they don't work for free and the last time I checked you don't have money."
    player "No but we can earn you money."
    male "Meaning?"
    player "We can put some shows that will make your viewers pay whatever you ask them for it."
    male "Will the women agree to do it?"
    player "I'm sure Rebecca will."
    male "We've seen enough of her, what our viewers really want is your mom."
    male "The blowjob you got from her in the morning when your sis was captured made us thousands!"
    player "{i}I knew it! She was sucking my cock after Lana left!{/i}"
    player "Right? Imagine how much money you can make if she is willing to do more!"
    male "So... make her do more and we can talk. Over and out!"
    call quest_sis_missing_advance_to_talk_rebecca from _call_quest_sis_missing_advance_to_talk_rebecca
    jump advance_time
    
#phase 2 talk
label quest_sis_missing_talk_rebecca:
    hide screen station_rooms
    player "Hi Rebecca!"
    rebecca "Hi Greg!"
    player "Listen, I talked with that guy from Earth and they are willing to help..."
    
    scene beach_rebecca_23 #rebecca sitting done
    
    rebecca "Really? How?"
    player "He is willing to give us the plans for the station, so we can plan a rescue for Lana."
    rebecca happy "That's really good news!"
    player "There is a catch..."
    rebecca "Of course there is..."
    player "The plans are classified and we need to pay to get them."
    rebecca "Pay? But we don't have any money."
    player "We don't but there are people on Earth willing to give them money for what we do here."
    rebecca happy "Of course! The pervs!"
    rebecca flirting "So what do they want me to do to earn the money?"
    player "Well... The thing is..."
    rebecca flirting "Spit it out, Greg! You know I would do anything!"
    player "That's the problem - you pretty much have done almost everything already."
    player "They... they want my mom."
    
    scene beach_rebecca_24 #rebecca sitting angry done
    
    rebecca angry "What?"
    player "He said that the users were constantly asking when my mom will do something more..."
    rebecca angry "Asking? How?"
    player "He didn't say... maybe they have a forum or something... anyway, we need to make her do it if we want help from Earth."
    
    scene beach_rebecca_25 #rebecca seductive done
    
    rebecca flirting "Are you sure I can't be convincing enough?"
    player "I know you can be, but the viewers..."
    rebecca flirting "So they have seen everything we did here as well as what we have done in the bedroom?"
    player "Yeah, they have access to those rooms..."
    rebecca flirting "Which means that they have seen me giving you blowjobs, handjobs and you fucking my ass..."
    player "I guess so..."
    
    scene beach_rebecca_26 #rebecca fj greg pants done
    
    rebecca flirting "Lana said that you enjoyed what she did with you in the VR bar at night."
    player "I did enjoy it!"
    rebecca flirting "You want me to do something like that too?"
    player "Would you?"
    rebecca flirting "You know I would!"
    
    scene beach_rebecca_27 #rebecca fj rebecca naked done
    
    rebecca flirting "You like feet, don't you?"
    player "Oh, yes!"
    rebecca flirting "I can see that!"
    rebecca flirting "So, what else do you like?"
    
    scene beach_rebecca_28 #rebecca bj done
    
    rebecca flirting "I know! How about something new that you couldn't have gotten from Lana?"
    player "You do?"
    rebecca flirting "What's even better than a blowjob and Lana lacks the 'equipment' to give it?"
    player "What?"
    rebecca flitring "Lay down..."
    
    scene beach_rebecca_29 #rebecca tj done
    
    rebecca flirting "This!"
    player "Oh yeah!"
    rebecca flirting "Do you think it's better?"
    player "So much better!"
    rebecca flirting "This way when you cum, it will get both on my face and my tits!"
    player "I'm close..."
    rebecca flirting "Don't hold back! Cover me in your cum!"
    
    scene beach_rebecca_30 #rebecca cum done
    
    rebecca flirting "So hot..."
    player "You are amazing!"
    rebecca flirting "Do you think your mom will do something like that?"
    player "I doubt it, but we have to convince her to do something..."
    rebecca flirting "Let's talk at dinner..."
    
    call quest_sis_missing_advance_to_dinner from _call_quest_sis_missing_advance_to_dinner
    jump advance_time
    
#phase 3 auto
label quest_sis_missing_dinner:
    rebecca sad "Amelia... we need to talk..."
    mom "About what?"
    rebecca sad "I'm worried about Lana and we need to do something fast!"
    mom "But we don't even know where they are holding her."
    player "What if there is a way for us to find out?"
    mom "Right! Your connection!"
    player "No mom... They have probably turned off the cameras already and even if they didn't, we still can't know where exactly is that."
    mom "How then?"
    rebecca sad "You won't like it..."
    mom "It doesn't matter if I like it or not - we need to do whatever it takes to help Lana!"
    player "Earth can help us..."
    mom angry "Those cowards won't lift their finger to do anything to help us! We've already tried that!"
    player "Officially... not. But there are few of them down there that are willing to help."
    rebecca "Unfortunately they are asking for money..."
    mom angry "Money? Those bastards should know that we don't have any!"
    player "..."
    rebecca "..."
    mom angry "What?"
    player "They are operating a business on the station, that we can help make more money for them..."
    mom happy "So, if we can do that, we have to in exchange for their help with freeing Lana!"
    mom "... Wait, why did you tell me that I won't like it?"
    player "The business is..."
    rebecca "Oh, come on! It's porn."
    mom angry "What?"
    rebecca "They stream a few cam feeds from the station to the pervs on Earth, and they pay them for the access."
    mom angry "Wait, which cams exactly?"
    player "The bedroom and the VR room..."
    mom angry "Oh my God! They have been watching me in the shower and..."
    rebecca "And whatever it was that you were doing alone in the room."
    player "Mom, we need to do this for Lana!"
    mom angry "How long have you known about this?"
    player "Pretty much from day one..."
    mom sad "Greg... Why didn't you tell me?"
    player "We needed their help... They were the ones that helped us with setting up the VR room."
    rebecca "Amelia, please! It's not Greg's fault. He wanted Lana to feel better being locked up on this station."
    mom "I enjoyed the beach too, but if I knew it was in exchange for that..."
    rebecca sad "What's done is done. What matters is what we do now! My daughter is held against her will somewhere on the station and if this is the only way for us to help her..."
    mom sad "She is my daughter too! I looked after her for years, so please don't make it sound like you are the only one that cares about her!"
    player "We all do! That's why we need to act fast!"
    mom "I'll think about it..."
    rebecca sad "Please do..."
    call quest_sis_missing_advance_to_mom_shower from _call_quest_sis_missing_advance_to_mom_shower
    jump advance_time
    
#phase 4 mom shower
label quest_sis_missing_mom_shower:
    mom "Please turn around so I can get dressed!"
    player "Don't you want me to go outside?"
    mom happy "No need for that, but please promise you won't peek!"
    player "I promise!"
    
    scene bedroom_window_1 #done
    
    player "{i}Usually mom wants me to wait outside for her to get dressed...{/i}"
    player "{i}I wonder what has changed!{/i}"
    mom happy "Greg, I need your help with something!"
    
    scene bedroom_mom_8 #mom topless done
    
    mom happy "I'm thinking of resting at the beach for a bit, but I can't put my swimsuit on."
    mom flirting "Can you help me with that?"
    player "Of course mom! Turn around!"
    
    scene bedroom_mom_9 #mom back suit tie done
    
    mom flirting "Hmmm..."
    mom flirting "What's that poking me?"
    player "Nothing mom!"
    
    scene bedroom_mom_10 #mom hold dick done
    
    mom flirting "That's a big nothing!"
    player "I'm sorry mom..."
    mom flirting "Don't be sorry! If anything it's flattering that you find me attractive!"
    mom flirting "Do you think I'm still sexy?"
    player "Yes mom! You look amazing!"
    mom flirting "Do you want to do something about your situation?"
    player "You mean I... With you in the room?"
    mom flirting "You are right!"
    mom flirting "It will be rude just to stay here and look at you while you do all the work!"
    
    scene bedroom_mom_11 #mom done
    
    mom flirting "I should help!"
    mom flirting "Oh my, it's been so long since I had someone in me..."
    
    scene bedroom_mom_15 #mom done
    
    mom flirting "What about we help each other out?"
    player "Don't you think it's wrong?"
    
    scene bedroom_mom_12 #mom doggy done
    
    mom flirting "Rebecca is right - Earth taboos have no place here!"
    mom flirting "Especially with no other men around... I have needs too!"
    
    scene bedroom_mom_13 #mom doggy next frame dome
    
    $renpy.pause()
    
    scene bedroom_mom_12
    
    $renpy.pause()
    
    scene bedroom_mom_13
    
    $renpy.pause()
    
    scene bedroom_mom_12
    
    player "Mom... I'm cumming!"
    mom flirting "Yes! Cum!"
    
    scene bedroom_mom_14 #mom cum ass done
    
    mom flirting "Did I really turned you on so much?"
    player "Oh yes! You are the sexiest woman I have ever seen, mom!"
    mom flirting "There goes my plan to go to the beach... Now I have to wash again..."
    call quest_sis_missing_advance_to_talk_breakfast from _call_quest_sis_missing_advance_to_talk_breakfast
    jump advance_time
    
#phase 5 auto breakfast
label quest_sis_missing_talk_breakfast:
    rebecca sad "Amelia, please! We have to help Lana!"
    mom happy "We might have already done that..."
    rebecca "What? When?"
    mom flirting "This morning."
    rebecca "I thought I heard something coming from your room..."
    mom happy "I hope we gave them a good enough show, so we don't have to repeat that."
    player "No?"
    mom "No. I'm doing this for Lana and once she is free, I intend to cut all connections to Earth!"
    rebecca "Fair enough. Once Lana is free, we can discuss it."
    mom "There is nothing to discuss. We are being used by them in return for what? A beach?"
    player "Let's just hope that they will help us now."
    call quest_sis_missing_advance_to_talk_earth_again from _call_quest_sis_missing_advance_to_talk_earth_again
    jump advance_time
    
#phase 6 terminal
label quest_sis_missing_talk_earth_again:
    hide screen station_rooms
    scene comm_rebecca_1 #done
    
    rebecca "Wait, we should call your mom!"
    
    scene comm_mom_rebecca_1 #done
    
    mom "Are you going to talk to them?"
    rebecca "Amelia, they don't know we are here, let's keep it that way."
    rebecca "And remember - they have no idea who I am, so let's not tell them that either!"
    player "Come in! This is Greg!"
    male "I wondered when you're gonna call!"
    male "By the way, do you know where is your mom? She's not in the bedroom or in the VR room..."
    player "Probably checking the life support systems."
    player "Anyway, I want the plans."
    male "I think we already discussed this!"
    player "Wasn't the morning show enough?"
    male "What? Of course not!"
    mom angry "{i}(whispering) Those bastards!{/i}"
    rebecca "{i}Shhh!{/i}"
    player "But you said..."
    male "I said we need to get enough money to pay for the plans, and you can't possibly think that we can earn that much with just one show!"
    player "Now what?"
    male "Now we use what we have for advertisement!"
    male "Each show will bring more customers which means more money!"
    player "But it was hard enough to convince her to do that one!"
    male "This is your problem, not mine! Last time I checked, it was you who needed those plans, not me!"
    player "You need to help too!"
    male "We already cranked up the power in the bedroom to the highest possible setting..."
    mom "{i}(whispering) What is he talking about?{/i}"
    rebecca "{i}(whispering) I'll tell you later...{/i}"
    male "We'll send you blueprints for some sexy clothes for the two of them!"
    male "They would fit some master/slave roleplay."
    player "I'll see what I can do."
    male "Over and out!"
    
    scene comm_mom_rebecca_2 #done
    
    mom "What the fuck was he talking about?"
    rebecca "The military did some research on behavior modification..."
    player "And those guys put the technology to use in the bedroom."
    mom "Is this why I have been so horny lately?"
    rebecca happy "No Amelia, they just remove your inhibitions about the consequences of your actions."
    rebecca flirting "You are more likely to give in to your desires, but those are still yours."
    mom embarassed "No, this can't be true - I don't have any sexual desires for my son!"
    rebecca flirting "Sure..."
    player "Anyway, we should make the clothes those guys sent and discuss what we will do next!"
    rebecca "Leave that to me! We'll talk at breakfast..."
    rebecca flirting "Sweet dreams... to both of you!"
    call quest_sis_missing_advance_to_setup_scene from _call_quest_sis_missing_advance_to_setup_scene
    jump sleep
    
#phase 7 auto breakfast
label quest_sis_missing_setup_scene:
    rebecca "I've got the clothes."
    
    scene mess_hall_mom_rebecca_2 #rebecca holding chain done
    
    rebecca flirting "This is your slave outfit!"
    mom angry "What? You must be kidding me!"
    rebecca flirting "Don't you like it?"
    mom "I like it, but this will be your slave outfit."
    rebecca "As long as you agree to do this, I don't really care which role I'll play."
    mom "Don't sound like you are the victim here! We are doing this for Lana."
    rebecca "Exactly!"
    player "So you are both up for this? When are we doing the show?"
    mom "We? No, no, no - there is no 'we' in this. It will be me and Rebecca only!"
    rebecca flirting "How about after my shower at noon?"
    mom "OK... if everyone is done eating, I'll recycle the leftovers."
    
    scene mess_hall_mom_rebecca_3 #mom turn away rebecca flirting done
    
    rebecca flirting "{i}(whispering) Meet me at the Med Bay at 11:00...{/i}"
    call quest_sis_missing_advance_to_med_bay from _call_quest_sis_missing_advance_to_med_bay
    jump advance_time
    
#phase 8 auto
label quest_sis_missing_med_bay:
    hide screen station_rooms
    if not station.get_room("med_bay").player:
        player "{i}Rebecca said to meet her in the mad bay, I should go there now.{/i}"
        $station.get_room(player_location).player = False
        $station.get_room("med_bay").player = True
        $player_location = "med_bay"
        
    scene med_bay_rebecca_2 #done
    
    rebecca "Oh, here you are!"
    player "What did you want to talk about?"
    rebecca "Do you want to watch the show?"
    player "Of course, but I doubt my mom will let me..."
    rebecca "Of course she won't... but maybe I can help with that"
    
    scene med_bay_rebecca_4 #done
    
    rebecca flirting "We just need to be extra careful for you not to cum!"
    
    scene med_bay_rebecca_5 #done
    
    $renpy.pause()
    
    scene med_bay_rebecca_6 #done
    
    $renpy.pause()
    
    scene med_bay_rebecca_5 #done
    
    $renpy.pause()
    
    scene med_bay_rebecca_6 #done
    
    $renpy.pause()
    
    scene med_bay_rebecca_5 #done
    
    $renpy.pause()
    
    scene med_bay_rebecca_4 #done
    
    rebecca flirting "I can feel your cock throbbing in my mouth. It's time to stop!"
    player "Just a bit more, please!"
    rebecca flirting "No. You are too close and I'm almost late for the show!"
    rebecca flirting "Sit back here and enjoy!"
    call quest_sis_missing_advance_to_lesb_show from _call_quest_sis_missing_advance_to_lesb_show
    jump advance_time
    
#phase 9 auto
label quest_sis_missing_lesb_show:
    hide screen station_rooms
    scene bedroom_mom_rebecca_2 #reb naked mom angry done
    
    rebecca "What are you doing here?"
    mom angry "Listen bitch! You leave my son alone!"
    rebecca scared "What?"
    mom angry "I know you have been fucking him and this stops now!"
    
    scene bedroom_mom_rebecca_3 #mom hit reb done
    
    mom angry "Do you understand?"
    rebecca sad "Yes."
    mom angry "And you will address me as 'mistress'!"
    rebecca sad "Yes... mistress..."
    mom "Good!"
    mom "You will learn your place on this station!"
    
    scene bedroom_mom_rebecca_4 #mom hold chain done
    
    mom "From now on, you will wear this and you will obey my every command!"
    rebecca sad "Yes..."
    mom angry "Do I need to slap you again, girl?"
    rebecca sad "No... mistress..."
    mom "Good! Now get dressed!"
    
    scene bedroom_mom_rebecca_5 #reb sad in chain done
    
    rebecca sad "..."
    mom "Now he will know what kind of slut you are!"
    mom happy "If only he could watch what I'm about to do to you..."
    
    scene bedroom_mom_rebecca_6 #done
    
    rebecca scared "What..."
    mom "Do I need to gag you?"
    rebecca "... no..."
    mom "Then speak only when spoken to!"
    mom flirting "We will put your mouth to use soon enough."
    
    scene bedroom_mom_rebecca_7 #done
    
    mom flirting "I can see why my son is always staring at your ass!"
    mom flirting "Did he already get to fuck it?"
    rebecca "... yes..."
    mom flirting "Speak louder!"
    rebecca "Yes."
    
    scene bedroom_mom_rebecca_8 #done
    
    mom flirting "Now I will enjoy it!"
    rebecca flirting "Oooh!"
    mom flirting "Did you say something?"
    rebecca flirting "..."
    mom flirting "I think you are enjoying this a bit too much."
    mom flirting "And we are not here for you to enjoy yourself!"
    mom flirting "We are here for me to enjoy myself!"
    
    scene bedroom_mom_rebecca_9 #reb lick mom standing done
    
    mom flirting "That's it!"
    mom flirting "You seem to have experience with licking pussy, don't you?"
    rebecca flirting "Yes, mistress!"
    
    scene bedroom_mom_rebecca_10 #mom lay bed spread legs done
    
    mom flirting "Show me how good you are at that!"
    
    scene bedroom_mom_rebecca_11 #mom bed reb lick done
    
    mom flirting "Oh, that's good!"
    mom flirting "I just hope Greg doesn't see me like that!"
    
    menu:
        "Go to the bedroom":
            player "{i}I'll just pretend that I walk-in on them by accident...{/i}"
            jump quest_sis_missing_lesb_show_threesome
        "Stay here and just watch":
            jump quest_sis_missing_lesb_show_continue
            
label quest_sis_missing_lesb_show_threesome:
    scene door_1 #done
    
    player "Mom, I wanted to ask you..."
    
    scene bedroom_mom_rebecca_12 #same as 11 reb mom look camera done
    
    player "What are you doing, mom!"
    mom embarassed "Greg, it's not what you think..."
    player "It's not? And what is Rebecca wearing?"
    rebecca "Your mom..."
    mom angry "Silence! I haven't given you the permission to talk"
    rebecca "..."
    
    scene bedroom_mom_rebecca_13 #mom standing reb four legs done
    
    mom "I know what you two were doing behind my back!"
    player "And what exactly do you know?"
    mom angry "I know you have been fucking her!"
    mom angry "She wanted to take my son away from me!"
    player "Mom, this is not true..."
    
    scene bedroom_mom_rebecca_14 #mom spread reb ass done
    
    mom flirting "It's not? Is it not true, that you were fucking her ass?"
    player "..."
    mom flirting "What is it that she can give you and I can't?"
    player "You are not suggesting..."
    
    scene bedroom_mom_rebecca_15 #mom show ass done
    
    mom flirting "It's exactly what I'm suggesting!"
    mom flirting "Don't you want to have my ass instead?"
    rebecca "Amelia, he's too big for you!"
    mom angry "Nobody asked you!"
    mom flirting "But maybe you are right... Slave, make my pussy wet, so he can enter more easily!"
    
    scene bedroom_mom_rebecca_16 #reb lick mom done
    
    mom flirting "That's it! Now put his cock in your mouth! And don't you dare make him cum!"
    
    scene bedroom_mom_rebecca_17 #reb blow greg done
    
    player "Oh, that's so good!"
    mom flirting "Good? This is nothing compared to what's coming next!"
    mom flirting "Move to the other side of the bed - I want you to enjoy the view."
    
    scene bedroom_mom_rebecca_18 #reb mom blow greg done
    
    mom flirting "Don't you think this is better?"
    player "Oh yes!"
    mom flirting "Do you like the view?"
    player "So very much!"
    rebecca flirting "Somehow I don't think he means the planet below, mistress! Do you think he's ready?"
    
    scene bedroom_mom_rebecca_19 #greg fuck mom pussy done
    
    mom flirting "He most definitely is!"
    mom flirting "You were right! He couldn't possibly fit in my ass!"
    player "We can try..."
    mom flirting "Don't you like fucking my pussy?"
    
    scene bedroom_mom_rebecca_20 #greg fuck mom pussy done
    
    player "Of course I do!"
    mom flirting "Look at that slut! All she ever thinks of is sex!"
    mom flirting "Do you want to cum on her face?"
    player "May I?"
    mom flirting "Of course you may! Girl, come here!"
    
    scene bedroom_mom_rebecca_21 #reb facial mom near done
    
    mom flirting "Oh, it's so much!"
    mom flirting "Come here, girl!"
    
    scene bedroom_mom_rebecca_22 #reb facial mom kiss done
    
    mom flirting "Tastes good too..."
    mom flirting "Now leave, both of you! And don't you even think about fucking him or I will punish you!"
    
    $global_events.greg_threesome = True
    call quest_sis_missing_advance_to_dinner_talk from _call_quest_sis_missing_advance_to_dinner_talk
    jump advance_time
    
label quest_sis_missing_lesb_show_continue:
    player "{i}It might be best not to bother them...{/i}"
    
    scene bedroom_mom_rebecca_23 #reb lick mom bed done
    
    mom flirting "Ohh, I like that!"
    mom flirting "How many girls did you have before?"
    rebecca flirting "Many."
    
    scene bedroom_mom_rebecca_24 #reb mom clit done
    
    mom flirting "Yes, that's it!"
    mom flirting "Lick my clit..."
    mom flirting "Make me cum!"
    
    scene bedroom_mom_rebecca_25 #reb mom org done
    
    mom flirting "Ahh, I'm cumming!"
    
    scene bedroom_mom_rebecca_26 #reb face squirt done
    
    rebecca flirting "Wow, I didn't know you had it in you!"
    mom flirting "Me neither..."
    mom flirting "Now leave... I need to catch my breath... And don't you even think about fucking Greg, or I will punish you again..."
    rebecca flirting "... You promise?"
    
    screen med_bay_1
    player "{i}Wow... I didn't know mom had it in her...{/i}"
    $global_events.greg_threesome = False
    call quest_sis_missing_advance_to_dinner_talk from _call_quest_sis_missing_advance_to_dinner_talk_1
    jump advance_time
    
#phase 10 auto dinner
label quest_sis_missing_dinner_talk:
    rebecca "I guess that should be enough for them to get the plans..."
    player "It was awesome!"
    if (global_events.greg_threesome):
        mom sad "Greg, please... I did what I had to do to help Lana..."
    else:
        mom angry "What? You saw that?"
        player "I..."
        mom angry "Rebecca, did you do something with Greg, just before we started?"
        rebecca happy "It was just a blowjob, it's not a big deal..."
        mom "I don't want to hear about it!"
        mom "Just so you know I did that only to help Lana!"
    rebecca happy "If you didn't enjoy it, I think you must be the greatest actor that I have ever seen!"
    player "So... did you enjoy it?"
    mom "I... I don't know."
    rebecca "Greg, your mom is feeling uncomfortable talking about this, so please stop bothering her."
    mom "Thank you, Rebecca..."
    rebecca "You're welcome..."
    rebecca happy "... mistress!"
    mom angry "Oh, fuck you!"
    rebecca happy "Sorry, I couldn't help it!"
    rebecca "But... thank you for doing this for my daughter... I mean it!"
    mom sad "I just hope she's OK..."
    call quest_sis_missing_advance_to_get_plans from _call_quest_sis_missing_advance_to_get_plans
    jump advance_time
    
label quest_sis_missing_get_plans:
    hide screen station_rooms
    player "{i}I should get mom and Rebecca here first...{/i}"
    
    scene comm_mom_rebecca_1 #done
    
    player "This is Greg from Antares..."
    player "Earth, come in..."
    male "Greg! My man!"
    mom "{i}(whspering) They seem excited...{/i}"
    male "That was amazing!"
    if (global_events.greg_threesome):
        male "Your mom having a threesome with you and that other girl made so much profit for us!"
    else:
        male "Our clients really liked your mom dominating that other girl!"
    rebecca angry "{i}(whispering) So I'm just 'that other girl'...{/i}"
    player "So you can send us the plans for the station now?"
    male "Uploading them now..."
    player "Wait, I thought you had to bribe some people first..."
    male "Yeah... I... I never doubted you, so I payed the with my own money right after you asked me!"
    player "Right... OK, we received the plans, I need to cut the link."
    male "Looking forward to working with you again!"
    
    scene comm_mom_rebecca_2 #done
    
    mom angry "That bastard!"
    mom angry "He had the plans and could send them right after we asked!"
    rebecca "That's not important now - let's look at them and think of a way to rescue Lana."
    player "Yep - let's discuss that at breakfast."
    
    call quest_sis_missing_advance_to_make_plan from _call_quest_sis_missing_advance_to_make_plan
    jump advance_time