label start_event_outpost_sex:
    $event_outpost_sex.active = True
    return
    
label event_outpost_sex_advance_to_first_dream:
    $event_outpost_sex.advance_phase()
    $event_outpost_sex.reset()
    $event_outpost_sex.req_clock = 25 #this will make the event not fire until changed to -1 in the quest_meet_rebecca phase 3
    return
    
label event_outpost_sex_advance_to_second_dream:
    $quest_meet_rebecca.req_day = -1
    $event_outpost_sex.advance_phase()
    $event_outpost_sex.reset()
    $event_outpost_sex.req_clock = 25 #this will make the event not fire until changed to -1 in the quest_meet_rebecca phase 3
    $quest_meet_rebecca.help = "I can't have any more of those exiting dreams while I'm in the same bed with mom. I must ask Earth to turn the bedroom equipment off"
    return
    
label event_outpost_sex_finish:
    $event_outpost_sex.advance_phase()
    $quest_meet_rebecca.req_day = -1
    $quest_meet_rebecca.help = "I should talk with Earth to find out why they didn't keep their word on turning the bedroom equipment off!"
    return
    
label event_outpost_sex_shared_beds_dream:
    scene blank
    $renpy.pause()
    scene shared_beds_rebecca_sis_2
    sis "Mom, can I ask you for something?"
    rebecca "Anything!"
    sis "I know you and Amelia can't be friends, but can you please not fight so much?"
    sis "She has been taking care of me ever since she and dad got married and..."
    rebecca "I... I'll try, Lana."
    rebecca "And what about Greg?"
    rebecca "Has he been '{i}taking care{/i}' of you?"
    scene shared_beds_rebecca_sis_3
    sis "What do you mean?"
    rebecca "Come on! He's handsome and with noone else around..."
    sis "He's my brother!"
    rebecca "Step brother. It's not like you are blood relatives."
    rebecca "And even if you were, there is nothing wrong with having fun together."
    rebecca "You just need to be careful not to get pregnant."
    sis "I guess you're right..."
    scene shared_beds_rebecca_sis_4
    sis smiling "And he would be fun!"
    rebecca "Meaning?"
    sis smiling "He's... His... dick is huge! I mean... it's bigger than any I have seen!"
    rebecca smiling "Have you seen that many?"
    sis smiling "I have seen enough to know he's huge."
    rebecca flirting "Hmmm, you sure?"
    sis flirting "I am!"
    rebecca flirting "OK, let's turn off the lights and get to sleep..."
    scene blank
    $renpy.pause()
    call event_outpost_sex_advance_to_first_dream from _call_event_outpost_sex_advance_to_first_dream
    jump morning

label event_outpost_sex_first_dream:
    scene blank
    $renpy.pause()
    scene outpost_dream_megan_susan_1
    megan flirting "I like it when you wear this!"
    susan happy "Why are you standing there?"
    male "I want to watch you!"
    megan flirting "Her lips are so soft!"
    susan flirting "Let me take my top off."
    scene outpost_dream_megan_susan_2
    susan flirting "I like it when you touch my pussy."
    megan flirting "I bet you do!"
    megan flirting "Do you want me to kiss it too?"
    susan flirting "Of course I do!"
    scene outpost_dream_megan_susan_3
    susan flirting "My nipples are getting hard!"
    megan flirting "And your pussy is getting wet!"
    megan happy "Are you sure you just want to watch?"
    male "Yes, I like watching you licking her pussy."
    megan happy "Suit yourself."
    scene outpost_dream_megan_susan_4
    susan flirting "Oh God, I like rubbing my clit on your face!"
    male "God? I didn't think you could be religious."
    megan happy "Why not? She can be if she wants to."
    susan flirting "Please don't stop!"
    mom "Greg!"
    scene blank
    mom "Greg! Wake up!"
    scene bedroom_mom_sleep_2
    player "What?"
    mom "You were dreaming... about something..."
    player "Why did you wake me up then?"
    mom "Because it's not right to have those kind of dreams when your mom is in the same bed as you."
    player "Wait, how do you know what I was dreaming about?"
    mom "I think it's pretty obvious..."
    scene bedroom_mom_sleep_7
    player "I'm sorry mom..."
    mom "It's OK, I guess that's normal for a boy of your age..."
    player "I'm not a boy anymore mom!"
    mom "Yes, I can clearly see that."
    mom "Now please calm yourself and let's go to sleep."
    scene blank
    $renpy.pause()
    call event_outpost_sex_advance_to_second_dream from _call_event_outpost_sex_advance_to_second_dream
    jump morning
    
label event_outpost_sex_second_dream:
    scene blank
    $renpy.pause()
    scene outpost_dream_megan_susan_5
    megan "Mmmm, I like that!"
    male "You started without me..."
    susan "I thought you liked to watch?"
    scene outpost_dream_megan_susan_6
    male "I do. But I wouldn't mind joining you..."
    megan "You know the rules. You can have sex with me, but not with her..."
    male "... unless she asks me to. I know!"
    scene outpost_dream_megan_susan_7
    susan "And '{i}she{/i}' has no intention of asking you such a thing."
    susan "Having sex with my mother should be good enough for you. It certainly is enough for me!"
    megan "I like it when you call me like that."
    scene outpost_dream_megan_susan_8
    male "It creeps me out..."
    megan "But it turns me on. It's considered a taboo on Earth."
    susan "We are not on Earth. I can't stand those people and their ridiculous rules!"
    megan "No, we are not. And thanks to M.A.L., we can have our own rules here."
    mom angry "Greg!"
    scene blank
    mom angry "Why are you naked?"
    scene bedroom_mom_sleep_2
    player "Huh?"
    scene bedroom_mom_sleep_3
    player "I..."
    scene bedroom_mom_sleep_2
    mom "Is it because of what happened today at the beach?"
    player "Well..."
    mom "But you have already seen me topless before... Is it because of Rebecca? Do you really think she is sexier than me?"
    player "Of course not! You are the most beautiful woman I have ever seen."
    mom "Anyway, make your... erection go away and let's get to sleep."
    player "You want me to masturbate in front of you? I don't think I can..."
    mom "OK, let me help you. But not a word about this to Lana or that bitch!"
    scene bedroom_mom_sleep_4
    $renpy.pause()
    scene bedroom_mom_sleep_5
    mom "It would probably be faster if you think about something nice..."
    scene bedroom_mom_sleep_4
    player "Like what happened at the beach?"
    scene bedroom_mom_sleep_5
    mom flirting "I don't think it would be appropriate to think about your mother's naked breasts..."
    scene bedroom_mom_sleep_4
    mom flirting "...while she is touching your penis..."
    scene bedroom_mom_sleep_5
    mom flirting "...stroking it..."
    scene bedroom_mom_sleep_4
    mom flirting "...faster..."
    scene bedroom_mom_sleep_5
    mom flirting "...and faster..."
    scene bedroom_mom_sleep_4
    player "I'm going to cum!"
    scene bedroom_mom_sleep_5
    mom "Yes! Do it!"
    scene bedroom_mom_sleep_6
    player "That was great!"
    mom "I only did it, so we can get back to sleep."
    player "So you didn't enjoy it?"
    mom "Greg, we have been locked here for [day] days... I miss Jack and sometimes I get horny too."
    mom "But doing such things with my son is wrong."
    player "I asked you if you enjoyed it, not whether it is wrong or not."
    mom "Greg, let's end this conversation and get back to sleep, please..."
    player "OK mom... I love you!"
    mom "I love you too son!"
    scene blank
    $renpy.pause()
    call event_outpost_sex_finish from _call_event_outpost_sex_finish
    jump morning