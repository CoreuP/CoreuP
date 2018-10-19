label help_sis_beach:
    player "[quest_sis_beach.help]"
    if quest_sis_beach.finished:
        player "{i}There is nothing more that can be done about this in the current version of the game{/i}"
    jump wait

#self.phase = 0
#self.active = False
#self.location = "any"
#self.mom_location = "any"
#self.sis_location = "any"
#self.alone = False
#self.req_efficiency = -1;
#self.req_energy = -1;
#self.req_capacity = -1;
#self.req_day = -1;
#self.req_clock = -1;
#self.day_mode = "at_least"
#self.clock_mode = "exactly"

#phase 0 talk
label start_quest_sis_beach:
    $talk_with_sis.add_topic("Ask why she is wearing this", "talk_sis_beach", quest_sis_beach, 0)
    $quest_sis_beach.active = True
    $quest_sis_beach.location = "vr_room"
    $quest_sis_beach.alone = False
    $quest_sis_beach.req_clock = -1
    $quest_sis_beach.sis_location = "vr_room"
    $quest_sis_beach.help = "{i}I have to talk to Lana in the VR room, which is now turned to a beach.{/i}"
    return
    
#phase 1 terminal
label quest_sis_beach_advance_to_check_processor:
    $talk_with_terminal.add_topic("Check for swim wear", "quest_sis_beach_check_processor", quest_sis_beach, 1)
    $quest_sis_beach.advance_phase()
    $quest_sis_beach.reset()
    $quest_sis_beach.location = "life_support"
    $quest_sis_beach.help = "{i}I need to check if the program I downloaded from the engineering room contains something for the beach.{/i}"
    return
    
#phase 2 terminal
label quest_sis_beach_advance_to_ask_earth:
    $talk_with_terminal.add_topic("Ask Earth for help with swim wear", "quest_sis_beach_ask_earth", quest_sis_beach, 2)
    $quest_sis_beach.advance_phase()
    $quest_sis_beach.reset()
    $quest_sis_beach.location = "comm"
    $quest_sis_beach.alone = True
    $quest_sis_beach.clock = 2
    $quest_sis_beach.clock_mode = "at_most"
    $quest_sis_beach.help = "{i}If those guys on Earth want to see some skin, they have to help me program some beach wear.{/i}"
    return
    
#phase 3 terminal
label quest_sis_beach_advance_to_make_skimpy_bikini:
    $talk_with_terminal.add_topic("Check the program", "quest_sis_beach_make_bikini", quest_sis_beach, 3)
    $quest_sis_beach.advance_phase()
    $quest_sis_beach.reset()
    $quest_sis_beach.alone = True
    $quest_sis_beach.req_energy = 450
    $quest_sis_beach.location = "mess_hall"
    $quest_sis_beach.help = "{i}Let's see if that guy really had programmed bikinis in the processor and make a couple. He said that they will require 450 kWh of energy, so I better make sure that we have that much stored in the battery.{/i}"
    return
    
#phase 4 goto
label quest_sis_beach_advance_to_give_skimpy_bikini:
    $quest_sis_beach.advance_phase()
    $quest_sis_beach.reset()
    $quest_sis_beach.location = "mess_hall"
    $quest_sis_beach.sis_location = "mess_hall"
    $quest_sis_beach.mom_location = "mess_hall"
    $quest_sis_beach.help = "{i}I will give the bikinis to mom and Lana while we are eating together.{/i}"
    return
    
#phase 5 terminal
label quest_sis_beach_advance_to_explain_earth:
    $talk_with_terminal.add_topic("Ask for something that mom would wear", "quest_sis_beach_explain_earth", quest_sis_beach, 5)
    $quest_sis_beach.advance_phase()
    $quest_sis_beach.reset()
    $quest_sis_beach.location = "comm"
    $quest_sis_beach.alone = True
    $quest_sis_beach.clock = 2
    $quest_sis_beach.clock_mode = "at_most"
    $quest_sis_beach.help = "{i}It's that guy's fault that he programmed such a skimpy suit in the processor, I need to let him know that mom refused to wear them.{/i}"
    return
    
#phase 6 talk
label quest_sis_beach_advance_to_ask_sis:
    $talk_with_sis.add_topic("Ask her to show something more", "quest_sis_beach_ask_sis", quest_sis_beach, 6)
    $quest_sis_beach.advance_phase()
    $quest_sis_beach.reset()
    $quest_sis_beach.location = "vr_room"
    $quest_sis_beach.sis_location = "vr_room"
    $quest_sis_beach.help = "{i}I have to explain to Lana that if she doesn't get naked in the beach, we would loose all the help that we've got from Earth.{/i}"
    return
    
#phase 7 auto
label quest_sis_beach_advance_to_shower:
    $quest_sis_beach.advance_phase()
    $quest_sis_beach.reset()
    $quest_sis_beach.location = "bedroom"
    $quest_sis_beach.alone = True
    $quest_sis_beach.help = "{i}Lana said that she would not do anything unless I masturbate in the shower.{/i}"
    return
    
#phase 8 talk
label quest_sis_beach_advance_to_show:
    $talk_with_sis.add_topic("Ask for a show", "quest_sis_beach_show", quest_sis_beach, 8)
    $quest_sis_beach.advance_phase()
    $quest_sis_beach.reset()
    $quest_sis_beach.location = "vr_room"
    $quest_sis_beach.sis_location = "vr_room"
    $quest_sis_beach.help = "{i}I did what Lana asked me, not it's her turn to get naked at the beach.{/i}"
    return
    
#phase 9 terminal
label quest_sis_beach_advance_to_feedback_earth:
    $quest_sis_beach.advance_phase()
    $quest_sis_beach.reset()
    $quest_sis_beach.location = "comm"
    $quest_sis_beach.alone = True
    $talk_with_terminal.add_topic("Ask them if they liked the show", "quest_sis_beach_feedback_earth", quest_sis_beach, 9)
    $quest_sis_beach.help = "{i}Let's ask Earth if their customers liked Lana's show{/i}"
    call add_event_sis_strip_beach from _call_add_event_sis_strip_beach
    return
    
#phase 10 auto
label quest_sis_beach_advance_to_sis_shower:
    $quest_sis_beach.advance_phase()
    $quest_sis_beach.reset()
    $quest_sis_beach.location = "bedroom"
    $quest_sis_beach.sis_location = "bedroom"
    $quest_sis_beach.req_clock = 8
    $quest_sis_beach.clock_mode = "exactly"
    $quest_sis_beach.help = "{i}So Lana masturbated while I was in the shower... Let's see what she has to say about this!{/i}"
    return
    
label quest_sis_beach_finish:
    $quest_sis_beach.advance_phase()
    $quest_sis_beach.reset()
    $global_events.sis_beach = True
    if (global_events.mom_beach):
        call start_quest_meet_megan from _call_start_quest_meet_megan
    $quest_sis_beach.help = "{i}So now Lana has no issues stripping on the beach and we can occasionally have some fun in mom's bedroom.{/i}"
    $quest_sis_beach.finished = True
    return
    
#phase 0
label talk_sis_beach:
    hide screen station_rooms
    player "Enjoying yourself?"
    sis "Of course!"
    player "Why are you here in those clothes?"
    sis "Because, dummy, I have nothing else to wear!"
    player "Oh, right!"
    player "By the way that guy from Earth said this room will be monitored as well."
    sis "I don't really care. As long as I can enjoy that beach, they can watch whatever they like!"
    player "But they also said that you need to wear something sexy - the viewers need to be \"happy\""
    sis "It's not like I have a choice - these are the only clothes that I have!"
    player "I'll see what I can do..."
    call quest_sis_beach_advance_to_check_processor from _call_quest_sis_beach_advance_to_check_processor
    jump wait_action

#phase 1
label quest_sis_beach_check_processor:
    hide screen station_rooms
    player "Lets see what we have here..."
    player "..."
    player "Shit! Nothing useful!"
    player "And I can't program it myself - I'll need to contact Earth and ask them for help."
    call quest_sis_beach_advance_to_ask_earth from _call_quest_sis_beach_advance_to_ask_earth
    jump wait_action
    
#phase 2
label quest_sis_beach_ask_earth:
    hide screen station_rooms
    player "This is Greg from Antares..."
    male "Finally! What's this shit that's been going in the VR room?"
    male "I think we agreed, the women need to show some skin!"
    player "I can't ask them to sunbathe naked and these are the only clothes that we can make!"
    male "OK, I'll upload some blueprints, and you can make some decent bathing suits!"
    male "But keep in mind that I'm not a specialist in this, so the program is not optimized and it will cost you 450 kWh to produce them."
    player "And by decent you mean..."
    male "Sexy bikini."
    player "Lana would wear them, but I don't know about my mom..."
    male "Not my problem! You have to make the clothes and convince the women to wear them!"
    male "We are already loosing customers and if we continue like this, there will be no point in keeping you around."
    player "You mean..."
    male "We will have to shut you down."
    male "I don't like it and believe me - you won't like it either!"
    player "I'll see what I can do."
    male "Over and out!"
    $global_events.deadline = day + 3
    call quest_sis_beach_advance_to_make_skimpy_bikini from _call_quest_sis_beach_advance_to_make_skimpy_bikini
    jump wait_action
    
#phase 3
label quest_sis_beach_make_bikini:
    hide screen station_rooms
    player "Let's see what did that guy upload in the processor..."
    player "I'll just press here and they should be ready in a few minutes."
    $energy -= 450
    player "..."
    player "OK they are ready - let's give them to mom and Lana while we are eating together."
    call quest_sis_beach_advance_to_give_skimpy_bikini from _call_quest_sis_beach_advance_to_give_skimpy_bikini
    jump wait_action
    
#phase 4
label quest_sis_beach_give_skimpy_bikini:
    hide screen station_rooms
    scene mess_hall_mom_sis_1
    player "Mom, Lana, look what I have for you!"
    player "I know you have been sunbathing in your daily clothes, so I managed to make you something more suitable to wear at a beach."
    sis "Let me try them on!"
    scene mess_hall_mom_sis_7
    sis "They are really good!"
    mom "Hmmm, can you please turn around?"
    scene mess_hall_mom_sis_8
    mom "I don't know Lana... They look a bit too revealing..."
    sis "They are not!"
    mom "I really think they are... Can't you make anything else, Greg?"
    player "It was hard enough programming those, I don't know if I can manage to change the program."
    player "And on top of that, they've already depleted much of our energy reserves."
    mom angry "What?!?"
    mom angry "How much exactly?"
    player "450 kWh"
    mom angry "That's almost half of the whole capacity of the battery!"
    player "I know, but I thought it would make you happy."
    mom "Thank you, but you should've asked first!"
    mom "I won't wear them - they are too revealing for me."
    sis "I will. Thank you Greg!"
    mom "But Lana..."
    sis "I'm not a little kid anymore. I like them and I think they are totally fine!"
    mom angry "As you wish. I'll wear my clothes until Greg makes something more appropriate."
    player "I'll see what I can do..."
    $global_events.sis_bikini = True
    call quest_sis_beach_advance_to_explain_earth from _call_quest_sis_beach_advance_to_explain_earth
    jump wait_action
    
#phase 5
label quest_sis_beach_explain_earth:
    hide screen station_rooms
    player "This is Greg from Antares."
    male "Did you convince the women to wear the bikinis?"
    player "No. They are too revealing. My mom refuses to wear them."
    male "And what about your sister?"
    player "She seems to like them."
    male "Nice! But you need to do something about your mom. Does she know that if she refuses to wear them, we will cut our support for the station?"
    player "What? It's your fault that she won't wear the bikinis. You made them so revealing and now my mom won't wear them."
    player "It's not fair!"
    male "OK - maybe you are right..."
    player "So what do you plan to do about that?"
    male "Me? It's your problem. Find a way to either convince her, or to change the program into something that she will wear."
    player "So you won't cut the power for the station?"
    male "I didn't say that. You need to show our customers it's worth paying for access to the feed from the station."
    player "And how would I do that?"
    male "Make your sister show some skin at the beach. And I'm not talking about laying around in the bikini."
    male "Our customers want to see some action."
    player "Action? You mean sex? She would never agree to that."
    male "At least convince her to undress. Put on some sun lotion... sunbathe nude or something like that. Figure it out!"
    $global_events.deadline = day + 3
    male "Over and out!"
    player "{i}So now I need to learn how to re-program the processor and have Lana undress at the beach.{/i}"
    call start_quest_mom_beach from _call_start_quest_mom_beach
    call quest_sis_beach_advance_to_ask_sis from _call_quest_sis_beach_advance_to_ask_sis
    jump wait_action
    
#phase 6
label quest_sis_beach_ask_sis:
    hide screen station_rooms
    player "Hey Lana."
    sis "Hi."
    sis "Did you enjoy the view at the beach?"
    player "I sure did! Those bikinis look really good on you."
    sis happy "Thank you!"
    player "I wanted to talk to you about something..."
    sis "What?"
    player "You know that the beach room is monitored from Earth?"
    sis "I do. And as I've already told you, I don't care."
    sis "They can watch - it's not like I'm wearing something different when I go at the beach on Earth."
    player "Well..."
    player "This is why I wanted to talk to you."
    sis "I think I know where this is heading and I don't like it..."
    player "They want to see something more."
    sis angry "No."
    player "It doesn't have to be something hardcore - just maybe show them your breasts or your butt."
    sis angry "No."
    player "But they said they would shut us down if we don't give their customers a reason to continue paying."
    sis "I said \"no\"!"
    player "But Lana..."
    sis "No buts."
    sis "No butts."
    sis "And certainly no tits either!"
    player "Please!"
    sis "Why me? Why don't you show your dick to those perverts on Earth?"
    player "They don't want to see my dick - they want to see you!"
    sis "Here is the deal - you said that they were monitoring mom's bedroom too, right?"
    player "Right."
    sis "So you go there alone, take a shower and touch yourself in front of everyone on Earth."
    player "And if I do this, you will do a little show on the beach?"
    sis "Yes."
    player "Deal!"
    sis "Deal!"
    call quest_sis_beach_advance_to_shower from _call_quest_sis_beach_advance_to_shower
    jump wait_action
    
#phase 7
label quest_sis_beach_shower:
    hide screen station_rooms
    scene shower_player_1
    player "{i}Lana promised she would do a show on the beach only if I masturbate in the shower.{/i}"
    player "{i}It's a pity that mom didn't want to wear the bikinis, I bet she would've looked gorgeous in them!{/i}"
    scene shower_player_2
    player "{i}I think white ones would suit her better than the red ones that I gave to Lana.{/i}"
    scene dream_mom_1
    mom "Hi Greg! Did you come to enjoy the beach as well?"
    player "Yes mom, it's so realistic!"
    mom "I still can't believe it!"
    player "Well, this is not just a hologram, the VR equipment actually produces everything you touch..."
    mom happy "Don't be boring! I don't care for the technical details... in fact all I want to know is if I should put some sunblock?"
    player "The light intensity..."
    mom happy "Simple answer please!"
    player "You should."
    mom happy "Would you help me with that?"
    scene dream_mom_2
    player "I'll need to untie the straps."
    mom happy "OK, just hurry up."
    scene dream_mom_3
    mom happy "Don't miss a spot!"
    player "I won't."
    mom happy "I like your strong hands."
    player "..."
    scene dream_mom_4
    mom happy "Now do the front."
    player "Are you sure?"
    mom happy "Of course! I don't want to get burned!"
    player "OK, but you should take your bra off."
    mom happy "Like this?"
    scene dream_mom_5
    mom "I think it's better to do this myself."
    player "It's not a problem!"
    mom happy "My eyes are up here."
    player "Sorry mom. It's just that you are so beautiful."
    mom happy "Thank you!"
    scene dream_mom_6
    mom "Do you want to go for a swim?"
    player "Sure!"
    scene dream_mom_7
    mom "You said that this feels real?"
    player "It does."
    scene dream_mom_8
    mom "In that case... I guess I won't be needing these."
    scene dream_mom_9
    mom happy "Are you coming?"
    scene shower_player_2
    player "{i}Yes, I am.{/i}"
    scene bedroom_1
    player "{i}Now let's talk with Lana.{/i}"
    call quest_sis_beach_advance_to_show from _call_quest_sis_beach_advance_to_show
    jump wait_action
    
#phase 8
label quest_sis_beach_show:
    hide screen station_rooms
    player "Are you ready?"
    scene beach_sis_4
    sis "For what?"
    player "To give a special show to the viewers on Earth of course!"
    sis "Did you jerk off in the shower?"
    player "I did."
    sis flirty "Did you think about me?"
    player "What?!?"
    player "You said you didn't like that - me being your step brother and stuff..."
    sis happy "So... did you think about me?"
    player "No!"
    sis "That's a pity!"
    sis "Let's fix that!"
    scene beach_sis_2
    sis "So you said the viewers would want to see my breasts?"
    player "Definitely!"
    scene beach_sis_6
    sis happy "And how about you?"
    sis happy "Would you want to see my breasts?"
    player "Of course!"
    scene beach_sis_7
    sis happy "Like that?"
    player "More please!"
    sis happy "Since you ask so nicely..."
    scene beach_sis_8
    sis "I wouldn't want to have tan lines, anyway!"
    player "In that case, you'd better take the bra off..."
    sis "I guess I should."
    scene beach_sis_9
    sis "I think I will remove the panties too."
    player "The viewers would be so happy!"
    sis "Forget about them - let's enjoy this private beach!"
    scene beach_sis_10
    sis "The sun feels so warm on my back!"
    sis "But it's not the sun, is it?"
    player "Projectors."
    sis "Can you get a tan?"
    player "Yes."
    sis "You'd better put some sun oil on me then."
    scene beach_sis_11
    sis "I really enjoy the beach. This view is my favorite!"
    player "Mine too!"
    sis happy "I bet it is!"
    sis "I really like the feel of the sand pressing against my skin. It feels so real!"
    player "That's because it is real."
    player "This is not some low-end holo-room. This is a fully equipped VR room."
    sis "What's the difference? I bet this ocean is a hologram too."
    player "Sure it is, but if you go there and touch the watter, you will feel that it's wet."
    player "If you taste it, you will find out that it's salty."
    sis "How come?"
    player "The equipment creates everything that we touch from energy."
    sis "But this will require massive amounts of energy!"
    player "Not at all. Sure we couldn't afford to have it without the help from Earth, but in fact everything is recycled."
    player "When you go to the ocean, the system creates the water that you touch, but recycles the sand that you no longer touch."
    player "So the amount of the wasted energy is not that much."
    scene beach_sis_12
    sis "Thank you for the lesson, but I think I should go now."
    sis "You don't want mom to find us like this, do you?"
    player "No."
    call quest_sis_beach_advance_to_feedback_earth from _call_quest_sis_beach_advance_to_feedback_earth
    jump wait_action

#phase 9
label quest_sis_beach_feedback_earth:
    hide screen station_rooms
    player "This is Greg from Antares. Come in."
    male "Hi Greg!"
    player "Did your viewers like the show?"
    male "You mean rubbing oil on your sister's naked ass or the other one?"
    if (global_events.mom_beach):
        player "Well, yes - I don't suppose they saw much of my mother..."
        male "Who's talking about your mother? I mean the other show of your sister!"
    player "What other show?"
    male "Oh! You don't know, do you?"
    player "Don't know what?"
    male "While you were in the shower, you weren't the only one touching yourself in that room."
    player "What?!"
    male "Let me show you! Sending the video now."
    scene shower_player_sis_1
    male "Your sister entered the room while you were in the shower. Let's fix the focus..."
    scene shower_player_sis_2
    male "OK, that's better."
    scene shower_player_sis_3
    male "She seemed to have followed you, because she knew exactly when you would be in the shower."
    male "She began undressing..."
    scene shower_player_sis_4
    male "... and touching herself."
    scene shower_player_sis_5
    player "How did you get such closeup?"
    male "I think you underestimate the equipment in that room. We get a 3D image of everything in the room and we can have a virtual camera at any point."
    scene shower_player_sis_6
    male "This is where it got interesting..."
    scene shower_player_sis_7
    male "Looks like her feet couldn't hold her anymore, so she needed to sit down."
    player "You know, I think it would be better without the live comments..."
    male "Don't tell me you are getting jealous."
    scene shower_player_sis_8
    male "She is probably not even thinking of you, but of all the people watching her."
    player "Oh right! She knew this room was monitored!"
    scene shower_player_sis_9
    male "Just look at her fingers sliding in and out of her..."
    player "..."
    male "Let's have a closeup!"
    scene shower_player_sis_10
    male "What a slut!"
    player "Don't call her that!"
    scene comm_1
    male "It goes on for a while and then you said something about your mom, so she gathered her clothes and left."
    player "Well, I understand how she feels - she's been here for [day] days without sex."
    male "But masturbating in front of everyone... man, I would trade my left nut to switch places with you and be around that horny fox!"
    player "Fuck off!"
    call quest_sis_beach_advance_to_sis_shower from _call_quest_sis_beach_advance_to_sis_shower
    jump wait_action
    
#phase 10
label quest_sis_beach_sis_shower:
    hide screen station_rooms
    player "Hey Lana!"
    sis "What are you doing here? What if mom comes in?"
    player "She won't - she is making breakfast in the kitchen. I wanted to ask you something..."
    sis "Fine, just give me a towel please."
    scene shower_sis_5
    sis "What's up?"
    player "Did you spied on me in the shower?"
    scene shower_sis_6
    sis "It's not like you haven't spied on me..."
    player "Fair enough. But I didn't masturbate while watching you!"
    sis "How did you know?"
    player "That's not important! Why did you do it?"
    sis flirting "Why? Because I was horny then... and talking about it makes me horny again..."
    sis flirting "But you are so upset about it, that you would probably not want to see me touching myself?"
    scene shower_sis_7
    sis flirting "Right?"
    player "Well..."
    sis happy "That's what I thought! You are as horny as I am!"
    player "I am, but I don't think it's appropriate..."
    sis flirting "As you wish, but I need to touch myself."
    scene shower_sis_8
    sis "Oh, yes! That's better!"
    sis "You were so hot in the shower..."
    scene shower_sis_9
    sis "Stroking that big cock of yours..."
    sis "Thinking about me..."
    sis "Thinking about sliding it between my thighs..."
    player "Stop it! You are making me hard!"
    sis "So what are you going to do about it?"
    sis flirting "I don't mind seeing it again!"
    scene shower_sis_10
    sis "Stroke it! Stroke it for me!"
    player "Lana, please stop it! You are my sister!"
    sis "Stop? I'm not doing anything!"
    sis flirting "I'm just touching my pussy, thinking about my step brother's cock."
    sis flirting "Let me see it better!"
    scene shower_sis_11
    sis "Oh yes!"
    sis "It's so hot me touching my clit while you stroke that big cock!"
    player "If you don't stop I'm going to cum!"
    sis "That would be so hot!"
    call quest_sis_beach_finish from _call_quest_sis_beach_finish
    jump shower_sis_cum
    
label shower_sis_cum:
    menu:
        "Cum on her":
            scene shower_sis_12
            sis angry "What the hell, Greg!"
            player "I thought you said..."
            sis angry "I never said you can cum on me! I'll need to get another shower!"
            sis angry "Get out this instant!"
            scene door_1
            player "What the fuck happened there? I couldn't stop myself and neither could Lana."
            if not quest_investigate_bedroom.active:
                call quest_investigate_bedroom_start from _call_quest_investigate_bedroom_start
            player "I think she will be angry at me for a while..."
            call event_sis_shower_five_days from _call_event_sis_shower_five_days
        "Cum in your hand":
            scene shower_sis_13
            sis happy "Wow, this was something!"
            player "What you said..."
            sis "Look Greg, I needed this, you needed this, so let's leave it like that."
            sis "We can do this again sometime."
            player "Like tomorrow?"
            sis "We'll see..."
            sis "I need to get dressed now."
            scene door_1
            player "What the fuck did we just do? I could barely stop myself from cumming all over her."
            if not quest_investigate_bedroom.active:
                call quest_investigate_bedroom_start from _call_quest_investigate_bedroom_start_1
            player "It's almost time for breakfast, let's go wash my hands."
            call event_sis_shower_two_days from _call_event_sis_shower_two_days
    jump advance_time
