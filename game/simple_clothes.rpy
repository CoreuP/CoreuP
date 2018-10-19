label help_simple_clothes:
    player "[quest_simple_clothes.help]"
    if quest_simple_clothes.finished:
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

#phase 0
label start_quest_simple_clothes:
    $quest_simple_clothes.active = True
    $quest_simple_clothes.req_day = 1
    $quest_simple_clothes.day_mode = "exactly"
    $quest_simple_clothes.req_clock = 7
    $quest_simple_clothes.help = "{i}I should talk with Lana in the morning{/i}"
    return
    
#phase 1 terminal
label quest_simple_clothes_advance_to_check_processor:
    $talk_with_terminal.add_topic("Erase the clothes from the program", "check_processor", quest_simple_clothes, 1)
    $quest_simple_clothes.advance_phase()
    $quest_simple_clothes.req_day = -1
    $quest_simple_clothes.req_clock = -1
    $quest_simple_clothes.location = "mess_hall"
    $quest_simple_clothes.alone = True
    $quest_simple_clothes.help = "{i}I should check the energy processor in the mess hall and see if it can make some clothes. It will be better if there is no one else around.{/i}"
    return

#phase 2 terminal
label quest_simple_clothes_advance_to_program_processor:
    $talk_with_terminal.add_topic("Erase the clothes from the program", "program_processor", quest_simple_clothes, 2)
    $quest_simple_clothes.advance_phase()
    $quest_simple_clothes.req_day = -1
    $quest_simple_clothes.req_clock = -1
    $quest_simple_clothes.location = "life_support"
    $quest_simple_clothes.alone = True
    $quest_simple_clothes.help = "{i}I have to remove all the clothes from the program, but I need to do it from the life support room. I will need to be alone while doing it."
    return
    
#phase 3 auto
label quest_simple_clothes_advance_to_checking_tags:
    $quest_simple_clothes.advance_phase()
    $quest_simple_clothes.reset()
    $quest_simple_clothes.req_day = day + 1
    $quest_simple_clothes.day_mode = "at_least"
    $quest_simple_clothes.req_clock = 7
    $quest_simple_clothes.clock_mode = "at_least"
    $quest_simple_clothes.sis_location = "shared_beds"
    $quest_simple_clothes.mom_location = "any"
    $quest_simple_clothes.location = "shared_beds"
    $quest_simple_clothes.help = "{i}Let's wait for Lana to spend another night in the suit. I bet she will be much more cooperative then.{/i}"
    return
    
#phase 4 terminal
label quest_simple_clothes_advance_to_restoring_clothes:
    $talk_with_terminal.add_topic("Restore the clothes in the program", "restore_clothes", quest_simple_clothes, 4)
    $quest_simple_clothes.reset()
    $quest_simple_clothes.advance_phase()
    $quest_simple_clothes.location = "life_support"
    $quest_simple_clothes.alone = True
    $quest_simple_clothes.help = "{i}I will have to restore some of the clothes into the program at the life support room. There should be no one else around while I'm doing it."
    return
    
#phase 5 terminal
label quest_simple_clothes_advance_to_making_clothes:
    $talk_with_terminal.add_topic("Make the clothes", "make_clothes", quest_simple_clothes, 5)
    $quest_simple_clothes.reset()
    $quest_simple_clothes.advance_phase()
    $quest_simple_clothes.location = "mess_hall"
    $quest_simple_clothes.alone = True
    $quest_simple_clothes.energy = 350
    $quest_simple_clothes.help = "{i}I need to use the energy processor to make clothes for Lana and mom, but that will require 350 energy.{/i}"
    return
    
#phase 6 talk
label quest_simple_clothes_advance_to_giving_clothes_sis:
    $talk_with_sis.add_topic("Give her the clothes", "give_clothes_sis", quest_simple_clothes, 6)
    $quest_simple_clothes.reset()
    $quest_simple_clothes.advance_phase()
    $quest_simple_clothes.location = "shared_beds"
    $quest_simple_clothes.sis_location = "shared_beds"
    $quest_simple_clothes.help = "{i}I have the clothes. Let's give them to Lana when we are alone in the sleeping quarters.{/i}"
    return
    
#phase 7 auto
label quest_simple_clothes_advance_to_giving_clothes_mom:
    $quest_simple_clothes.reset()
    $quest_simple_clothes.advance_phase()
    $quest_simple_clothes.req_clock = 19
    $quest_simple_clothes.clock_mode = "exactly"
    $quest_simple_clothes.location = "mess_hall"
    $quest_simple_clothes.sis_location = "mess_hall"
    $quest_simple_clothes.mom_location = "mess_hall"
    $quest_simple_clothes.help = "{i}I will give mom her clothes while we are having dinner at 19:00{/i}"
    return
    
label quest_simple_clothes_finish:
    $quest_simple_clothes.reset()
    $quest_simple_clothes.advance_phase()
    $global_events.simple_clothes = True
    $quest_simple_clothes.help = "{i}There is nothing else to be done about this.{/i}"
    $quest_simple_clothes.finished = True
    return
    
#phase 0
label day_1_morning:
    hide screen station_rooms
    scene shared_beds_sis_1
    show screen day_time
    player "Good morning Lana! Did you sleep well?"
    sis "Not at all. This suit is awful!"
    player "Well... you could sleep without it..."
    sis smiling "Yeah, you wish! I'm wearing only my panties underneath it."
    player "Didn't that woman from Earth say that the energy processor could produce not only food but clothes too?"
    sis "It should be possible. Food is not different from any other item - you need to arrange the atoms into molecules and then into objects."
    sis smiling "If you knew a bit of physics, you would know this!"
    player smiling "If you knew a bit of programming, you'd be able to program the energy processor to produce the clothes."
    sis "I bet there already are clothes in the list of items that the processor can produce..."
    player "You don't sound too confident."
    sis angry "I don't have time for this! I'm going to mom's room to take a shower."
    scene shared_beds_1
    player "{i}Lana needs clothes and seems willing to do anything to get them.{/i}"
    player "{i}... This gives me an idea.{/i}"
    player "{i}I'll need to go to the mess hall and check if the energy processor has some in it's list.{/i}"
    player "{i}But I'd better be alone in the room for that - I don't want anyone else to see what I'm about to do.{/i}"
    call quest_simple_clothes_advance_to_check_processor from _call_quest_simple_clothes_advance_to_check_processor
    jump wait_action
    
#phase 1
label check_processor:
    hide screen station_rooms
    scene mess_hall_1
    player "{i}There is the energy processor.{/i}"
    player "{i}Let's check if it has any clothes in the list of available items...{/i}"
    player "{i}... Seems Lana was right - there are some basic clothes. Let's see if I can make them disappear...{/i}"
    player "{i}... Looks like the processor can't be programmed from here. I should check the life support room - there was a terminal.{/i}"
    call quest_simple_clothes_advance_to_program_processor from _call_quest_simple_clothes_advance_to_program_processor
    jump wait_action
    
#phase 2
label program_processor:
    hide screen station_rooms
    scene life_support_1
    player "{i}Here is the terminal. I should be able to delete all clothes from the energy processor's list from here.{/i}"
    player "{i}But first let's make a backup, so I can quickly restore them later.{/i}"
    player "{i}...{/i}"
    player "{i}All done!{/i}"
    scene life_support_sis_1
    sis "What are you doing here?"
    player "I was checking if the energy processor has any clothes in it's item list."
    sis "And?"
    player "You were wrong. It can make only protein bars and basic drinks. You lost the bet!"
    sis smiling "What bet? I don't remember us betting anything on this."
    sis "Looks like I'll be sleeping in this stinky suit then."
    player "As I've told you - you can sleep naked if you wish."
    sis smiling "As I've told you - in your dreams!"
    player "I can try to program the processor to make some clothes."
    sis "Would you do that?"
    player "I just need to know the right size."
    sis "I'm M 36C"
    player "I need to make sure - let me see the tags of your suit"
    sis "You can't - they are on the inside."
    player "Take it off then."
    scene life_support_sis_2
    sis "What?!?"
    player "I'm not going to waste my time programing the processor for clothes that won't fit."
    sis angry "I'm not undressing in front of you!"
    player "OK then, I guess you'll sleep in that stinky suit."
    sis "..."
    scene life_support_1
    player "{i}Let her sleep in that suit for one more night - I bet she'll be much more cooperative after she has another awful night.{/i}"
    call quest_simple_clothes_advance_to_checking_tags from _call_quest_simple_clothes_advance_to_checking_tags
    jump wait_action
    
#phase 3
label check_tags:
    hide screen station_rooms
    scene shared_beds_sis_2
    player "You don't look good."
    sis "I slept really bad... This suit is not made for sleeping..."
    player "Well?"
    sis "What?"
    player "If you let me check the tags on the suit I can make you some comfortable clothes."
    sis "I'm M, 36C - why don't you believe me?"
    player "We can't waste any energy on clothes that won't fit. I need to check the tags myself."
    sis "..."
    scene shared_beds_sis_3
    sis "Fine! Happy now?"
    player "Sure I am. It really does say M, 36C."
    sis angry "I told you so!"
    player "OK, let's make you some clothes."
    call quest_simple_clothes_advance_to_restoring_clothes from _call_quest_simple_clothes_advance_to_restoring_clothes
    jump wait_action
    
#phase 4
label restore_clothes:
    hide screen station_rooms
    scene life_support_1
    player "Let's restore the clothes into the program..."
    player "..."
    player "All done! Now I should go to the processor in the mess hall and have it produce the clothes."
    player "According to the documentation it will take 350 kWh to re-sequence the matter for that."
    call quest_simple_clothes_advance_to_making_clothes from _call_quest_simple_clothes_advance_to_making_clothes
    jump wait_action
    
#phase 5
label make_clothes:
    hide screen station_rooms
    player "This should be easy: Just press the button and after a few minutes the clothes will be ready."
    player "..."
    $energy -= 350
    player "Done!"
    player "Let's find Lana to give them to her."
    call quest_simple_clothes_advance_to_giving_clothes_sis from _call_quest_simple_clothes_advance_to_giving_clothes_sis
    jump wait_action
    
#phase 6
label give_clothes_sis:
    hide screen station_rooms
    scene shared_beds_sis_2
    player "I've got the clothes."
    sis "Thank you!"
    player "Not so fast! Let's make sure it fits."
    sis angry "What? You want me to try it in front of you?"
    player "Yes."
    scene shared_beds_sis_4
    sis "So this is what you want?"
    sis "To see your step sister naked?"
    player "Pretty much."
    sis "OK then. Prepare for the show of your life!"
    scene shared_beds_sis_5
    sis "Do you like what you see?"
    player "Of course!"
    sis "Just wait - it gets better!"
    scene shared_beds_sis_6
    sis "Should I take my panties off too?"
    player "It's up to you."
    sis "Then... no."
    player "I meant 'yes', you should definitely take them off."
    sis "Too late."
    player "Damn."
    sis "Now give me the new clothes!"
    player "Here you go."
    scene shared_beds_sis_7
    sis "The top fits really well!"
    player "Of course it does."
    sis "Now let's try the pants too."
    scene shared_beds_sis_8
    sis "How do I look."
    player "Amazing!"
    sis smiling "What a shame, I thought I looked better without the clothes..."
    player "You do! You have the most beautiful body I've ever seen!"
    sis smiling "Being the nerd that you are, this doesn't mean much, but thank you!"
    sis smiling "Did you like the show?"
    player "I did!"
    sis smiling "You should've taken a picture, because you'll never see this again!"
    player "Why?"
    sis "What would mom say if I tell her what just happened?"
    player "What? Are you going to tell mom?"
    sis smiling "Maybe..."
    sis smiling "The fact is that now you owe me a favor or two."
    player "{i}I knew this was going to end bad...{/i}"
    player "{i}But it was totally worth it.{/i}"
    call quest_simple_clothes_advance_to_giving_clothes_mom from _call_quest_simple_clothes_advance_to_giving_clothes_mom
    jump wait_action
  
#phase 7
label give_clothes_mom:
    hide screen station_rooms
    scene mess_hall_mom_sis_1
    sis "Hey mom, guess what! Greg made me new clothes!"
    mom "I hope you didn't drain all our energy supply for that."
    player "It didn't require that much energy..."
    mom "I wish there was one for me too - this suit is really uncomfortable."
    sis smiling "But he needs to know your size, don't you, Greg?"
    player "No need for that - the fabric is special and it's one-size-fits-all"
    sis angry "What?!?"
    player "I said it's one-size-fits-all. Is there something wrong with your ears?"
    mom "Stop it you two!"
    player "Sorry, mom."
    sis "Sorry, mom."
    mom "Can I have the new clothes now? This suit is killing me."
    player "Here you go."
    mom "I'll go and change into these. You two behave yourselves!"
    scene mess_hall_sis_1
    sis "So it's one-size-fits-all, huh?"
    player "Yep."
    sis "But you asked me to undress so you can check the size."
    player "Yep."
    sis "Why?"
    player "I guess I wanted to see you naked."
    sis "That's flattering, but what if mom had entered the room while I was naked?"
    player "I don't know. Let's just be glad that she didn't."
    sis "Shhh, I think she's coming back."
    scene mess_hall_mom_sis_3
    player "Do you like it?"
    mom "I love it! I can move much more freely in it. See!"
    scene mess_hall_mom_sis_4
    sis "Turn around!"
    scene mess_hall_mom_sis_5
    $renpy.pause()
    scene mess_hall_mom_sis_6
    sis "It looks good on you!"
    player "It most certainly does..."
    sis "We should wear only this from now on!"
    mom "I don't think going arond the station in underwear is appropriate."
    sis "But I hate that stinky suit!"
    mom "I do too, but we will still have to wear it during the day."
    call quest_simple_clothes_finish from _call_quest_simple_clothes_finish
    jump wait_action