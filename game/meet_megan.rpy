label help_meet_megan:
    player "[quest_meet_megan.help]"
    if quest_meet_megan.finished:
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

#phase 0 auto
label start_quest_meet_megan:
    $quest_meet_megan.active = True
    $quest_meet_megan.req_day = day + 2
    $quest_meet_megan.req_clock = 1
    return
    
#phase 1 terminal
label quest_meet_megan_advance_to_talk_med_bay:
    $quest_meet_megan.advance_phase()
    $quest_meet_megan.reset()
    $talk_with_terminal.add_topic("Open the door", "quest_meet_megan_open_med_bay", quest_meet_megan, 1)
    $quest_meet_megan.location = "med_bay"
    $quest_meet_megan.help = "{i}I need to find out more about the incident from Megan.{/i}"
    return
    
#phase 2 terminal
label quest_meet_megan_advance_to_hack_camera:
    $quest_meet_megan.advance_phase()
    $quest_meet_megan.reset()
    $quest_meet_megan.chance = 5 + player_stat.programming / 2
    $quest_meet_megan.location = "med_bay"
    $quest_meet_megan.help = "{i}I need to find another way of talking with Megan. Perhaps if I can hack the door comm system...{/i}"
    return

#phase 3 auto
label quest_meet_megan_advance_to_dinner:
    $quest_meet_megan.advance_phase()
    $quest_meet_megan.reset()
    $quest_meet_megan.location = "mess_hall"
    $quest_meet_megan.req_clock = 19
    $quest_meet_megan.help = "{i}I'll talk with the others to tell them what happened to Megan{/i}"
    return
    
#phase 4 terminal
label quest_meet_megan_advance_to_talk_med_bay_again:
    $quest_meet_megan.advance_phase()
    $quest_meet_megan.reset()
    $quest_meet_megan.location = "med_bay"
    $quest_meet_megan.help = "{i}Let's try and see if I can learn something else from Megan{/i}"
    $talk_with_terminal.add_topic("Talk with Megan", "quest_meet_megan_talk_med_bay_again", quest_meet_megan, 4)
    return
    
#phase 5 talk
label quest_meet_megan_advance_to_talk_sis:
    $quest_meet_megan.advance_phase()
    $quest_meet_megan.reset()
    $quest_meet_megan.location = "shared_beds"
    $quest_meet_megan.sis_location = "shared_beds"
    $quest_meet_megan.req_clock = 21
    $quest_meet_megan.clock_mode = "at_least"
    $quest_meet_megan.help = "{i}I should talk with Lana to see shat she thinks about Megan.{/i}"
    $talk_with_sis.add_topic("Talk about Megan", "quest_meet_megan_talk_sis", quest_meet_megan, 5)
    return
    
#phase 6 talk
label quest_meet_megan_advance_to_talk_mom:
    $quest_meet_megan.advance_phase()
    $quest_meet_megan.reset()
    $quest_meet_megan.location = "vr_room"
    $quest_meet_megan.mom_location = "vr_room"
    $quest_meet_megan.help = "{i}I think I have a better chance of convincing mom if she is calm and relaxed.{/i}"
    $talk_with_mom.add_topic("Talk about Megan", "quest_meet_megan_talk_mom", quest_meet_megan, 6)
    return
    
#phase 7 terminal
label quest_meet_megan_advance_to_unlock_door:
    $quest_meet_megan.advance_phase()
    $quest_meet_megan.reset()
    $quest_meet_megan.location = "med_bay"
    $quest_meet_megan.req_clock = 3
    $quest_meet_megan.clock_mode = "at_most"
    $quest_meet_megan.unlock_again = False
    $quest_meet_megan.help = "{i}I've got mom's permission to unlock the med bay door, but I'd better do this at night when everyone is asleep, so I can claim my prize{/i}"
    $talk_with_terminal.add_topic("Unlock the door", "quest_meet_megan_unlock_door", quest_meet_megan, 7)
    return
    
label quest_meet_megan_finish:
    $quest_meet_megan.advance_phase()
    $quest_meet_megan.reset()
    $global_events.megan = False
    $global_events.meet_megan = True
    $quest_meet_megan.help = "{i}Last thing I remember is Megan saying that she is sorry and then she disappeared{/i}"
    $quest_meet_megan.finished = True
    if (quest_investigate_bedroom.phase >= 2):
        call start_quest_meet_rebecca from _call_start_quest_meet_rebecca_1
    call event_outpost_start from _call_event_outpost_start
    return
    
#phase 0 auto
label quest_meet_megan_open_door:
    player "{i}I think I hear something!{/i}"
    player "{i}It's definitely coming from the section's door!{/i}"
    scene door_2
    female "Please open the door!"
    female "Can anyone hear me? Please!"
    player "Who are you?"
    female "Thank God there is someone alive! Open the door, please!"
    player "Tell me who you are or I'm leaving right now!"
    female "My name is Megan and M.A.L.'s bots attacked the section we were in."
    female "They captured everyone, I was the only one that managed to escape, please let me in before they find me!"
    player "I... I need to speak with the others."
    female "There is not time, please let me in!"
    menu:
        "Hack the door":
            jump quest_meet_megan_open_door_2
        "Check the camera feed":
            jump quest_meet_megan_check_camera
            
label quest_meet_megan_check_camera:
    scene corridor_megan_1
    female "I can hear them coming closer, please open the door!"
    scene door_2
    jump quest_meet_megan_open_door_2
    
label quest_meet_megan_open_door_2:
    player "OK, Stand back!"
    female "Please hurry!"
    megan "Close it, close it now!"
    scene door_megan_1
    megan "Thank you!"
    player "Are you hurt?"
    megan "Those are just scratches."
    scene door_mom_megan_1
    mom angry "Stay back!"
    mom angry "Who are you and how the hell did you come inside?"
    megan "Please! My name is Megan and I'm a propulsion engineer. I worked on the Gamma drive before the incident."
    mom "How do I know you are telling the truth?"
    megan "You can check the station database if you have access."
    mom "No we don't. In the meantime, you will be confined to the med bay until we figure out what to do with you."
    megan "You'll lock me up?"
    mom angry "You're damn right I will!"
    mom angry "Move!"
    $global_events.megan = True
    call quest_meet_megan_advance_to_talk_med_bay from _call_quest_meet_megan_advance_to_talk_med_bay
    jump wait_action
    
#phase 1 terminal
label quest_meet_megan_open_med_bay:
    hide screen station_rooms
    player "..."
    player "{i}The door is sealed shut and I don't think I can hack the terminal. Mom took care of that...{/i}"
    player "{i}Let's try to restore the med bay camera feed instead.{/i}"
    call quest_meet_megan_advance_to_hack_camera from _call_quest_meet_megan_advance_to_hack_camera
    jump quest_meet_megan_hack_camera
    
#phase 2 terminal
label quest_meet_megan_hack_camera:
    hide screen station_rooms
    player "OK, let's see what I can do..."
    $rand = renpy.random.randint(0, 100)
    if (rand < quest_meet_megan.chance):
        jump quest_meet_megan_talk_camera
    else:
        player "I couldn't do it."
        player "Maybe if I improve my skills, I'll be able to hack the camera"
        $talk_with_terminal.add_topic("Restore the feed (%param% success)", "quest_meet_megan_hack_camera", quest_meet_megan, 2, ["chance"])
        jump wait_action
    
label quest_meet_megan_talk_camera:
    player "I think I did it!"
    scene med_bay_megan_1
    player "Can you hear me?"
    megan "Yes!"
    megan "Finally someone to speak to!"
    megan "Please let me out!"
    player "I can't do that. What if you kill us all?"
    megan "Why would I do that?"
    player "I don't know..."
    player "First tell me what do you know about the incident."
    scene med_bay_megan_3
    megan sad "Not much. We were in our lab when the light went out and we heard screams down the hall."
    megan sad "One of my colleagues went out to check what's happening and when he returned, he was wounded and said that the security bots were shooting everyone."
    megan sad "He bled to death a couple of hours later..."
    player "I'm sorry..."
    megan sad "The rest of us locked the door and we decided to stay there until the corridor was clear."
    megan sad "It was horrible - hearing the bots outside, searching for survivors, shooting everyone they could find..."
    megan sad "We waited for more than a day and when we couldn't hear any more noises through the lab door, we opened it and went for one of the emergency sections."
    megan sad "Good thing that when the military built the station they made such sections completely autonomous so the central processor has no control over them."
    player "Yes, I've been thinking about that..."
    player "M.A.L. still has control over most of the station - why didn't it just shut down the life support? Or open the docking seals, so everyone would die?"
    scene med_bay_megan_2
    megan "I don't know. I'm just a propulsion engineer, not one of those cybernetics guys that think they understand how an AI thinks."
    player "What happened then? You said that you managed to find an emergency section and lock yourself in."
    megan sad "We did. There was an energy processor so we could basically stay there forever."
    megan sad "Unfortunately the solar panels were in bad shape and our control terminal could not connect to any maintenance bots."
    megan sad "We ran out of energy. Without it, there were no food, no water, even the oxygen levels started to drop."
    megan sad "So we decided to move to another emergency section."
    megan sad "We went outside and that's when the bots attacked."
    megan sad "I think I'm the only one that made it."
    player "How many of you were in that section?"
    megan "Four."
    scene med_bay_megan_4
    megan "Now please let me out! I'm no threat to you. I don't want to be locked here!"
    player "I'll talk with the others."
    megan "Don't leave me here!"
    player "I need to go, they don't know that I restored the comm system."
    player "And I think my mom will be pretty mad that I did."
    call quest_meet_megan_advance_to_dinner from _call_quest_meet_megan_advance_to_dinner
    jump wait_action

#phase 3 auto
label quest_meet_megan_dinner:
    hide screen station_rooms
    scene mess_hall_mom_sis_1
    player "Mom, I've talked with Megan..."
    mom angry "What? When?"
    player "Calm down, I didn't open the door. I've talked with her on the intercom."
    player "She said..."
    mom "I don't care what she says! Our safety comes first!"
    player "But she is locked up - how can she harm us?"
    mom "And she will remain locked up until I say so!"
    sis "Don't you think you might be wrong?"
    sis "I mean keeping her locked up against her will is... kidnapping!"
    mom "So? The rules have changed, Lana."
    mom "Laws apply to Earth and with Earth don't giving a damn about us, we can make our own rules."
    sis "What are you saying?"
    mom "I'm saying that I'm willing to do whatever is necessary in order to keep us safe."
    player "Even if this hurts somebody else?"
    mom "Yes."
    player "OK but just listen to me for a bit."
    player "Megan said that she sealed herself along with three other people on a section similar to this one."
    player "But they couldn't manage to fix their solar panels, so eventually they ran out of power."
    player "And when they decided to move to another section, they were attacked."
    mom "There are other sections like this one?"
    player "Yes."
    mom "Do you think..."
    sis "There can be other people still alive!"
    player "Possibly."
    mom "We need to try and contact them!"
    sis "I'll try to modify the comm equipment."
    mom "Greg, you need to find out if Megan is telling the truth."
    player "OK mom."
    $global_events.contact_others = True
    call quest_meet_megan_advance_to_talk_med_bay_again from _call_quest_meet_megan_advance_to_talk_med_bay_again
    jump wait_action

#phase 4 terminal
label quest_meet_megan_talk_med_bay_again:
    hide screen station_rooms
    scene med_bay_megan_1
    player "Hi Megan!"
    megan "Hi Greg!"
    player "Listen, I wanted to ask you..."
    megan "Me first!"
    scene med_bay_megan_4
    megan "When you left the last time, you said that your mom will be mad that you've talked with me?"
    player "So?"
    megan "So the older woman is your mother, right?"
    player "Yes."
    megan "And who is the other one? Your girlfriend?"
    player "No, she is my sister... well, step sister, to be exact."
    megan "Is there anyone else in this section?"
    player "No, my father remained locked outside."
    megan "So you've been sealed here for [day] days only with your mother and your sister?"
    megan "It must be hard for you not to have any women around that are not part of your family..."
    player "What do you mean?"
    megan "Come on, you are young male, not having any females around that you can have sex with."
    megan "Or maybe you have something with your sister?"
    megan "Her being you {i}step{/i} sister..."
    player "No."
    megan "I bet you'd want to, though."
    player "No."
    megan "Come on, you can tell me!"
    scene med_bay_megan_5
    megan "Or maybe you prefer more experienced women?"
    megan "Like your mom?"
    scene med_bay_megan_6
    megan "Do you mind me taking off my suit? It's really uncomfortable and I'm getting hot in it."
    player "Not at all."
    megan "That's what I thought."
    megan "So who would it be - your mom or your sister?"
    scene med_bay_megan_7
    megan "Or me?"
    megan "Do you like what you see?"
    player "Of course I do!"
    megan "I also haven't had sex since the incident."
    megan "The other three were an old couple and a teen girl."
    megan "No young, handsome males like yourself."
    scene med_bay_megan_8
    megan "I'm getting wet just thinking about you."
    megan "Hmmm..."
    scene med_bay_megan_9
    megan "I'd like to feel your hands touching me."
    megan "Squeezing my breasts..."
    scene med_bay_megan_10
    megan "Playing with my pussy."
    megan "Sliding your fingers in me."
    scene med_bay_megan_11
    megan "Can you see how wet I am?"
    megan "Come inside and we can have some fun together."
    player "I don't think I should do this."
    megan "If you change your mind, you know where to find me."
    call quest_meet_megan_advance_to_talk_sis from _call_quest_meet_megan_advance_to_talk_sis
    jump wait_action
    
#phase 5
label quest_meet_megan_talk_sis:
    hide screen station_rooms
    player "Hi Lana, I wanted to ask you something?"
    sis "Sure Greg!"
    player "Do you think Megan can be trusted?"
    sis "I don't know. But if she is alive, dad might be alive too, right?"
    player "I hope so. Anyway do you think we should let her out?"
    sis "Mom said..."
    player "I know what mom said. But keeping her locked against her will is not right!"
    player "What if she tells the truth? She has suffered so much and we are keeping her locked."
    sis "I don't know Greg... What if she is lying to us?"
    player "Why would she lie?"
    player "I've talked with her and I think we should let her out."
    scene shared_beds_sis_10
    sis "Wait a minute! What did you two talk about?"
    player "About us being sealed together... only family members..."
    sis "I see... and what's wrong with being with your family?"
    player "You know... there are things that you shouldn't do with your family..."
    sis happy "Oh, you mean like making your sister undress in front of you?"
    scene shared_beds_sis_11
    sis happy "Or putting sun lotion on her ass?"
    player "Lana, please!"
    sis flirting "Don't worry - I'm not complaining."
    sis "I don't mind you rubbing lotion on my back while some perverts on Earth are watching."
    sis "By the way, did she promise you anything if you let her out?"
    player "No."
    scene shared_beds_sis_11
    sis "No? Not even \"{i}I'm getting wet just thinking about you{/i}\"?"
    player "How do you know?"
    sis "You've got your secrets, I've go mine."
    sis "I quite liked the show, by the way."
    player "..."
    sis "If I were you, I'd have let her out and fucked her right there."
    sis "I mean we've been locked here for [day] days and I'm pretty sure you didn't have sex with your mother, so..."
    player "Yeah, it's been hard..."
    scene shared_beds_sis_12
    sis happy "Oh, I'm pretty sure it has been hard. And judging by what I can see, It's hard right now..."
    player "I'm sorry..."
    sis flirting "There is no need to be sorry - I too get horny sometimes."
    sis flirting "Do you want to do something about it?"
    player "What? Here? In front of you?"
    sis flirting "Why not? And if you ask nicely, I might even help you."
    player "Really?"
    sis flirting "Sure!"
    sis flirting "But I'd want something in return."
    player "Anything!"
    sis flirting "So? Are you going to drop your pants or are you going to talk?"
    menu:
        "Undress":
            jump quest_meet_megan_sis_handjob
        "Ask what does she want in return":
            jump quest_meet_megan_ask_sis
            
label quest_meet_megan_sis_handjob:
    if (quest_sis_beach.phase < 9):
        sis "Oh, my! I knew you were big, but this is..."
    else:
        sis "I know how big you are and yet..."
    sis flirting "Do you want me to touch it?"
    player "Yes, please!"
    scene shared_beds_sis_13
    sis "Do you like it?"
    player "Oh, yes!"
    sis flirting "I bet you'd like me to kiss it."
    player "Would you?"
    sis flirting "Is my hand not enough for you?"
    player "No... yes... I mean..."
    sis happy "I won't suck it, but I can show you my tits if you ask nicely."
    player "Please. Pretty please!"
    scene shared_beds_sis_14
    sis "I know they aren't as big as Megan's but judging from what I'm holding in my hand, I think you still like them."
    player "I do!"
    scene shared_beds_sis_15
    $renpy.pause()
    scene shared_beds_sis_14
    $renpy.pause()
    scene shared_beds_sis_15
    $renpy.pause()
    scene shared_beds_sis_14
    sis "Do you like it?"
    player "Of course! Please don't stop!"
    scene shared_beds_sis_16
    sis "I'm afraid I'll have to."
    sis "Remember that I asked for something in return?"
    jump quest_meet_megan_ask_sis
    
label quest_meet_megan_ask_sis:
    player "What do you want for your 'help'?"
    sis "A toy."
    player "A toy?"
    sis "A vibrator."
    player "Lana, I'm not sure I can make it."
    player "The energy processor is intended for food and clothing."
    player "Manufacturing electronics will be hard, even impossible maybe..."
    sis "Are you trying to ask for more? Because if you are, it won't work."
    sis "I'm willing to give you a handjob but nothing more."
    player "No Lana, I mean it."
    player "I'll do my best, but it might not work."
    sis "Fair enough."
    call start_quest_lanas_vibrations from _call_start_quest_lanas_vibrations
    call quest_meet_megan_advance_to_talk_mom from _call_quest_meet_megan_advance_to_talk_mom
    jump wait_action
    
#phase 6 talk
label quest_meet_megan_talk_mom:
    hide screen station_rooms
    player "How are you, mom?"
    mom "Fine, thanks for asking."
    player "I've talked with Megan..."
    mom "And?"
    player "I really think we should let her out."
    player "She's been through enough already."
    mom "There is something fishy about her story. I don't know what, but I dont trust her!"
    player "Anyway, you've asked me to find if she's telling the truth and I think she is."
    mom "OK Greg. I guess, I'll need to have more faith in both yourself and Lana."
    mom "I'll go and unlock the med bay door."
    player "No need for that, mom. I'll unlock the door myself."
    player "You stay here and enjoy the sun."
    call quest_meet_megan_advance_to_unlock_door from _call_quest_meet_megan_advance_to_unlock_door
    jump wait_action

#phase 7 terminal
label quest_meet_megan_unlock_door:
    hide screen station_rooms
    if (quest_meet_megan.unlock_again):
        jump quest_meet_megan_choose_again
    scene med_bay_megan_0
    player "Can you hear me?"
    scene med_bay_megan_4
    megan "Yes?"
    player "About what you said last time..."
    scene med_bay_megan_5
    megan flirting "I don't remember what it was, can you please remind me?"
    player "That if I unlock this door, you and me will have some 'fun'"
    megan happy "Of course I remember, Greg! I'm just teasing you."
    player "Did you mean it?"
    megan "I meant it. I too didn't have sex for the last [day] days and I'm as horny as you are."
    megan "And if this get's me free, it's even better!"
    $quest_meet_megan.megan_in_bra = False
    jump quest_meet_megan_choose
    
label quest_meet_megan_choose_again:
    scene med_bay_megan_0
    player "Hi Megan!"
    scene med_bay_megan_4
    megan "Greg! where did you go last time?"
    megan "Please open the door, I have a surprise for you"
    scene med_bay_megan_6
    $quest_meet_megan.megan_in_bra = True
    jump quest_meet_megan_choose
    
label quest_meet_megan_choose:
    menu:
        "Open the door":
            jump quest_meet_megan_fuck_megan
        "Not yet":
            $quest_meet_megan.unlock_again = True
            player "I'll have to think about it..."
            $talk_with_terminal.add_topic("Unlock the door", "quest_meet_megan_unlock_door", quest_meet_megan, 7)
            jump wait_action
            
label quest_meet_megan_fuck_megan:
    if quest_meet_megan.megan_in_bra:
        scene med_bay_megan_13
        megan "Nice to see you again!"
        player "By the way, where did you get that bra and why didn't you have any panties on last time?"
    else:
        scene med_bay_megan_12
        megan "Nice to see you again!"
        player "By the way, where did you get that bra I saw you with last time and why didn't you have any panties on?"
        megan "This bra?"
        scene med_bay_megan_13
    megan "This is not important right now!"
    megan flirting "And I think you'd be more interested in what's inside the bra."
    scene med_bay_megan_14
    megan flirting "Am I right?"
    player "Definitely!"
    megan flirting "And guess what - I still don't have panties on."
    scene med_bay_megan_15
    player "Yes, I can see that!"
    megan "And I can see that you are getting aroused."
    scene med_bay_megan_16
    megan "It's fun using my fingers, but judging from what I see in your pants, it will be much more fun with you!"
    scene med_bay_megan_17
    megan "Come closer, I won't bite... unless you want me to."
    scene med_bay_megan_18
    megan flirting "Can you see how wet I am? Do you want to feel my pussy with your fingers?"
    scene med_bay_megan_19
    player "Oh, you are so wet!"
    megan flirting "I've told you - I haven't had sex since we were locked up and I'm as horny as you are!"
    megan "Let me see how hard you are."
    scene med_bay_megan_20
    player "I like that!"
    megan flirting "I bet you do!"
    megan flirting "No one has ever complained from my blowjobs."
    scene med_bay_megan_20_b
    $renpy.pause()
    scene med_bay_megan_20
    $renpy.pause()
    scene med_bay_megan_20_b
    $renpy.pause()
    scene med_bay_megan_20
    megan "I need you inside me. Please!"
    scene med_bay_megan_21
    megan "Oh, it so big! I can feel you stretching my pussy."
    scene med_bay_megan_22
    megan "Can you see how deep it's in me?"
    player "Lean back!"
    scene med_bay_megan_23
    player "Oh yes! That's it!"
    scene med_bay_megan_23_b
    $renpy.pause()
    scene med_bay_megan_23
    $renpy.pause()
    scene med_bay_megan_23_b
    $renpy.pause()
    megan "Oh, yeah, I like it!"
    scene med_bay_megan_23
    $renpy.pause()
    scene med_bay_megan_23_b
    player "I'm cumming!"
    scene med_bay_megan_24
    megan "Oh God, this was wonderful!"
    scene med_bay_megan_25
    megan happy "Greg, you were amazing!"
    megan sad "I'm really sorry for what I'm about to do next..." 
    scene blank
    $renpy.pause()
    jump quest_meet_megan_find_greg
    
label quest_meet_megan_find_greg:
    scene med_bay_greg_1
    player "What the..."
    player "Why am I lying over there... and how can I see myself?"
    scene med_bay_greg_2
    sis scared "Greg! Are you all right?"
    player "Lana! Call mom!"
    sis scared "Greg! Can you hear me?"
    sis scared "Greg!"
    sis scared "Mom! Come quickly! Greg is lying on the med table and not moving!"
    scene med_bay_greg_3
    mom scared "Lana, move aside! Give him some room to breathe!"
    mom scared "Greg! Can you hear me?"
    player "Yes I can! I'm right here!"
    mom scared "Help me get him in the scanner, we need to find out what's wrong with him!"
    call quest_meet_megan_finish from _call_quest_meet_megan_finish
    jump morning
    
label morning_after_megan:
    hide screen startion_rooms
    scene shared_beds_sis_9
    sis "Oh, you are awake..."
    player "What happened?"
    sis "Put on some clothes, we will talk at breakfast."
    show screen station_rooms
    return
    
label breakfast_after_megan:
    hide screen station_rooms
    scene mess_hall_mom_sis_1
    mom "Greg, how are you feeling?"
    player "I'm fine. What happened last night?"
    sis "We found you in the med bay... naked."
    mom "And Megan was gone."
    mom "What happened there?"
    player "I don't remember... The last thing I do remember is me opening the door to let her out..."
    sis "Yeah, right..."
    mom "Lana, please!"
    sis "I'm just saying that there must have been something else that happened there too."
    mom "Anyway, we ran a full scan on you..."
    sis "After that we carried you to our room and put you in bed."
    player "When will we have the results from the scanner?"
    mom "Few days at least."
    mom "Let's hope we find out what caused it!"
    sis happy "If I had to guess, I'd say it was blood flowing out of his head and into... other organs."
    player "Not funny Lana!"
    mom "We can't know before we have the results. Let's have breakfast."
    jump wait_action