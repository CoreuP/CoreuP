label help_black_market:
    player "[quest_black_market.help]"
    if quest_black_market.finished:
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

#phase 0 terminal
label start_quest_black_market:
    $talk_with_terminal.add_topic("Call Earth", "call_earth_night", quest_black_market, 0)
    $quest_black_market.active = True
    $quest_black_market.location = "comm"
    $quest_black_market.alone = True
    $quest_black_market.req_clock = 2
    $quest_black_market.clock_mode = "at_most"
    $quest_black_market.help = "{i}The day shift on Earth station is not willing to talk, I should try during the night.{/i}"
    return
    
#phase 1 auto
label quest_black_market_advance_to_spy_sis_shower:
    $quest_black_market.advance_phase()
    $quest_black_market.reset()
    $quest_black_market.req_clock = 8
    $quest_black_market.clock_mode = "exactly"
    $quest_black_market.help = "{i}I have to spy on Lana while she is taking a bath. The guy from Earth said he will take care of the lock.{/i}"
    return
    
#phase 2 auto
label quest_black_market_advance_to_breakfast:
    $quest_black_market.advance_phase()
    $quest_black_market.reset()
    $quest_black_market.req_clock = 9
    $quest_black_market.clock_mode = "exactly"
    $quest_black_market.location = "mess_hall"
    $quest_black_market.sis_location = "mess_hall"
    $quest_black_market.mom_location = "mess_hall"
    $quest_black_market.help = "{i}I'm in trouble now - mom saw me spying on Lana...{/i}"
    return

#phase 3 talk
label quest_black_market_advance_to_talk_sis:
    $talk_with_sis.add_topic("Tell her about Earth", "black_market_talk_sis", quest_black_market, 3)
    $quest_black_market.advance_phase()
    $quest_black_market.reset()
    $quest_black_market.location = "shared_beds"
    $quest_black_market.sis_location = "shared_beds"
    $quest_black_market.req_clock = 7
    $quest_black_market.clock_mode = "at_least"
    $quest_black_market.help = "{i}I'll talk with Lana while we are alone in our bedroom.{/i}"
    return
    
#phase 4 terminal
label quest_black_market_advance_to_call_earth_2:
    $talk_with_terminal.add_topic("Ask about the lock", "black_market_call_earth_2", quest_black_market, 4)
    $quest_black_market.advance_phase()
    $quest_black_market.reset()
    $quest_black_market.location = "comm"
    $quest_black_market.alone = True
    $quest_black_market.req_clock = 2
    $quest_black_market.clock_mode = "at_most"
    $quest_black_market.help = "{i}I have to talk with Earth again during the night.{/i}"
    return
    
#phase 5 talk
label quest_black_market_advance_to_sis_vr:
    $talk_with_sis.add_topic("Talk about making a beach", "black_market_sis_vr", quest_black_market, 5)
    $quest_black_market.advance_phase()
    $quest_black_market.reset()
    $quest_black_market.location = "vr_room"
    $quest_black_market.sis_location = "vr_room"
    $quest_black_market.help = "{i}Lana has been spending some time in the VR room lately - let's talk with her there.{/i}"
    return
    
#phase 6 talk
label quest_black_market_advance_to_mom_vr:
    $talk_with_mom.add_topic("Talk about making a beach", "black_market_mom_vr", quest_black_market, 6)
    $quest_black_market.advance_phase()
    $quest_black_market.reset()
    $quest_black_market.location = "vr_room"
    $quest_black_market.mom_location = "vr_room"
    $quest_black_market.help = "{i}Lana has agreed to make the VR room into a beach. Let's see if I can convince mom too.{/i}"
    return

#phase 7 terminal
label quest_black_market_advance_to_call_earth_3:
    $talk_with_terminal.add_topic("Make the VR room into a beach", "black_market_call_earth_3", quest_black_market, 7)
    $quest_black_market.advance_phase()
    $quest_black_market.reset()
    $quest_black_market.location = "comm"
    $quest_black_market.alone = True
    $quest_black_market.req_clock = 2
    $quest_black_market.clock_mode = "at_most"
    $quest_black_market.help = "{i}Let's talk with Earth again and let them beam the energy required for the VR room.{/i}"
    return
    
label quest_black_market_finish:
    $quest_black_market.advance_phase()
    $quest_black_market.reset()
    $global_events.black_market = True
    $quest_black_market.help = "{i}I have established a relationship with the night shift on Earth. That's good enough for now...{/i}"
    $quest_black_market.finished = True
    return
    
#phase 0
label call_earth_night:
    player "Anybody there?"
    male "Hello? Is this someone from Antares?"
    player "Yes! Who are you?"
    male "This doesn't matter right now. We don't have much time."
    player "Are you from Control Center \"Liberty\"?"
    male "Yes I am, but we are under orders not to talk with you."
    player "And why are you talking with me then?"
    male "Because I think we might be of some help to each other."
    player "How is that?"
    male "Few of the guys here are running a betting ring and I think you can help me swing the odds in my favor."
    player "A betting ring? I don't see how I can help you win some sporting bets."
    male "We are not betting on sports. That's too boring. We are betting on your daily interactions."
    player "What?"
    male "For example I have a $100 bet that says tomorrow you will spy on your sister in the bathroom."
    player "And how would you know that?"
    male "If you help me win that bet, I might tell you."
    player "Tell me now, or I won't do it!"
    male "I need to know that I can trust you. Spy on your sister at 8:00AM in your mother's bathroom and I will consider it."
    player "If you know so much, I are probably aware that Lana locks the door while she is in the bathroom."
    male "Leave that to me - you will be able to open the door whenever you wish."
    $global_events.sis_lock_door = False
    $global_events.mom_lock_door = False
    male "Over and out."
    player "{i}I don't have anything to loose, so I might as well do it.{/i}"
    call quest_black_market_advance_to_spy_sis_shower from _call_quest_black_market_advance_to_spy_sis_shower
    jump wait_action
    
#phase 1
label black_market_spy_sis_shower:
    hide screen station_rooms
    scene door_1
    player "{i}Here is the door to mom's bedroom.{/i}"
    player "{i}I hope Lana won't notice me peeking at her.{/i}"
    scene shower_sis_1
    player "{i}I wonder how do those guys know if I had peeked at her or not...{/i}"
    scene shower_sis_2
    player "{i}Not that I'm complaining - Lana has a really beautiful body.{/i}"
    scene shower_sis_3
    mom angry "Greg!"
    scene door_mom_1
    mom angry "What are you doing here?"
    player "I was just..."
    mom angry "I can't believe it! Spying on your sister while she is in the shower!"
    mom angry "How messed up is that!"
    player "I..."
    mom angry "Not another word, young man!"
    mom "We will talk about that at breakfast!"
    scene door_1
    player "{i}I'm really in trouble now...{/i}"
    call quest_black_market_advance_to_breakfast from _call_quest_black_market_advance_to_breakfast
    jump wait_action
    
#phase 2
label black_market_breakfast:
    hide screen station_rooms
    scene mess_hall_mom_sis_1
    mom angry "Lana, do you know what just happened?"
    sis "What?"
    mom "I caught Greg spying on you while you were in the shower!"
    sis "Again?"
    mom "What do you mean \"again\"?"
    sis "I caught him spying on me too."
    mom "Why didn't you tell me?"
    sis "Come on - it's not a big deal."
    mom "Not a big deal?!? How can you say such a thing - he's your brother!"
    sis "Step brother. And it's not like he has a choice - he's 18 and we are the only women around."
    player "She's right, mom."
    mom "Still, this is unacceptable! Earth said that they won't risk a rescue mission, which means that we will be stuck here for quite some time."
    mom "You'll have to learn to control yourself."
    player "I'll try..."
    mom "Good! Now let's eat and try to forget that this ever happened."
    call quest_black_market_advance_to_talk_sis from _call_quest_black_market_advance_to_talk_sis
    jump wait_action
    
#phase 3
label black_market_talk_sis:
    hide screen station_rooms
    scene shared_beds_sis_9
    sis "So you were peeping on me again?"
    player "Look, Lana..."
    sis "What I really want to know is how did you manage to unlock the door."
    player "I don't know if I should tell you this..."
    sis "What?"
    player "I finally got in contact with Earth."
    sis "Really?!?"
    player "Yes. There are a few people down there, who seem to be monitoring the station."
    sis "Who are they?"
    player "I don't know. I only spoke with one of them and he said that he can help us if we do something for him."
    sis "Like what?"
    player "Like me spying on you."
    sis "Sounds weird."
    player "It is weird. He refused to tell me how he will know if I spied on you or not."
    player "I wonder what else do they know about us."
    sis "They probably managed to connect to the security cameras."
    player "But I thought you tuned them off to prevent M.A.L. from knowing that we are alive."
    sis "I did. That's what puzzles me..."
    sis "Talk with them again and try to find out what do they know and how they can help us."
    player "I will."
    player "And thank you for standing up for me when mom was angry at me."
    sis "Don't mention it. I really think it's not your fault."
    call quest_black_market_advance_to_call_earth_2 from _call_quest_black_market_advance_to_call_earth_2
    jump wait_action
    
#phase 4
label black_market_call_earth_2:
    hide screen station_rooms
    male "Identify yourself!"
    player "It's Greg from Antares."
    male "Nice to hear from you again! Thanks for the favor. Nobody else thought you would be able to unlock the door while your sister was in the bathroom."
    player "But I didn't unlock it - you did."
    male "Don't ever say that again! You managed to unlock it, understand?"
    player "I guess your buddies won't be happy to learn that you made me spy on my sister, so you can win that bet?"
    male "..."
    player "Tell me how did you know if I spied on her or not and I might be willing to keep quiet about your help."
    male "OK, here is the deal..."
    male "That room with the shower is \"special\"."
    male "Have you wondered why is it different for all the other rooms and doesn't really look like something that belongs on a space station?"
    player "I thought there were some high class people living in it before the incident."
    male "Not at all - that whole part of the station is a studio for making low-G movies."
    player "Low-G movies? like in \"low gravity\" or what?"
    male "Exactly - it's a niche market but there are people that get turned on but that kind of stuff."
    player "Wait. \"Turned on\" as in..."
    male "Yes. Porn."
    player "No way - this is a porn studio?"
    male "And we still have access to the feed from that room."
    player "And what about the rest of the section? Do you have access to the security cameras?"
    male "Unfortunately we lost that right after the incident. Do you know what happened to them?"
    player "No."
    male "Hmmm - you don't sound too convincing... Anyway - if you manage to get the other VR room working again, we might come to some sort of a deal."
    player "What kind of a deal?"
    male "We can beam the necessary energy to sustain the VR in exchange for access to the feed."
    player "And everything that happens there will be recorded?"
    male "Yes. Do you care?"
    player "Not at all."
    male "So you talk with the others to convince them to turn on the VR room and I will arrange the beaming of the energy to the station."
    player "We have a deal!"
    call quest_black_market_advance_to_sis_vr from _call_quest_black_market_advance_to_sis_vr
    jump wait_action
    
#phase 5
label black_market_sis_vr:
    hide screen station_rooms
    player "I talked with Earth."
    sis "What did they say?"
    player "They said they will help us get the VR room running if we allow them to watch."
    sis "Watch what?"
    player "Us."
    sis "So I can enjoy the beach here if some pervs are peeping on me?"
    player "Pretty much..."
    sis "Just like if we were on Earth!"
    player "So you are up for this?"
    sis "Of course!"
    player "I should talk with mom then."
    call quest_black_market_advance_to_mom_vr from _call_quest_black_market_advance_to_mom_vr
    jump wait_action
    
#phase 6
label black_market_mom_vr:
    hide screen station_rooms
    player "Hi mom, what are you doing?"
    mom "Looking for ways to make this room require less energy."
    mom "Your sister looks depressed and I wanted to make her happy."
    player "What if I ask Earth to beam us the needed energy for this room to become a beach?"
    mom "I already tried - they don't even want to talk with us."
    player "I think I might convince them."
    mom "OK then - if you do, plaese configure this room into a beach, so Lana will be happier."
    player "OK, mom."
    call quest_black_market_advance_to_call_earth_3 from _call_quest_black_market_advance_to_call_earth_3
    jump wait_action
    
#phase 7
label black_market_call_earth_3:
    hide screen station_rooms
    player "This is Greg from station \"Antares\""
    male "Hi, Greg! Did you manage to convince the others for the VR room?"
    player "I did. But we can't spare any energy for this."
    male "Don't worry, we will beam you all the required energy. Just make sure the women wear sexy swimsuits! We need to keep our customers happy!"
    player "Hey! this is my mom and step sister that you are talking about!"
    male "Even better! Some incest action will spice things up!"
    player "... Just make sure you prepare the room!"
    male "It will be ready tomorrow. Remember - we want some skin showing in that room!"
    male "Over and out!"
    player "Over and out..."
    call quest_black_market_finish from _call_quest_black_market_finish
    jump wait_action