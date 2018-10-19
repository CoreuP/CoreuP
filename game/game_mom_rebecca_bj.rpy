# 'game' object should have the following methods returning call labels:
# on_player_start()
# on_opponent_start()
# on_opponent_second()
# on_game_end()
# on_opponent_hit()
# on_opponent_stay()
# on_opponent_win()
# on_player_win()
# on_draw()

init python:
    class MomRebeccaBJ:
        def __init__(self):
            self.player_points = 0

        def on_player_start(self):
            return "mom_rebecca_bj_on_player_start"

        def on_player_second(self):
            return "mom_rebecca_bj_on_player_second"

        def on_opponent_start(self):
            return "mom_rebecca_bj_on_opponent_start"

        def on_opponent_second(self):
            return "mom_rebecca_bj_on_player_start"

        def on_opponent_second(self):
            return "mom_rebecca_bj_on_opponent_second"

        def on_game_end(self):
            return "mom_rebecca_bj_on_game_end"

        def on_opponent_hit(self):
            return "mom_rebecca_bj_on_opponent_hit"

        def on_opponent_stay(self):
            return "mom_rebecca_bj_on_opponent_stay"

        def on_opponent_win(self):
            return "mom_rebecca_bj_on_opponent_win"

        def on_player_win(self):
            return "mom_rebecca_bj_on_player_win"

        def on_draw(self):
            return "mom_rebecca_bj_on_draw"

        def on_opponent_bust(self):
            return "mom_rebecca_bj_on_opponent_bust"

        def on_player_bust(self):
            return "mom_rebecca_bj_on_player_bust"


label game_mom_rebecca_bj_start:
    $game = MomRebeccaBJ()
    $bj_delegate = EngineBlackJack(game)
    scene bar_mom_rebecca_strip_1
    mom flirting "Are you ready?"
    player "Are you?"
    rebecca flirting "We will be playing 2-on-1."
    rebecca flirting "Just the way you like it..."
    player "So, who is dealing first?"
    mom flirting "We are."
    jump game_mom_rebecca_bj_deal

label game_mom_rebecca_bj_deal:
    show screen bj_opponent_cards_shown
    show screen bj_player_cards
    jump bj_start_round

label mom_rebecca_bj_on_player_start:
    mom "Do you want a new card or do you stay?"
    jump bj_player_play

label mom_rebecca_bj_on_player_second:
    player "My turn now."
    jump bj_player_play

label mom_rebecca_bj_on_opponent_start:
    rebecca "OK, let's see..."
    jump bj_opponent_play

label mom_rebecca_bj_on_opponent_second:
    player "I stay."
    mom "Now it's our turn!"
    jump bj_opponent_play

label mom_rebecca_bj_on_game_end:
    player "That's enough for me."
    jump bj_player_stay

label mom_rebecca_bj_on_opponent_hit:
    rebecca "Let's have another card!"
    jump bj_opponent_hit

label mom_rebecca_bj_on_opponent_stay:
    mom "I think this will be enough."
    rebecca "Me too."
    jump bj_opponent_stay

label mom_rebecca_bj_on_opponent_win:
    rebecca "We win!"
    hide screen bj_opponent_cards_shown
    hide screen bj_player_cards
    $bj_delegate.game.player_points -= 1
    if (bj_delegate.game.player_points == -5):
        mom "You've lost..."
        rebecca flirting "But we have something planned..."
        jump mom_rebecca_bj_strip_4
    elif (bj_delegate.game.player_points == -4):
        rebecca "The boxers must go..."
    elif (bj_delegate.game.player_points == -3):
        mom "The pants are next!"
    elif (bj_delegate.game.player_points == -2):
        mom "Take off your shoes!"
    elif (bj_delegate.game.player_points == -1):
        rebecca "Let's start with the shirt!"
    elif (bj_delegate.game.player_points == 0):
        scene bar_mom_rebecca_strip_1
    elif (bj_delegate.game.player_points == 1):
        scene bar_mom_rebecca_strip_2
    elif (bj_delegate.game.player_points == 2):
        scene bar_mom_rebecca_strip_3
    elif (bj_delegate.game.player_points == 3):
        scene bar_mom_rebecca_strip_4
    jump game_mom_rebecca_bj_deal

label mom_rebecca_bj_on_player_win:
    mom "It's your fault!"
    rebecca "How is this my fault?"
    hide screen bj_opponent_cards_shown
    hide screen bj_player_cards
    $bj_delegate.game.player_points += 1
    if (bj_delegate.game.player_points == -3):
        call mom_rebecca_bj_get_boxers from _call_mom_rebecca_bj_get_boxers
    elif (bj_delegate.game.player_points == -2):
        call mom_rebecca_bj_get_pants from _call_mom_rebecca_bj_get_pants
    elif (bj_delegate.game.player_points == -1):
        call mom_rebecca_bj_get_shoes from _call_mom_rebecca_bj_get_shoes
    elif (bj_delegate.game.player_points == 0):
        call mom_rebecca_bj_get_shirt from _call_mom_rebecca_bj_get_shirt
    elif (bj_delegate.game.player_points == 1):
        call mom_rebecca_bj_strip_1 from _call_mom_rebecca_bj_strip_1
    elif (bj_delegate.game.player_points == 2):
        call mom_rebecca_bj_strip_2 from _call_mom_rebecca_bj_strip_2
    elif (bj_delegate.game.player_points == 3):
        call mom_rebecca_bj_strip_3 from _call_mom_rebecca_bj_strip_3
    elif (bj_delegate.game.player_points == 4):
        mom flirting "You've won again, Greg..."
        rebecca flirting "And I think you deserve a prize!"
        jump mom_rebecca_bj_strip_4
    jump game_mom_rebecca_bj_deal

label mom_rebecca_bj_on_draw:
    mom "It's a draw."
    jump game_mom_rebecca_bj_deal

label mom_rebecca_bj_on_player_bust:
    hide screen bj_buttons
    player "Shit! I went too far."
    jump mom_rebecca_bj_on_opponent_win

label mom_rebecca_bj_on_opponent_bust:
    mom "I told you not to get that last card..."
    jump mom_rebecca_bj_on_player_win

label mom_rebecca_bj_get_boxers:
    rebecca "You win your boxers back."
    mom "Oh, I liked you playing naked..."
    return

label mom_rebecca_bj_get_pants:
    mom "There are your pants."
    rebecca "Pity..."
    return

label mom_rebecca_bj_get_shoes:
    rebecca "OK - here are your shoes."
    return

label mom_rebecca_bj_get_shirt:
    mom "Here is your shirt."
    return

label mom_rebecca_bj_strip_1:
    hide screen bj_opponent_cards_shown
    hide screen bj_player_cards
    scene bar_mom_rebecca_strip_1_1
    pause
    scene bar_mom_rebecca_strip_1_2
    pause
    scene bar_mom_rebecca_strip_1_3
    pause
    scene bar_mom_rebecca_strip_1_4
    pause
    scene bar_mom_rebecca_strip_1_5
    pause

    scene bar_mom_rebecca_strip_2
    return

label mom_rebecca_bj_strip_2:
    hide screen bj_opponent_cards_shown
    hide screen bj_player_cards
    scene bar_mom_rebecca_strip_2_1
    pause
    scene bar_mom_rebecca_strip_2_2
    pause
    scene bar_mom_rebecca_strip_2_3
    pause
    scene bar_mom_rebecca_strip_2_4
    pause

    scene bar_mom_rebecca_strip_3
    return

label mom_rebecca_bj_strip_3:
    hide screen bj_opponent_cards_shown
    hide screen bj_player_cards
    mom "I think you sabotage our game, so Greg can see you naked... I'll need to punish you!"
    scene bar_mom_rebecca_strip_3_1
    pause
    scene bar_mom_rebecca_strip_3_2
    pause
    scene bar_mom_rebecca_strip_3_3
    pause
    scene bar_mom_rebecca_strip_3_4
    pause

    scene bar_mom_rebecca_strip_4
    return

label mom_rebecca_bj_strip_4:
    hide screen bj_opponent_cards_shown
    hide screen bj_player_cards
    scene bar_mom_rebecca_strip_4_1
    pause
    scene bar_mom_rebecca_strip_hj animated:
        "bar_mom_rebecca_strip_4_2" with dissolve
        pause 0.6
        "bar_mom_rebecca_strip_4_2_a" with dissolve
        pause 0.6
        repeat
    pause
    mom flirting "I want you inside me!"
    scene bar_mom_rebecca_strip_4_3
    mom "Oh that's so good!"
    player "{i}Looks like Rebecca is having fun too...{/i}"
    scene bar_mom_rebecca_strip_4_4
    player "{i}I wonder how will mom react if I...{/i}"
    scene bar_mom_rebecca_strip_4_5
    mom flirting "You naughty boy!"
    scene bar_mom_rebecca_strip_doggy animated:
        "bar_mom_rebecca_strip_4_5" with dissolve
        pause 0.6
        "bar_mom_rebecca_strip_4_5_a" with dissolve
        pause 0.6
        repeat
    pause
    player "I'm going to cum!"
    mom flirting "I want it on my tits!"
    scene bar_mom_rebecca_strip_4_6
    mom flirting "You sprayed your cum all over me!"
    rebecca flirting "I want to taste it!"
    scene bar_mom_rebecca_strip_4_7
    rebecca flirting "Mmmm..."
    mom flirting "That's not fair! I want a lick too!"
    scene bar_mom_rebecca_strip_4_8
    pause

    jump mom_rebecca_bj_win

label mom_rebecca_bj_win:
    rebecca "Oh shit! How is he going to connect now?"
    mom "What do you... oh shit!"
    player "What?"
    mom "Didn't you need to be... {i}excited{/i} to establish the connection to the surveillance system?"
    player "And what makes you think that I'm not?"
    mom "But you just came!"
    player "If it was up to me, we'd have another round right here and now!"
    rebecca flirting "Let's finish the job first and then you can have us anytime you want!"
    jump quest_make_a_plan_execute_plan
