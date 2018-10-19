#phase 1
label final_start:
    $quest_final.started = True
    $quest_final.advance_phase()
    $quest_final.time = "EVENING"
    return

#phase 2
label quest_final_advance_to_susan:
    $quest_final.advance_phase()
    $quest_final.time = "MORNING"
    return

#phase 3
label quest_final_advance_to_shower:
    $quest_final.advance_phase()
    $quest_final.time = "MORNING"
    return

#phase 4 lab
label quest_final_advance_to_lab:
    $quest_final.advance_phase()
    $quest_final.time = "AFTERNOON"
    return

#phase 5 lana's room
label quest_final_advance_to_susan_talk:
    $quest_final.advance_phase()
    $quest_final.time = "AFTERNOON"
    return

#phase 6 dinner
label quest_final_advance_to_wake_up:
    $quest_final.advance_phase()
    $quest_final.time = "EVENING"
    return

#phase 7 morning
label quest_final_advance_to_greg_morning:
    $quest_final.advance_phase()
    $quest_final.time = "MORNING"
    return

#phase 8 morning
label quest_final_advance_to_recon:
    $quest_final.advance_phase()
    $quest_final.time = "MORNING"
    return

#phase 1
label quest_final_jack_dinner:
    scene outpost_dining_5 #done

    tiara "Are you alright, Greg?"
    player "You mean me sitting here or me laying in that machine in the other room?"

    scene outpost_dining_8 #done

    megan angry "Cut the bullshit! You are the same person! I've already explained it to you!"
    mom angry "Fuck off, Megan! He didn't ask for this! It was you who put him there!"
    megan angry "Well, excuse me for saving your son then! I guess it's also my fault that Lana didn't learn to shoot at unarmed civilians like her mother and hit him in the head!"
    rebecca happy "Give me a gun and stand right there, so I can teach her how to shoot properly!"
    tiara happy "Reminds me of my family reunion dinners back on Earth! Thank you guys for the acting like a real family!"

    scene outpost_dining_7 #done

    megan angry "Sometimes I think it would be better to just open the hangar doors and deal with what's on the other side than being stuck here with you!"
    tiara happy "Just let me know first, so I can shoot you!"
    tiara "This is serious - nobody even thinks about letting them out! Do you understand me?"

    scene outpost_dining_9 #jack standing behind

    jack "This might not be necessary. I've finished the machine, so if the boy is ready with his part..."
    player "{i}The boy{/i} is not ready, so I guess we will be staying around for a bit longer..."
    jack "You stay. I'm going. Fuck all of you! I'm taking Lana with me and getting out of here!"

    scene outpost_dining_10 #jack lookin at Lana

    sis angry "Won't you ask me if I even want to go with you?"
    jack "What? Ask you? I'm your father and you will do as you are told!"
    sis angry "No! You can go wherever you like! I'm not going with you! I'll be in my room and don't you dare come inside!"

    scene outpost_dining_11 #lana left

    jack "Fine! Stay here with that abomination then! I hope she never wakes up!"
    megan angry "Call her an abomination one more time and I'll..."
    jack "You will what? Without me, you'd never have the machine!"

    scene outpost_dining_12 #rebecca waving at jack

    rebecca happy "But in fact we already have the machine, so... bye Jack!"
    jack "What?"
    rebecca happy "If I'm not mistaken as to where Lana was heading, you should be going away in 3... 2... 1..."

    scene outpost_dining_13 #jack fallen

    megan "What..."
    tiara happy "Good for you, girl!"
    rebecca happy "Yeah... if it was me, I'd pull the plug on him a long time ago."
    megan "You mean she..."

    scene outpost_dining_14 #lana back

    sis happy "I did. I disconnected him from the avatar."
    tiara "But what if he wakes up?"
    megan "He won't. There is too much damage to his brain and even if he wakes up, he will have no control over his body. At best he will be conscious and will be aware of what's going on around him, but no motor skills."
    sis "Good! ... Wait, so you are saying that his brain still has some capacity that we can use?"
    megan "I'll go get the chip!"
    player "I don't need to see that. I'll be going to sleep."

    call quest_final_advance_to_susan from _call_quest_final_advance_to_susan

    jump pod_advance_time

#phase 2
label quest_final_susan:
    scene blank

    susan "Wakey wakey..."
    player "What the..."

    if (global_events.pod_woman == "rebecca"):
        jump quest_final_susan_rebecca
    else:
        jump quest_final_susan_mom

label quest_final_susan_rebecca:
    scene pod_susan_rebecca_1 with dissolve #rebecca sleeping, susan standing

    player "Susan!"

    scene pod_susan_rebecca_2 #rebecca sitting

    rebecca "What the fuck! What are you doing here?"
    susan happy "Relax... if I was here to hurt you, you'd never have woken up."
    susan "Get dressed and come with me. Mom has something she needs to explain in the dining area."

    jump quest_final_breakfast

label quest_final_susan_mom:
    scene pod_susan_mom_1 with dissolve #mom sleeping, susan standing

    player "Susan!"

    scene pod_susan_mom_2 #mom sitting

    mom "What the fuck! What are you doing here?"
    susan happy "Relax... I'm not here to hurt you."
    susan "Get dressed and come with me. Mom has something she needs to explain in the dining area."

    jump quest_final_breakfast

label quest_final_breakfast:
    scene outpost_all_1 #everone in the outpost

    player "So? What's so urgent?"
    megan "We managed to reboot Susan's body using Jack's brain capacity..."
    rebecca "Why do I feel there is {i}but{/i} coming?"
    megan "But... Jack's brain was irreversibly damaged in the process. We can use him to help solve the equation, but the brain is dying fast."
    mom "Is this why you called us here? What makes you think anyone gives a fuck about him?"

    scene outpost_all21 #megan talking to mom

    megan sad "I don't. I've called you here to tell you that we found out why M.A.L. was loosing capacity lately."
    sis "It's a virus and we can't stop it from shutting down M.A.L."
    rebecca "When?"
    megan "We don't know for sure, but it will be soon. I fear that we won't be able to finish solving the equation."
    tiara "So we fire up the machine and get out of here."

    scene outpost_all_3 #megan angry at tiara

    megan angry "No! We've talked about this! We need to know where we are going! Susan might end up in the same situation!"
    tiara angry "It's a risk we all have to take!"
    megan angry "No! You risk not being a queen of an island full of horny men! Susan risks her life! What if we end up somewhere with..."
    tiara "Honey, when those things in the hangar break loose, we all die."
    rebecca "You don't know that..."

    scene outpost_all_4 #tiara talking rebecca

    tiara "I do. You do too. You saw the picture from the camera, what did it look like to you?"
    rebecca "Like a blurry frame of a hacked camera! There is nothing there!"
    tiara angry "Stop kidding yourself! It's the special unit! There is no negotiation with them - they follow their orders to the letter!"
    tiara "And you know what those orders say. You had them, I had them."
    susan "Enough! Until M.A.L. is online, we are safe. They won't risk anything until he has the launch codes."

    scene outpost_all_5 #mom talking

    tiara "Fine! But with M.A.L. failing, how would Greg solve the equation?"
    mom "Yeah, I though it was actually M.A.L. that we doing all the work and Greg was just providing the brain capacity..."
    megan "We have Susan now..."
    rebecca "Is she capable of doing that?"
    susan "I am... to a certain degree..."

    scene outpost_all_6 #rebecca talking

    rebecca "Shit..."
    megan "It's not ideal, but that's the best we can do for now... So here is the plan!"
    if (global_events.pod_woman == "rebecca"):
        megan "Greg, your mom will move in with you and Rebecca."
    else:
        megan "Rebecca, you will move in with Greg and Amelia."
    player "Who made you the boss of who sleeps where?"
    mom "Greg, it's for the best... I don't mind, I'm sure Rebecca wouldn't mind too..."

    scene outpost_all_7 #rebecca flirting with camera

    rebecca flirting "And I know you won't mind either!"
    sis "Greg, please! This is our only chance. Our moms will... keep you excited and Susan will do her best to solve the equation..."
    player "How about some help? Why don't you inject one of those chips and let Susan use your brain?"
    megan "You are the only one here that is compatible with the chip. I was going to make a new version of it, but never got the chance to do that."
    susan "Greg, we can talk about this later if you like. For now, please do as my mom says!"
    player "... fine..."

    call quest_final_advance_to_shower from _call_quest_final_advance_to_shower

    jump pod_advance_time

label quest_final_shower:
    scene pod_shower_mom_rebecca_1 #mom rebecca showering

    player "{i}This looks like fun...{/i}"
    mom flirting "Hey handsome! You are awake!"
    player "Indeed I am."
    rebecca flirting "Your mom and I thought we can get a shower together..."
    player "Don't mind me..."

    scene pod_shower_mom_rebecca_2 #mom rebecca kissing

    rebecca flirting "Amelia, I think we have a voyeur here..."
    mom flirting "Oh, please! All men are voyeurs."
    rebecca flirting "Sounds like you are speaking from experience..."
    mom flirting "Maybe I am!"

    scene pod_shower_mom_rebecca_3 #mom rebecca kissing

    rebecca flirting "I'd like to hear that story..."
    player "Me too!"
    mom flirting "Maybe later..."

    scene pod_shower_mom_rebecca_4 #rebecca licking mom

    rebecca flirting "Mmmm... it must be a really fun memory - you got wet almost instantly!"
    player "Now I really want to hear it!"
    mom "I was on a school trip with the girls from college... Rebecca, please stop that, I can't concentrate!"
    player "Rebecca please stop, I want to hear this!"

    scene pod_shower_mom_rebecca_5 #rebecca flirting with camera

    rebecca flirting "OK, fine, I'll leave your mom alone... on one condition!"
    player "What?"
    rebecca flirting "You don't need to concentrate, so... get on the bed!"

    scene pod_shower_mom_rebecca_6 #rebecca bj mom in background

    rebecca flirting "Don't mind me, Amelia. Please continue!"
    mom flirting "As I said, I was on a school trip with the girls from college. We were on a yacht, sailing to a underwater research facility."
    rebecca flirting "Wait! Was that facility by any chance 'Poseidon'?"
    mom "As a matter of fact it was..."
    rebecca flirting "Oh I see... I think I know why you assume all men are voyeurs..."

    scene pod_shower_mom_rebecca_7 #rebecca looking at mom touching

    mom flirting "No. 'Poseidon' was... will you let me finish my story?"
    player "Yeah, Rebecca! Stop interrupting! Don't you have something better to do with your mouth?"

    scene pod_shower_mom_rebecca_6 #as above

    mom flirting "We rescued a young man, about the same age as Greg, in the ocean."
    mom flirting "You can imagine him being the only man on a ship filled with young college girls and their female teachers..."
    mom flirting "Even the captain and the crew were all women."
    player "Sound like fun!"

    scene pod_shower_mom_rebecca_8 #rebecca sitting on greg

    rebecca flirting "Definitely!"
    mom flirting "Fun? It was fun, sure, but it was hard for him! Our teachers were really strict and were monitoring him closely."
    rebecca flirting "Oh, come on! Don't tell me that a shipload of horny college girls couldn't find a way to sneak in the night and have some fun with the only man on the ship!"
    mom happy "Of course we did! And not just in the night too! It was like a game for us - we were playing cat and mouse with the teachers."

    scene pod_shower_mom_rebecca_9 #rebecca sex with greg

    rebecca flirting "Aren't you jealous? You weren't the first forbidden fruit your mom picked from the tree!"
    player "I don't care for some guy like 25 ago. I'm just glad she did!"
    mom flirting "Though for some weird reason we didn't actually have sex, he always liked watching me finger my ass!"

    scene pod_shower_mom_rebecca_10 #mom sex with greg

    mom flirting "...just like you!"
    player "That memory {i}did{/i} make you wet!"
    rebecca flirting "Told you!"

    scene pod_shower_mom_rebecca_11 #mom finger ass

    mom flirting "Mmmm... You like my tight ass, don't you?"
    player "I sure do!"
    mom flirting "Do you want to put it inside?"

    scene pod_shower_mom_rebecca_12 #mom anal

    rebecca flirting "Stop it Amelia, you know you shouldn't make him cum!"
    mom flirting "But I want to!"
    rebecca flirting "No! Let's get that thing solved first."

    scene pod_shower_mom_rebecca_13 #mom standing

    mom flirting "I'm sorry Greg..."
    rebecca "Let's get dressed and go to breakfast."

    $pod_player.add_arousal(100)

    scene outpost_dining_2

    player "Where is Susan?"
    megan happy "Susan? She doesn't need to eat, and neither do you, so the real question is why are you here?"
    sis angry "Leave him alone, Megan!"
    sis "I'm glad you are here, Greg! I enjoy spending time with you..."
    megan "Go down the corridor, second door on the right, laying in the pod on the left. That's where he is, you can spend all the time you want with him!"
    rebecca angry "Fuck off!"

    scene outpost_dining_3

    megan happy "Actually we should all fuck off! I will fuck off to work, and the rest of you can fuck off to wherever you like. Just not the lab. I don't want to see you there!"

    call quest_final_advance_to_lab from _call_quest_final_advance_to_lab

    jump pod_advance_time

label quest_final_lab:
    scene lab_megan_1 #megan sitting in lab

    megan angry "I thought I told you not to be here!"
    player "You did. But I wanted to check what you are working on now that Susan is awake."
    megan "M.A.L. ... the prognosis is not good... he's loosing systems way too fast..."
    player "I thought M.A.L. had missiles targeting Earth. Can't he launch them?"

    scene lab_megan_2 #megan talking

    megan "That's the tricky part. He doesn't know he's loosing capacity. The virus is shutting down systems in such order that he is not aware of that... like a person suffering of dementia."
    player "But you can explain that to him, right? You can make him aware of the virus."
    megan "And then what? If he fires the missiles, we are finished. We loose our only restraining factor and the squad in the hangar will kill us all."
    megan "Besides, killing millions of innocent people is not something I'd want on my conscience."
    player "What about all the people on the station?"

    scene lab_megan_3 #megan talking

    megan "They were far from innocent, making weapons and worse..."
    megan "Besides, their death was necessary, so we could finish and use Jack's machine."
    player "OK, so as far as I understand, M.A.L. is beyond repair, Susan is fine, I'm... okay, I guess... so you don't have much to do..."

    scene lab_megan_4 #megan sad

    megan sad "Yes... and I hate it! I'm not used to sitting around doing nothing and waiting others to finish the job."
    player "So that's why you've been so cranky lately..."
    megan "Whatever... just finish your job. By the way, did you talk with Susan? She had some ideas on how to increase your brain's... productivity."
    player "Where is she?"
    megan "In her room I guess."

    call quest_final_advance_to_susan_talk from _call_quest_final_advance_to_susan_talk

    jump pod_advance_time

label quest_final_susan_talk:
    scene blank with fade

    player "{i}Megan said that Susan could help me solve the equation faster.{/i}"

    scene outpost_bed_susan_1 with fade

    player "Megan said you wanted to talk with me."
    susan "I do! We don't have much time, so we need to speed up the process!"
    player "How? And please don't say I need to be more horny, because I feel I'll go insane if I have to have more sex."
    sis happy "That's something I never thought I'd hear!"

    scene outpost_bed_susan_2 #lana happy sitting next to susan

    sis happy "So, what are you two talking about?"
    susan "I was just about to explain Greg how we can move faster on the equation."
    susan "You know that we are using Jack's brain too, right?"
    player "Yes, I saw a considerable progress since he... hmm... 'joined'..."

    scene outpost_bed_susan_3 #lana happy

    sis happy "Well, that bastard was as smart as he was sick."
    player "So what does he have to do with me?"
    susan "We can try to reverse the damage to your brain, freeing the capacity consumed by the avatar link."
    player "No catch?"

    scene outpost_bed_susan_4

    sis "Well... the interface may stop working..."
    susan "It's a risk we have to take. I've done the calculations - M.A.L. will shut down before you manage to solve the equation if we don't do it."
    player "What? Does Megan know about this?"
    sis "Of course not! She will freak out."
    susan happy "Yeah, if you haven't figured it out by now, my mom is a bit of a control freak."
    player "A bit?"
    susan "The risk is minimal though, so we need to try!"
    player "Fine... When?"

    scene outpost_bed_susan_5 #susan flirting

    susan flirting "The best time to do it is during dinner. But there is something I wanted to do first..."
    susan flirting "I'm not into men, but since your body is cybernetic, I guess I can try and see what it is to make sex with a male."
    player "And if I say no?"
    sis flirting "Then she will have to take my word for how good you are at it."

    menu:
        "Have sex with them":
            $quest_final.sex_lana = True
            jump quest_final_susan_talk_sex
        "Leave":
            $quest_final.sex_lana = False
            jump quest_final_susan_talk_leave

label quest_final_susan_talk_sex:
    player "{i}She won't have to.{/i}"

    scene outpost_bed_susan_6 #lana lick susan breast

    sis flirting "Let me get her ready for you!"
    susan flirting "I like it when you suck my nipples."
    sis flirting "Take off your panties!"

    scene outpost_bed_susan_7 #lana touch susan pussy

    susan flirting "Oh yes! Play with my clit!"
    sis flirting "Touching it makes me wet too."
    susan flirting "Oh really? Let me see!"

    scene outpost_bed_susan_8 #lana susan 69

    susan flirting "Mmmm, and tasty too!"
    sis flirting "Let's get this pussy wet for your dick!"

    scene outpost_bed_susan_9 #lana touch susan pussy

    sis flirting "Greg, be gentle with her!"

    scene outpost_bed_susan_10 #lana touch susan pussy closeup frame 1

    sis flirting "She has the sweetest pussy! I envy you that you'll be the first man to enter her."

    scene outpost_bed_clit animated with fade:
        "outpost_bed_susan_10" with dissolve
        pause 0.6
        "outpost_bed_susan_11" with dissolve
        pause 0.6
        repeat

    pause 2

    sis flirting "Are you ready?"

    scene outpost_bed_susan_12 #greg susan doggy

    player "Oh, she sure is tight!"

    scene outpost_bed_susan_13 #greg susan doggy look at greg frame 2

    susan scared "Oh, it's too big!"

    scene outpost_bed_doggy animated with fade:
        "outpost_bed_susan_13" with dissolve
        pause 0.6
        "outpost_bed_susan_14" with dissolve
        pause 0.6
        repeat

    pause 2

    susan scared "It hurts!"
    susan scared "Please! No more!"
    sis flirting "She is not so tough after all!"
    sis flirting "Greg, let me make you cum!"

    scene outpost_bed_susan_16 #greg lana 69 lana open mouth

    sis flirting "This reminds me of the old times..."

    scene outpost_bed_bj animated with fade:
        "outpost_bed_susan_15" with dissolve
        pause 0.6
        "outpost_bed_susan_17" with dissolve
        pause 0.6
        repeat

    pause 2

    susan flirting "I can't believe that you can fit the whole thing in your mouth!"
    player "Lana, I'm gonna cum!"

    scene white with dissolve

    pause 0.5

    scene outpost_bed_susan_15 with dissolve

    pause 0.5

    scene white with dissolve

    pause 0.5

    scene outpost_bed_susan_15 with dissolve

    pause 0.5

    scene white with dissolve

    pause 1.5

    scene outpost_bed_susan_18 #susan lana cummy kiss

    susan flirting "I want to taste it!"
    sis flirting "I thought you could turn off your pain receptors..."
    susan flirting "I wanted to experience it as real as possible!"

    scene outpost_bed_susan_19 #susan lana cummy kiss closeup

    susan flirting "And I'm glad I did! Now I know that I'm really not into men... I like the taste though..."
    player "{i}I hope I don't regret this later.{/i}"
    player "{i}And that the procedure will go as planned while the others are dining.{/i}"

    call quest_final_advance_to_wake_up from _call_quest_final_advance_to_wake_up
    jump pod_advance_time

label quest_final_susan_talk_leave:
    player "No hard feelings, but I don't think I want to have something to do with you two."
    susan "That's unfortunate. Anyway, our appointment for tomorrow during dinner still stands, right?"
    player "Yeah, sure!"
    sis sad "Bye Greg... I was hoping you could forgive me for shooting you."
    player "I'm more furious at you because you lied to me all that time than for shooting me! Bye Lana!"

    call quest_final_advance_to_wake_up from _call_quest_final_advance_to_wake_up_1

    jump pod_advance_time

#phase 6
label quest_final_wake_up:
    scene blank

    player "{i}Susan said to meet her in the lab during dinner, so she could try and reverse the damage to my brain.{/i}"

    scene lab_susan_talk_1

    susan "Good! You are here!"
    susan "I started to wonder if you had given up..."
    player "Let's get this over with!"
    susan "Cool! Step into the tank!"
    player "What? Why?"
    susan "It's perfectly safe! Did you forget that I've spent quite some time inside?"

    scene lab_susan_talk_2 #camera inside the tank

    player "I can't breathe!"
    susan "Breathe? Why the hell do you need to breathe? This is just a robotic shell, remember? Suppress your desire to {i}'breathe'{/i} and relax..."
    susan "This tank dampers all sensory input, freeing your brain to focus on more important stuff. Like finding pathways around the damaged centers."
    player "Can it be done so quickly?"

    scene lab_susan_talk_3 #susan working

    susan "Enough talking. See you when you wake up in the other room!"
    susan "Engaging sensory dampeners... now!"

    scene blank with fade

    player "{i}...{/i}"
    player "{i}What if something goes wrong?{/i}"
    player "{i}What if I end up like Jack? Sitting in that pod like a vegetable, my brain being used by Megan and Susan to find their desired destination... and Tiara to be the queen of an island.{/i}"

    scene armory_wake_up_1 with fade #mom bend over camera

    mom scared "Greg! Are you okay?"
    player "Am I?"

    scene armory_wake_up_2 #mom and megan next to pod

    megan angry "What did you do?"
    player "Susan said..."
    megan angry "Susan? I should've known! Where is she?"
    player "In the lab I guess..."

    scene armory_wake_up_3 #mom, megan and susan talking to each other

    susan happy "Good! You are alive!"
    player "Alive? I thought you said the only risk was that I would loose the interface..."
    megan angry "And then we would all be dead! How could you be so stupid, Susan? Did Lana put you up for this? Is she feeling so guilty about shooting him, that she made you wake him up risking everything we fought for?"
    susan "Mom, stop it! Lana has nothing to do with that!"
    megan angry "The little bitch is so manipulative, that you'd probably not even notice it!"
    player "I second that..."

    scene armory_wake_up_4 #susan, megan and mom talking

    mom "Megan, I think you are overreacting..."
    susan "Yeah mom. You seem to forget that I can calculate if someone is trying to manipulate me."
    megan "Oh really? And can you calculate the risk of him loosing the interface and leaving us stranded here?"
    susan "It's lower that the 100\% chance of us loosing M.A.L. and have the squad in the hangar kill us all before the equation is solved."
    megan "... Fine! You could've at least asked me first..."
    mom "Come, Greg! You look tired, let's get some sleep."

    call quest_final_advance_to_greg_morning from _call_quest_final_advance_to_greg_morning

    jump pod_advance_time

#phase 7 morning
label quest_final_greg_morning:
    scene pod_morning_mom_rebecca_1 #both looking at greg

    mom "How are you feeling?"
    player "Fine, I guess... but I think there is something wrong with the interface..."
    rebecca "What? Why?"
    player "I couldn't connect to the cameras during the night."

    scene pod_morning_mom_rebecca_2 #megan angry in the room

    megan angry "How could you be so stupid! We are dead because of you!"
    player "Because of me? It was Susan's idea!"
    mom angry "Yeah - how about you finally open your eyes and have a good look at your daughter? None of this would've happened if you had just let her go!"
    rebecca "This is getting us nowhere. We need to make a plan how to solve that thing before M.A.L. goes offline!"
    megan "We'll need Susan for that. Let's discus this over breakfast."

    scene outpost_all_6

    rebecca "First of all we have to know how much time do we have before M.A.L. goes offline."
    tiara "What I'd like to know is what we are up against. Can't we fix the blurred frame we got from the camera?"

    scene outpost_all_5

    susan "I can help with that."
    sis "Me too."

    scene outpost_all_3

    megan angry "Haven't you two done enough? Because of you we lost all hope of getting out of here."
    mom "We haven't lost hope Megan. If it comes to this, we can fire up the machine and go anywhere but here."

    scene outpost_all_5

    megan "That's because you are stupid. Random coordinates could send us to an Earth which can't support life, or even worse - we can end up in space. Do you have any idea what happens with your body if you are exposed to hard vacuum?"

    scene outpost_all_4

    tiara "Nothing that dramatic. You can even survive for a couple of minutes if you exhale immediately. Moisture in your body will start to evaporate, but would definitely not burst your skin. The saliva in your mouth will begin to boil though."
    mom "This doesn't sound right - it's extremely cold."

    scene outpost_all_6

    susan "It's not about the temperature - it's about pressure. Any fluid in vacuum begins to boil. And because boiling is a process that looses heat, the fluid will actually freeze while boiling."

    scene outpost_all21

    megan "I can't believe you don't know this stuff. It's basic!"
    rebecca "The result is that you'd die. That's all I need to know."

    scene outpost_all_5

    rebecca "Lana, do you know how to operate the machine?"
    sis "I do. It's not hard at all, you just need to..."
    rebecca "I don't care. As long as you know how to do it."
    rebecca "Megan, Amelia, you need to keep Jack alive for as long as possible. He's our only chance of getting the coordinates right."
    player "What do I do?"

    scene outpost_all_6

    rebecca "You, me and Tiara will try to hold them off as for as long as possible."
    mom "What? No! Greg is no solider, he can get hurt!"
    rebecca "Relax. He won't be. We will use the avatar. Greg, you'll need to get in that pod again and use the avatar to help us out defending this place."
    player "Can I? I mean is it possible?"

    scene outpost_all_3

    susan "Of course it is. Both the pod and the avatar are in good condition, so you can always connect."
    player "Fine then. So what are we waiting for then?"

    call quest_final_advance_to_recon from _call_quest_final_advance_to_recon

    jump pod_advance_time

label quest_final_recon:
    scene pod_morning_mom_rebecca_1

    mom happy "Good morning sweetie! Did you have a good sleep?"
    player "It feels like the best I had in months..."
    rebecca "That's good, now get dressed and let's prepare for the operation."
    player "The operation?"
    rebecca happy "You, me and Tiara will go outside and set up a few traps for Earth's squad."
    mom "And I'll check on Megan to see if she needs any help with Jack."

    scene bedroom2_rebecca_tiara_1 #tiara rebecca talking

    tiara happy "Finally! I've got the weapons and have charged the chameleon suit."
    rebecca "Thank you! I didn't think you'd do that for me."
    tiara "For you? Oh no, missy - I'll be the one wearing it."
    rebecca "Are you kidding me? We'll play for it. Whoever wins will get to wear the suit!"
    tiara "Deal!"

    scene bedroom2_rebecca_tiara_2 #both looking at camera

    tiara flirting "Strip!"
    player "Strip? What kind of game are you..."
    rebecca flirting "The fun one! The rules are simple..."
    tiara flirting "Don't tell him! It's more fun that way!"
    rebecca flirting "You are gonna loose anyway!"

    scene bedroom2_rebecca_tiara_3 #kissing

    tiara flirting "That feels like old times again, lieutenant!"
    rebecca flirting "It sure does. And by the way I can't remember a single time when you beat me at it!"
    tiara flirting "Which will make this time even more special."

    scene bedroom2_rebecca_tiara_4 #69

    rebecca flirting "Oh, that's good! Greg, do you want to try how wet I am?"
    tiara flirting "You are, but he can try me too. So who do you choose to fuck first?"

    $quest_final.recon_fuck_phase = 0

    menu:
        "Rebecca":
            jump quest_final_recon_fuck_rebecca
        "Tiara":
            jump quest_final_recon_fuck_tiara

label quest_final_recon_fuck_rebecca:
    if (quest_final.recon_fuck_phase == 0):
        player "Let's start with Rebecca!"
        rebecca happy "Ha!"
        tiara happy "Ha! Let's see how long he lasts with me after you sucking his dick!"

        scene bedroom2_rebecca_tiara_5 #rebecca bj

        rebecca happy "Fuck my throat!"

        scene bedroom2_rebecca_bj animated:
            "bedroom2_rebecca_tiara_5" with dissolve
            pause 0.7
            "bedroom2_rebecca_tiara_6" with dissolve
            pause 0.7
            repeat

        pause 2

        rebecca flirting "Do you want to blow your load in my mouth? I will swallow it!"
        menu:
            "Cum":
                jump quest_final_recon_cum_rebecca
            "Switch to Tiara":
                $quest_final.recon_fuck_phase += 1
                jump quest_final_recon_fuck_tiara

    elif (quest_final.recon_fuck_phase == 1):
        player "Rebecca, I want you!"
        rebecca flirting "I'll never get tired hearing this! I remember you liked my feet..."

        scene bedroom2_rebecca_tiara_8 #rebecca fj

        player "Oh, it's so good!"

        scene bedroom2_rebecca_fj animated:
            "bedroom2_rebecca_tiara_8" with dissolve
            pause 0.7
            "bedroom2_rebecca_tiara_9" with dissolve
            pause 0.7
            repeat

        pause 2

        rebecca flirting "You can spray your cum on my feet whenever you like..."
        tiara flirting "Or you can feel how soft my tits are with your hard dick!"
        menu:
            "Cum":
                jump quest_final_recon_cum_rebecca
            "Switch to Tiara":
                $quest_final.recon_fuck_phase += 1
                jump quest_final_recon_fuck_tiara

    elif (quest_final.recon_fuck_phase == 2):
        player "Rebecca, I want to put it between your tits!"

        scene bedroom2_rebecca_tiara_11 #rebecca tj

        rebecca flirting "I remember when we did this for the first time!"
        rebecca flirting "And the pearl necklace you gave me then."

        scene bedroom2_rebecca_tj animated:
            "bedroom2_rebecca_tiara_11" with dissolve
            pause 0.7
            "bedroom2_rebecca_tiara_12" with dissolve
            pause 0.7
            repeat

        pause 2

        rebecca flirting "Don't you want to see my tits covered with your cum?"
        menu:
            "Cum":
                jump quest_final_recon_cum_rebecca
            "Switch to Tiara":
                $quest_final.recon_fuck_phase += 1
                jump quest_final_recon_fuck_tiara

    elif (quest_final.recon_fuck_phase == 3):
        player "Rebecca, spread your legs!"
        rebecca flirting "Oh yeah! I want to feel how hard you are in my pussy!"

        scene bedroom2_rebecca_tiara_14 #rebecca sex

        rebecca flirting "Oh my God! You sure are hard!"

        scene bedroom2_rebecca_sex animated:
            "bedroom2_rebecca_tiara_14" with dissolve
            pause 0.7
            "bedroom2_rebecca_tiara_15" with dissolve
            pause 0.7
            repeat

        pause 2

        rebecca flirting "Do you want to fill me with your cum? To see it dripping from my wet pussy?"
        menu:
            "Cum":
                jump quest_final_recon_cum_rebecca
            "Switch to Tiara":
                $quest_final.recon_fuck_phase += 1
                jump quest_final_recon_fuck_tiara

    elif (quest_final.recon_fuck_phase == 4):
        player "Rebecca, spread your ass!"
        rebecca flirting "Mmmm! I was wondering when you would want to put it in!"

        scene bedroom2_rebecca_tiara_17 #rebecca sex

        rebecca flirting "Oh my God! You sure are big!"

        scene bedroom2_rebecca_sex animated:
            "bedroom2_rebecca_tiara_17" with dissolve
            pause 0.7
            "bedroom2_rebecca_tiara_18" with dissolve
            pause 0.7
            repeat

        pause 2

        rebecca flirting "Do you want to fill my ass with your cum? To see it dripping down on my wet pussy?"

        jump quest_final_recon_cum_rebecca

label quest_final_recon_cum_rebecca:
    player "I can't hold on any longer! I'm gonna cum!"
    if (quest_final.recon_fuck_phase == 0):
        rebecca flirting "Oh yes! Fill my mouth with your cum!"

        scene bedroom2_rebecca_tiara_6

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_6 with dissolve

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_6 with dissolve

        pause 0.8

        scene white with dissolve

        pause 1.5

        scene bedroom2_rebecca_tiara_7 with dissolve #rebecca cum lips

    elif (quest_final.recon_fuck_phase == 1):

        rebecca flirting "Oh yes! I want to feel your cum on my toes!"

        scene bedroom2_rebecca_tiara_9

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_9 with dissolve

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_9 with dissolve

        pause 0.8

        scene white with dissolve

        pause 1.5

        scene bedroom2_rebecca_tiara_10 with dissolve #rebecca cum feet

    elif (quest_final.recon_fuck_phase == 2):

        rebecca flirting "Oh yes! I want to feel your cum on my tits!"

        scene bedroom2_rebecca_tiara_12

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_12 with dissolve

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_12 with dissolve

        pause 0.8

        scene white with dissolve

        pause 1.5

        scene bedroom2_rebecca_tiara_13 with dissolve #rebecca cum tits

    elif (quest_final.recon_fuck_phase == 3):

        rebecca flirting "Oh yes! I want to feel your cum dripping from my pussy!"

        scene bedroom2_rebecca_tiara_15

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_15 with dissolve

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_15 with dissolve

        pause 0.8

        scene white with dissolve

        pause 1.5

        scene bedroom2_rebecca_tiara_16 with dissolve #rebecca cum pussy

    elif (quest_final.recon_fuck_phase == 4):

        rebecca flirting "Oh yes! I want to feel your cum dripping from my ass!"

        scene bedroom2_rebecca_tiara_18

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_18 with dissolve

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_18 with dissolve

        pause 0.8

        scene white with dissolve

        pause 1.5

        scene bedroom2_rebecca_tiara_19 with dissolve #rebecca cum pussy

    rebecca flirting "I didn't think you'd blow your load so fast..."
    tiara "You cheated! I don't know how, but you cheated!"
    rebecca happy "Cheated? How can you possibly cheat at this game? You lost, so the suit is mine!"
    $quest_final.suit = "rebecca"

    jump quest_final_go_outside

label quest_final_recon_fuck_tiara:
    if (quest_final.recon_fuck_phase == 0):
        player "Let's start with Tiara!"
        rebecca happy "Nice! She can suck you off and I'll take your cum!"
        tiara happy "That's {i}if{/i} he doesn't cum in my mouth first!"

        scene bedroom2_rebecca_tiara_20 #tiara bj

        tiara happy "Fuck my throat!"

        scene bedroom2_tiara_bj animated:
            "bedroom2_rebecca_tiara_20" with dissolve
            pause 0.7
            "bedroom2_rebecca_tiara_21" with dissolve
            pause 0.7
            repeat

        pause 2

        tiara flirting "Do you want to blow your load in my mouth? I will swallow it!"
        menu:
            "Cum":
                jump quest_final_recon_cum_tiara
            "Switch to Rebecca":
                $quest_final.recon_fuck_phase += 1
                jump quest_final_recon_fuck_rebecca

    elif (quest_final.recon_fuck_phase == 1):
        player "Tiara, I want you!"
        tiara flirting "Ha! I knew this slut couldn't make you cum!"

        scene bedroom2_rebecca_tiara_23 #tiara fj

        player "Oh, it's so good!"

        scene bedroom2_tiara_fj animated:
            "bedroom2_rebecca_tiara_23" with dissolve
            pause 0.7
            "bedroom2_rebecca_tiara_24" with dissolve
            pause 0.7
            repeat

        pause 2

        tiara flirting "You can spray your cum on my feet whenever you like..."
        rebecca flirting "I bet he would rather see his hard dick between my tits!"
        menu:
            "Cum":
                jump quest_final_recon_cum_tiara
            "Switch to Rebecca":
                $quest_final.recon_fuck_phase += 1
                jump quest_final_recon_fuck_rebecca

    elif (quest_final.recon_fuck_phase == 2):
        player "Tiara, I want to put it between your tits!"

        scene bedroom2_rebecca_tiara_26 #tiara tj

        tiara flirting "You like them big and natural don't you?"

        scene bedroom2_tiara_tj animated:
            "bedroom2_rebecca_tiara_26" with dissolve
            pause 0.7
            "bedroom2_rebecca_tiara_27" with dissolve
            pause 0.7
            repeat

        pause 2

        tiara flirting "Don't you want to see my tits covered with your cum?"
        menu:
            "Cum":
                jump quest_final_recon_cum_tiara
            "Switch to Rebecca":
                $quest_final.recon_fuck_phase += 1
                jump quest_final_recon_fuck_rebecca

    elif (quest_final.recon_fuck_phase == 3):
        player "Tiara, spread your legs!"
        tiara flirting "Oh yeah! Once you feel my wet pussy around your hard dick, I know I would win!"

        scene bedroom2_rebecca_tiara_28 #tiara sex

        tiara flirting "Oh my God! Your dick feels so good in my pussy!"

        scene bedroom2_rebecca_sex animated:
            "bedroom2_rebecca_tiara_28" with dissolve
            pause 0.7
            "bedroom2_rebecca_tiara_29" with dissolve
            pause 0.7
            repeat

        pause 2

        tiara flirting "Do you want to fill me with your cum? To see it dripping from my wet pussy?"
        rebecca flirting "Her pussy may be good, but my ass is better!"
        menu:
            "Cum":
                jump quest_final_recon_cum_tiara
            "Switch to Rebecca":
                $quest_final.recon_fuck_phase += 1
                jump quest_final_recon_fuck_rebecca

    elif (quest_final.recon_fuck_phase == 4):
        player "Tiara, it's turn for your ass!"
        tiara flirting "Mmmm! The thought of your big dick stretching my ass..."

        scene bedroom2_rebecca_tiara_31 #tiara anal

        tiara flirting "Oh my God! Your dick is tearing up my asshole!"
        rebecca flirting "You can always give up, if it's too much for you!"

        scene bedroom2_rebecca_sex animated:
            "bedroom2_rebecca_tiara_31" with dissolve
            pause 0.7
            "bedroom2_rebecca_tiara_32" with dissolve
            pause 0.7
            repeat

        pause 2

        tiara flirting "Give up? Who would give up on that dick?"
        tiara flirting "I can feel him so deep in my ass! And he's getting even harder!"

        jump quest_final_recon_cum_tiara

label quest_final_recon_cum_tiara:
    player "I can't hold on any longer! I'm gonna cum!"
    if (quest_final.recon_fuck_phase == 0):
        tiara flirting "Oh yes! Fill my mouth with your cum!"

        scene bedroom2_rebecca_tiara_21

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_21 with dissolve

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_21 with dissolve

        pause 0.8

        scene white with dissolve

        pause 1.5

        scene bedroom2_rebecca_tiara_22 with dissolve #tiara cum lips

    elif (quest_final.recon_fuck_phase == 1):

        tiara flirting "Oh yes! I want to feel your cum on my toes!"

        scene bedroom2_rebecca_tiara_24

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_24 with dissolve

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_24 with dissolve

        pause 0.8

        scene white with dissolve

        pause 1.5

        scene bedroom2_rebecca_tiara_25 with dissolve #tiara cum feet

    elif (quest_final.recon_fuck_phase == 2):

        tiara flirting "Oh yes! I want to feel your cum on my tits!"

        scene bedroom2_rebecca_tiara_27

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_27 with dissolve

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_27 with dissolve

        pause 0.8

        scene white with dissolve

        pause 1.5

        scene bedroom2_rebecca_tiara_27_a with dissolve #tiara cum tits

    elif (quest_final.recon_fuck_phase == 3):

        tiara flirting "Oh yes! I want to feel your cum dripping from my pussy!"

        scene bedroom2_rebecca_tiara_29

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_29 with dissolve

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_29 with dissolve

        pause 0.8

        scene white with dissolve

        pause 1.5

        scene bedroom2_rebecca_tiara_30 with dissolve #tiara cum pussy

    elif (quest_final.recon_fuck_phase == 4):

        tiara flirting "Oh yes! I want to feel your cum dripping from my ass!"

        scene bedroom2_rebecca_tiara_32

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_32 with dissolve

        pause 0.8

        scene white with dissolve

        pause 0.8

        scene bedroom2_rebecca_tiara_32 with dissolve

        pause 0.8

        scene white with dissolve

        pause 1.5

        scene bedroom2_rebecca_tiara_33 with dissolve #tiara cum ass

    tiara flirting "I didn't think you'd blow your load so fast..."
    rebecca "You cheated! I don't know how, but you cheated!"
    tiara happy "Cheated? How can you possibly cheat at this game? You lost, so the suit is mine!"
    $quest_final.suit = "tiara"

    jump quest_final_go_outside

label quest_final_go_outside:
    rebecca "Let's get dressed and prepare for the mission."

    scene bedroom2_rebecca_tiara_1

    rebecca "Greg, you should go to the pod and connect to the avatar."
    tiara "We will meet you at the laboratory."

    scene armory_6 #only jack in pod

    player "{i}There it is... Jack is still in the pod - they are probably using its interface to boost the chip in his head.{/i}"
    player "{i}Poor bastard... He got what he deserved though - if it wasn't for him, Megan would've not come up with that fucked up plan to save Susan and all the people on the station would still be alive.{/i}"
    player "{i}I should really do something about them when I get back. They don't deserve to get out of this alive. The only issue is how do I get rid of Lana if she's the only one that can operate the machine.{/i}"

    scene armory_7 #empty pod

    player "{i}Let's get this over with!{/i}"

    scene blank with fade

    pause 2

    scene lab_wake_1 #greg hands

    player "Fuck! This feels so real!"

    if (quest_final.suit == "rebecca"):
        scene lab_wake_tiara_1 #armed
        rebecca "That's because it is."
        player "Rebecca?"
        tiara happy "Yeah, she is in the room too. She already activated the suit."
    else:
        scene lab_wake_rebecca_1 #armed
        tiara "That's because it is."
        player "Tiara?"
        rebecca happy "She already activated the suit."
    player "We should go then. We don't have much time."
    rebecca "Yep - a couple of hours."
    tiara "Then we must hurry!"
    if (quest_final.suit == "rebecca"):
        rebecca "I'll go ahead of you and disable to security system."
    else:
        rebecca "Since Tiara is with the suit, she will disable to cameras as we go."
    tiara "Yes. Greg, you will be setting up the traps since you are with the avatar. Even if something goes wrong, you will be safe in the pod."
    if (quest_final.suit == "rebecca"):
        rebecca "And Tiara will be the last line of defense for the section. She also has your avatar's vitals monitor, as well as my suit's."
        rebecca "I'll be unarmed, so I won't be able to stop any soldiers if they get past me, but I'll try to warn you."
    else:
        rebecca "I'll provide security for the section. I've connected my monitor to your avatar's vitals, and also the chameleon suit, so I'll be coordinating you."
        tiara "Yes, I won't be able to stop any armed soldiers if they get past me, but I'll do my best to warn you."
    player "Let's go then!"

    scene corridor_2

    player "{i}I have a bad feeling about this...{/i}"
    player "{i}Shit...{/i}"

    scene corridor_3

    player "{i}...{/i}"
    player "{i}Those stairs seem like a good position to place a charge...{/i}"

    if (quest_final.suit == "rebecca"):
        player "{i}I'd better warn Rebecca, so she doesn't set it off on her way back.{/i}"
        player "Rebecca can you hear me?"
        rebecca scared "{i}Shit! Not now!{/i}"
        player "..."
        player "Rebecca! ...do you read me?"
        player "..."
        tiara angry "Greg, get back here now! Her suit just went dark!"
    else:
        player "{i}I need to tell Tiara first, so she doesn't blow herself up on her way back.{/i}"
        player "Tiara, listen..."
        rebecca angry "{i}Greg! Shut up!{/i}"
        tiara angry "{i}Fuck!{/i}"
        tiara angry "{i}Greg, Rebecca, get back now! Start the machine and go wherever! They are coming! It's the...{/i}"
        rebecca scared "{i}Tiara! Respond! Tiara!{/i}"

    player "I'll try to rescue her. You go back and warn the others!"

    scene corridor_3_blur with dissolve

    player "{i}What the...{/i}"

    scene blank with fade

    pause 3

    if (quest_final.suit == "rebecca"):
        jump quest_final_rebecca_dead
    else:
        jump quest_final_tiara_dead


label quest_final_rebecca_dead:
    scene armory_rebecca_1 #lana mom megan

    player "What happened?"
    megan "You tell me! Why did the connection to the avatar got interrupted? What did you see there?"

    scene armory_rebecca_2 #tiara angry

    tiara angry "You little piece of shit! You exposed her position! You killed her!"
    mom scared "What? Where is Rebecca? Did you leave her out there?"
    tiara angry "Your stupid son broke radio silence and they found her!"
    sis scared "They? Who's {i}they{/i}?"
    tiara angry "I don't know! But Rebecca sounded terrified and I've never seen her scared of anything."

    scene armory_rebecca_3 #susan inside

    susan "I may have an answer to that..."
    megan "Did you manage to fix the picture?"
    susan "I did. Let's get to the terminal in Greg's room."

    scene pod_desk_1

    susan "Did you seal the section?"
    tiara "Of course."
    sis scared "But this way mom won't be able to come back!"
    susan sad "Lana, she won't come back. This is what's inside the hangar..."

    scene door_intruder_1

    pause 1

    scene door_intruder_2 with dissolve

    pause 0.2

    tiara angry "Shit!"
    megan "What the fuck is this thing?"
    susan "I was hoping you would know..."

    scene armory_rebecca_4 #tiara and megan argue in pod

    tiara angry "We need to go! Now!"
    megan "We can't. We are not ready yet..."
    tiara angry "I don't care if we are ready or not! Don't you get it? We are dead if those things get here!"
    megan angry "No! I won't risk taking Susan to a place where she will be in a worse situation than she is in now!"

    scene armory_rebecca_5 #tiara gun point at susan

    tiara "That's an easy choice then!"
    mom scared "Greg! Look out!"

    scene armory_rebecca_6 #susan on the ground

    megan scared "Noooo!"
    sis scared "What did you do? Why?"

    scene armory_rebecca_7 #megan holding susan

    tiara "I made a choice. You can all thank me later."
    megan angry "I'll kill you for this!"
    tiara "Lana, who do I have to kill, so you would start the machine?"
    sis sad "Nobody. Megan, please I need your help..."

    scene machine_rebecca_1 with fade #tiara pointing gun at lana

    tiara angry "Let's get this over with! Start it up and let's go!"
    megan "Lana... do you see what I see?"
    sis "This can't be right..."
    tiara angry "What?"
    sis "We don't have enough power to send ourselves through."

    scene machine_rebecca_2 #tiara angry pointing gun at megan

    tiara angry "How could you let that happen?"
    megan "If you had volunteered to clean the solar panels at least once, we might be in a different situation. But you thought that you were too cool for that."
    tiara angry "Volunteered? OK, let's talk about volunteering! Who volunteers to stay behind? Megan?"
    megan "You don't get it do you, bitch? With the energy we've got left, the chances of even one person getting through are less than 10\%."
    tiara angry "That's good enough for me! Press the button!"

    scene machine_rebecca_3 #tiara standing

    pause 1.5

    scene machine_rebecca_4 with dissolve #tiara diappearing

    pause 0.5

    scene machine_rebecca_5 with dissolve #tiara gone gun on the ground

    pause 1

    mom "Did she make it?"
    sis happy "She is no longer here, that's for sure. And don't worry - we have enough power for all of us. I just wanted to make her go alone, so we won't end up in the places I sent her."
    player "Places? As in more than one?"
    sis happy "Yep."
    mom "Good."

    scene machine_rebecca_6 #sis talking mom

    sis "Right! Who's next?"
    megan sad "Not me. I'm staying."
    mom "Why?"
    megan sad "I created this mess with the only purpose of having Susan alive. I don't care what happens with me anymore. I can operate the machine myself. Lana, do you want to go with them, or you prefer to be sent somewhere else alone?"
    sis sad "I think they are the ones to decide that. Greg, Amelia, I know I've betrayed your trust and can't ask for forgiveness, but if you allow me to go with you, I'd be glad."

    if (quest_final.sex_lana):
        scene machine_rebecca_7

        player "Mom?"
        mom "It's your call, Greg. I can understand why she did what she did, so if you want all of us to go together..."
        player "Fine."
        sis happy "Thank you!"
        megan "Don't thank them yet. All this means that I'll send you together, not that you'll all end up in the same place... or time... or even the same universe."
        sis "We would be in the same universe, almost certainly in the same time, but the place..."
        megan "Here goes nothing..."

        scene machine_rebecca_7_blur with dissolve

        pause 1.5

        jump quest_final_final
    else:
        scene machine_rebecca_8 #lana sad

        player "I'm sorry Lana, but I don't want to see you anymore! You lied to us, you put our lives in danger and you betrayed us."
        megan "Looks like no one likes you... Farewell!"

        scene machine_rebecca_9 #lana scared

        sis scared "No wait, you haven't reprogrammed the destination yet!"
        megan "Tell Tiara I said 'hi'!"

        scene machine_rebecca_10 with dissolve #lana disappearing

        pause 0.5

        scene machine_rebecca_11 with dissolve #lana gone

        megan "Now that this is over... Let me just change the destination... Done."
        mom "How can we know that you won't kill us too."
        megan happy "You can't. But I won't. At least not intentionally."
        player "Where are you sending us?"
        megan "The truth is... I don't know. But at least you two would end up in the same universe, at the same time..."
        player "Same place?"
        megan "I can't guarantee that..."
        mom "Greg, we need to go! They've breached the section - I can hear the alarm!"
        megan "Bye!"

        scene machine_rebecca_11_blur with dissolve

        pause 1.5

        jump quest_final_final

label quest_final_tiara_dead:
    scene armory_rebecca_1 #as above

    mom scared "What happened?"
    player "I don't know... they used some kind of signal blocker..."
    megan "They? Did you see them?"

    scene armory_megan_2 #with susan

    susan "I did... but you are not going to like this..."
    megan "Tiara talked about some kind of death squad, that left no one alive on their missions... is that it?"
    susan "Most probably."

    scene armory_megan_3 #plus rebecca

    rebecca angry "You were not supposed to use the radio!"
    player "I wanted to warn her!"
    rebecca angry "And now she's dead... or worse!"
    mom scared "Worse? What could possibly be worse?"
    susan "Come to the other room, I'll show you on the terminal there."

    scene pod_desk_1

    susan "I managed to clear out the picture we've got from the camera next to the hangar."

    scene door_intruder_1

    susan "This is the original..."

    scene door_intruder_2 with dissolve #clear

    pause 1.5

    rebecca "Shit! So Tiara was right - we need to go. Now!"
    megan "No! We are not ready yet!"
    rebecca angry "Are you seeing what I'm seeing? There is no way for you to negotiate your way out of this!"
    sis sad "But if we go now, we might loose Susan!"
    rebecca angry "If this is all you care about, then..."

    scene armory_megan_4 #rebecca pointing gun at susan in pod

    rebecca "We can do this the easy way, or the really easy way!"
    susan "She's not bluffing!"
    rebecca happy "Thanks Sherlock! So Megan, what's it gonna be?"
    megan "Fine! I don't need any of you anyway..."

    scene armory_megan_5 #rebecca gun down

    rebecca "What are we waiting for, then? Let's go!"
    susan "After you!"
    rebecca happy "No, please, after you! I'm the one with the gun, so I make the rules. You three, lead the way. Greg, Amelia, stay close!"

    scene machine_megan_1 with fade #all to the machine

    rebecca "Lana, you know how to make this work, don't you?"
    sis "Yes... but there is something you should know."
    sis "Even if I send two people together, there is a chance they might end up on a slightly different location..."
    mom "How {i}'slightly'{/i}?"
    sis "A few hundred miles... it's really hard to say..."
    rebecca "What about the time? After all this thing transports through time as well, right?"

    scene machine_megan_2 #megan talking

    megan "It will definitely be the same universe, and it will most probably be the same time."
    sis "Yes, the time line will be correct and also the chances are the time coordinate will be correct too, so both will end up in the same time."
    player "Why the difference in the location then?"
    megan "A couple of hundred miles is nothing compared to the speed of light. The universe moves at that speed 'sideways' through space which we perceive as time, so..."

    scene machine_megan_3 #rebecca lana talk

    rebecca "Spare me the details! I'll have to take your word for it. Lana, how do you operate the machine?"
    sis "You select the people you want to transport and then press here..."

    scene machine_megan_4 #rebecca push lana

    rebecca "Got it!"

    scene machine_megan_5 with dissolve #lana disappearing on the ground

    pause 0.5

    scene machine_megan_6 with dissolve #lana gone

    pause 1

    scene machine_megan_7 #susan talking

    susan angry "What did you do that for?"
    rebecca happy "I wanted to make sure that if she had programmed the wrong coordinates, she would be there too."
    megan "'Wrong coordinates'?"
    rebecca happy "Like the center of the Sun or something..."

    scene machine_megan_8 #megan angry

    megan angry "You would've killed your own daughter!"
    rebecca "Only if she would've killed her own mother..."
    susan angry "But we were supposed to be together!"
    rebecca happy "Tough luck, kiddo! I can send you right away, if you like!"
    megan scared "No! Please!"

    scene machine_megan_6 #rebecca happy

    rebecca happy "Relax, I don't want you in our universe anyway!"
    mom "We sure don't."
    rebecca happy "Ready Greg?"
    player "I am."
    mom happy "Let's go then."

    scene machine_megan_6_blur with dissolve

    pause 1

    jump quest_final_final

label quest_final_final:
    hide screen s_pod_stats
    scene ocean_1 with fade

    player "What the fuck!"
    player "Where am I? Where are the others?"
    automated "Pull up. Pull up. Pull up."
    player "Shit! I don't know how to fly this thing!"

    scene ocean_2

    player "There is a ship down there! I hope they rescue me... if I survive the crash..."

    scene spaced_out_end

    jump wait
