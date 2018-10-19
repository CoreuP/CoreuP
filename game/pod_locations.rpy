label pod_wait:
    show screen s_pod_day
    $renpy.pause()
    jump pod_wait

label pod_advance_time:
    $pod_time = pod_time + 1
    if (pod_time == 5):
        $pod_time = 1
        $pod_time_text = "MORNING"
        if (pod_player.equation >= 30 and not quest_released.started):
            $quest_released.started = True
    elif (pod_time == 2):
        $pod_time_text = "AFTERNOON"
    elif (pod_time == 3):
        $pod_time_text = "EVENING"
    if (pod_time == 4):
        $pod_time_text = "NIGHT"
        scene blank with fade
        call reunited_position_night from _call_reunited_position_night
        hide screen s_pod_day

        if (quest_released.meets_requirements(1)):
            jump quest_released_voyeur
        if (quest_released.meets_requirements(6)):
            jump quest_released_check_recordings
        if (quest_released.meets_requirements(11)):
            jump quest_released_check_code
        if (quest_released.meets_requirements(12)):
            jump quest_released_open_armory
        if (quest_final.phase >= 7):
            pause 1
            jump pod_advance_time

        show screen s_pod_night
    else:
        hide screen s_pod_night
        show screen s_pod_day
    show screen s_pod_stats
    if (pod_time == 1):
        jump pod_morning
    elif (pod_time == 2):
        jump pod_afternoon
    elif (pod_time == 3):
        jump pod_evening
    jump wait

label pod_morning:
    call hide_pod_screens from _call_hide_pod_screens
    $global_events.pod_had_sex = False
    $location = "pod"
    if (quest_final.phase >= 2):
        $pod_player.add_equation(math.floor(float(pod_equation_cap - pod_player.equation) / float(2)))
    elif (pod_player.arousal < 30):
        $pod_player.add_equation(0)
        if (quest_released.meets_requirements(3)):
            $quest_released.days_with_no_advance += 1
    elif (pod_player.arousal < 100):
        $pod_player.add_equation(1)
    else:
        $pod_player.add_equation(2)
    if (pod_player.arousal >= 30):
        $pod_player.add_stress(15)
    $pod_had_sex = 0
    if (pod_player.equation == pod_equation_cap):
        player "{i}You have reached the maximum equation value for this version. You can continue playing, but this will not increase the equation value further.{/i}"

    if (quest_released.meets_requirements(0)):
        jump pod_add_shower
    elif (quest_released.meets_requirements(2)):
        jump quest_released_shower
    elif (quest_released.meets_requirements(3) and quest_released.days_with_no_advance == 2):
        jump quest_released_megan
    elif (quest_released.meets_requirements(5)):
        jump quest_released_morning_megan
    elif (quest_released.meets_requirements(7)):
        jump quest_released_morning_camera
    elif (quest_released.meets_requirements(8)):
        jump quest_released_talk_tiara
    elif (quest_final.meets_requirements(2)):
        jump quest_final_susan
    elif (quest_final.meets_requirements(3)):
        jump quest_final_shower
    elif (quest_final.meets_requirements(7)):
        jump quest_final_greg_morning
    elif (quest_final.meets_requirements(8)):
        jump quest_final_recon

    if (quest_final.phase >= 3):
        scene pod_1
        player "{i}Hmmm... I guess mom and Rebecca had already left for breakfast...{/i}"
        jump outpost_breakfast

    if (quest_released.phase >= 3):
        jump pod_morning_shower

    if (global_events.pod_woman == "rebecca"):
        scene pod_rebecca_1
        rebecca flirting "Good morning, Greg! Did you spend the whole night spying on the others... or did you spy on me?"
    else:
        scene pod_mom_4
        mom happy "Morning sweetheart! Did you sleep well?"
    show screen s_pod_day
    jump wait

label pod_afternoon:
    call hide_pod_screens from _call_hide_pod_screens_1
    $location = "pod"

    if (quest_final.meets_requirements(4)):
        jump quest_final_lab
    elif (quest_final.meets_requirements(5)):
        jump quest_final_susan_talk

    if (quest_final.phase >= 3):
        scene pod_mom_rebecca_sitting_1
    elif (global_events.pod_woman == "rebecca"):
        scene pod_rebecca_1
        rebecca flirting "So..."
        if (pod_had_sex > 0):
            rebecca flirting "Are you up for another round?"
        else:
            rebecca flirting "Are we going to spend the whole day doing nothing, or...?"
    else:
        scene pod_mom_4
        mom flirting "..."
        if (pod_had_sex > 0):
            mom flirting "You were really hard this morning... Do you want to try something else?"
        else:
            mom flirting "I really think you should cum at least once a day... so... how about now...?"
    show screen s_pod_day
    jump wait

label pod_evening:
    call hide_pod_screens from _call_hide_pod_screens_33
    if (quest_final.meets_requirements(1)):
        jump quest_final_jack_dinner
    elif (quest_final.meets_requirements(6)):
        jump quest_final_wake_up

    if (quest_released.phase >= 4):
        jump outpost_dinner

    if (global_events.pod_woman == "rebecca"):
        jump pod_rebecca_dinner
    else:
        jump pod_mom_dinner

label reunited_position_night:
    $pod_station.clear()
    $pod_station.get("pod").put("player")
    $pod_station.get("pod").put(global_events.pod_woman)
    if (global_events.pod_woman == "rebecca"):
        $pod_station.get("bedroom").put("mom")
    else:
        $pod_station.get("bedroom").put("rebecca")
    $pod_station.get("bedroom").put("tiara")
    $pod_station.get("outpost").put("lana")
    if (global_events.outpost_phase > 0 and global_events.outpost_phase < 3):
        $pod_station.get("outpost").put("megan")
    $pod_station.get("bunk").put("megan")
    if (global_events.bunk_phase < 2):
        $pod_station.get("bunk").put("jack")
    $chance = renpy.random.randint(1, 4)
    if (global_events.bunk_phase == 2 and chance > 1 and global_events.pod_woman == "rebecca"):
        $pod_station.get("bunk").put("mom")
    $pod_station.get("lab").put("susan")
    if (global_events.bunk_phase == 2 or global_events.outpost_phase == 3):
        $pod_station.get("lab").put("megan")
    return

label pod_night:
    call hide_pod_screens from _call_hide_pod_screens_2

    $room_night = pod_station.get("pod")
    if (room_night.has("player") and room_night.has("rebecca")):
        jump pod_night_rebecca_greg
    elif (room_night.has("player") and room_night.has("mom")):
        jump pod_night_mom_greg
    elif (room_night.has("rebecca")):
        jump pod_night_rebecca
    elif (room_night.has("mom")):
        jump pod_night_mom
    else:
        jump pod_night_empty

label bedroom_night:
    call hide_pod_screens from _call_hide_pod_screens_3
    $room_night = pod_station.get("bedroom")
    if (room_night.has("tiara") and room_night.has("rebecca")):
        jump bedroom_night_tiara_rebecca
    elif (room_night.has("tiara") and room_night.has("mom")):
        jump bedroom_night_tiara_mom
    elif (room_night.has("tiara")):
        jump bedroom_night_tiara
    elif (room_night.has("rebecca")):
        jump bedroom_night_rebecca
    elif (room_night.has("mom")):
        jump bedroom_night_mom
    else:
        jump bedroom_night_empty

label bunk_night:
    call hide_pod_screens from _call_hide_pod_screens_4
    $room_night = pod_station.get("bunk")
    if (quest_final.phase >= 3):
        jump bunk_night_megan
    elif (room_night.has("megan") and room_night.has("rebecca")):
        jump bunk_night_megan_rebecca
    elif (room_night.has("megan") and room_night.has("mom")):
        jump bunk_night_megan_mom
    elif (room_night.has("megan") and room_night.has("jack")):
        jump bunk_night_megan_jack
    elif (room_night.has("megan")):
        jump bunk_night_megan
    else:
        jump bunk_night_empty

label outpost_night:
    call hide_pod_screens from _call_hide_pod_screens_5
    $room_night = pod_station.get("outpost")
    if (room_night.has("susan") and room_night.has("lana")):
        jump outpost_night_susan_lana
    elif (room_night.has("susan")):
        jump outpost_night_susan
    elif (room_night.has("lana") and room_night.has("megan")):
        jump outpost_night_lana_megan
    elif (room_night.has("lana")):
        jump outpost_night_lana
    else:
        jump outpost_night_empty

label lab_night:
    call hide_pod_screens from _call_hide_pod_screens_6
    $room_night = pod_station.get("lab")
    if (quest_final.phase >= 3):
        jump lab_night_empty
    if (room_night.has("megan") and room_night.has("susan")):
        jump lab_night_megan_susan
    elif (room_night.has("susan")):
        jump lab_night_susan
    else:
        jump lab_night_empty

label bedroom_night_tiara_mom:
    if (global_events.bedroom2_phase == 0):
        jump bedroom_night_tiara_mom_0
    else:
        jump bedroom_night_tiara_mom_1

label bedroom_night_tiara_mom_0:
    scene bedroom2_tiara_mom_1

    mom scared "Stay away from me!"
    tiara happy "Come on! It will be fun! The submissive role is fun too!"
    mom angry "It might be fun for you, but I don't like it! I won't do it!"
    tiara happy "Oh, I think you would!"

    scene bedroom2_tiara_mom_2

    tiara happy "Let me tell you why is that. That bitch Rebecca managed to short circuit Susan and the only one stopping Megan from throwing your asses off the station is me."
    tiara happy "So you'd either choose to be punished for what she did to her, or it will be Megan's way..."
    mom sad "... fine..."
    tiara happy "Get ready while I take my clothes off!"

    scene bedroom2_tiara_mom_9

    tiara flirting "Are you ready to receive your punishment?"
    mom scared "Don't hurt me, please!"
    tiara flirting "Silence!"

    scene bedroom2_tiara_mom_spank_mom animated:
        "bedroom2_tiara_mom_9" with dissolve
        pause 0.8
        "bedroom2_tiara_mom_10" with dissolve
        pause 0.8
        repeat

    pause

    mom sad "Please, it hurts!"
    tiara flirting "It's supposed to hurt! In time you'll learn to enjoy it!"
    tiara flirting "I'm not that big fan of women, but you can choose to lick me instead..."
    mom sad "Please... anything but this!"
    tiara flirting "Fine then! Come here!"

    scene bedroom2_tiara_mom_11

    tiara flirting "Let's see what has Rebecca taught you!"
    mom flirting "You'd be surprised..."
    tiara flirting "Stop talking and start licking, girl!"

    scene bedroom2_tiara_mom_12

    tiara flirting "Oh, that's good!"
    tiara flirting "I see you two haven't wasted your time while you were alone..."

    scene bedroom2_tiara_mom_11

    mom flirting "There wasn't much to do while we were alone..."
    tiara "Did I tell you to stop licking?"

    scene bedroom2_tiara_mom_12

    player "{i}Well, at least mom and Rebecca had some fun the last couple of weeks... Lots of fun judging from how good she is at this...{/i}"
    tiara flirting "That's it! Lick my clit!"
    tiara flirting "Yes! I'm cumming! Yes!"

    scene bedroom2_tiara_mom_13

    tiara flirting "Your turn now!"
    mom flirting "Ohhh, your fingers are soo deep in my pussy!"
    tiara flirting "Did you get so wet from the spanking on licking my pussy?"
    mom flirting "... both."

    scene bedroom2_tiara_mom_14

    player "{i}Mom seems to really enjoy Tiara's fingers in her pussy...{/i}"
    player "{i}I always thought that she enjoyed playing the dominant role, but it looks like she get's turned on by playing the submissive one too.{/i}"

    scene bedroom2_tiara_mom_15

    tiara flirting "You slut! I have my fingers buried in you and you suck on your thumb!"
    tiara flirting "Looks like someone dreams of having two cocks at once..."
    mom flirting "Mhmm..."
    tiara happy "You are such a slut..."

    scene blank

    player "{i}Wow, there is so much I didn't knew about mom...{/i}"
    player "{i}Anyway, let's try to get some sleep{/i}"

    $global_events.bedroom2_phase = 1

    jump pod_advance_time

label bedroom_night_tiara_mom_1:
    scene bedroom2_tiara_mom_1

    tiara happy "Want to have some fun?"
    $rand = renpy.random.randint(1, 3)
    if rand == 1:
        mom "Tiara, please, I'm tired... Let's just get some sleep!"
        tiara sad "Fine."

        scene blank

        player "{i}Nothing interesting here...{/i}"
        player "{i}Let's get some sleep.{/i}"

    elif rand == 2:
        mom flirting "If I get to choose, I'd like to see your ass spanked!"

        scene bedroom2_tiara_mom_2

        tiara flirting "You'd like that, won't you!"
        tiara flirting "Fine, I'll let you spank me today."

        scene bedroom2_tiara_mom_3

        tiara flirting "Let's see what you've got!"

        scene bedroom2_tiara_mom_4

        tiara "Is that all? You hit like a girl!"
        mom flirting "Is that so?"

        scene bedroom2_tiara_mom_spank_tiara animated:
            "bedroom2_tiara_mom_3" with dissolve
            pause 0.7
            "bedroom2_tiara_mom_4" with dissolve
            pause 0.7
            repeat

        pause

        tiara flirting "Much better!"
        player "{i}Mom is really getting into that...{/i}"

        scene bedroom2_tiara_mom_5

        player "{i}And it looks like she enjoys spanking Tiara's ass...{/i}"
        tiara flirting "You like that, don't you?"
        mom "Silence! Get up and fuck my pussy!"

        scene bedroom2_tiara_mom_6

        tiara "Yes mistress!"

        scene bedroom2_tiara_mom_finger animated:
            "bedroom2_tiara_mom_6" with dissolve
            pause 0.8
            "bedroom2_tiara_mom_7" with dissolve
            pause 0.8
            repeat

        pause

        mom flirting "That's it! Yes!"
        tiara flirting "You like that, don't you?"
        mom flirting "Faster!"

        scene bedroom2_tiara_mom_finger_fast animated:
            "bedroom2_tiara_mom_6" with dissolve
            pause 0.5
            "bedroom2_tiara_mom_7" with dissolve
            pause 0.5
            repeat

        mom flirting "Don't stop! Please!"
        tiara flirting "I can feel you getting closer... your pussy is squeezing my fingers!"
        mom flirting "Yes! Yes!"

        scene bedroom2_tiara_mom_7

        mom flirting "I need to sit down..."

        scene bedroom2_tiara_mom_8

        mom flirting "That was amazing... thank you..."
        tiara flirting "Don't mention it - I like the taste of your juices."

        scene blank with fade

        player "{i}I'd better get some sleep...{/i}"

    else:
        mom happy "You want your ass spanked?"
        tiara happy "Actually, I was thinking more of me spanking your ass..."

        scene bedroom2_tiara_mom_2

        mom happy "Have I been a bad girl?"
        tiara flirting "Yes. And you know what happens to girls that have been bad..."

        scene bedroom2_tiara_mom_9

        tiara flirting "Are you ready for your punishment?"
        mom flirting "No, please!"

        scene bedroom2_tiara_mom_spank_mom animated:
            "bedroom2_tiara_mom_9" with dissolve
            pause 0.8
            "bedroom2_tiara_mom_10" with dissolve
            pause 0.8
            repeat

        pause 3

        mom flirting "Please stop! I'm sorry! I won't do it anymore!"
        tiara flirting "You promise?"
        mom flirting "I do!"

        scene bedroom2_tiara_mom_11

        tiara flirting "Then show me how much sorry you are..."

        scene bedroom2_tiara_mom_12

        tiara flirting "That's it! Lick my clit!"
        tiara flirting "You are so good at that! I can't believe Rebecca was your first... you are so good at that..."
        tiara flirting "Yes! Suck on it... I'm cumming!"

        scene bedroom2_tiara_mom_11

        mom flirting "I want to cum too, mistress..."
        tiara flirting "Do bad girls get to cum?"
        mom sad "I'll be good... I promise..."
        tiara flirting "Fine. Come here!"

        scene bedroom2_tiara_mom_13

        tiara flirting "You like that, huh?"
        mom flirting "Mmmm-hmmm..."

        scene bedroom2_tiara_mom_15

        tiara flirting "Sucking on your thumb again?"

        scene bedroom2_tiara_mom_14

        tiara flirting "And rubbing your clit while I fuck you with my fingers..."
        tiara flirting "Someone is really horny tonight..."
        mom flirting "Oh yes! Yes!"
        tiara flirting "I love to feel your pussy squeezing my fingers when you cum!"

        scene blank with fade

        player "{i}Time to get some sleep...{/i}"

    jump pod_advance_time

label bedroom_night_tiara_rebecca:
    if (global_events.bedroom2_phase == 0):
        jump bedroom_night_tiara_rebecca_0
    else:
        jump bedroom_night_tiara_rebecca_1

label bedroom_night_tiara_rebecca_0:
    scene bedroom2_tiara_rebecca_1

    tiara happy "Here we are..."
    rebecca happy "Just like old times!"
    tiara happy "Not quite. This time it will be your ass that gets spanked!"

    scene bedroom2_tiara_rebecca_2

    rebecca flirting "I don't mind!"

    scene bedroom2_tiara_rebecca_3

    player "{i}Wow! She doesn't waste her time, that's for sure!{/i}"
    tiara flirting "Mmmm, I like that! You know, you are the only woman, that I've been attracted to!"

    scene bedroom2_tiara_rebecca_2

    rebecca flirting "That's flattering! But don't tell me you haven't fucked any of the women here?"
    tiara happy "Your daughter is in love with the robot and..."
    rebecca flirting "That didn't stop her from having sex with me!"
    tiara flirting "What! You had sex with your daughter? You need to be punished for that!"
    tiara flirting "Take your clothes off and lean over!"

    scene bedroom2_tiara_rebecca_4

    rebecca flirting "Do what you need to do..."

    scene bedroom2_tiara_rebecca_spank_rebecca animated:
        "bedroom2_tiara_rebecca_4" with dissolve
        pause 0.7
        "bedroom2_tiara_rebecca_5" with dissolve
        pause 0.7
        repeat

    pause 3

    rebecca flirting "Is this all you've got? Hit harder!"
    tiara flirting "Like this?"
    rebecca flirting "..."
    rebecca flirting "That's better!"

    pause

    scene bedroom2_tiara_rebecca_6

    rebecca flirting "Did you like it?"
    tiara happy "I like that I got to spank your ass for once."
    rebecca flirting "But did you enjoy it more than when I was spanking you?"
    tiara "... No."
    rebecca flirting "See? I've told you that you were submissive type. You enjoy being commanded what to do."
    rebecca flirting "Now kiss me!"

    scene bedroom2_tiara_rebecca_7

    tiara flirting "You are wet already? So you did enjoy being spanked!"
    rebecca flirting "I did... While we were locked with Amelia, we've had a lot of time on our hands..."
    rebecca flirting "And she is pretty dominant, so I got to try the submissive role... and I liked it."
    tiara flirting "I'm starting to feel sorry that Greg chose his mom and I ended up with you instead of her..."
    rebecca flirting "Let's see what we can do about that..."

    scene bedroom2_tiara_rebecca_8

    rebecca flirting "Still sorry that you are with me?"
    tiara flirting "Oh, God! That's so good!"
    rebecca flirting "So I take it as a 'no' then."
    tiara flirting "Yes... I mean no... I mean don't stop!"
    rebecca flirting "Stop? No, I don't intend to stop at all!"

    scene bedroom2_tiara_rebecca_9

    tiara flirting "Oh, yeah! Rub my clit!"
    rebecca flirting "You like it?"
    tiara flirting "Yeah! I feel it coming!"
    rebecca flirting "Me too!"
    tiara flirting "Yes! I'm cumming!"
    rebecca flirting "Oh, yes! Yes! God!"

    scene bedroom2_tiara_rebecca_10

    tiara happy "That was great!"
    rebecca happy "Yes it was... So am I better than Megan?"
    tiara flirting "So much better!"
    rebecca flirting "I still can't figure out why you agreed to take their side..."
    tiara "It's a long story and I want to sleep now. Ask me some other day..."

    $global_events.bedroom2_phase = 1

    jump pod_advance_time

label bedroom_night_tiara_rebecca_1:
    scene bedroom2_tiara_rebecca_1

    tiara flirting "Are you in the mood to have some fun?"

    $rand = renpy.random.randint(1, 3)
    if rand == 1:
        rebecca "Not really."
        tiara sad "That's a shame..."

    elif rand == 2:
        scene bedroom2_tiara_rebecca_2

        rebecca flirting "Only if I get to spank you this time."
        tiara flirting "That'll be fun!"
        rebecca flirting "Take your clothes off and assume the position!"

        scene bedroom2_tiara_rebecca_11

        rebecca flirting "Ready?"
        tiara flirting "As ready, as I'll ever be..."

        scene bedroom2_tiara_rebecca_spank_tiara animated:
            "bedroom2_tiara_rebecca_11" with dissolve
            pause 0.7
            "bedroom2_tiara_rebecca_12" with dissolve
            pause 0.7
            repeat

        pause 4

        tiara flirting "Mmmmm!"
        rebecca flirting "You like it?"
        tiara flirting "Just like old times..."
        rebecca flirting "I seem to remember something else we did back then..."

        scene bedroom2_tiara_rebecca_13

        tiara flirting "I love sucking your toes!"
        rebecca flirting "Just like old times. Gets me wet instantly."
        tiara flirting "Let me see!"

        scene bedroom2_tiara_rebecca_7

        tiara flirting "Mmmmm, you sure are wet!"
        rebecca flirting "Told you!"
        tiara flirting "This makes me wet too..."
        rebecca flirting "I want to taste you!"

        scene bedroom2_tiara_rebecca_8

        tiara flirting "Oh yeah! I like that!"
        rebecca flirting "I can see that."
        tiara flirting "Stop talking and lick my pussy!"
        rebecca flirting "..."
        tiara flirting "Just like that! Yes! That's it! I can feel it!"
        tiara flirting "Don't stop! Yes! Yes! I'm cumming!"

        scene bedroom2_tiara_rebecca_10

        tiara happy "That was great!"
        rebecca happy "It sure was!"

    else:
        scene bedroom2_tiara_rebecca_2

        rebecca flirting "Do you want to spank me again?"
        tiara flirting "I'd love that!"

        scene bedroom2_tiara_rebecca_4

        rebecca flirting "Don't hold back!"

        scene bedroom2_tiara_rebecca_spank_rebecca animated:
            "bedroom2_tiara_rebecca_4" with dissolve
            pause 0.7
            "bedroom2_tiara_rebecca_5" with dissolve
            pause 0.7
            repeat

        pause 3

        rebecca flirting "Oh, that's good!"
        tiara flirting "I'm starting to like it too..."
        rebecca flirting "That you should be glad you are with me instead of Amelia... she would have chosen to spank you instead."

        scene bedroom2_tiara_rebecca_6

        tiara "I'm a bit jealous of her..."
        rebecca flirting "Stop it... you don't even like girls! How can you be jealous of what me and Amelia did?"
        tiara "Well... I am."

        scene bedroom2_tiara_rebecca_7

        rebecca flirting "You don't need to be... See how wet you make me?"
        tiara flirting "I do."
        rebecca flirting "Come..."

        scene bedroom2_tiara_rebecca_8

        tiara flirting "I love it when you lick my pussy!"
        rebecca flirting "I love the taste of it!"
        tiara flirting "Mmmm, that's good!"
        rebecca flirting "Oh yeah? How about this?"

        scene bedroom2_tiara_rebecca_9

        tiara flirting "Oh, yes! Rub your clit on mine! Yes!"
        rebecca flirting "You love me fucking you, don't you?"
        tiara flirting "I do! I really do!"
        rebecca flirting "I fell it coming..."
        tiara flirting "Yes! Don't stop! Please! Yes!"
        tiara flirting "I'm cumming!"

        scene bedroom2_tiara_rebecca_10

        tiara happy "You are amazing!"
        rebecca happy "Thank you!"

    if (global_events.bedroom2_phase == 1):
        rebecca happy "I wanted to ask you something... What happened to my suit?"
        tiara happy "You don't stop thinking about gaining the upper hand even for a minute, do you?"
        tiara happy "It's locked in a secure place, so you don't get it and kill us all."
        rebecca "You know me - I would never do that!"
        tiara "I do know you... and that's the problem..."
        $global_events.bedroom2_phase = 2

    elif (global_events.bedroom2_phase == 2):
        rebecca happy "I haven't seen Susan since I tried to fry her brain..."
        tiara happy "Megan is still mad at you for that! But this is not her biggest problem."
        rebecca "What do you mean?"
        tiara "You know that station was invaded, right? They did something to M.A.L. ... I don't know the details, but it barely manages to keep the systems here running."
        tiara "This is why Megan hasn't thrown your sweet ass off the station yet - she needs Greg more than ever if she hopes to get the machine running."
        $global_events.bedroom2_phase = 3

    elif (global_events.bedroom2_phase == 3):
        rebecca happy "I was wondering... why did you choose to switch sides? My daughter is here, so I couldn't destroy the station, but you..."
        tiara "You know what they are trying to do here, right? The reason Megan need Greg..."
        rebecca "Something about Jack's research..."
        tiara "He found a way to transport matter through time and space. And not just back through time, but... sideways as well."
        rebecca "Sideways? You mean to a parallel universes?"
        tiara "Exactly! So... if M.A.L. manages to find that particular universe, I can get what I want."
        rebecca "Which is..."
        tiara "... it's getting late. We should get some sleep."
        $global_events.bedroom2_phase = 4

    scene blank with fade

    player "{i}Let's get some sleep.{/i}"

    jump pod_advance_time

label outpost_night_lana:
    $rand = renpy.random.randint(1, 2)
    if (quest_final.phase >= 3):
        scene outpost_lana_1
        player "{i}Hmmm... she's alone... I guess Susan is working.{/i}"
        player "{i}I need to sleep.{/i}"
    elif (rand == 1 and global_events.outpost_phase > 0):
        scene outpost_lana_1
        player "{i}She's sleeping... Nothing to see here.{/i}"
        player "{i}I should get some sleep too...{/i}"
    else:
        scene outpost_lana_2

        player "{i}Oh, good! She's awake...{/i}"
        sis "I'm so bored!"
        sis "With Susan gone, there is nothing fun I can do around here!"
        sis "I'm not allowed to see neither mom nor Greg or even Amelia and I can't stand the others..."

        scene outpost_lana_3

        sis flirting "What about having some fun on my own?"
        sis flirting "The vibrator is still under Susan's pillow..."
        sis flirting "And Greg might be watching too!"
        if (global_events.pod_woman == "mom"):
            sis flirting "I bet he has fucked his mom in her ass tonight and is connected to M.A.L. already!"
        else:
            sis flirting "I bet mom had his dick in her ass tonight so he surely is connected to M.A.L. already!"

        scene outpost_lana_4

        sis flirting "Hey Greg! Remember how much fun we used to have while we were locked together?"
        if (not global_events.lana_confronted):
            sis flirting "You are probably thinking 'wasn't she supposed to be a prisoner just like me?'... well, not exactly."
            sis flirting "Me and Susan are... friends and there is a way we can get her back to the person she used to be."
            sis flirting "So I agreed to help them out. I didn't know it would end up like this, but it's too late to do anything now."
            sis flirting "Let's just hope wherever dad's machine gets us, we won't remember what we did here... though I'd like to keep the memory of your dick forever!"
            $global_events.lana_confronted = True
        sis flirting "The only think I regret is not having your dick up my ass!"
        sis flirting "But I guess the vibrator would have to suffice."

        scene outpost_lana_5

        sis flirting "Mmmm, that's good..."
        sis flirting "I can feel the vibrations loosening my anus."
        sis flirting "But I need to get it wet before pushing it in... how do you suggest I do that?"

        scene outpost_lana_6

        sis flirting "Good thinking! My pussy is all wet from the thought that you will watch me stick that thing in my ass!"
        sis flirting "I'll dip the head in my wet pussy, so it would slide easier."

        scene outpost_lana_7

        sis flirting "Oh, God! That thing is huge!"
        sis flirting "Not as huge as you, but I can feel it ripping my ass..."
        sis flirting "I with you were here, so you could see how deep it is in me!"
        player "{i}That's actually a good idea!{/i}"

        scene outpost_lana_8

        sis flirting "Now that you are so deep in my ass, I guess it's OK to fuck it too!"

        scene outpost_lana_anal animated:
            "outpost_lana_8" with dissolve
            pause 0.7
            "outpost_lana_9" with dissolve
            pause 0.7
            repeat

        pause 3

        sis flirting "Mmmm, I like that!"
        sis flirting "I wonder why we haven't done that before!"
        sis flirting "It's so good feeling it slide in and out of my ass!"
        sis flirting "I wonder would I be able to cum just from fucking my ass..."

        scene outpost_lana_anal_fast animated:
            "outpost_lana_8" with dissolve
            pause 0.5
            "outpost_lana_9" with dissolve
            pause 0.5
            repeat

        pause 3

        sis flirting "Oh yes! Yes!"
        sis flirting "I can feel it comming!"

        pause 2

        scene outpost_lana_8

        sis flirting "Yes! That's it! Yes! Yes!"

        scene outpost_lana_10 with dissolve

        pause 3

        scene outpost_lana_8 with dissolve

        sis flirting "That was amazing! We should've definitely done that together!"
        sis flirting "I bet your dick would have been much better than this silicone thing..."
        sis sad "Unfortunately it is too late now... silicone is the only thing I can have... I'm sorry for this too..."

        scene blank with fade

        player "{i}What did she mean by that?{/i}"
        player "{i}I guess there is no point in spending too much thought on that... let's get to sleep!{/i}"

        if (global_events.outpost_phase == 0):
            $global_events.outpost_phase = 1

    jump pod_advance_time

label outpost_night_lana_megan:
    scene outpost_lana_megan_2

    player "{i}Good! Megan is here too, so I might get some useful info...{/i}"

    if (global_events.outpost_phase == 1):
        megan "So, Lana, what's this you wanted to talk about?"
        sis "How's Susan?"
        megan "I don't know... I uploaded her back to M.A.L., because her hardware can't sustain her mind anymore..."
        sis "Did the EMP blast damage her so much? Greg seemed fine after that..."

        scene outpost_lana_megan_1

        megan "He's different... You can't compare the AI android that she is with Greg..."
        megan "Also he was further away from the blast. The EM field decreases exponentially with distance, so if he was twice as far from the grenade, as Susan was, the field would be..."
        sis "You know I don't understand that stuff... You are the expert, so I'll take your word for it. So why can't Susan be back?"

        scene outpost_lana_megan_2

        megan "Ever since the invasion, M.A.L.'s capacity is shrinking... I can't explain it, but it looks like they did something to him..."
        megan "I've hooked Susan's body for diagnostics, but I can't find the reason yet."
        sis "Is she in danger?"

        scene outpost_lana_megan_1

        megan "We all are..."

        scene blank with fade

        player "{i}Fuck... This doesn't sound good!{/i}"
        player "{i}Anyway, there is nothing I can do from here, so better to get some sleep.{/i}"
        $global_events.outpost_phase = 2
    elif (global_events.outpost_phase == 2):
        sis "Thanks for coming..."
        megan "There is no use of staying in the lab, staring at Susan..."
        sis "Any progress in finding out what's wrong with her?"
        megan "... no..."
        sis "At least her mind is safe in M.A.L.'s memory banks."

        scene outpost_lana_megan_1

        megan "That might not be entirely true..."
        sis scared "What? How?"
        megan "Remember how I told you that he was loosing his capacity? We might get to a point where keeping her mind will be too much for him..."
        sis scared "When?"

        scene outpost_lana_megan_2

        megan "I can't tell exactly, but I'm sure it will not happen anytime soon. The bad news is that we are almost entirely dependent on Greg to solve the equation."
        sis "Aren't you worried that he might be listening to us right now?"
        if (global_events.pod_woman == "mom"):
            megan "No. The little pervert is probably watching Tiara spanking his mom's ass right now..."
        else:
            megan "Not at all. That little fucker is probably watching Tiara and Rebecca spanking each other's ass."

        scene outpost_lana_megan_1

        megan "Even if he tuned to this room, he would probably immediately switched the streams since you are not stuffing the vibrator in your ass..."
        sis "You know about that?"
        megan flirting "Of course I do! I like the view too..."
        sis sad "But... you are Susan's mother... did you watch us having sex too?"

        scene outpost_lana_megan_2

        megan flirting "Of course I did! And I was close to joining you a couple of times, but Susan wouldn't let me."
        sis angry "She knew?"
        megan flirting "Yep. She said she enjoyed being watched by her mom, but didn't know how you would react if I joined."
        sis angry "..."

        scene blank with fade

        player "{i}Hmmm, this might prove useful.{/i}"
        player "{i}Enough for tonight, let's get some sleep...{/i}"

        $global_events.outpost_phase = 3

    jump pod_advance_time

label lab_night_empty:
    scene lab_no_susan_1

    player "{i}The lab is empty...{/i}"
    player "{i}I need to get some sleep.{/i}"

    jump pod_advance_time

label lab_night_susan:
    scene lab_susan_1

    player "{i}Nothing interesting going on here...{/i}"
    player "{i}I should get some sleep.{/i}"

    jump pod_advance_time

label lab_night_megan_susan:
    scene lab_susan_megan_1

    megan sad "What's wrong with you..."
    megan sad "Every system in the lab says you are fine, but you are still rejecting the upload..."
    megan sad "I flashed every chip in you, even put you in the tank to mute all the sensory input to offload the processing and you still fail!"

    scene blank with fade

    player "{i}Looks like Megan can't figure out what's wrong with Susan... good!{/i}"
    if (global_events.outpost_phase > 0):
        player "{i}The more they depend on me to finish the job, the better!{/i}"
    player "{i}Time to get some sleep...{/i}"

    jump pod_advance_time

label bunk_night_megan:
    scene bunk_megan_1 #megan sleep

    if (quest_final.phase >= 3):
        player "{i}Megan is already asleep.{/i}"
        player "{i}I should get some sleep too...{/i}"
    else:
        player "{i}Hmmm... Megan is alone there... Jack is probably working on the machine.{/i}"
        player "{i}Time to get some sleep...{/i}"

    jump pod_advance_time

label bunk_night_megan_jack:
    scene bunk_megan_jack_1 #sitting on bed

    player "{i}They are not yet asleep, maybe I'll learn something valuable.{/i}"
    if (global_events.bunk_phase == 0):
        jack "How's M.A.L.?"
        megan "Fine."
        jack "..."

        scene bunk_megan_jack_2 #megan angry

        megan angry "Aren't you going to ask about Susan too?"
        jack "I suppose she's fine too, being part of M.A.L. ..."
        megan angry "She's not just a 'part of M.A.L.'! She has her own mind! She's connected to him but she makes her own decisions... when she was in the android..."

        scene bunk_megan_jack_1

        jack "Once we finish the machine and find the destination, we can put all of this behind us."
        megan sad "About that... M.A.L. looses capacity every day."
        jack "Why?"
        megan sad "Don't know yet. Could be connected to what the task force did when they cut off their part of the station."
        jack "You'll figure it out... Do you want to have sex?"

        scene bunk_megan_jack_2

        megan angry "Is this all you can think about? Besides, you know too well that you need your sleep if you are going to finish the machine in time!"
        megan angry "I'm going to bed and don't you dare to touch me!"
        jack "..."

        scene bunk_megan_jack_3 #sleeping
        $global_events.bunk_phase = 1

    elif (global_events.bunk_phase == 1):
        jack "Any news on Susan?"
        megan "Like you care..."
        jack "Well... she threatened to kill me, so what do you expect?"

        scene bunk_megan_jack_2

        megan angry "I expect you to finish your damn machine in time!"
        megan angry "The sooner you get it done, the better!"
        jack "It's not that simple..."
        megan angry "Well, neither is keeping M.A.L. functional, but I do it anyway!"
        jack "Yeah, good job on that..."
        megan angry "You have no idea what is happening to him!"
        jack "Do you?"

        scene bunk_megan_jack_1

        megan sad "I might have... and if I'm correct about that, we don't have much time."
        jack "Can you be more specific?"
        megan "They might have managed to crack the encryption on the safeguard chips and uploaded something there..."
        jack "I thought we disconnected them when Susan made him take over the station so Earth didn't flip his switch."
        megan "It's not that simple... see, he can't function without them, but Susan managed to mock the interface, so every instruction that goes through them gets verified."
        jack "So disable the mocks and flush them. Simple as that!"

        scene bunk_megan_jack_2

        megan angry "Are you that stupid? What do you think will happen once the mocks are disabled? Do you have any idea how he would react once those chips try to verify the targeting of the nukes?"
        megan angry "And if I'm correct, once those chips are connected, whatever they managed to upload on them will get loose in M.A.L. Good luck isolating it then!"
        megan angry "So, no, it's not simple at all! And you can forget about having sex tonight!"

        scene bunk_megan_jack_3
        $global_events.bunk_phase = 2

    else:
        megan "I'm tired, I want to sleep."
        jack "... okay..."

        scene bunk_megan_jack_3

    pause

    scene blank with fade

    player "{i}I should get some sleep too...{/i}"

    jump pod_advance_time

label bunk_night_megan_mom:
    scene bunk_megan_mom_1 #meggan sitting
    $rand = renpy.random.randint(1, 2)

    if (rand == 1):
        mom "You called..."
        megan happy "What is this? The 'Addams Family' special?"
        megan happy "{b}You rang?{/b}"

    megan "Took you long enough..."
    mom "What do you need me for?"
    megan "Jack is working late and I want to tease him a bit when he gets back. So I need you to help me decide what to wear."
    mom angry "You want me to help you fuck my husband! Are you fucking insane?"
    megan happy "Fuck him? No way! I want just to tease him."
    megan flirting "So... strip!"

    scene bunk_megan_mom_2 #mom naked

    megan flirting "So what do you think I should wear..."
    megan flirting "I know! What about we let Greg decide!"
    megan flirting "Greg, if you are watching this, move the camera once for the red nightie, twice for the black one and three times for the white lingerie."
    player "{i}Fuck! Should I let them know that I'm watching?{/i}"
    $bunk_mom_knows = True

    menu:
        "Move once":
            megan happy "Oh, look! He {i}is{/i} spying on us! The red nightie it is!"
            jump bunk_night_megan_mom_red
        "Move twice":
            megan happy "I knew it! Greg wouldn't miss spying on you! Put on the black one!"
            jump bunk_night_megan_mom_black
        "Move three times":
            megan happy "The little pervert {i}does{/i} spy on us!"
            mom "Don't call him that!"
            megan happy "I'll call him whatever I like! Take the white lingerie and get dressed!"
            jump bunk_night_megan_mom_white
        "Don't move":
            $bunk_mom_knows = False
            jump bunk_night_megan_mom_rand

label bunk_night_megan_mom_red:
    scene bunk_megan_mom_3

    megan happy "That look nice! Do you like it?"
    mom "I wish there were panties too..."
    megan happy "Boring!"
    megan flirting "Turn around!"

    scene bunk_megan_mom_4

    megan flirting "You have a really nice ass!"
    mom happy "Jack liked it too!"
    megan happy "If you think you can make me jealous, you should try better than that."
    megan flirting "Now, bend over!"
    mom angry "What?!?"
    megan happy "I said 'bend over'!"
    if (bunk_mom_knows):
        mom sad "But... Greg is watching..."
        megan flirting "Exactly!"
        mom "..."

    scene bunk_megan_mom_5

    mom "Happy now?"
    megan happy "I am."
    if (bunk_mom_knows):
        megan happy "But there is someone that is even happier! Greg, are you watching this?"
        megan flirting "What am I saying! Of course you are watching your slutty mom!"
        megan flirting "Take a closer look!"
    else:
        player "{i}That's hot! I wish I could take a closer look...{/i}"
        player "{i}Should I zoom in?{/i}"

    menu:
        "Do it":
            scene bunk_megan_mom_6
            player "{i}I wish I was there...{/i}"
            if (not bunk_mom_knows):
                megan happy "Did you hear that Amelia?"
                megan happy "Your son has been watching after all..."
                mom sad "Greg..."
            else:
                megan happy "Good boy!"
                megan flirting "Your mom is really wet because of you watching her!"
                mom "That's not true..."
                megan "It is!"
        "Don't do it":
            if (bunk_mom_knows):
                megan "Hmmm... No zooming of the camera... Maybe Greg isn't that interested in you as I thought..."
                megan happy "Who could blame him - probably Rebecca is giving him a blowjob right now."
                mom "..."
            else:
                megan "Hmmm... I guess Greg is not watching after all..."

    megan "That's all for now! Take it off..."

    scene bunk_megan_mom_2

    megan "Now get out! I don't need you anymore."
    mom angry "Won't you let me get dressed first?"
    megan happy "No. Get out!"

    scene blank with fade

    player "{i}Mom looked really sexy in that red nightie...{/i}"
    player "{i}I should get some sleep now...{/i}"

    jump pod_advance_time

label bunk_night_megan_mom_black:
    scene bunk_megan_mom_11

    megan happy "That's hot! Do you like it?"
    mom "You can see everything through..."
    megan happy "That's the point!"
    megan flirting "Turn around and show me your ass!"

    scene bunk_megan_mom_12

    megan flirting "Sexy! You have a fantastic ass, do you know that?"
    mom happy "You are not the only one to say this. I seem to remember Jack having a particular interest in it too..."
    megan happy "If you think you can make me jealous, you should try better than that."
    megan flirting "Now, turn around and make a sexy pose to the camera!"
    mom angry "What?!?"
    if (not bunk_mom_knows):
        mom sad "But... Greg is not watching..."
        megan flirting "Are you sure about that?"
        mom "..."

    scene bunk_megan_mom_13

    mom "Like this?"
    megan happy "Just like this."
    if (bunk_mom_knows):
        megan happy "Greg, do you think your mom looks sexy?"
        megan flirting "You can take a closer look if you like!"
    else:
        player "{i}That's hot! I wish I could zoom in a bit...{/i}"
        player "{i}Should I?{/i}"

    menu:
        "Do it":
            scene bunk_megan_mom_14
            player "{i}Wow! Mom has such a sexy body...{/i}"
            if (not bunk_mom_knows):
                megan happy "Did you hear the lens zooming Amelia?"
                megan happy "Your son has been watching after all..."
                mom sad "Greg..."
            else:
                megan happy "Good boy!"
                megan flirting "She is all wet by the fact that you are watching her."
                mom "I'm not..."
                megan "Liar!"
        "Don't do it":
            if (bunk_mom_knows):
                megan "Hmmm... No zooming of the camera... Maybe Greg isn't that interested in you as I thought..."
                megan happy "Who could blame him - probably Rebecca is giving him a blowjob right now."
                mom "..."
            else:
                megan "Hmmm... I guess Greg is not watching after all..."

    megan "That's all for now! Take it off..."

    scene bunk_megan_mom_2

    megan "Now get out! I don't need you anymore."
    mom angry "Won't you let me get dressed first?"
    megan happy "No. Get out!"

    scene blank with fade

    player "{i}Mom looked really sexy in that black nightie...{/i}"
    player "{i}I should get some sleep now...{/i}"

    jump pod_advance_time

label bunk_night_megan_mom_white:
    scene bunk_megan_mom_7

    megan happy "That look nice! Do you like it?"
    mom "You can see everything through..."
    megan happy "That's the point!"
    megan flirting "Turn around and stick out your ass!"

    scene bunk_megan_mom_8

    megan flirting "Sexy! You have a fantastic ass, do you know that?"
    mom happy "You are not the first one to say this. I seem to remember Jack having a particular interest in it too..."
    megan happy "If you think you can make me jealous, you should try better than that."
    megan flirting "Now, turn around and make a sexy pose to the camera!"
    mom angry "What?!?"
    if (not bunk_mom_knows):
        mom sad "But... Greg is not watching..."
        megan flirting "Let's see if that's true!"
        mom "..."

    scene bunk_megan_mom_9

    mom "Like this?"
    megan happy "Just like this."
    if (bunk_mom_knows):
        megan happy "Greg, do you think your mom looks sexy?"
        megan flirting "You can take a closer look if you like!"
    else:
        player "{i}That's hot! I wish I could take a closer look...{/i}"
        player "{i}Should I zoom in?{/i}"

    menu:
        "Do it":
            scene bunk_megan_mom_10
            player "{i}I wish I was there...{/i}"
            if (not bunk_mom_knows):
                megan happy "Did you hear that Amelia?"
                megan happy "Your son has been watching after all..."
                mom sad "Greg..."
            else:
                megan happy "Good boy!"
                megan flirting "She is turned on by the fact that you are watching her. Can you see her erect nipples sticking through the lace!"
                mom "They are not..."
                megan "Liar!"
        "Don't do it":
            if (bunk_mom_knows):
                megan "Hmmm... No zooming of the camera... Maybe Greg isn't that interested in you as I thought..."
                megan happy "Who could blame him - probably Rebecca is giving him a blowjob right now."
                mom "..."
            else:
                megan "Hmmm... I guess Greg is not watching after all..."

    megan "That's all for now! Take it off..."

    scene bunk_megan_mom_2

    megan "Now get out! I don't need you anymore."
    mom angry "Won't you let me get dressed first?"
    megan happy "No. Get out!"

    scene blank with fade

    player "{i}Mom looked really sexy in that lingerie...{/i}"
    player "{i}I should get some sleep now...{/i}"

    jump pod_advance_time

label bunk_night_megan_mom_rand:
    megan "..."
    megan happy "Hmmmm... He's probably busy spying on Lana..."
    $chance = renpy.random.randint(1, 3)
    megan flirting "I'll choose then!"
    if (chance == 1):
        megan flirting "The red one!"
        jump bunk_night_megan_mom_red
    elif (chance == 2):
        megan flirting "The black one!"
        jump bunk_night_megan_mom_black
    else:
        megan flirting "I like the white one best!"
        jump bunk_night_megan_mom_white
