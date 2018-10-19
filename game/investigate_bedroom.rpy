label help_investigate_bedroom:
    player "{i}[quest_investigate_bedroom.help]{/i}"
    if quest_investigate_bedroom.finished:
        player "{i}There is nothing more that can be done about this in the current version of the game{/i}"
    jump wait

#phase 0 terminal
label quest_investigate_bedroom_start:
    $quest_investigate_bedroom.active = True
    $quest_investigate_bedroom.location = "comm"
    $quest_investigate_bedroom.alone = True
    $quest_investigate_bedroom.req_clock = 3
    $quest_investigate_bedroom.clock_mode = "at_most"
    $talk_with_terminal.add_topic("Ask them about the bedroom", "quest_investigate_bedroom_talk_earth", quest_investigate_bedroom, 0)
    $quest_investigate_bedroom.help = "I should talk with Earth to find out more about the bedroom"
    return
    
#phase 1 shower mom
label quest_investigate_bedroom_advance_to_shower_mom:
    $quest_investigate_bedroom.advance_phase()
    $quest_investigate_bedroom.reset()
    $quest_investigate_bedroom.help = "I need to check if all this about the equipment in the bedroom is true"
    return
    
#phase 2 terminal
label quest_investigate_bedroom_advance_to_talk_earth_again:
    if (global_events.meet_megan):
        call start_quest_meet_rebecca from _call_start_quest_meet_rebecca
    $quest_investigate_bedroom.advance_phase()
    $quest_investigate_bedroom.reset()
    $quest_investigate_bedroom.location = "comm"
    $quest_investigate_bedroom.alone = True
    $quest_investigate_bedroom.req_clock = 3
    $quest_investigate_bedroom.clock_mode = "at_most"
    $talk_with_terminal.add_topic("Ask about your mom's reaction", "quest_investigate_bedroom_talk_earth_again", quest_investigate_bedroom, 2)
    $quest_investigate_bedroom.help = "Let's talk with Earth about my mom's reaction when we talked in the bedroom"
    return
    
#phase 3
label quest_investigate_bedroom_finish:
    $quest_investigate_bedroom.advance_phase()
    $quest_investigate_bedroom.reset()
    $quest_investigate_bedroom.help = "To be continued in the next version."
    $quest_investigate_bedroom.finished = True
    return
    
#phase 0 terminal
label quest_investigate_bedroom_talk_earth:
    player "This is Greg, please come in."
    male "Hi Greg! Good news - we have even more subscribers than we had before!"
    player "This is all great, but I want to know what's going on in the bedroom!"
    male "What are you talking about?"
    player "I'm talking about my sister acting like a bitch on heat when she is taking a shower!"
    male "And your mother masturbating at night?"
    player "What?"
    male "Man, she is hot..."
    player "Hey, that's my mother you are talking about!"
    male "I know, right! Looking like that at her age... do you think it's the low G-s that have a positive effect on aging?"
    player "Don't change the subject! I want to know what is going on that room!"
    male "How much do you know about the research that was going on at the station?"
    player "Not that much really... I know Jack was involved in some research on relativity effects..."
    male "Relativity effects... More like time travel?"
    player "Time travel? That's bullshit!"
    male "This station had research departments on almost everything that would make the soldiers more efficient."
    male "Imagine soldiers that could go back in time and prevent the conflict from ever taking place!"
    male "Though Jack's research was considered a dud, others were more successful..."
    player "Like what?"
    male "Like the equipment we have in the bedroom."
    male "It basically removes inhibitions and all fears of the consequences of your actions."
    male "Imagine soldiers that don't feel any compassion or remorse about those they kill. Or even don't fear death!"
    player "You are talking about mind control!"
    male "Nothing of the sort!"
    male "We can't {i}control{/i} the people, they still act on their own will, but just don't care about the consequences."
    male "Think of it as being drunk but without all the physical effects of the alcohol."
    player "So that's why Lana is so horny while in the shower..."
    male "And you too."
    player "Shit..."
    male "Look at the bright side - there is no way she would let you watch her touching herself if it weren't for the equipment in that room."
    player "Please don't tell her about this!"
    male "I don't intend to - it will probably ruin everything. If she knows what's going on, she will probably choose not to give in to her desires while she is there."
    call quest_investigate_bedroom_advance_to_shower_mom from _call_quest_investigate_bedroom_advance_to_shower_mom
    jump advance_time
    
#phase 1 auto
label quest_investigate_bedroom_shower_mom:
    scene shower_mom_bedroom_1
    mom "Oh, hi Greg!"
    mom "Sleep well?"
    player "Yes mom!"
    mom "Can you please hand me that towel over there?"
    scene shower_mom_bedroom_2
    mom "You know... it's not polite to stare..."
    player "Sorry mom."
    mom "Don't be, I totally get that it's hard for you."
    scene shower_mom_bedroom_3
    mom "But you can't have those urges for your mom or your sister."
    mom "Have you tried to... you know '{i}take matters into your own hands{/i}'?"
    player "Mom... I can't really talk with you about this!"
    scene shower_mom_bedroom_4
    mom "Why not? It's perfectly normal!"
    mom "I'm sure any healthy man does it. Or woman."
    player "Do you?"
    scene shower_mom_bedroom_5
    mom "If you must know, yes, I do."
    mom "And I'm pretty sure Lana does it too. Have you seen her?"
    player "...No."
    scene shower_mom_bedroom_6
    mom "Maybe not in her bed, but I'm pretty sure that she uses mine after she showers."
    mom "I've seen some tell-tale signs on it."
    player "Are you sure?"
    scene shower_mom_bedroom_7
    mom "I think she was laying like that..."
    mom "Touching herself..."
    scene shower_mom_bedroom_8
    mom "My God, what am I doing?!?"
    mom "I'm making you uncomfortable!"
    player "No... It's OK."
    mom "It's not OK, I shouldn't be talking like that in front of you!"
    scene shower_mom_bedroom_9
    mom "I'm so sorry, Greg! Please leave the room, so I can get dressed!"
    scene door_1
    player "{i}I thought the equipment in the room was supposed to free you of any remorse about your actions!{/i}"
    player "{i}Why did mom stop?{/i}"
    player "{i}I'll have to check with Earth if they have any idea about this.{/i}"
    call quest_investigate_bedroom_advance_to_talk_earth_again from _call_quest_investigate_bedroom_advance_to_talk_earth_again
    jump advance_time
    
#phase 2 terminal
label quest_investigate_bedroom_talk_earth_again:
    player "This is Greg..."
    player "Is anyone there?"
    male "Hi Greg! What's up?"
    player "I talked with my mom after she took a shower..."
    male "You were trying to test our equipment, didn't you!"
    player "Most of the stuff you told me was pretty unbelievable, so I had to check for myself."
    male "And instead of our viewers getting a proper show from your mother in the shower, they were given a PG-13 shit of you talking on the bed!"
    male "If any of our paying customers decide to leave our channel, I'll hold you personally responsible!"
    player "What? First of all, if the equipment in the room worked as you said it did, that wouldn't be a PG-13 show!"
    male "It does work, but you can't expect miracles."
    male "As I've told you this is not some voodoo mind control stuff!"
    player "But she obviously cared about the consequences! Otherwise she wouldn't stop just as it got interesting!"
    male "What did you expect? She is your mother! You can't expect her to jump on you the moment you walk in the room!"
    male "In order for the equipment to be able to override such mental barriers, we will have to use a lot of extra power."
    male "And it might not be safe for the people inside!"
    player "You sound as if you don't want to have a video with me and my mom."
    male "You sound as if you want me to have a video with you and your mom."
    male "Look, I care about the long term business - you've been locked up for [day] days and there is no foreseeable end to the standoff between Earth and M.A.L."
    male "You should try to ease you mom into doing more stuff with you."
    male "You can't just force her to have sex with you."
    player "Why?"
    male "Because at some point the guilt will catch up with her and then no power setting will be able to overcome the barriers in her mind."
    player "So you won't help me with that?"
    male "Not until I think it's safe for both you and your mom."
    player "Over and out!"
    call quest_investigate_bedroom_finish from _call_quest_investigate_bedroom_finish
    jump advance_time