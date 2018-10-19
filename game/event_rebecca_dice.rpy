init python:
    def find_dice():
        best_v = 0
        best_q = 0
        best_p = 0
        for v in range(0,5):
            for q in range(0,10):
                if q < chosen_qty or (q == chosen_qty and v <= chosen_val):
                    prob = 0
                else:
                    missing_dices = q - dice_sum[v]
                    if missing_dices > 0:
                        prob = 100 - missing_dices * 20
                    else:
                        prob = 100
                if prob > best_p:
                    best_p = prob
                    best_v = v
                    best_q = q
        return [best_p, best_q, best_v + 1]

screen hidden_dice:
    hbox:
        xpos 10
        ypos 50
        spacing 0
        image "gui/dice_unknown.png"
        image "gui/dice_unknown.png"
        image "gui/dice_unknown.png"
        image "gui/dice_unknown.png"
        image "gui/dice_unknown.png"
        
screen common_dice:
    hbox:
        xpos 10
        ypos 225
        spacing 0
        image common_dice[0]
        image common_dice[1]
        image common_dice[2]
        image common_dice[3]
        image common_dice[4]

screen player_dice:
    hbox:
        xpos 10
        ypos 400
        spacing 0
        image player_dice[0]
        image player_dice[1]
        image player_dice[2]
        image player_dice[3]
        image player_dice[4]
        
screen rebecca_dice:
    hbox:
        xpos 10
        ypos 50
        spacing 0
        image rebecca_dice[0]
        image rebecca_dice[1]
        image rebecca_dice[2]
        image rebecca_dice[3]
        image rebecca_dice[4]
        
screen choose_qty:
    if (dice_qty > 0):
        hbox:
            xpos 970
            ypos 208
            spacing 0
            imagebutton:
                idle "gui/liar.png"
                action Jump("player_call_liar")
                
    hbox:
        xpos 970
        ypos 244
        spacing 0
        if dice_qty > 1 or (dice_qty == 1 and dice_val == 6):
            image "gui/qty_blank.png"
        elif chosen_qty == 1:
            image "gui/qty_1x_hl.png"
        else:
            imagebutton:
                idle "gui/qty_1x.png"
                action Jump("dice_choose_qty_1")
        
        if dice_qty > 2 or (dice_qty == 2 and dice_val == 6):
            image "gui/qty_blank.png"
        elif chosen_qty == 2:
            image "gui/qty_2x_hl.png"
        else:
            imagebutton:
                idle "gui/qty_2x.png"
                action Jump("dice_choose_qty_2")
                
        if dice_qty > 3 or (dice_qty == 3 and dice_val == 6):
            image "gui/qty_blank.png"
        elif chosen_qty == 3:
            image "gui/qty_3x_hl.png"
        else:
            imagebutton:
                idle "gui/qty_3x.png"
                action Jump("dice_choose_qty_3")
                
        if dice_qty > 4 or (dice_qty == 4 and dice_val == 6):
            image "gui/qty_blank.png"
        elif chosen_qty == 4:
            image "gui/qty_4x_hl.png"
        else:
            imagebutton:
                idle "gui/qty_4x.png"
                action Jump("dice_choose_qty_4")
                
        if dice_qty > 5 or (dice_qty == 5 and dice_val == 6):
            image "gui/qty_blank.png"
        elif chosen_qty == 5:
            image "gui/qty_5x_hl.png"
        else:
            imagebutton:
                idle "gui/qty_5x.png"
                action Jump("dice_choose_qty_5")
                
    hbox:
        xpos 970
        ypos 280
        spacing 0
        if dice_qty > 6 or (dice_qty == 6 and dice_val == 6):
            image "gui/qty_blank.png"
        elif chosen_qty == 6:
            image "gui/qty_6x_hl.png"
        else:
            imagebutton:
                idle "gui/qty_6x.png"
                action Jump("dice_choose_qty_6")
        
        if dice_qty > 7 or (dice_qty == 7 and dice_val == 6):
            image "gui/qty_blank.png"
        elif chosen_qty == 7:
            image "gui/qty_7x_hl.png"
        else:
            imagebutton:
                idle "gui/qty_7x.png"
                action Jump("dice_choose_qty_7")
                
        if dice_qty > 8 or (dice_qty == 8 and dice_val == 6):
            image "gui/qty_blank.png"
        elif chosen_qty == 8:
            image "gui/qty_8x_hl.png"
        else:
            imagebutton:
                idle "gui/qty_8x.png"
                action Jump("dice_choose_qty_8")
                
        if dice_qty > 9 or (dice_qty == 9 and dice_val == 6):
            image "gui/qty_blank.png"
        elif chosen_qty == 9:
            image "gui/qty_9x_hl.png"
        else:
            imagebutton:
                idle "gui/qty_9x.png"
                action Jump("dice_choose_qty_9")
                
        if dice_qty > 10 or (dice_qty == 10 and dice_val == 6):
            image "gui/qty_blank.png"
        elif chosen_qty == 10:
            image "gui/qty_10x_hl.png"
        else:
            imagebutton:
                idle "gui/qty_10x.png"
                action Jump("dice_choose_qty_10")
                
screen choose_val:
    hbox:
        xpos 1090
        ypos 340
        spacing 0
        if (chosen_qty == dice_qty and dice_val >= 1) or chosen_qty == 0:
            image "gui/dice_blank.png"
        else:
            imagebutton:
                idle "gui/dice_1.png"
                action Jump("dice_choose_val_1")
        if (chosen_qty == dice_qty and dice_val >= 2) or chosen_qty == 0:
            image "gui/dice_blank.png"
        else:
            imagebutton:
                idle "gui/dice_2.png"
                action Jump("dice_choose_val_2")
        if (chosen_qty == dice_qty and dice_val >= 3) or chosen_qty == 0:
            image "gui/dice_blank.png"
        else:
            imagebutton:
                idle "gui/dice_3.png"
                action Jump("dice_choose_val_3")
                
    hbox:
        xpos 1090
        ypos 400
        spacing 0
        if (chosen_qty == dice_qty and dice_val >= 4) or chosen_qty == 0:
            image "gui/dice_blank.png"
        else:
            imagebutton:
                idle "gui/dice_4.png"
                action Jump("dice_choose_val_4")
        if (chosen_qty == dice_qty and dice_val >= 5) or chosen_qty == 0:
            image "gui/dice_blank.png"
        else:
            imagebutton:
                idle "gui/dice_5.png"
                action Jump("dice_choose_val_5")
        if (chosen_qty == dice_qty and dice_val >= 6) or chosen_qty == 0:
            image "gui/dice_blank.png"
        else:
            imagebutton:
                idle "gui/dice_6.png"
                action Jump("dice_choose_val_6")
                
screen rebecca_bet:
    vbox:
        xpos 1210
        ypos 10
        spacing 0
        image dice_qty_image
        image dice_val_image
        

label start_event_rebecca_dice:
    $dice_player = 0
    call roll_dice from _call_roll_dice
    scene bar_rebecca_dice_strip_1 
    menu:
        "Explain the rules":
            jump dice_help
        "Let's play":
            scene bar_rebecca_dice_strip_2
            jump show_dice_ui
    
label show_dice_ui:
    hide screen rebecca_dice
    show screen hidden_dice
    show screen common_dice
    show screen player_dice
    show screen choose_qty
    jump wait
    
label hide_dice_ui:
    hide screen rebecca_dice
    hide screen hidden_dice
    hide screen common_dice
    hide screen player_dice
    hide screen rebecca_bet
    hide screen choose_val
    hide screen choose_qty
    return
    
label roll_dice:
    python:
        chosen_qty = 0
        chosen_val = 0
        dice_qty = 0
        dice_val = 0
        dice_strategies = ["cautious", "risky", "bluffing"]
        dice_sum = [0,0,0,0,0,0]
        dice_history = [0,0,0,0,0,0]
        rebecca_dice_int = [0,0,0,0,0]
        player_dice_int = [0,0,0,0,0]
        common_dice_int = [0,0,0,0,0]
        rebecca_dice = ["","","","",""]
        player_dice = ["","","","",""]
        common_dice = ["","","","",""]
        for i in range(0,5):
            dice_strategy = dice_strategies[renpy.random.randint(0,2)]
            rebecca_dice_int[i] = renpy.random.randint(1,6)
            player_dice_int[i] = renpy.random.randint(1,6)
            common_dice_int[i] = renpy.random.randint(1,6)
            rebecca_dice[i] = "gui/dice_" + str(rebecca_dice_int[i]) + ".png"
            player_dice[i] = "gui/dice_" + str(player_dice_int[i]) + ".png"
            common_dice[i] = "gui/dice_" + str(common_dice_int[i]) + ".png"
            dice_sum[rebecca_dice_int[i] - 1] += 1
            dice_sum[common_dice_int[i] - 1] += 1
    return
    
label dice_choose_qty_1:
    $chosen_qty = 1
    jump dice_choose_qty_end
    
label dice_choose_qty_2:
    $chosen_qty = 2
    jump dice_choose_qty_end
    
label dice_choose_qty_3:
    $chosen_qty = 3
    jump dice_choose_qty_end
    
label dice_choose_qty_4:
    $chosen_qty = 4
    jump dice_choose_qty_end
    
label dice_choose_qty_5:
    $chosen_qty = 5
    jump dice_choose_qty_end
    
label dice_choose_qty_6:
    $chosen_qty = 6
    jump dice_choose_qty_end
    
label dice_choose_qty_7:
    $chosen_qty = 7
    jump dice_choose_qty_end
    
label dice_choose_qty_8:
    $chosen_qty = 8
    jump dice_choose_qty_end
    
label dice_choose_qty_9:
    $chosen_qty = 9
    jump dice_choose_qty_end
    
label dice_choose_qty_10:
    $chosen_qty = 10
    jump dice_choose_qty_end
    
label dice_choose_qty_end:
    show screen choose_qty
    show screen choose_val
    jump wait
    
label dice_choose_val_1:
    $chosen_val = 1
    jump dice_choose_val_end
    
label dice_choose_val_2:
    $chosen_val = 2
    jump dice_choose_val_end
    
label dice_choose_val_3:
    $chosen_val = 3
    jump dice_choose_val_end
    
label dice_choose_val_4:
    $chosen_val = 4
    jump dice_choose_val_end
    
label dice_choose_val_5:
    $chosen_val = 5
    jump dice_choose_val_end
    
label dice_choose_val_6:
    $chosen_val = 6
    jump dice_choose_val_end
    
label dice_choose_val_end:
    hide screen choose_qty
    hide screen choose_val
    $dice_last_move_player = True
    player "Call me a liar, but I say that there are at least [chosen_qty] dices showing [chosen_val]'s"
    $dice_history[chosen_val - 1] = chosen_qty
    jump rebecca_move
    
label rebecca_move:
    $missing_dices = chosen_qty - dice_sum[chosen_val - 1]
    if (dice_strategy == "cautious"):
        if (missing_dices > 1):
            #rebecca "I'm cautious and you are missing [missing_dices] short"
            jump rebecca_call_liar
        else:
            $best_dice = find_dice()
            if (best_dice[0] < 60):
                #rebecca "I'm cautious and the best move is to say I have [best_dice[1]] of [best_dice[2]] but it has probability of only [best_dice[0]]%"
                jump rebecca_call_liar
    if (dice_strategy == "risky"):
        if (missing_dices > 1):
            #rebecca "I'm risky and you are missing [missing_dices] short"
            jump rebecca_call_liar
        else:
            $best_dice = find_dice()
            if (best_dice[0] < 40):
                #rebecca "I'm risky and the best move is to say I have [best_dice[1]] of [best_dice[2]] but it has probability of only [best_dice[0]]%"
                jump rebecca_call_liar
    if (dice_strategy == "bluffing"):
        if (missing_dices > 2):
            #rebecca "I'm bluffing and you are missing [missing_dices] short"
            jump rebecca_call_liar
        else:
            $best_dice = find_dice()
            if (best_dice[0] < 40):
                #rebecca "I'm bluffing and the best move is to say I have [best_dice[1]] of [best_dice[2]] but it has probability of only [best_dice[0]]%"
                jump rebecca_call_liar
    $dice_qty = best_dice[1]
    $dice_val = best_dice[2]
    $dice_last_move_player = False
    rebecca "I say there are at least [dice_qty] dices showing [dice_val]'s and you may call me a liar if you dare!"
    $dice_qty_image = "gui/qty_" + str(dice_qty) + "x.png"
    $dice_val_image = "gui/dice_" + str(dice_val) + ".png"
    show screen rebecca_bet
    jump show_dice_ui
    
label player_call_liar:
    player "You are a liar and I'll see you naked for that!"
    show screen rebecca_dice
    jump dice_calculate_result
    
label rebecca_call_liar:
    rebecca "You are a liar! Let's see what you've got!"
    show screen rebecca_dice
    jump dice_calculate_result
    
label dice_calculate_result:
    python:
        dice_results = [0,0,0,0,0,0]
        for i in range(0,5):
            dice_results[rebecca_dice_int[i] - 1] += 1
            dice_results[common_dice_int[i] - 1] += 1
            dice_results[player_dice_int[i] - 1] += 1
    if (dice_last_move_player):
        if (dice_results[chosen_val - 1] >= chosen_qty):
            player "Don't call me a liar!"
            jump dice_rebecca_loose
        else:
            player "You got me this time..."
            jump dice_player_loose
    else:
        if (dice_results[dice_val - 1] >= dice_qty):
            player "Ahhh, I really thought I got you this time..."
            jump dice_player_loose
        else:
            rebecca "Fuck! Are you cheating?"
            jump dice_rebecca_loose
            
label dice_rebecca_loose:
    $dice_player -= 1
    
    if dice_player == -1:
        jump dice_rebecca_strip_coat
    elif dice_player == -2:
        jump dice_rebecca_strip_bra
    elif dice_player == -3:
        jump dice_rebecca_strip_stockings
    elif dice_player == -4:
        jump dice_rebecca_strip_panties
    elif dice_player == -5:
        jump dice_rebecca_lost
    elif dice_player == 0:
        rebecca "You win back your boots."
    elif dice_player == 1:
        rebecca "OK, you can have your shirt back."
    elif dice_player == 2:
        rebecca "Such a pity, I quite liked you without your pants..."
    elif dice_player == 3:
        rebecca "Oh, are you really going to put your boxers back on?"
    jump dice_next_roll
    
label dice_player_loose:
    $dice_player += 1
    
    if dice_player == 0:
        rebecca flirting "May I have my coat back? My nipples are getting hard from the cold."
        scene bar_rebecca_dice_strip_2
    elif dice_player == -1:
        rebecca happy "I guess you don't like my breasts or you would've played smarter."
        scene bar_rebecca_dice_strip_3
    elif dice_player == -2:
        rebecca happy "May I have my shoes and stockings back please!"
        scene bar_rebecca_dice_strip_4
    elif dice_player == -3:
        rebecca flirting "Don't think I didn't see you sniffing my panties! Give them back now!"
        scene bar_rebecca_dice_strip_5
    elif dice_player == 1:
        player "I guess I'll have to give you my boots."
    elif dice_player == 2:
        rebecca flirting "I like what I see under your shirt!"
    elif dice_player == 3:
        rebecca happy "Pants! Pants! Pants! Take them off!"
    elif dice_player == 4:
        rebecca happy "Don't try to cheat - your boxers are mine now! Give them to me."
    elif dice_player == 5:
        jump dice_player_lost
    jump dice_next_roll
    
label dice_next_roll:
    call hide_dice_ui from _call_hide_dice_ui
    call roll_dice from _call_roll_dice_1
    jump show_dice_ui
    
label dice_help:
    rebecca "On the left side, you'll see three rows of dices."
    show screen hidden_dice
    rebecca "The top one is mine and only I can see them."
    show screen common_dice
    rebecca "The middle one is the common set - we both know the values of the dices in it."
    show screen player_dice
    rebecca "The bottom one is yours. This means that I can't see them and don't know their values."
    rebecca "We can both bet on how many dices of a certain value there are in the three rows."
    rebecca "The only rule is that you can't bet on a lower number of dices or the same number of dices with a lower value."
    rebecca "If you think that there are less dices of a certain value than what I had bet, you may call me a liar and we both show our dices."
    rebecca "If you were correct in your assumption, I loose and if I was right, you loose."
    rebecca "We play until there is no more clothes left to bet."
    rebecca "I hope it's all clear now, let's not waste anymore time and start playing."
    rebecca "You start first."
    show screen choose_qty
    jump wait
    
label dice_rebecca_strip_coat:
    scene bar_rebecca_coat_strip_1
    $renpy.pause()
    scene bar_rebecca_coat_strip_2
    $renpy.pause()
    scene bar_rebecca_coat_strip_3
    $renpy.pause()
    scene bar_rebecca_dice_strip_3
    jump dice_next_roll
    
label dice_rebecca_strip_bra:
    scene bar_rebecca_bra_strip_1
    $renpy.pause()
    scene bar_rebecca_bra_strip_2
    $renpy.pause()
    scene bar_rebecca_bra_strip_3
    $renpy.pause()
    scene bar_rebecca_dice_strip_4
    jump dice_next_roll
    
label dice_rebecca_strip_stockings:
    scene bar_rebecca_stockings_strip_1
    $renpy.pause()
    scene bar_rebecca_stockings_strip_2
    $renpy.pause()
    scene bar_rebecca_stockings_strip_3
    $renpy.pause()
    scene bar_rebecca_dice_strip_6
    jump dice_next_roll
    
label dice_rebecca_strip_panties:
    scene bar_rebecca_panties_strip_1
    $renpy.pause()
    scene bar_rebecca_panties_strip_2
    $renpy.pause()
    scene bar_rebecca_panties_strip_3
    $renpy.pause()
    scene bar_rebecca_dice_strip_7
    jump dice_next_roll
    
label dice_player_lost:
    rebecca "I've told you I'd see your dick!"
    player "Now what?"
    rebecca happy "Now we go to sleep. It's late."
    call hide_dice_ui from _call_hide_dice_ui_1
    call start_event_rebecca_dice_game from _call_start_event_rebecca_dice_game
    jump sleep
    
label dice_rebecca_lost:
    call hide_dice_ui from _call_hide_dice_ui_2
    player "Looks like you have nothing more to bet."
    rebecca flirting "I can think of something..."
    player "What?"
    rebecca flirting "How about a blowjob?"
    player "Deal, let's play!"
    rebecca flirting "I don't want to play any more."
    rebecca flirting "I want to suck your dick. Take of your pants!"
    scene bar_rebecca_bj_4
    rebecca happy "Oh my! Lana told me you were big, but this is... wow!"
    scene bar_rebecca_bj_2
    $renpy.pause()
    scene bar_rebecca_bj_1
    rebecca flirting "I'm using my both hands and there is so much more of it..."
    scene bar_rebecca_bj_3
    rebecca flirting "I wonder how it tastes."
    player "Only one way to find out."
    scene bar_rebecca_bj_5
    rebecca flirting "I don't know if it would fit in my mouth..."
    scene bar_rebecca_bj_6
    player "I guess it does."
    if (quest_sis_missing.phase >= 11 and (energy >= 300 or global_events.mom_leather)):
        $energy -= 300
        $global_events.mom_leather = True
        jump dice_rebecca_mom
    scene bar_rebecca_bj_5
    rebecca flirting "It does fit, but I don't think I'd be able to deepthroat that monster."
    scene bar_rebecca_bj_6
    $renpy.pause()
    scene bar_rebecca_bj_5
    $renpy.pause()
    scene bar_rebecca_bj_6
    $renpy.pause()
    scene bar_rebecca_bj_5
    player "I'm cumming!"
    scene bar_rebecca_bj_6
    $renpy.pause()
    scene bar_rebecca_bj_7
    rebecca flirting "Thanks for warning me, I didn't want to waste even a drop, but it was so much!"
    player "You were great!"
    rebecca flirting "Better than your mom?"
    player "I don't know - she never gave me a blowjob."
    rebecca happy "I bet you'd like her to..."
    rebecca "Anyway, it's too late - let's go to sleep!"
    call start_event_rebecca_dice_game from _call_start_event_rebecca_dice_game_1
    jump sleep
    
label dice_rebecca_mom:
    if not global_events.mom_leather:
        mom "What the hell are you doing?"
        scene bar_mom_rebecca_1
        player "Mom..."
        mom "I will deal with you later, young man! Right now I want to know why this slut is sucking your dick when I forbade her to have sex with you!"
    else:
        scene bar_mom_rebecca_1
        mom "Are you sucking my son's dick again? Do you want to be punished or what?"
    scene bar_mom_rebecca_2
    rebecca "I'm sorry mistress... It was just a blowjob..."
    mom "You are {i}'sorry'{/i}?"
    rebecca "..."
    mom "Let's see how much {i}'sorry'{/i} you can be!"
    mom "Get down!"
    scene bar_mom_rebecca_3
    mom "So, who will administer the punishment? Me or you?"
    menu:
        "Mom":
            player "You are her master, it should be you."
            jump dice_rebecca_mom_spank_mom
        "Me":
            player "Let me do it for you, mom."
            jump dice_rebecca_mom_spank_greg
                
label dice_rebecca_mom_spank_mom:
    mom "Girl, I want my boots cleaned!"
    scene bar_mom_rebecca_4
    rebecca "Yes, mistress!"
    mom "I said {i}'clean'{/i}! Don't you know what this means? Do I need to punish you?"
    rebecca "..."
    mom "It seems that I do... Assume the position!"
    scene bar_mom_rebecca_5
    mom "When {i}(smack){/i}... I {i}(smack){/i}... Say {i}(smack){/i}... Clean {i}(smack){/i}..."
    mom "You {i}(smack){/i}... Need {i}(smack){/i}... To {i}(smack){/i}... Lick {i}(smack){/i}... Them {i}(smack){/i}"
    scene bar_mom_rebecca_6
    mom "Am I clear?"
    rebecca "Yes, mistress..."
    mom "Good! Now I want you to lick me!"
    scene bar_mom_rebecca_7
    mom flirting "That's it! You are really good in it!"
    mom flirting "Greg, come closer, so you can watch this slut licking my clit!"
    scene bar_mom_rebecca_8
    player "Wow!"
    mom flirting "You like that, don't you?"
    mom flirting "You like watching this slut lick your mom's clit?"
    player "I do..."
    mom flirting "I have an idea..."
    scene bar_mom_rebecca_9
    mom flirting "How about I jerk you off, so you can cum on her face?"
    mom flirting "Would you like that?"
    player "Of course!"
    mom flirting "I wasn't asking you. Girl, would you like my son to cum on your face while you lick my clit?"
    rebecca flirting "Yes, mistress!"
    mom "Greg, I want you to pinch my nipples while she is servicing me!"
    scene bar_mom_rebecca_10
    mom flirting "Hmmm... I like that!"
    mom flirting "Do you like playing with my nipples while I jerk you off?"
    player "Yes mom!"
    mom flirting "Do you want to cum?"
    player "Oh, yes!"
    mom flirting "Alright! Cum on her face!"
    scene bar_mom_rebecca_11
    rebecca flirting "Oh, it's so much!"
    mom "Lick it up, slut! Don't waste even a drop!"
    player "{i}Wow... Mom is really into this...{/i}"
    mom "We are done here! Off to bed, both of you!"
    call start_event_rebecca_dice_game from _call_start_event_rebecca_dice_game_3
    jump sleep

label dice_rebecca_mom_spank_greg:
    mom "OK, but you need to do it hard enough, so she learns her lesson!"
    scene bar_mom_rebecca_12
    $renpy.pause()
    scene bar_mom_rebecca_13
    rebecca flirting "Ohhh!"
    scene bar_mom_rebecca_12
    $renpy.pause()
    scene bar_mom_rebecca_13
    rebecca flirting "Ahhh!"
    scene bar_mom_rebecca_14
    mom "She is enjoying this!"
    player "I think you are right... we need to think of some other punishment!"
    mom flirting "What do you have in mind?"
    player "Get down on your knees!"
    scene bar_mom_rebecca_15
    rebecca flirting "Oh, it's so big!"
    mom "Did I give you permission to talk?"
    rebecca flirting "Sorry, mistress..."
    mom flirting "Though, I have to agree, seeing his big cock stretching your pussy is making me kind of hot..."
    player "{i}What is mom doing?{/i}"
    scene bar_mom_rebecca_16
    mom flirting "I remember what was it like having that big cock in me..."
    mom flirting "Stretching me..."
    mom flirting "It's basically all I can think about since we... you know... fucked."
    scene bar_mom_rebecca_17
    player "Oh yeah!"
    mom flirting "Girl, so you like riding my son?"
    rebecca flirting "Yes mistress!"
    mom flirting "I like watching you do it too."
    scene bar_mom_rebecca_18
    player "{i}She sure does...{/i}"
    mom flirting "I want to taste his cum, so don't make him cum yet!"
    player "{i}What? Mom wants me to cum in her mouth?{/i}"
    player "{i}That is so hot, I don't know if I can hold it any more...{/i}"
    player "Aghhh!"
    mom "Nooo! I said I wanted it!"
    rebecca flirting "It's not too late..."
    scene bar_mom_rebecca_19
    mom flirting "You slut! You want your mistress to lick the cum off your pussy?"
    rebecca flirting "It's the only way..."
    scene bar_mom_rebecca_20
    mom flirting "I don't think that was an effective punishment for her giving you a blowjob, but it sure was fun!"
    mom "Now go to bed, both of you!"
    call start_event_rebecca_dice_game from _call_start_event_rebecca_dice_game_4
    jump sleep
