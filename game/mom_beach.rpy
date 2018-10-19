label help_mom_beach:
    player "[quest_mom_beach.help]"
    if quest_mom_beach.finished:
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
label start_quest_mom_beach:
    $talk_with_mom.add_topic("Ask her if she would wear the bikini", "quest_mom_beach_convince_mom", quest_mom_beach, 0)
    $quest_mom_beach.active = True
    $quest_mom_beach.location = "vr_room"
    $quest_mom_beach.mom_location = "vr_room"
    $quest_mom_beach.help = "{i}I should try to convince mom to wear the bikinis or Earth might shut us down.{/i}"
    return
    
#phase 1 terminal
label quest_mom_beach_advance_to_make_bikini:
    $quest_mom_beach.cost = 400 - 2 * player_stat.programming
    $quest_mom_beach.chance = 10 + player_stat.programming * 9 / 10
    $talk_with_terminal.add_topic("Make mom's bikini (-%paramkWh, %param% success)", "quest_mom_beach_make_bikini", quest_mom_beach, 1, ["cost", "chance"])
    $quest_mom_beach.advance_phase()
    $quest_mom_beach.reset()
    $quest_mom_beach.location = "life_support"
    $quest_mom_beach.alone = True
    $quest_mom_beach.help = "{i}My mom won't wear those bikinis, so I need to learn how to program the processor and try to make her new ones.{/i}"
    return
    
#phase 2 talk
label quest_mom_beach_advance_to_give_bikini:
    $talk_with_mom.add_topic("Give the new bikini", "quest_mom_beach_give_bikini", quest_mom_beach, 2)
    $quest_mom_beach.advance_phase()
    $quest_mom_beach.reset()
    $quest_mom_beach.location = "bedroom"
    $quest_mom_beach.mom_location = "bedroom"
    $quest_mom_beach.req_clock = 21
    $quest_mom_beach.clock_mode = "at_least"
    $quest_mom_beach.help = "{i}I made a new set of bikini, let's give them to mom in the evening while she is in her room.{/i}"
    return
    
#phase 3 talk
label quest_mom_beach_advance_to_mom_beach:
    $talk_with_mom.add_topic("Ask her is she wants some sunblock", "quest_mom_beach_mom_beach", quest_mom_beach, 3)
    $quest_mom_beach.advance_phase()
    $quest_mom_beach.reset()
    $quest_mom_beach.location = "vr_room"
    $quest_mom_beach.mom_location = "vr_room"
    $quest_mom_beach.help = "{i}Let's check on mom while she is enjoying the beach.{/i}"
    return
    
#phase 4 talk
label quest_mom_beach_finish:
    $quest_mom_beach.advance_phase()
    $quest_mom_beach.reset()
    $global_events.mom_beach = True
    if (global_events.sis_beach):
        call start_quest_meet_megan from _call_start_quest_meet_megan_1
    $quest_mom_beach.help = "{i}Mom seems to be enjoying the beach as much as Lana and doesn't mind me putting sunblock on her every day.{/i}"
    $quest_mom_beach.finished = True
    call add_event_mom_strip_beach from _call_add_event_mom_strip_beach
    return
    
#phase 0
label quest_mom_beach_convince_mom:
    hide screen station_rooms
    player "Hi mom!"
    mom "Hi Greg! This beach is really amazing. The VR equipment in this room is far beyond anything that I have seen."
    player "It really is."
    mom "I wonder why there is such advanced equipment on a military research station. It doesn't make sense..."
    player "They probably used this for practice. You know - shooting stuff."
    mom "I doubt it - a simple holo room would be enough for that."
    player "I guess you're right... anyway, I wanted to ask you why won't wear the suit I made for you?"
    mom "I told you already - it's too revealing."
    player "But I put so much effort, not to mention the energy I spent for producing it."
    mom "I know and I'm thankful for that, but it's not my type."
    player "Not your type?"
    mom "I don't think it's appropriate."
    mom "I'm not happy with Lana wearing it in front of you either, but I can't just forbid her to."
    player "Why?"
    mom "Have you forgotten that I caught you spying on her while she was taking a shower?"
    player "I'm sorry mom."
    mom "As Lana said, it's not like there are other women around, so we should expect you to be \"interested\" in us."
    mom "But I think we should try not to excite you."
    player "So you are not mad at me anymore?"
    mom "Of course not. But I won't wear such revealing bikinis."
    player "But this is a beach - what do you expect from a bikini to look like?"
    mom "At least to hide my private parts! Did you see Lana's ass?"
    mom happy "Why am I asking you this - of course you did!"
    player "So if I make a new one that is not so revealing, you will wear them?"
    mom "I will."
    player "I'll see what I can do then..."
    call activate_work_learn_programming from _call_activate_work_learn_programming
    call quest_mom_beach_advance_to_make_bikini from _call_quest_mom_beach_advance_to_make_bikini
    jump wait_action
    
#phase 1
label quest_mom_beach_make_bikini:
    hide screen station_rooms
    if (energy < quest_mom_beach.cost):
        player "We don't have enough energy stored in the batteries."
        $talk_with_terminal.add_topic("Make mom's bikini (-%paramkWh, %param% success)", "quest_mom_beach_make_bikini", quest_mom_beach, 1, ["cost", "chance"])
        jump map
    else:
        player "Here goes nothing..."
        $energy -= quest_mom_beach.cost
        $rand = renpy.random.randint(0, 100)
        if (rand <= quest_mom_beach.chance):
            player "I did it!"
            player "I hope mom would like them."
            call quest_mom_beach_advance_to_give_bikini from _call_quest_mom_beach_advance_to_give_bikini
        else:
            player "Fuck!"
            player "What a waste of energy. I just hope I can recycle as much as I can from that."
            $energy += quest_mom_beach.cost * 9 / 10
            $talk_with_terminal.add_topic("Make mom's bikini (-%paramkWh, %param% success)", "quest_mom_beach_make_bikini", quest_mom_beach, 1, ["cost", "chance"])
        jump wait_action
        
#phase 2
label quest_mom_beach_give_bikini:
    hide screen station_rooms
    player "Mom, I think I managed to make a new set of bikini, that you'll like."
    mom "Let me see!"
    mom "Hmmm..."
    mom "They look OK, let me try them on."
    mom "Turn around please! You can enjoy the view of the Earth beneath us while I get changed."
    scene bedroom_wall_1
    mom "They are definitely better than the previous ones..."
    mom "OK, you can turn around now."
    scene bedroom_mom_bikini_1
    mom "How do I look?"
    player "You look beautiful mom!"
    scene bedroom_mom_bikini_2
    mom "Thank you!"
    mom "Even though I'm sure you are saying this just because I'm your mother."
    player "No, I mean it. You really look good in those!"
    scene bedroom_mom_bikini_3
    mom "And how about from behind?"
    mom "Do you think they are too revealing?"
    player "Not at all!"
    scene bedroom_mom_bikini_4
    mom "So you don't like them then?"
    player "I didn't say that!"
    scene bedroom_mom_bikini_5
    mom happy "I'm just teasing you!"
    mom "Thank you for the effort to make this for me!"
    mom "We can hang out at the beach together."
    player "I'd really like that."
    $global_events.mom_bikini = True
    call quest_mom_beach_advance_to_mom_beach from _call_quest_mom_beach_advance_to_mom_beach
    jump wait_action
    
#phase 3
label quest_mom_beach_mom_beach:
    hide screen station_rooms
    player "Hi mom!"
    mom "Hi Greg! I wanted to thank you for the bikinis - they are really comfortable."
    player "I'm glad you like them."
    player "That VR beach is really something..."
    mom "I wanted to ask you about the sun though - do you think I should have some sun screen?"
    player "Of course you should - the light has the same intensity and spectrum as if you are at a real beach down on Earth."
    mom "Oh, I did know that..."
    mom "Can you help me?"
    player "Sure."
    player "Turn around."
    scene beach_mom_5
    mom "Let me take off my bra too. I hate having tan lines."
    mom smiling "Just please don't get too excited..."
    player "I won't."
    scene beach_mom_6
    mom "Make sure you don't get distracted and miss a spot!"
    player "I won't."
    player "All done!"
    scene beach_mom_7
    mom "Thank you!"
    player "You're welcome."
    call quest_mom_beach_finish from _call_quest_mom_beach_finish
    jump wait_action
