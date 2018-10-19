label start_event_rebecca_dice_game:
    $event_rebecca_dice_game.active = True
    $event_rebecca_dice_game.reset()
    $event_rebecca_dice_game.phase = 0
    $event_rebecca_dice_game.location = "vr_room"
    $event_rebecca_dice_game.rebecca_location = "vr_room"
    $event_rebecca_dice_game.req_energy = 550
    $event_rebecca_dice_game.req_efficiency = 100
    $talk_with_rebecca.add_topic("Play another game", "event_rebecca_dice_game_setup", event_rebecca_dice_game, 0)
    return

label event_rebecca_dice_game_advance_to_midnight:
    $event_rebecca_dice_game.advance_phase()
    $event_rebecca_dice_game.reset()
    $event_rebecca_dice_game.locaation = "life_support"
    $event_rebecca_dice_game.rebecca_location = "life_support"
    $event_rebecca_dice_game.req_clock = 0
    $event_rebecca_dice_game.clock_mode = "exactly"
    return

label event_rebecca_dice_game_setup:
    hide screen station_rooms
    player "Are you up for another game?"
    scene beach_rebecca_13
    rebecca "Anytime!"
    player "How much energy would we need?"
    rebecca "I already have the clothes, so it will be just 500kWh for the room and another 50kWh for a glass of whiskey."
    if (global_events.sis and global_events.played_game_with_lana):
        player "But Lana doesn't drink, so if I play with her, it will be only 500kWh?"
        rebecca "Not quite!"
        rebecca "Lana is a bit of a show off and she will want to have the pole in the room which will require additional 50kWh, so it will be 550kWh too."
    rebecca "And of course the efficiency of the panels need to be at 100\% to be able to sustain the setting."
    menu:
        "OK, deal!":
            rebecca "Meet me in the engineering room at midnight."
            call event_rebecca_dice_game_advance_to_midnight from _call_event_rebecca_dice_game_advance_to_midnight
        "I'm not sure we can spare that much":
            rebecca "Another time then."
            call start_event_rebecca_dice_game from _call_start_event_rebecca_dice_game_5
    jump advance_time

label event_rebecca_dice_game_play:
    hide screen station_rooms
    if (global_events.sis and quest_lanas_vibrations.phase >= 14):
        jump event_rebecca_dice_game_with_lana
    else:
        jump event_rebecca_dice_game_without_lana

label event_rebecca_dice_game_without_lana:
    if (energy < 550 or efficiency < 100):
        rebecca "I'm here, but it looks like that we don't have the required power to reset the VR room."
        player "Another time then?"
        rebecca "I'll be waiting."
        jump advance_time
    else:
        rebecca "Ready?"
        player "Anytime!"
        $energy = energy - 550
        rebecca "..."
        rebecca "OK, the room is reset, go there and wait for me."
        scene bar_1
        $renpy.pause()
        scene bar_rebecca_1
        rebecca "OK, I'm ready, let's start the game!"
        jump start_event_rebecca_dice

label event_rebecca_dice_game_with_lana:
    if (global_events.played_game_with_lana):
        jump event_rebecca_dice_game_with_lana_repeat
    else:
        jump event_rebecca_dice_game_with_lana_first

label event_rebecca_dice_game_with_lana_first:
    player "Are we ready?"
    rebecca happy "Not quite."
    player "Why?"
    rebecca happy "You can come in now!"
    scene life_support_rebecca_sis_1
    player "Lana!?"
    player "What are you doing here?"
    sis flirting "I want to play too!"
    if (energy < 550 or efficiency < 100):
        rebecca "But there is not enough power to reset and sustain the VR room. We need at least 550kWh stored in the batteries..."
        player "... and the panels to be operating at 100\%. I know!"
        rebecca happy "And yet - here you are..."
        sis sad "So we can't play?"
        rebecca "Not today."
        rebecca "And if you want to play, you'll need a proper dress, so it will take at least 250kWh to make those for the first game."
        player "Another time then?"
        sis "I'll be waiting."
        jump advance_time
    if (energy < 800 or efficiency < 100):
        rebecca "Unfortunately you are not dressed properly for the game."
        rebecca "I can make you some clothes for 250kWh of energy, but we don't have a total of 800kWh to make the clothes and to reset the VR room."
        rebecca "So what would it be? Playing with me or waiting till it will be enough for a game with Lana?"
        menu:
            "Play with Rebecca (-550kWh)":
                player "I'll play with you!"
                $energy = energy - 550
                rebecca "..."
                rebecca "OK, the room is reset, go there and wait for me."
                scene bar_1
                $renpy.pause()
                scene bar_rebecca_1
                rebecca "OK, I'm ready, let's start the game!"
                jump start_event_rebecca_dice
            "Wait till there are 800kWh":
                player "I think it will be polite to wait so Lana can play."
                rebecca happy "You are such a gentleman! Or are you just bored with me?"
                player "No way! But..."
                rebecca happy "I'm just messing with you! We can play another time!"
                sis happy "Thanks!"
                jump advance_time
    else:
        rebecca happy "We have enough energy to make some proper clothes for Lana and to reset the VR room."
        rebecca flirting "It's up to you who you'd like to play with - me or your sister!"
        menu:
            "Choose Rebecca (-550kWh)":
                player "I think I'll play with you..."
                sis sad "You don't want to see me stripping?"
                player "No, I just..."
                rebecca "Come on Lana, It's not the end of the world!"
                rebecca happy "Let's do it!"
                $energy = energy - 550
                rebecca "..."
                rebecca "OK, the room is reset, go there and wait for me."
                sis sad "And I will go to bed."
                scene bar_1
                $renpy.pause()
                scene bar_rebecca_1
                rebecca "OK, I'm ready, let's start the game!"
                jump start_event_rebecca_dice
            "Choose Lana (-800kWh)":
                sis happy "Thank you!"
                rebecca "Fair enough! I'll make the clothes and reset the VR room."
                $energy = energy - 800
                rebecca "..."
                rebecca "OK, the room is reset, go there and wait for her."
                scene bar_sis_1
                sis "OK, I'm ready, let's start the game!"
                jump game_sis_poker_dice_start

label event_rebecca_dice_game_with_lana_repeat:
    scene life_support_rebecca_sis_1
    if (energy < 550 or efficiency < 100):
        rebecca "So we are both here, but it looks like that we don't have the required power to reset the VR room."
        player "Another time then?"
        sis "I'll be waiting."
        jump advance_time
    else:
        rebecca "Ready?"
        player "Anytime!"
        sis happy "Choose which on you'd like to play with."
        player "Can't I have both?"
        rebecca flirting "Can you handle both of us?"
        player "Yes!"
        sis flirting "But I don't feel like sharing!"
        rebecca flirting "I'd agree, but if Lana won't like it, then you'd have to choose only one!"
        menu:
            "Choose Rebecca":
                player "In that case, I'd prefer to play with Rebecca!"
                sis sad "Fine."
                $energy = energy - 550
                rebecca "..."
                rebecca "OK, the room is reset, go there and wait for me."
                scene bar_1
                $renpy.pause()
                scene bar_rebecca_1
                rebecca "OK, I'm ready, let's start the game!"
                jump start_event_rebecca_dice
            "Choose Lana":
                player "OK Lana, let's play."
                $energy = energy - 550
                rebecca "..."
                rebecca "OK, the room is reset, go there and wait for her."
                scene bar_sis_1
                sis "OK, I'm ready, let's start the game!"
                jump game_sis_poker_dice_start
