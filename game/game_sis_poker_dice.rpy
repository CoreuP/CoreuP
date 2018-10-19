#'game' object should have 'opponent_fold()' method returning call label
#'game' object should have 'opponent_call()' method returning call label
#'game' object should have 'on_player_folded()' method returning jump label
#'game' object should have 'on_dice_roll()' method returning call label
#'game' object should have 'on_player_win()' method returning call label
#'game' object should have 'on_player_loose()' method returning call label
#'game' object should have 'on_game_tie()' method returning call label
#'game' object should have 'on_game_finished()' method returning jump label
#'game' object should have 'is_finished()' method returning boolean

init python:
    class SisPokerDice:
        def __init__(self):
            self.player_points = 0
        
        def opponent_fold(self):
            return "game_sis_poker_dice_sis_fold"
            
        def opponent_call(self):
            return "game_sis_poker_dice_sis_call"
            
        def on_player_folded(self):
            return "game_sis_poker_dice_player_fold"
            
        def on_oponent_switch(self, number):
            return "game_sis_poker_opponent_switch_" + str(number)
            
        def on_dice_roll(self):
            return "game_sis_poker_dice_on_roll"
            
        def on_player_win(self):
            self.player_points +=1
            return "game_sis_poker_dice_player_win"
            
        def on_player_loose(self):
            self.player_points -=1
            return "game_sis_poker_dice_player_loose"
            
        def on_game_tie(self):
            return "game_sis_poker_dice_game_tie"
            
        def on_game_finished(self):
            return "game_sis_poker_dice_on_finished"
            
        def is_finished(self):
            return self.player_points < 5
            
label game_sis_poker_dice_start:
    $game = SisPokerDice()
    $dice_poker_delegate = EnginePokerDice(game)
    call start_event_rebecca_dice_game from _call_start_event_rebecca_dice_game_2
    if not global_events.played_game_with_lana:
        sis happy "My mom explained the rules of the game she played with you, but I don't like it."
        sis happy "Let's play something else."
        player "Like what?"
        sis happy "Have you heard of poker dice?"
        sis happy "The rules are the same as in poker but instead of cards, you play with dices."
    else:
        sis flirting "Are you ready to loose your clothes?"
    $global_events.played_game_with_lana = True
    menu:
        "Explain the rules":
            jump game_sis_poker_dice_explain_rules
        "Let's begin":
            sis happy "OK then, let's start!"
            scene bar_sis_strip_1
            jump poker_dice_start_round
    
label game_sis_poker_dice_explain_rules:
    sis happy "The rules are very simple."
    sis happy "On the top, you'll see my dices, on the bottom, you'll see yours."
    sis happy "You can choose which dices to change and which to keep."
    sis happy "Once you are done with that, you can decide if you want to play or fold."
    sis happy "But you can't fold two games in a row, so if you fold one game you are required to play the next one."
    sis happy "The sets are matched just like hands in poker."
    sis happy "A pair, two pairs, three of the same, a straight, full house, a four and a five."
    sis happy "Of course the looser has to strip."
    player "Sounds fun! Let's start!"
    scene bar_sis_strip_1
    jump poker_dice_start_round

label game_sis_poker_dice_sis_fold:
    sis sad "This is bullshit! I fold!"
    hide screen engine_poker_dice_player
    hide screen engine_poker_dice_hidden
    $dice_poker_delegate.fold_opponent()
    jump poker_dice_start_round
    
label game_sis_poker_dice_sis_call:
    sis happy "I have a good feeling about these dices!"
    return
    
label game_sis_poker_dice_on_roll:
    sis "New game, new chance to see you naked!"
    return 
    
label game_sis_poker_opponent_switch_0:
    sis happy "I don't want to switch any dices"
    return
    
label game_sis_poker_opponent_switch_1:
    sis happy "I want to switch just one dice."
    return
    
label game_sis_poker_opponent_switch_2:
    sis happy "I want to switch just a couple of dice."
    return
    
label game_sis_poker_opponent_switch_3:
    sis "I want to switch three dices."
    return
    
label game_sis_poker_opponent_switch_4:
    sis sad "I want to switch four dices."
    return
    
label game_sis_poker_opponent_switch_5:
    sis sad "I want to switch all five dices."
    return
    
label game_sis_poker_dice_player_fold:
    sis happy "I didn't think you were a chicken!"
    jump poker_dice_start_round
    
label game_sis_poker_dice_player_win:
    sis "Shit! You win!"
    hide screen engine_poker_dice_player
    hide screen engine_poker_dice_opponent
    if (game.player_points == 5):
        sis "I shouldn't have promised that!"
        sis flirting "I think it was too big of an incentive for you to win!"
        player "Don't try to talk yourself out of it!"
        sis flirting "Who's trying?"
        sis flirting "Drop your pants!"
        call game_sis_poker_dice_finish from _call_game_sis_poker_dice_finish
        jump sleep
    elif (game.player_points == -3):
        sis "You win your boxers back... Pity!"
    elif (game.player_points == -2):
        sis "You can have your pants back."
    elif (game.player_points == -1):
        sis "Here is your shirt... I liked you more without it!"
    elif (game.player_points == 0):
        sis "You can put on your shoes."
    elif (game.player_points == 1):
        sis happy "I don't like the dress anyway!"
        call game_sis_poker_dice_strip_1 from _call_game_sis_poker_dice_strip_1
    elif (game.player_points == 2):
        sis happy "This bra is really uncomfortable!"
        call game_sis_poker_dice_strip_2 from _call_game_sis_poker_dice_strip_2
    elif (game.player_points == 3):
        sis happy "What would it be... the panties or the shoes?"
        sis flirting "I really like the shoes!"
        call game_sis_poker_dice_strip_3 from _call_game_sis_poker_dice_strip_3
    elif (game.player_points == 4):
        sis happy "So sad that the shoes must go too..."
        call game_sis_poker_dice_strip_4 from _call_game_sis_poker_dice_strip_4
        player "I win!"
        sis flirting "Let's play another round."
        player "But you have nothing more to bet!"
        sis flirting "What about some playtime with my feet?"
        player "Deal!"
    jump poker_dice_start_round
    
label game_sis_poker_dice_player_loose:
    sis happy "My dices are better!"
    hide screen engine_poker_dice_player
    hide screen engine_poker_dice_opponent
    if (game.player_points == -4):
        sis flirting "Finally! Your boxers are mine!"
        player "I want a re-match!"
        sis flirting "Anytime!"
        call game_sis_poker_dice_finish from _call_game_sis_poker_dice_finish_1
        jump sleep
    if (game.player_points == -3):
        sis "The pants! Give them to me!"
    elif (game.player_points == -2):
        sis happy "So what would it be this time? Your pants or your shirt?"
        player "The shirt."
        sis flirting "Whatever - I'll have your pants too after the next game!"
    elif (game.player_points == -1):
        sis flirting "So what would you like to start off with?"
        player "How about my shoes?"
        sis happy "Boring!"
    elif (game.player_points == 0):
        sis happy "Let me put my dress back on..."
        scene bar_sis_strip_1
    elif (game.player_points == 1):
        sis happy "Don't you enjoy looking at my tits?"
        player "Of course I do! You don't have to put your bra on, if you don't like it..."
        sis flirting "But how will you know that you should try harder to win?"
        scene bar_sis_strip_2
    elif (game.player_points == 2):
        sis happy "OK you may sniff my panties one last time before giving them back... pervert!"
        scene bar_sis_strip_3
    elif (game.player_points == 3):
        sis happy "Yey! I won my shoes back!"
        player "What's with women and their shoes?"
        sis happy "Just give them back!"
        scene bar_sis_strip_4
    jump poker_dice_start_round
    
label game_sis_poker_dice_game_tie:
    sis "I can't believe it! We have a tie!"
    jump poker_dice_start_round
    
label game_sis_poker_dice_on_finished:
    sis happy "Enough fooling around. Let's go to bed!"
    jump sleep
    
label game_sis_poker_dice_strip_1:
    scene bar_sis_strip_dress_1
    $renpy.pause()
    scene bar_sis_strip_dress_2
    $renpy.pause()
    scene bar_sis_strip_dress_3
    $renpy.pause()
    scene bar_sis_strip_dress_4
    $renpy.pause()
    scene bar_sis_strip_dress_5
    $renpy.pause()
    scene bar_sis_strip_dress_6
    $renpy.pause()
    scene bar_sis_strip_2
    return
    
label game_sis_poker_dice_strip_2:
    scene bar_sis_strip_bra_1
    $renpy.pause()
    scene bar_sis_strip_bra_2
    $renpy.pause()
    scene bar_sis_strip_bra_3
    $renpy.pause()
    scene bar_sis_strip_bra_4
    $renpy.pause()
    scene bar_sis_strip_3
    return
    
label game_sis_poker_dice_strip_3:
    scene bar_sis_strip_panties_1
    $renpy.pause()
    scene bar_sis_strip_panties_2
    $renpy.pause()
    scene bar_sis_strip_panties_3
    $renpy.pause()
    scene bar_sis_strip_panties_4
    $renpy.pause()
    scene bar_sis_strip_panties_5
    $renpy.pause()
    scene bar_sis_strip_4
    return
    
label game_sis_poker_dice_strip_4:
    scene bar_sis_strip_shoes_1
    $renpy.pause()
    scene bar_sis_strip_shoes_2
    $renpy.pause()
    scene bar_sis_strip_shoes_3
    $renpy.pause()
    scene bar_sis_strip_shoes_4
    $renpy.pause()
    scene bar_sis_strip_shoes_5
    $renpy.pause()
    scene bar_sis_strip_5
    return
    
label game_sis_poker_dice_finish:
    scene bar_sis_strip_fj_1
    sis flirting "You really like my feet, don't you?"
    player "I do."
    sis flirting "And I really like you hard dick rubbing against them!"
    scene bar_sis_strip_fj_2
    sis flirting "Isn't this better?"
    player "Your feet are so soft!"
    sis flirting "Kneel down!"
    scene bar_sis_strip_fj_3
    player "Oh yeah! This is so much better!"
    sis flirting "I'm glad you like it!"
    sis flirting "But I have an idea what you would like even more!"
    scene bar_sis_strip_fj_4
    sis flirting "Do you like my ass?"
    sis flirting "From what I can feel, I must say that you really like looking at my ass!"
    scene bar_sis_strip_fj_5
    player "Oh yeah! I'm cumming!"
    sis flirting "Yes! Spray your cum all over my ass!"
    scene bar_sis_strip_fj_6
    player "You are incredible!"
    sis happy "Thank you! You are not so bad yourself, you know..."
    sis happy "But now it's time to clean ourselves and go to bed."
    if not quest_sis_missing.active:
        call quest_sis_missing_start from _call_quest_sis_missing_start
    return