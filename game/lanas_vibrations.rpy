label help_lanas_vibrations:
    player "{i}[quest_lanas_vibrations.help]{/i}"
    if quest_lanas_vibrations.finished:
        player "{i}There is nothing more that can be done about this in the current version of the game{/i}"
    jump wait
    
#phase 0 terminal
label start_quest_lanas_vibrations:
    $quest_lanas_vibrations.active = True
    $quest_lanas_vibrations.location = "mess_hall"
    $quest_lanas_vibrations.alone = True
    $quest_lanas_vibrations.help = "I should check with the energy processor if it can make what something more than just food and clothes."
    $talk_with_terminal.add_topic("Check for more stuff", "quest_lanas_vibrations_check_processor", quest_lanas_vibrations, 0)
    return

#phase 1 terminal
label quest_lanas_vibrations_advance_to_check_engineering:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.location = "life_support"
    $quest_lanas_vibrations.alone = True
    $quest_lanas_vibrations.help = "I don't think the processor is capable of making anything else, but let's check to be sure."
    $talk_with_terminal.add_topic("Try to program it for electronics", "quest_lanas_vibrations_check_engineering", quest_lanas_vibrations, 1)
    return
    
#phase 2 talk
label quest_lanas_vibrations_advance_to_tell_lana:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.location = "shared_beds"
    $quest_lanas_vibrations.sis_location = "shared_beds"
    $quest_lanas_vibrations.alone = True
    $quest_lanas_vibrations.help = "I should tell Lana, that I won't be able to make the vibrator."
    $talk_with_sis.add_topic("Tell her about the vibrator", "quest_lanas_vibrations_tell_lana", quest_lanas_vibrations, 2)
    return
    
#phase 3 auto
label quest_lanas_vibrations_advance_to_wait_for_rebecca:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.help = "I can't program the processor by myself and I can't ask mom for help..."
    return
    
#phase 4 talk
label quest_lanas_vibrations_advance_to_talk_rebecca:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.location = "life_support"
    $quest_lanas_vibrations.rebecca_location = "life_support"
    $quest_lanas_vibrations.alone = True
    $quest_lanas_vibrations.help = "Maybe I can ask Rebecca for help with that!"
    $talk_with_rebecca.add_topic("Ask for help", "quest_lanas_vibrations_talk_rebecca", quest_lanas_vibrations, 4)
    return
    
#phase 5 talk
label quest_lanas_vibrations_advance_to_spend_power:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.location = "life_support"
    $quest_lanas_vibrations.rebecca_location = "life_support"
    $quest_lanas_vibrations.alone = True
    $quest_lanas_vibrations.help = "We need at least 500 kWh stored in the batteries to charge the suit."
    if (energy >= 500):
        jump quest_lanas_vibrations_spend_power
    else:
        call quest_lanas_vibrations_add_topic_spend_power from _call_quest_lanas_vibrations_add_topic_spend_power
    return
        
label quest_lanas_vibrations_add_topic_spend_power:
    $talk_with_rebecca.add_topic("Charge the suit", "quest_lanas_vibrations_spend_power", quest_lanas_vibrations, 5)
    return
    
#phase 6 auto
label quest_lanas_vibrations_advance_to_meet_midnight:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.req_day = day + 1
    $quest_lanas_vibrations.day_mode = "at_least"
    $quest_lanas_vibrations.req_clock = 0
    $quest_lanas_vibrations.clock_mode = "exactly"
    $quest_lanas_vibrations.help = "Rebecca told me to meet her at the engineering section at midnight."
    return
    
#phase 7 auto
label quest_lanas_vibrations_advance_to_breakfast:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.req_clock = 9
    $quest_lanas_vibrations.clock_mode = "exactly"
    $quest_lanas_vibrations.req_day = day
    $quest_lanas_vibrations.day_mode = "at_least"
    $quest_lanas_vibrations.help = "Let's not tell the others about Rebecca's trip outside the section."
    return
    
#phase 8 talk
label quest_lanas_vibrations_advance_to_spoils:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.location = "vr_room"
    $quest_lanas_vibrations.rebecca_location = "vr_room"
    $quest_lanas_vibrations.help = "I need to talk to Rebecca to find out what did she manage to recover from her trip outside the section."
    $talk_with_rebecca.add_topic("Ask about her trip", "quest_lanas_vibrations_spoils", quest_lanas_vibrations, 8)
    return
    
#phase 9 auto
label quest_lanas_vibrations_advance_to_mom_disappear:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.req_day = day + 1
    $quest_lanas_vibrations.day_mode = "exactly"
    $quest_lanas_vibrations.req_clock = 7
    $quest_lanas_vibrations.clock_mode = "exactly"
    $quest_lanas_vibrations.help = "Rebecca said she has all the electronics required for a vibrator."
    return
    
#phase 10 auto
label quest_lanas_vibrations_advance_to_breakfast_no_mom:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.req_clock = 9
    $quest_lanas_vibrations.clock_mode = "exactly"
    $quest_lanas_vibrations.help = "Mom is missing and by 9 o'clock we will know for sure that the suit is out of power."
    return
    
#phase 11 terminal
label quest_lanas_vibrations_advance_to_make_vibrator:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.location = "life_support"
    $quest_lanas_vibrations.alone = True
    $quest_lanas_vibrations.help = "Now that I have the electronics from Rebecca, I can make a vibrator for Lana."
    $talk_with_terminal.add_topic("Make a vibrator (-100kWh)", "quest_lanas_vibrations_make_vibrator", quest_lanas_vibrations, 11)
    return
    
#phase 12 talk
label quest_lanas_vibrations_advance_to_give_vibrator:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.location = "vr_room"
    $quest_lanas_vibrations.sis_location = "vr_room"
    $quest_lanas_vibrations.help = "Let's give the vibrator to Lana while she is at the beach."
    $talk_with_sis.add_topic("Give the vibrator", "quest_lanas_vibrations_give_vibrator", quest_lanas_vibrations, 12)
    return
    
#phase 13 auto
label quest_lanas_vibrations_advance_to_shower:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.help = "Lana said to meet her while she's taking a shower."
    return
    
#phase 14
label quest_lanas_vibrations_finish:
    $quest_lanas_vibrations.reset()
    $quest_lanas_vibrations.advance_phase()
    $quest_lanas_vibrations.help = "Now Lana has her vibrator and she 'paid' what she had promised and then more..."
    $quest_lanas_vibrations.finished = True
    return

#phase 0 terminal
label quest_lanas_vibrations_check_processor:
    hide screen station_rooms
    player "{i}Hmmmm...{/i}"
    player "{i}Just as I thought - nothing more than basic food and clothes in the program...{/i}"
    player "{i}Maybe the processor is not capable of making anything else or there was no need to program it until now.{/i}"
    player "{i}Maybe I should try to program it via the terminal in the engineering room...{/i}"
    call quest_lanas_vibrations_advance_to_check_engineering from _call_quest_lanas_vibrations_advance_to_check_engineering
    jump advance_time
    
#phase 1 terminal
label quest_lanas_vibrations_check_engineering:
    hide screen station_rooms
    player "{i}OK, let's try to find out if the processor is capable of producing electronics...{/i}"
    player "{i}...{/i}"
    player "{i}What if...{/i}"
    player "{i}No, that won't work...{/i}"
    player "{i}...{/i}"
    player "{i}......{/i}"
    player "{i}.........{/i}"
    player "{i}What a waste of time! Either I lack the knowledge to make it, or it's just not possible!{/i}"
    player "{i}Whatever the reason, I won't be able to make a vibrator for Lana. I'd better go and tell her.{/i}"
    call quest_lanas_vibrations_advance_to_tell_lana from _call_quest_lanas_vibrations_advance_to_tell_lana
    jump advance_time
    
#phase 2 talk
label quest_lanas_vibrations_tell_lana:
    hide screen station_rooms
    player "Hey!"
    sis "Oh, hi Greg!"
    player "About your request..."
    sis flirting "You mean the vibrator?"
    player "Yes... well... I don't think it's possible."
    sis "But I thought you can program the processor to make anything you like?"
    player "Only basic stuff. Not electronics."
    sis "You are not telling me this so you can try and bargain a better deal, right?"
    player "No, I mean it. If I could make anything with the processor, I'd start with some weapons, so we can defend ourselves if M.A.L. manages to override the lock."
    player "Unfortunately I can't. And I don't think it's because I lack the knowledge to do it. I think it's impossible to make it with that machine."
    sis sad "I see... would you still try?"
    player "I tried! The best I can do is some basic stuff... like a dildo."
    sis "A dildo?"
    sis "Let me explain something. Drop your pants!"
    player "What?"
    sis flirting "You heard me! Drop 'em!"
    scene shared_beds_sis_17
    sis flirting "A dildo, compared to a vibrator is like comparing this..."
    scene shared_beds_sis_18
    sis flirting "To this..."
    sis flirting "Which would you prefer to get in return for your services?"
    scene shared_beds_sis_17
    player "The blowjob of course!"
    sis "Of course!"
    call quest_lanas_vibrations_advance_to_wait_for_rebecca from _call_quest_lanas_vibrations_advance_to_wait_for_rebecca
    if (global_events.rebecca):
        jump quest_lanas_vibrations_rebecca_joins
    jump advance_time
    
label quest_lanas_vibrations_rebecca_joins:
    scene shared_beds_rebecca_sis_5
    rebecca angry "What's going on here?"
    player "We were just..."
    rebecca angry "Just... what? Why is Lana holding your dick?"
    sis "Mom..."
    rebecca angry "Quiet! I see what's going on here!"
    scene shared_beds_rebecca_sis_6
    rebecca flirting "You want to keep his huge dick all to yourself!"
    sis "What?"
    rebecca happy "Haven't you learn that sharing is caring?"
    rebecca happy "Don't you care about your mom?"
    sis "Mom, stop it!"
    scene shared_beds_rebecca_sis_7
    rebecca flirting "Stop? Oh, dear, we have just began..."
    rebecca happy "Or would you like me to go to Amelia and tell her that her step daughter likes to hold her son's dick?"
    player "No, please don't!"
    rebecca flirting "So do as I say and this can be our little secret!"
    sis "Mom, he's my brother..."
    rebecca happy "Step brother. And that doesn't seem to bother you."
    rebecca flirting "And it sure as hell doesn't bother me either."
    rebecca flirting "Now show me what you were doing when I entered the room."
    scene shared_beds_rebecca_sis_8
    sis "Nothing. I was just trying to prove a point."
    sis "Isn't that right, Greg?"
    player "Ummm... sort of..."
    rebecca happy "So, did my daughter managed to convince you?"
    rebecca flirting "Because judging by the fact that you're still hard, I don't think she has finished that task."
    rebecca flirting "I think I can help her with that - I'm her mother after all."
    rebecca flirting "Let me change my suit into something more... convincing."
    scene shared_beds_rebecca_sis_9
    player "Oh, wow!"
    rebecca happy "I knew you'd like that!"
    sis flirting "Oh, he definitely likes it!"
    sis flirting "I can feel him getting even harder!"
    rebecca flirting "Is that right? You like having your dick held by your sister while her mother is in the room in nothing but lingerie?"
    player "I do... You are both hot!"
    scene shared_beds_rebecca_sis_10
    sis flirting "See I told you he was a pervert!"
    rebecca happy "Lana, there is nothing wrong with him enjoying a handjob."
    sis happy "But he made me strip so he can see my breasts! Doesn't this make him a pervert?"
    rebecca flirting "Did you like her tits?"
    player "Of course!"
    scene shared_beds_rebecca_sis_11
    rebecca flirting "What do you think of mine?"
    player "Oh, my!"
    sis flirting "My hand can tell you what he thinks!"
    rebecca flirting "Oh, I think he likes them so much that he wants to spray his cum all over my tits."
    rebecca flirting "Is that right, young man?"
    sis "Ewww! Gross!"
    rebecca flirting "Don't mind her, she doesn't know what she's missing."
    sis "Maybe I do and maybe I just don't like it?"
    rebecca flirting "So stroke him harder and let me have his cum!"
    sis "..."
    scene shared_beds_rebecca_sis_12
    player "Ughhh"
    rebecca flirting "Oh yes!"
    rebecca flirting "It's so much! And it's so warm!"
    rebecca happy "Would you like a taste Lana?"
    sis angry "Ewww! No!"
    rebecca happy "OK, so I'll go wash it!"
    rebecca happy "You two can continue whatever you were talking about."
    sis "I think we're finished."
    $global_events.rebecca_vibrations = True
    call quest_lanas_vibrations_advance_to_talk_rebecca from _call_quest_lanas_vibrations_advance_to_talk_rebecca
    jump advance_time
    
#phase 4 talk
label quest_lanas_vibrations_talk_rebecca:
    hide screen station_rooms
    player "Hey!"
    rebecca "Hey, Greg!"
    player "I want to ask you something..."
    rebecca "What?"
    player "Let's say I need to make some electronics... Can I use the energy processor for that?"
    rebecca "No."
    player "No?"
    rebecca "No."
    rebecca "The processor is designed just for basic stuff like food and clothes."
    if (quest_meet_rebecca.phase >= 9):
        player "But I've seen you use it for other stuff... like the dices for our game and the alcohol you brought with you!"
        rebecca "The dices are just plastic and alcohol is carbohydrates - chemically it's no different than food."
        rebecca "Actually the protein bars that we have every day are more sophisticated than a glass of whiskey."
    player "But what I need is pretty basic too - just a small motor, a simple circuit board and a battery."
    rebecca happy "Aren't a bit too old to be playing with toys?"
    player "It's not... for me."
    rebecca happy "Who then? Your mom or Lana?"
    rebecca happy "I kind of can't imagine them playing with toys either... unless it's not exactly the type of toy I thought it was!"
    rebecca flirting "Is it by any chance a sex toy?"
    player "Yep."
    rebecca happy "Oh, please let this be for your mom! Please!"
    player "It's not."
    rebecca happy "So Lana then..."
    if (global_events.rebecca_vibrations):
        rebecca flirting "Wait! Was this what you two were \"talinkg\" about when I walked on you two and saw her holding your dick?"
        player "Yes. I was trying to explain her that I won't be able to make it... it's just not possible..."
        rebecca flirting "So she thought she can make the processor capable of producing electronics, by giving you a handjob?"
        player "Not exactly. I suggested she should forget about the vibrator and settle for a dildo instead..."
        rebecca flirting "Oh, silly boy... no woman would ever settle for a dildo, if she could have a vibrator!"
        player "{i}If{/i} she could have it. But she can't... the processor can't make it."
    else:
        player "Anyway, it doesn't matter... the processor can't make it."
    rebecca "{i}This{/i} processor can't make it."
    player "Meaning?"
    rebecca "Greg, this is a military research station. There is equipment that can do anything here!"
    player "But we can't get to it, if it's outside this section. If M.A.L.'s bots find us, they will kill us!"
    rebecca "You are right. {i}If{/i} they find us!"
    rebecca "I already managed to sneak past them when I got here. I'm sure I can do that again."
    player "The chameleon suit!"
    rebecca "Yes - the chameleon suit. We can use it to go outside the section and collect supplies or gather intelligence!"
    rebecca "There is one drawback though..."
    player "What?"
    rebecca "It requires a lot of power to activate the cloak."
    rebecca "And it only lasts for a couple of hours."
    call quest_lanas_vibrations_advance_to_spend_power from _call_quest_lanas_vibrations_advance_to_spend_power
    jump advance_time

#phase 5
label quest_lanas_vibrations_spend_power:
    hide screen station_rooms
    player "I think we have 500kWh stored in the battery."
    scene life_support_rebecca_2
    menu:
        "Let's use them!":
            $energy -= 500
            jump quest_lanas_vibrations_charge_suit
        "Not yet.":
            call quest_lanas_vibrations_add_topic_spend_power from _call_quest_lanas_vibrations_add_topic_spend_power_1
            jump advance_time
            
label quest_lanas_vibrations_charge_suit:
    rebecca happy "Nice!"
    player "What are you so happy about?"
    rebecca happy "That I'd go out on a mission!"
    if (global_events.rebecca_vibrations):
        rebecca happy "I've been here for quite a while and I was beginning to think that I was becoming soft."
    rebecca "Anyway, let's charge the suit..."
    scene life_support_rebecca_3
    player "What are you doing?"
    rebecca flirting "I'm not going to wear the suit while it's plugged in!"
    rebecca happy "I might be into some really kinky stuff, but electrocuting myself is not something I want to try."
    if (global_events.rebecca_vibrations):
        rebecca happy "Oh, I was beginning to worry that I was becoming soft, but I guess you can be hard for both of us!"
    else:
        rebecca happy "And what's poking from your pants?"
    player "I'm sorry!"
    rebecca flirting "Don't be!"
    rebecca flirting "I've told you - I'm totally fine with that. Sex is pretty much the only fun you can have on long missions, so all members of the black ops unit are... open minded."
    player "That sounds interesting! Please tell me more!"
    rebecca happy "Maybe later."
    scene life_support_rebecca_4
    rebecca flirting "Right now we have to do something about your \"problem\"!"
    scene life_support_rebecca_5
    player "But my mom and Lana are awake!"
    rebecca flirting "Then we'll have to be very quiet!"
    scene life_support_rebecca_6
    player "Oh, God!"
    scene life_support_rebecca_4
    rebecca flirting "Shhh! We don't want anyone coming here, ruining our fun!"
    scene life_support_rebecca_7
    $renpy.pause()
    scene life_support_rebecca_8
    $renpy.pause()
    scene life_support_rebecca_7
    $renpy.pause()
    scene life_support_rebecca_8
    $renpy.pause()
    scene life_support_rebecca_7
    $renpy.pause()
    scene life_support_rebecca_8
    $renpy.pause()
    scene life_support_rebecca_7
    $renpy.pause()
    scene life_support_rebecca_8
    $renpy.pause()
    scene life_support_rebecca_9
    rebecca happy "You could've warned me!"
    player "You told me to be quiet, so..."
    rebecca flirting "Naughty boy!"
    rebecca "Anyway, the suit is almost charged."
    player "Let's meet here at midnight, so we can do this thing!"
    rebecca "Deal!"
    call quest_lanas_vibrations_advance_to_meet_midnight from _call_quest_lanas_vibrations_advance_to_meet_midnight
    jump advance_time

#phase 6 auto
label quest_lanas_vibrations_meet_midnight:
    hide screen station_rooms
    $rebecca_location = "life_support"
    $station.get_room("life_support").rebecca = True
    $player_location = "life_support"
    $station.get_room("life_support").player = True
    scene life_support_rebecca_1
    rebecca "Good! You are here!"
    player "What's the plan?"
    rebecca "We do it the classic way - I go in, grab whatever I can find and get out before they even know something has happened."
    rebecca "Stealth is essential, so the whole thing must be done in a couple of hours."
    player "Should I wait for you?"
    rebecca "No need. I know what I'm doing - I've been doing this for quite some time."
    player "But how will you get back in?"
    rebecca happy "I've done it before, remember?"
    player "Right!"
    rebecca happy "I can't wait to get out of this section and have some fun!"
    player "Fun? You can get yourself killed!"
    rebecca happy "Then so be it! No one lives forever!"
    player "OK, let's go."
    scene door_rebecca_1
    player "Here is the door... shouldn't we check what's outside?"
    if (quest_meet_rebecca.phase >= 3):
        rebecca "Oh right! We can use your interface with the surveillance system!"
        player "I don't know how to control that... we can use the monitor."
    player "I restored the connection to the camera outside this door when Megan arrived."
    scene corridor_1
    player "All clear."
    scene door_rebecca_1
    rebecca happy "Wish me luck!"
    scene door_rebecca_2
    $renpy.pause()
    scene door_rebecca_1
    player "Be safe!"
    rebecca "I will!"
    scene door_rebecca_3
    scene door_rebecca_4
    scene door_rebecca_5
    rebecca "Open the door!"
    player "Done."
    rebecca "Seal it as soon as I get through!"
    player "Ummm... how should I know when you are through?"
    rebecca happy "Right! You can't see me!"
    rebecca "..."
    rebecca "OK, seal the door!"
    player "... Done!"
    player "{i}She said I shouldn't wait for her... let's go to sleep.{/i}"
    call quest_lanas_vibrations_advance_to_breakfast from _call_quest_lanas_vibrations_advance_to_breakfast
    jump sleep
    
#phase 7 auto
label quest_lanas_vibrations_breakfast:
    hide screen station_rooms
    mom "When I was preparing the breakfast, I noticed that a lot of our energy supply has disappeared."
    mom "Anyone knows something about that?"
    sis "Mom?"
    rebecca "Why do you think I have something to do with that?"
    sis "Because you weren't in our bedroom after midnight!"
    rebecca "OK, I used some of the power to charge my suit and go outside..."
    mom angry "Outside!"
    rebecca "What's the big deal?"
    mom angry "The big deal is that you can't decide for all of us on what we should spend our power supply!"
    rebecca happy "I wasn't the only one involved."
    mom angry "Greg!"
    player "Mom, calm down! We need to know what's going on with the rest of the station."
    rebecca "Exactly - think of it as a reconnaissance mission."
    rebecca "You've been stuck here for [day] days - you need to know what's happening, to be prepared!"
    mom "Of course, but it's not safe to open that door."
    mom "Look what happened the last time we did that!"
    rebecca "You mean Greg having the time of his life with Megan?"
    mom angry "What!"
    rebecca happy "Oops! It was supposed to be a secret!"
    mom angry "Greg, please tell me this isn't true!"
    player "Well..."
    mom angry "I'm disgusted with you!"
    rebecca happy "Oh, come on! Greg is a healthy young man, with whom do you suppose he should satisfy his needs?"
    rebecca happy "You or Lana?"
    mom angry "Shut up!"
    rebecca happy "Don't you want me to tell you what I found out?"
    sis "Of course we do!"
    rebecca "The weird thing is that I've met no bots outside."
    rebecca "No dead bodies either."
    mom "How far did you go?"
    rebecca "I went through some labs and managed to get to some kind of a lift."
    mom "The one that goes down to the hangar?"
    rebecca "I don't think so - I've been through that one."
    mom "So it's either the one that goes up to the command room one or the one that goes down to the storage."
    rebecca "Anyway, there are no bodies, everything is cleaned up."
    mom "Why is this weird?"
    player "M.A.L. shouldn't care if there are a bunch of dead people in the corridors yet it went through all the trouble of clearing them."
    rebecca "Exactly!"
    mom "So basically you learned nothing and wasted so much of our energy reserve."
    rebecca angry "God! You are unbelievable! I risked my life out there, the least I can get is a 'thank you'!"
    mom happy "Nobody asked you to! But seeing you angry might just be worth all the wasted power!"
    rebecca angry "Fuck you! I'm done with the breakfast!"
    call quest_lanas_vibrations_advance_to_spoils from _call_quest_lanas_vibrations_advance_to_spoils
    jump advance_time
    
#phase 8 talk
label quest_lanas_vibrations_spoils:
    hide screen station_rooms
    rebecca "Something on your mind?"
    player "What's it like out there?"
    rebecca "I've told you - the whole station looks deserted. No bots, no bodies... nothing."
    rebecca "And lots of abandoned stuff, just laying around."
    player "Did you manage to find the components?"
    rebecca flirting "Depends..."
    player "Depends? On what?"
    rebecca happy "Depends on what you are willing to do to get them."
    player "Ummm... Anything?"
    rebecca happy "Good! So you'd be happy to fuck Lana on your mother's bed while she is watching you?"
    player "What?!"
    rebecca happy "That bitch made me angry. It's time for her to learn a valuable lesson."
    rebecca happy "You. Don't. Fuck. With. Me."
    player "Anyway - Lana would never agree to that!"
    rebecca flirting "Oh, yes, she will!"
    rebecca flirting "She wants the vibrator bad, right?"
    player "Right."
    rebecca flirting "But she won't have sex with you, because she thinks it's wrong, right?"
    player "Right."
    rebecca flirting "So what if there was such a place on the station that lowers your inhibitions and lets you give in to your desires?"
    player "The bedroom!"
    rebecca happy "The bedroom."
    player "Deal!"
    rebecca flirting "Not so fast!"
    rebecca flirting "First I need to make sure your cock is worthy of entering my daughter!"
    player "You mean... you want me to fuck you?"
    rebecca flirting "Exactly"
    player "Here?"
    rebecca happy "Why not?"
    player "Everyone is awake and..."
    rebecca flirting "This will make it even spicier!"
    rebecca flirting "So? Will you fuck me or not?"
    scene beach_rebecca_15
    rebecca flirting "You can put it anywhere..."
    player "Anywhere?"
    rebecca happy "Yes. But if you want to fuck my ass, I'd want you to lick me first!"
    player "Deal!"
    scene beach_rebecca_16
    rebecca flirting "Oh, yes! You know your way around a woman!"
    player "You are not the first one..."
    rebecca flirting "Less talking, more licking!"
    rebecca flirting "My clit is about to explode!"
    rebecca flirting "Lay down! I need you inside me!"
    scene beach_rebecca_17
    player "Are you sure it will fit in your ass?"
    rebecca happy "Don't start bragging. You are big, but I have some experience too."
    scene beach_rebecca_18
    player "Oh, man! Your asshole is so tight!"
    rebecca flirting "Can you feel it squeezing your dick?"
    rebecca flirting "So you thought I can't fit you inside my ass?"
    scene beach_rebecca_20
    player "You are amazing!"
    rebecca flirting "Oh God! You are big!"
    scene beach_rebecca_19
    rebecca flirting "I can feel you stretching my insides."
    scene beach_rebecca_17
    $renpy.pause()
    scene beach_rebecca_18
    $renpy.pause()
    scene beach_rebecca_17
    $renpy.pause()
    scene beach_rebecca_18
    rebecca flirting "Don't you even think about cumming without telling me!"
    scene beach_rebecca_22
    rebecca flirting "I want to feel your warm cum all over my tits!"
    scene beach_rebecca_17
    $renpy.pause()
    scene beach_rebecca_17
    player "I'm about to cum!"
    scene beach_rebecca_21
    rebecca flirting "Oh yes!"
    player "Well? Will you let me fuck Lana?"
    rebecca "So all you could think about while you had your dick up my ass was fucking my daughter?"
    player "But you said..."
    rebecca happy "I'm just messing with you! Yes you may fuck her, but not her ass. You are too big for someone that has less experience in anal."
    player "And you'll give me the parts for the vibrator?"
    rebecca happy "I will."
    call quest_lanas_vibrations_advance_to_mom_disappear from _call_quest_lanas_vibrations_advance_to_mom_disappear
    jump advance_time
    
#phase 9 auto
label quest_lanas_vibrations_mom_disappear:
    hide screen station_rooms
    $global_events.mom = False
    if (energy >= 500):
        $energy -= 500
    else:
        $energy = 0
    player "Where is mom? She is usually taking a shower at this time..."
    scene bedroom_rebecca_1
    rebecca angry "That bitch!"
    rebecca angry "Where is she?"
    player "What's going on?"
    rebecca angry "That bitch stole my suit! Where is she?"
    player "I don't know, she wasn't here when I woke up..."
    player "Do you think something happened to her?"
    rebecca angry "If she gets killed or captured we loose the suit."
    rebecca angry "And without the suit, we won't be able to go outside the section."
    player "I hope nothing bad happens to mom..."
    rebecca "Greg, I know she's you mother, but going out without proper training is incredibly stupid."
    rebecca "Do you know when she left?"
    player "She was here when I went to sleep last night."
    rebecca "Let's hope she took the suit in the last couple of hours."
    rebecca "It's charge won't hold much longer than that."
    player "Probably even less if she didn't charge it fully..."
    scene bedroom_rebecca_2
    sis angry "Mom! What the hell! Why are you naked?"
    rebecca "It's not what you think, Lana!"
    rebecca "Amelia took my suit and went outside. I have nothing to wear!"
    sis "Let's go to the mess hall and make some clothes for you."
    rebecca "No need for that - I have something laying around..."
    sis "You do? Why didn't you put it on before coming here then?"
    rebecca "I was too angry to care about that!"
    player "Let's just keep calm and wait for breakfast. If mom isn't back, we will know that her suit ran out of power and she is in trouble."
    rebecca "My suit!"
    sis "Mom, please..."
    call quest_lanas_vibrations_advance_to_breakfast_no_mom from _call_quest_lanas_vibrations_advance_to_breakfast_no_mom
    jump advance_time
    
#phase 10
label quest_lanas_vibrations_breakfast_no_mom:
    hide screen station_rooms
    scene mess_hall_rebecca_sis_2
    sis "What the hell are you wearing?"
    rebecca happy "Oh, this? This is a little something that I made for a game we played."
    sis "You and Greg played a game and you were wearing this!"
    rebecca flirting "I wasn't wearing it the whole time!"
    sis "Mom, you are unbelievable!"
    rebecca "Anyway, we have something far more important to discuss."
    scene mess_hall_rebecca_sis_1
    rebecca "It's been more than two hours since we know that Amelia is missing and by now her suit should be out of power for sure..."
    sis sad "Greg, I'm sure she's fine..."
    player "How? How can you be sure M.A.L. hasn't captured her... or worse..."
    rebecca "Greg, I think I know a way to be sure..."
    player "You do? Tell me!"
    rebecca "It's you. You can connect to the security cameras and look for her."
    sis "I don't understand..."
    rebecca "Megan did something to Greg."
    sis "What?"
    rebecca "She put a chip in him, that acts as an interface between his brain and the systems on the station."
    rebecca "He was able to connect to the surveillance network and even spied on our conversation the first night I got here."
    sis angry "You did what!"
    player "It wasn't my fault! I can't control what I see. And that's the issue - I can't control what I see!"
    rebecca "You weren't able to control it {i}yet{/i}."
    rebecca "You need to try!"
    sis "Yes, Greg, you need to try!"
    scene blank
    player "..."
    scene mess_hall_rebecca_sis_1
    player "It's no use! I can't!"
    rebecca "We need to recreate the conditions under which you managed to connect to the cameras."
    sis "Where did you manage to do that?"
    player "They all happened at night..."
    rebecca "Let's get to the bedroom then."
    scene bedroom_rebecca_sis_1
    rebecca "Sit on the bed and try again."
    scene blank
    player "..."
    scene bedroom_rebecca_sis_2
    player "Nothing..."
    rebecca "OK, what are we missing?"
    player "I was asleep during those episodes..."
    rebecca "We can't wait that long - what else?"
    player "I... I was..."
    rebecca "What?"
    sis "Come on, Greg! Tell us!"
    player "I was horny."
    rebecca "Lana, take off your clothes?"
    sis angry "What?"
    rebecca angry "We don't have the time for you to play hard to get!"
    rebecca angry "You were holding his dick when I walked in on you and God knows what else have you two done already!"
    sis angry "Nothing!"
    rebecca "I don't care! I've already told you - you can't be a slave to society's taboos if you are in my unit."
    rebecca "Right now we need to know if Amelia and my suit are captured."
    sis "Why don't you do it then?"
    rebecca "Girl, stop wasting my time or I will slap your ass! Undress, now!"
    scene bedroom_rebecca_sis_3
    rebecca flirting "Greg, lay down on the bed!"
    rebecca flirting "Lana, follow my lead."
    scene bedroom_rebecca_sis_4
    sis flirting "I see that you have some experience with that..."
    rebecca flirting "More than you can think of."
    sis flirting "Really?"
    sis flirting "What else do you have experience with?"
    scene bedroom_rebecca_sis_5
    rebecca flirting "This..."
    sis flirting "Something tells me that this is not the first time you two have done something like this..."
    rebecca flirting "And I can tell you he's not half bad at it!"
    scene bedroom_rebecca_sis_6
    player "What the..."
    rebecca "What?"
    player "I can see us."
    sis "You are connected! Can you change the cameras?"
    player "..."
    player "I don't think so."
    rebecca flirting "Let's try something..."
    scene bedroom_rebecca_sis_7
    rebecca "Megan probably injected the chip in the limbic system, so we need to activate the neurons in it to power the chip."
    sis "Which part of the mind is the limbic system responsible for?"
    rebecca "Primal stuff..."
    rebecca flirting "Sexual arousal, among other things."
    scene corridor_1
    player "I think it's working... I can see the corridor outside this section."
    rebecca "Any sign of your mom?"
    player "None."
    rebecca "Keep looking!"
    scene outpost_1
    $renpy.pause()
    scene outpost_2
    player "I see Megan's section."
    sis "How do you know which one is it?"
    rebecca "No time for that now! Can you see them there?"
    player "No."
    rebecca "That's bad!"
    rebecca "Keep looking!"
    scene elevator_mom_1
    player "There!"
    player "I see her!"
    rebecca "Where?"
    player "Near the elevator!"
    rebecca "Lana, I need to go get her before the others find her!"
    rebecca flirting "Keep him busy in the meantime!"
    rebecca "I'll need his help checking for M.A.L.'s bots and the others, so they don't capture me."
    rebecca "Just be careful not to cum, or you might loose the connection!"
    sis "But how will we be able to warn you?"
    rebecca "While I was outside I found a couple of communicators. I'll leave one here and take the other with me."
    sis "Be careful!"
    rebecca happy "You too... not to finish while I'm still out there."
    scene corridor_1
    rebecca "{i}Greg, I'm about to leave the section. Is the door clear?{/i}"
    player "Yes, I can't see anyone!"
    scene corridor_rebecca_1
    rebecca "{i}I'm going out!{/i}"
    rebecca "{i}Nice! I'll need you to check the way ahead of me.{/i}"
    scene corridor_2
    player "All clear!"
    rebecca "{i}Nice!{/i}"
    scene corridor_rebecca_2
    rebecca "{i}Stay ahead of me!{/i}"
    player "What an ass!"
    rebecca "{i}What?{/i}"
    player "I meant 'all clear!'"
    scene bedroom_rebecca_sis_8
    sis flirting "So you like my mom's ass?"
    player "Lana? You are distracting me!"
    sis flirting "On the contrary - I'm making sure the neurons around the chip are fired up."
    rebecca "{i}Greg, I need you on the cameras!{/i}"
    scene bedroom_rebecca_sis_9
    rebecca "{i}Do you see anything?{/i}"
    player "I... do..."
    sis flirting "See anything you like?"
    rebecca "{i}Unbelievable! I'm risking my life and all you two can think of is fucking each other!{/i}"
    player "I'm sorry... It's the room..."
    rebecca "{i}Yeah, right! Nevermind, I'm at the elevator already!{/i}"
    scene elevator_mom_2
    mom "{i}Rebecca! What are you doing here?{/i}"
    rebecca angry "{i}What does it look like - I'm saving your ass!{/i}"
    mom angry "{i}I bet you are here just for the suit! And speaking of - what the hell are you wearing?{/i}"
    rebecca happy "{i}Oh this? This is just a little something I made for myself and Greg.{/i}"
    mom angry "{i}What!{/i}"
    player "Mom, please stop arguing and get back in our section."
    player "I don't know how much longer I can hold the connection!"
    mom "{i}Greg? What connection?{/i}"
    rebecca "{i}He's right! Knowing Lana, we might loose Greg's connection any second!{/i}"
    scene corridor_2
    player "The corridor is clear. Hurry!"
    scene corridor_rebecca_mom_1
    rebecca "{i}We are getting closer. Check the door!{/i}"
    scene corridor_1
    player "Clear!"
    sis "OK, they are almost here. Turn the radio off!"
    scene bedroom_rebecca_sis_9
    sis flirting "We don't have much time! I want you inside me!"
    scene bedroom_rebecca_sis_11
    player "Oh, this is so good! I can see us from the cameras!"
    sis flirting "So you like to watch?"
    player "Oh yes!"
    sis flirting "But your eyes are open!"
    player "Yes... I think I'm starting to understand how to control this."
    sis flirting "You can switch between your point of view and the cameras?"
    scene bedroom_rebecca_sis_12
    player "Yes!"
    player "And I like what I see!"
    mom angry "Greg! Lana! What are you two doing!"
    scene bedroom_rebecca_mom_sis_1
    player "Mom, I..."
    rebecca angry "Take my fucking suit off right now!"
    mom angry "Why are those two fucking like rabbits? What's going on here?"
    rebecca angry "I said give me back my suit! Now!"
    scene bedroom_rebecca_mom_sis_2
    mom "Here! Happy now!"
    mom "Now explain me what's going on here!"
    scene bedroom_rebecca_mom_sis_3
    rebecca "Remember how you found Greg unconscious after Megan escaped?"
    rebecca "She managed to connect one of her AI interface chips to his brain."
    mom "What! Is he OK?"
    rebecca "Lana, go and get dressed while I explain to Amelia why you were sitting on Greg's dick."
    scene bedroom_rebecca_mom_sis_4
    rebecca "As far as I tell, he is fine."
    player "I'm fine mom."
    rebecca "What we know for sure is that the chip allows him to connect to the surveillance system on the station."
    rebecca "The chip is near the limbic system and to activate it, you need to fire the neurons in that part of the brain."
    mom "The limbic system..."
    rebecca happy "And the easiest way to trigger the neurons there is sexual stimulation."
    rebecca happy "I needed Greg to be my eyes on the way to the elevator."
    rebecca flirting "And Lana was more than happy to help with that."
    mom "But she is his sister!"
    rebecca "Step sister. And if you think that Earth's taboos are valid out here, you are kidding yourself."
    rebecca happy "During my travels I've seen things you wouldn't want to believe."
    mom "I thought you spent most of the travels in cryo-sleep?"
    rebecca happy "Most of the time. And we've learned to enjoy ourselves while we are not sleeping."
    rebecca happy "It's the only way you can keep your sanity."
    mom "I doubt you had much success in that..."
    rebecca "Anyway, you are welcome for saving your ass out there!"
    mom "Can you both get out now, so I can get dressed?"
    player "Sure, mom."
    scene door_bedroom_rebecca_1
    rebecca "OK, you can have the parts."
    player "Really?"
    rebecca happy "Yes, really! I don't think it could've went any better."
    rebecca happy "You fucked Lana, your mom saw it and as a bonus I made her undress in front of you, which should've been humiliating for her!"
    rebecca happy "I think she learned her lesson even though she didn't look too embarrassed to be naked in front of you..."
    player "Didn't she?"
    rebecca flirting "No... Not at all! If I didn't know her, I'd say she enjoyed being naked in front of you..."
    rebecca happy "Don't put too much thought into that! You have a more important task right now - go and make that vibrator."
    $global_events.mom = True
    call quest_lanas_vibrations_advance_to_make_vibrator from _call_quest_lanas_vibrations_advance_to_make_vibrator
    jump advance_time
    
#phase 11 terminal
label quest_lanas_vibrations_make_vibrator:
    hide screen station_rooms
    if (energy < 100):
        $talk_with_terminal.add_topic("Make a vibrator (-100kWh)", "quest_lanas_vibrations_make_vibrator", quest_lanas_vibrations, 11)
        player "{i}There isn't enough energy stored in the batteries for that...{/i}"
        jump advance_time
    player "OK, I have the electronics, all I need now is to make the soft silicone shell."
    $energy -= 100
    player "..."
    player "Done!"
    player "Let's find Lana at the beach and give it to her."
    call quest_lanas_vibrations_advance_to_give_vibrator from _call_quest_lanas_vibrations_advance_to_give_vibrator
    jump advance_time
    
#phase 12 talk
label quest_lanas_vibrations_give_vibrator:
    hide screen station_rooms
    player "Guess what I have for you!"
    scene beach_sis_13
    sis happy "You managed to make it?"
    player "I did. Your mom managed to get the electronics when she was out."
    player "I made the rest with the processor."
    scene beach_sis_14
    sis happy "Let me see!"
    scene beach_sis_15
    sis happy "Wow! It looks really nice!"
    player "You want to try it?"
    sis "Here? Hmmmm... I don't think this is such a good idea..."
    sis "What if your mom walks in?"
    player "I think she has seen worse..."
    sis "... OK"
    sis flirting "But no touching!"
    player "I promise!"
    scene beach_sis_16
    $renpy.pause()
    scene beach_sis_17
    sis flirting "Oh my! That's amazing!"
    scene beach_sis_18
    $renpy.pause()
    scene beach_sis_19
    sis flirting "I will have some fun with it tonight."
    player "What about my reward?"
    sis flirting "I thought you had your reward already. And you got much more than what we agreed on!"
    player "That was for something else!"
    sis flirting "OK, meet me after I take a shower and we will figure it out."
    player "Fine."
    call event_lana_rebecca_sleep_start from _call_event_lana_rebecca_sleep_start
    call quest_lanas_vibrations_advance_to_shower from _call_quest_lanas_vibrations_advance_to_shower
    jump advance_time
    
#phase 13 auto
label quest_lanas_vibrations_shower:
    hide screen station_rooms
    player "Mind if I join you?"
    sis happy "Not at all!"
    scene shower_sis_5
    sis happy "I guess you'd like me to show you how much I enjoy the vibrator?"
    player "I wouldn't mind that."
    scene shower_sis_22
    sis flirting "Make yourself comfortable..."
    sis flirting "I tried it last night..."
    player "I know."
    sis flirting "Were you in the room?"
    player "Not exactly..."
    sis flirting "You pervert! You used your connection to spy on me!"
    player "I wasn't the only one enjoying the view."
    sis happy "That horny bitch!"
    player "You really shouldn't talk about your mom like that..."
    sis happy "But she spied on my while I was masturbating!"
    sis happy "I thought I heard something on the upper deck!"
    sis flirting "Anyway... Let's not waste any more time!"
    scene shower_sis_18
    sis flirting "Oh yeah!"
    sis flirting "That's so good!"
    player "You seem to enjoy my gift."
    scene shower_sis_19
    sis flirting "Indeed I do!"
    sis flirting "But if I remember correctly, it wasn't exactly a gift."
    sis flirting "We arranged for a 'payment' of some sort."
    player "We did!"
    scene shower_sis_20
    sis flirting "So how would you like me to thank you for the vibrator?"
    player "You promised me a handjob."
    sis flirting "Indeed. But I've been thinking... we kind of already did that..."
    sis flirting "And I wanted to thank you in a {i}special{/i} way."
    scene shower_sis_21
    player "I'd love a blowjob."
    sis flirting "I bet you would. But it's not what I have in mind!"
    sis flirting "Lay down!"
    scene shower_sis_14
    player "Oh that is so hot!"
    sis flirting "Isn't it!"
    sis flirting "I like it how hard you are between my feet!"
    scene shower_sis_15
    player "..."
    sis flirting "You naughty boy! You closed your eyes so you could watch through the cameras, didn't you!"
    player "Busted!"
    sis flirting "Do you like what you see?"
    player "You are amazing!"
    sis flirting "Do you want to spray your cum all over my feet?"
    player "Can I?"
    sis flirting "You can, but only this time!"
    player "Ughhh!"
    scene shower_sis_17
    sis flirting "Oh it's so much!"
    sis happy "Look!"
    scene shower_sis_16
    player "That's so sexy!"
    sis happy "Yeah, but now I need to wash again!"
    sis happy "You should go before your mom comes!"
    call quest_lanas_vibrations_finish from _call_quest_lanas_vibrations_finish
    jump advance_time
    