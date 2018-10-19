label help_meet_rebecca:
    player "{i}[quest_meet_rebecca.help]{/i}"
    if quest_meet_rebecca.finished:
        player "{i}There is nothing more that can be done about this in the current version of the game{/i}"
    jump wait

#phase 0 auto
label start_quest_meet_rebecca:
    $quest_meet_rebecca.active = True
    $quest_meet_rebecca.location = "mess_hall"
    $quest_meet_rebecca.req_day = day + 3
    $quest_meet_rebecca.req_clock = 19
    $quest_meet_rebecca.help = ""
    return
    
#phase 1 auto
label quest_meet_rebecca_advance_to_sleep_talk:
    $global_events.rebecca = True
    if (quest_lanas_vibrations.phase == 3):
        call quest_lanas_vibrations_advance_to_talk_rebecca from _call_quest_lanas_vibrations_advance_to_talk_rebecca_1
    $quest_meet_rebecca.advance_phase()
    $quest_meet_rebecca.reset()
    $quest_meet_rebecca.req_clock = 23
    $quest_meet_rebecca.clock_mode = "exactly"
    $quest_meet_rebecca.help = "Now that Rebecca is on the station, we should think about who's sleeping where"
    return
    
#phase 2 talk
label quest_meet_rebecca_advance_to_dreams:
    $global_events.sleep_bedroom = True
    $quest_meet_rebecca.reset()
    $quest_meet_rebecca.advance_phase()
    $quest_meet_rebecca.location = "med_bay"
    $quest_meet_rebecca.rebecca_location = "med_bay"
    $talk_with_rebecca.add_topic("Talk about the dreams", "quest_meet_rebecca_talk_dreams", quest_meet_rebecca, 2)
    $quest_meet_rebecca.help = "So now I'm sleeping in the bedroom with mom... Maybe I should talk with Rebecca about the weird dreams I'm having"
    call start_event_outpost_sex from _call_start_event_outpost_sex
    return
    
#phase 3 terminal
label quest_meet_rebecca_advance_to_talk_earth:
    $event_outpost_sex.req_clock = -1
    $quest_meet_rebecca.reset()
    $quest_meet_rebecca.advance_phase()
    $quest_meet_rebecca.location = "comm"
    $quest_meet_rebecca.req_clock = 3
    $quest_meet_rebecca.req_day = 10000 #set to -1 in event_outpost_sex phase 2
    $quest_meet_rebecca.clock_mode = "at_most"
    $talk_with_terminal.add_topic("Talk about you sleeping in the bedroom", "quest_meet_rebecca_talk_earth", quest_meet_rebecca, 3)
    $quest_meet_rebecca.help = "So according to Rebecca, I got some chip that managed to connect my brain to the security cameras... I wonder what else I will 'see'..."
    return
    
#phase 4 talk
label quest_meet_rebecca_advance_to_beach:
    $quest_meet_rebecca.reset()
    $quest_meet_rebecca.advance_phase()
    $quest_meet_rebecca.location = "vr_room"
    $quest_meet_rebecca.rebecca_location = "vr_room"
    $talk_with_rebecca.add_topic("Ask her for a show", "quest_meet_rebecca_beach", quest_meet_rebecca, 4)
    $quest_meet_rebecca.help = "Rebecca promised a show at the beach - let's see if it will be as good as she promised"
    return
    
#phase 5 terminal
label quest_meet_rebecca_advance_to_talk_again:
    $event_outpost_sex.req_clock = -1
    $global_events.rebecca_topless = True
    $quest_meet_rebecca.reset()
    $quest_meet_rebecca.advance_phase()
    $quest_meet_rebecca.location = "comm" 
    $quest_meet_rebecca.req_clock = 3
    $quest_meet_rebecca.clock_mode = "at_most"
    $quest_meet_rebecca.req_day = 10000 #set to -1 in event_outpost_sex phase 3 
    $talk_with_terminal.add_topic("Ask about the dream", "quest_meet_rebecca_talk_again", quest_meet_rebecca, 5)
    $quest_meet_rebecca.help = "Let's see if Earth will keep their word and turn off the equipment this night"
    return
    
#phase 6 talk
label quest_meet_rebecca_advance_to_engineering:
    $quest_meet_rebecca.reset()
    $quest_meet_rebecca.advance_phase()
    $quest_meet_rebecca.location = "life_support"
    $quest_meet_rebecca.rebecca_location = "life_support"
    $talk_with_rebecca.add_topic("Talk about the game", "quest_meet_rebecca_engineering", quest_meet_rebecca, 6)
    $quest_meet_rebecca.help = "Rebecca said to look for her in the engineering room"
    return
    
#phase 7 talk
label quest_meet_rebecca_advance_to_setup_game:
    $quest_meet_rebecca.reset()
    $quest_meet_rebecca.advance_phase()
    $quest_meet_rebecca.location = "vr_room"
    $quest_meet_rebecca.rebecca_location = "vr_room"
    $quest_meet_rebecca.req_energy = 850
    $quest_meet_rebecca.req_efficiency = 100
    $talk_with_rebecca.add_topic("Setup game", "quest_meet_rebecca_setup_game", quest_meet_rebecca, 7)
    $quest_meet_rebecca.help = "Once we have 850kWh energy stored and the panels operate at 100% efficiency, Rebecca said to talk with her at the beach"
    return
    
#phase 8 auto
label quest_meet_rebecca_advance_to_play_game:
    $quest_meet_rebecca.reset()
    $quest_meet_rebecca.advance_phase()
    $quest_meet_rebecca.req_clock = 0
    $quest_meet_rebecca.clock_mode = "exactly"
    $quest_meet_rebecca.help = "Everything is set up for tonight. Rebecca said to find her at the engineering at midnight"
    return
    
label quest_meet_rebecca_finish:
    $quest_meet_rebecca.reset()
    $quest_meet_rebecca.advance_phase()
    $quest_meet_rebecca.help = "I should be able to convince Rebecca to play another game whenever we have enough energy."
    $quest_meet_rebecca.finished = True
    return
    
#phase 0 auto
label quest_meet_rebecca_dinner:
    hide screen station_rooms
    scene mess_hall_mom_sis_1
    mom "Bon apetit, everyone!"
    sis "I hope we don't have to eat those cookies for too long..."
    mom "It's the best that machine can do right now."
    scene mess_hall_power_outage_1
    mom "What the..."
    sis "What happened? Why are we on emergency power?"
    player "Shit! The bots might have found a way to cut the power to get through the door."
    mom "We should check!"
    player "No! You stay here, I'll take a look."
    mom "Please don't do anything stupid. Take a look and get back."
    sis "Don't try to confront them if they went through."
    player "I won't..."
    scene corridor_outage_1
    player "{i}That was stupid... Going out by myself, what if they have gone through?{/i}"
    player "{i}We have no weapons, so it won't matter if I try to stop them at the door or go back to mom and Lana.{/i}"
    player "{i}Have they really broken through? I guess I'll know soon enough - the door is just around the corner...{/i}"
    mom "Greg! Come back! There is something in the room!"
    player "{i}Shit! I shouldn't have left them alone!{/i}"
    scene mess_hall_power_outage_2
    sis "Mom, please sit down!"
    mom "I won't! Let her try to make me sit down!"
    female "Believe me, I'd like nothing better than forcing your ass to sit down, but this will help noone."
    sis "Mom, please, do as she says!"
    player "Who is she?"
    female "All of you, for the last time, please sit down!"
    scene mess_hall_power_outage_3
    mom "Happy now?"
    female "Amelia, trust me, being here is not something that would make me happy."
    mom "How do you know my name?"
    female "Power should be back in 4... 3... 2... 1..."
    scene mess_hall_power_outage_4
    sis "Show yourself!"
    female "Just about to do exactly that..."
    scene mess_hall_power_outage_5
    scene mess_hall_power_outage_6 with dissolve
    scene mess_hall_power_outage_7 with dissolve
    sis "Mom!"
    scene mess_hall_power_outage_8
    player "Mom?"
    sis "Everyone, this is my mother, Rebecca!"
    mom "But how..."
    rebecca "I'll explain everything in a minute, but first I need to check something."
    rebecca "Is this energy processor plugged in the network?"
    player "It is."
    scene mess_hall_power_outage_9
    rebecca "OK, looks like our little power mishap went unnoticed."
    rebecca "Which is good..."
    rebecca "Are the three of you the only ones here? Where is Jack?"
    mom sad "He couldn't make it... we don't even know if he's alive or not."
    rebecca "Let's not feel sorry for him just yet."
    sis "What do you mean?"
    scene mess_hall_power_outage_10
    rebecca "What exactly do you know about his work here?"
    mom "He was working at the relativity theory applications unit on something classified."
    rebecca "His unit was working on a way to transport people across space and time. The military never seemed to mind throwing money in the furnace for weird research."
    rebecca "They were finally getting fed up with his failures and my guess is that he somehow managed to hijack M.A.L. to target Earth so we all ended up in this shitty standoff situation."
    sis "You are wrong! Dad wouldn't do such a thing!"
    rebecca "Jack is a lying piece of shit that would take advantage of every situation. Like when he ran off with that bimbo over there!"
    mom "Hey!"
    player "Don't call my mom a 'bimbo'!"
    rebecca "Sorry, but this is what happened."
    mom "No it wasn't. Jack said you were never around, always traveling on missions..."
    rebecca "Guess what? This is my job! Someone needs to keep the miners on the belt stations and Jupiter moons calm and working, so you can have all the shiny things on Earth!"
    rebecca "That's what we do - we go there, suppress the riots, beat some of them, kill if we need to, all because you can't keep your hands off the supplies that they send back."
    rebecca "So please, don't even try to blame me for that!"
    sis "Enough! Mom, how did you get here?"
    rebecca "Let me sit down first."
    scene mess_hall_power_outage_11
    rebecca "I was on Mars when I heard what happened here. I convinced my commanders to give me one of the experimental stealth ships that they have there and a chameleon suit and send me here."
    rebecca "My mission is to do reconnaissance and report back, so they can plan how to take the station."
    player "Why didn't they send more people?"
    rebecca "We didn't know if the stealth ship would be able to approach the station undetected, so we couldn't risk sending more. If detected, they could provoke a strike on Earth."
    mom "So let's get to your ship and fly back to Earth."
    rebecca "It's not that easy. First of all, we have only one suit, so we can't all just sneak to the hangar bay undetected."
    rebecca "Second, it's an experimental ship, meaning it's a one man craft. And third, it is already on it's way back to Mars."
    sis "What? Why?"
    rebecca "We can't risk it falling in wrong hands so I was ordered to set the autopilot to bring it back immediately."
    player "I have a few questions."
    $talk_with_rebecca.add_topic("Ask about her scar", "quest_meet_rebecca_ask_scar", quest_meet_rebecca, 0)
    $talk_with_rebecca.add_topic("Ask about her age", "quest_meet_rebecca_ask_age", quest_meet_rebecca, 0)
    $talk_with_rebecca.add_topic("Ask about her suit", "quest_meet_rebecca_ask_suit", quest_meet_rebecca, 0)
    jump ask_rebecca
    
label ask_rebecca:
    scene mess_hall_power_outage_11
    if (talk_with_rebecca.has_topics()):
        jump talk_rebecca
    else:
        player "That's all."
        rebecca "OK, can we all have dinner now? I'm hungry."
        call quest_meet_rebecca_advance_to_sleep_talk from _call_quest_meet_rebecca_advance_to_sleep_talk
        jump wait_action
        
label quest_meet_rebecca_ask_scar:
    player "Where did you get that scar?"
    scene mess_hall_power_outage_13
    rebecca "On Mars. The workers that operated the O2 pumps claimed they don't get their fair share of the mining profits, so they decided to barricade themselves in the engineering section."
    rebecca "We couldn't risk the lives of the miners, so we had to... persuade them to stop their strike."
    rebecca "One of them attacked our unit and got a little too close."
    player "What happened to him?"
    rebecca "Let's just say that he won't be causing any trouble again."
    jump ask_rebecca
    
label quest_meet_rebecca_ask_age:
    scene mess_hall_power_outage_12
    player "I can't believe you are Lana's mom. You look too young!"
    rebecca "Ever heard of the cryo-soldier programme?"
    player "You were frozen!"
    rebecca "The military command decided that it was spending too much money on training soldiers that spent most of their time traveling between Earth and the mining stations."
    rebecca "So they fitted the transport ships with cryo-pods. We spend most of the time in space frozen in the pods."
    player "Isn't it dangerous?"
    rebecca "Not at all. As long as your brain can recover from the constant 'cryo-mission-cryo' cycle, we are fine. We play some fun games while not in the pods."
    player "What games?"
    rebecca flirting "Maybe I'll show you sometime..."
    mom angry "You most certainly will not!"
    rebecca happy "Sorry Greg, looks like your mom is not allowing you to play."
    jump ask_rebecca
    
label quest_meet_rebecca_ask_suit:
    player "What is this suit, that you are wearing?"
    scene mess_hall_power_outage_14
    rebecca "We call it a chameleon suit."
    rebecca "It can morph into any appearance we want and also can make the person wearing it invisible."
    player "Can it morph into a weapon?"
    rebecca "No. Only clothes."
    sis "That might be useful! Can we program the energy processor to make another one?"
    rebecca "I doubt it - it's too complicated and mostly electronics."
    rebecca happy "And by the way my eyes are up here!"
    scene mess_hall_power_outage_13
    player "I'm sorry..."
    rebecca happy "It's OK, I'm just teasing you - look as much as you want to!"
    mom "Greg!"
    jump ask_rebecca
    
#phase 1 auto
label quest_meet_rebecca_sleep_talk:
    hide screen station_rooms
    mom "Greg, can you please come to my bedroom!"
    player "Coming mom..."
    $location = "bedroom"
    $station.move_to(location)
    scene bedroom_mom_5
    mom "Greg, we should think about who's sleeping where."
    player "Oh, right... I guess it will be me and you."
    mom "It's the logical choice - I'm not sharing a room with that bitch and I'll not have it you to sleep with her in one room either."
    scene bedroom_mom_rebecca_1
    rebecca "Did someone mention my name?"
    mom "Well, I said 'bitch', so I guess we did..."
    player "Mom, please, cut it out."
    rebecca happy "I don't mind. I've been called worse."
    rebecca "What were you talking about?"
    mom "Greg will move in to sleep with me and you and Lana will sleep in her room."
    rebecca flirting "Oh, that's not fun, let's think of something else!"
    mom angry "What?!?"
    player "Mom, she's just teasing you. Can't you see?"
    rebecca happy "And it's almost too easy to do it."
    rebecca "Anyway, that sounds like a good arrangement."
    mom "Greg, I'm really tired, let's go to bed early today."
    player "OK mom!"
    call quest_meet_rebecca_advance_to_dreams from _call_quest_meet_rebecca_advance_to_dreams
    jump sleep
    
#phase 2 talk
label quest_meet_rebecca_talk_dreams:
    hide screen station_rooms
    rebecca "Hi Greg!"
    player "Hi Rebecca."
    rebecca "Something on your mind?"
    player "Yeah... I don't know how to ask this, but did you and Lana talk about me last night?"
    rebecca "We did."
    player "Anything in particular or..."
    rebecca happy "Oh, you want to know how Lana feels about you?"
    player "Did she say anything?"
    rebecca happy "She did. She said a {i}huge{/i} amount of stuff for you."
    rebecca happy "She really thinks you are {i}great{/i}."
    rebecca happy "Almost like you are her {i}big{/i} brother."
    player "I think I know where this is going."
    rebecca flirting "Oh, you do?"
    player "Did she say that my dick is bigger than any she has seen?"
    rebecca "Exactly her words."
    player "And then you asked her if she has seen that many."
    rebecca "How do you know this? We locked the door!"
    player "I had a dream about that..."
    rebecca "A dream?"
    player "Yes, a dream. I've been having those since Megan did something to me."
    scene med_bay_rebecca_2
    rebecca "What did you say? Megan?"
    player "Yes, why?"
    rebecca "Do you know who she is?"
    player "Some lab assistant or something?"
    rebecca "She was working on the human / AI interface project."
    rebecca "What did she do to you?"
    player "I don't know. I woke up on the med bed over there and since then I've been having those strange dreams."
    rebecca "What dreams exactly?"
    player "Like I'm in another room, looking at the people there, listening to their conversations..."
    rebecca "That's bad... how did she get that close to you to be able to inject you with the chip?"
    player "What chip? Did she put something in me?"
    rebecca "From what I'm hearing, you are probably connected to the surveillance network of the station."
    player "But your room's cameras are disconnected! It's only mom's bedroom and the VR room that have their cameras connected."
    rebecca "What about this room?"
    player "Well... I turned it on when Megan arrived and we locked her up here..."
    rebecca "Are you sure this is the only camera that you connected?"
    player "...No."
    rebecca "Shit!"
    scene med_bay_rebecca_3
    rebecca "OK, let me try to hack into the system and see if I can learn something more."
    rebecca "..."
    player "Well?"
    rebecca "You did turn on the cameras in the whole section."
    rebecca "But I don't think they were accessed from the outside..."
    rebecca "Except for the bedroom and the VR room cameras."
    rebecca "..."
    rebecca flirting "Oh!"
    player "What?"
    rebecca happy "I just found out how did Megan manage to install the chip in your head."
    player "You did?"
    rebecca happy "There is a recording of the whole 'incident'."
    rebecca flirting "And Lana was right - you are huge!"
    player "..."
    rebecca "Does Lana or your mother know about what happened here?"
    player "I don't think so..."
    rebecca happy "Don't worry, your secret is safe with me. Though thinking of how upset your mother will be, I might just tell her about her son sticking his huge dick in Megan."
    player "Please don't."
    rebecca flirting "Don't worry, that would be too easy. I think I can do better!"
    player "What do you mean?"
    rebecca happy "You'll see!"
    call quest_meet_rebecca_advance_to_talk_earth from _call_quest_meet_rebecca_advance_to_talk_earth
    jump advance_time

#phase 3 terminal
label quest_meet_rebecca_talk_earth:
    hide screen station_rooms
    scene comm_rebecca_1
    rebecca "What are you doing here?"
    player "I was just..."
    rebecca "Look, Lana told me everything about that Earth's scumbag."
    rebecca "I know all about your arrangement with them and I don't mind."
    rebecca "But they can't know who I am."
    player "Why?"
    rebecca "We are Black Ops. We don't exist."
    rebecca "Just tell him I'm a survivor from the station or something."
    player "OK, keep quiet then."
    scene comm_rebecca_2
    player "This is Greg from Antares..."
    male "Hi Greg! I wanted to talk with you about..."
    player "You listen to me first! You know that I'm sleeping in the bedroom, right?"
    male "We saw that, yes."
    male "Is it because of the other woman on the station?"
    player "You saw her, huh?"
    male "We all did! Man she is something!"
    male "Tits, ass... I can't believe I've never seen her before!"
    male "She is from the station, right?"
    player "She is, but..."
    male "But nothing! We had access to all the station files and I personally have gone through all females looking for potential actresses."
    male "I have never seen her before."
    player "That's because..."
    rebecca "(whispering){i}Don't tell him!{/i}"
    player "She was transfered here just before the incident and haven't logged in."
    player "She was still in her ship in the hangar when it all began."
    rebecca "(whispering){i}Good one!{/i}"
    player "But I didn't call to talk about that. I need your equipment turned off for the night."
    player "I can't have you using the equipment in the bedroom while I'm with my mother there."
    male "I'll need something in return!"
    player "What?"
    male "Some action with the new chick in the VR room!"
    rebecca flirting "(whispering){i}I don't mind.{/i}"
    player "OK, deal!"
    player "But how will I know that you keep your end of the deal?"
    male "I guess you'll have to trust me!"
    male "Over and out!"
    scene comm_rebecca_3
    player "You know what he meant by that, right?"
    rebecca happy "Of course I do!"
    rebecca flirting "Meet me at the beach and we will give them more than they bargained for!"
    call quest_meet_rebecca_advance_to_beach from _call_quest_meet_rebecca_advance_to_beach
    jump advance_time
    
#phase 4 talk
label quest_meet_rebecca_beach:
    hide screen station_rooms
    player "Hey Rebecca, do you want some sunblock?"
    scene beach_rebecca_1
    rebecca "Yes, thank you!"
    rebecca "Should I take my top off?"
    player "It's up to you... do you like tan lines?"
    rebecca "God no!"
    rebecca flirting "Let me take it off."
    scene beach_rebecca_2
    rebecca "Am I making you uncomfortable?"
    player "No, I do this with Lana and mom too."
    scene beach_rebecca_3
    rebecca "Your mom does not look like the type of person that enjoys being naked in front of her son."
    player "She is not exactly naked - she turns around to unstrap her top and after I'm done with her back, she lies on her stomach."
    player "You can't really see anything"
    scene beach_rebecca_4
    rebecca "Like that?"
    player "Yeah, something like that..."
    scene beach_rebecca_5
    player "Shit someone's coming!"
    scene beach_rebecca_6
    player "It's my mom, cover yourself!"
    rebecca flirting "This will be fun!"
    scene beach_rebecca_7
    mom "Do you mind if I join you?"
    player "Not at all!"
    rebecca "In fact I was hoping that you would join us!"
    mom "And why are you naked then?"
    rebecca "I hate tan lines and I had to take my top off, so Greg can put some sunscreen on me."
    mom "Did he?"
    rebecca "Not yet."
    scene beach_rebecca_8
    rebecca "Do you mind doing my front first?"
    mom angry "What the fuck are you doing!"
    rebecca happy "What? Afraid that you son will see some skin?"
    mom angry "I don't think it's appropriate..."
    rebecca happy "Appropriate? Look at him! Maybe if he was used to being around naked women, he wouldn't be staring like this now."
    mom angry "So you suggest that I should walk around naked with my son right here?"
    rebecca happy "Maybe you should!"
    mom angry "Maybe I would!"
    rebecca happy "You don't have the guts to do it!"
    scene beach_rebecca_9
    mom "Oh yeah? What do you have to say now?"
    rebecca "Nice tits!"
    scene beach_rebecca_10
    rebecca "Which do you like best? Your mom's or mine?"
    player "Uhhh..."
    mom "This is ridiculous!"
    rebecca flirting "Don't worry, I already got my answer poking from your pants just before your mom arrived."
    scene beach_rebecca_11
    rebecca happy "I'm leaving and while I do that, you can think about whose ass you like better."
    mom "God, I hate her!"
    player "Mom, she is just teasing you."
    mom "I know and she is still making me mad!"
    mom angry "And please cover yourself!"
    player "Sorry mom..."
    mom "I'm sorry that I made you... have an erection... Please just go and... have a cold shower or something..."
    call quest_meet_rebecca_advance_to_talk_again from _call_quest_meet_rebecca_advance_to_talk_again
    jump advance_time
    
#phase 5 terminal
label quest_meet_rebecca_talk_again:
    hide screen station_rooms
    scene comm_rebecca_1
    rebecca "Mind if I stay?"
    player "Not at all. I was going to ask them if they kept their part of the deal."
    rebecca "Just don't let them know I'm here."
    player "I won't."
    player "This is Greg from Antares."
    male "Hi Greg! Man, what a show!"
    male "The new girl sure knows how to push your mom's buttons!"
    player "Yeah, she does!"
    player "So did you like the show?"
    male "We sure did!"
    male "And all our customers loved it!"
    male "They are asking for more shows with her."
    rebecca flirting "(whispering) {i}This can be arranged...{/i}"
    male "Anyway, I don't suppose you called me just to ask if we liked her."
    player "You are right. I want to know why you didn't keep your part of the deal?"
    male "What are you talking about?"
    player "You promised to turn off the equipment in our bedroom during the night."
    male "I did..."
    player "But I keep having those dreams."
    player "And my mom caught me having an erection during the night and even gave me a handjob, so we could get some sleep."
    male "She did? Now I'm sorry we turned off everything in the room - our ratings would've gone through the roof with that!"
    rebecca happy "(whispering) {i}Now I'm jealous!{/i}"
    male "I can promise you we don't have anything to do with that! I wish we do, though..."
    player "OK, this was everything I wanted to know..."
    male "We can hang up then?"
    player "Thank you, over and out!"
    rebecca flirting "So they would have liked your mom watching you jerk off more than my show on the beach?"
    player "What do you expect - they are all a bunch of perverts down there..."
    rebecca happy "The equipment was turned off and your mother still gave you a handjob..."
    rebecca happy "Did you have to beg her to do it or you just made up some excuse... like having a rare disease and your wrists hurt?"
    player "Well... I didn't have to 'beg' her, neither did I lied to her... she just sort of... did it"
    rebecca happy "And she called {i}me{/i} a slut! What a hypocrite!"
    rebecca flirting "Anyway, I won't let her beat me at my own game..."
    rebecca flirting "And speaking of games, how about we play one?"
    player "Game? What game?"
    rebecca flirting "The fun kind."
    rebecca "But we will need a suitable setting! I think the VR room will do, but we would still need to re-fit it."
    rebecca "Meet me at the engineering room tomorrow and we will figure it out."
    player "OK"
    rebecca happy "Have a nice dream! You know... the kind of dream that gets you a handjob."
    call quest_meet_rebecca_advance_to_engineering from _call_quest_meet_rebecca_advance_to_engineering
    jump sleep
    
#phase 6
label quest_meet_rebecca_engineering:
    hide screen station_rooms
    rebecca "Hi Greg!"
    player "Hey! So, about that game..."
    rebecca happy "Oh, you seem really interested?"
    player "I am - there is not much entertainment here."
    rebecca "OK, as I've told you, the game is fun, but we will need the VR room re-fitted to something else."
    player "What?"
    rebecca "A bar."
    player "Is it a drinking game?"
    rebecca flirting "Even better - a strip game!"
    player "I like where this is going!"
    rebecca "I'm sure you do. Anyway, I can re-fit the room, but it will require a lot of energy."
    player "How much?"
    rebecca "At least 500kWh for the room..."
    player "I think we can spare that..."
    rebecca "And I'll need an additional 350kWh for an outfit."
    player "What kind of outfit?"
    rebecca flirting "You'll see."
    player "Can't you use the chameleon suit to mimic some clothes?"
    rebecca flirting "I can, but how do you suggest I can strip if it's just the suit?"
    rebecca flirting "We will miss the whole fun!"
    player "OK, 850kWh is manageable..."
    rebecca "Also the efficiency of the panels needs to be at 100\% to be able to sustain the VR room."
    player "So 850kWh stored in the battery, efficiency at 100\%. Anything else?"
    rebecca "Once you manage that, find me in the VR room during the day and we can set it up for the evening."
    rebecca flirting "It will be best if everyone else is asleep."
    player "Will do."
    call quest_meet_rebecca_advance_to_setup_game from _call_quest_meet_rebecca_advance_to_setup_game
    call advance_time from _call_advance_time
    
#phase 7
label quest_meet_rebecca_setup_game:
    hide screen station_rooms
    player "I think everything is ready for this evening."
    rebecca "Your mom and Lana are usually asleep at midnight, so let's meet at the engineering room and we will set it up"
    player "Should I bring something?"
    rebecca flirting "Only your clothes and your dick. I intend to see it tonight."
    player "What if I win?"
    rebecca flirting "Then I will definitely see it!"
    call quest_meet_rebecca_advance_to_play_game from _call_quest_meet_rebecca_advance_to_play_game
    jump advance_time
    
#phase 8
label quest_meet_rebecca_play_game:
    hide screen station_rooms
    player "Ready?"
    rebecca happy "Someone is in a hurry."
    rebecca happy "I'm just finishing the upload of the new setting for the VR room."
    if (energy < 850 or efficiency < 100):
        rebecca "We don't have enough energy stored in the batteries."
        player "We don't?"
        rebecca "Yes. I've told you - we need 850kWh and the efficiency needs to be at 100\%"
        player "OK, let's leave it for another day."
        rebecca "Sweet dreams!"
        jump sleep
    else:
        $energy = energy - 850
        rebecca "..."
        rebecca flirting "Done! Go there and wait for me, I have to swing by the energy processor to get my clothes and something to drink."
        player "Don't be long..."
        rebecca happy "I won't."
        scene bar_1
        player "Wow! This is good!"
        scene bar_rebecca_1
        rebecca happy "Are you ready?"
        player "Yes!"
        rebecca "Do you want me to explain the rules?"
        call quest_meet_rebecca_finish from _call_quest_meet_rebecca_finish
        jump start_event_rebecca_dice