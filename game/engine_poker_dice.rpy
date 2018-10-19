init python:
    class EnginePokerDice:
        #'game' object should have 'opponent_fold()' method returning call label
        #'game' object should have 'opponent_call()' method returning call label
        #'game' object should have 'on_player_folded()' method returning jump label
        #'game' object should have 'on_dice_roll()' method returning call label
        #'game' object should have 'on_player_win()' method returning call label
        #'game' object should have 'on_player_loose()' method returning call label
        #'game' object should have 'on_game_tie()' method returning call label
        #'game' object should have 'on_game_finished()' method returning jump label
        #'game' object should have 'is_finished()' method returning boolean
        
        
        def __init__(self, game):
            self.game = game
            self.player_folded = False
            self.opponent_folded = False
            self.player_called = False
            self.opponent_called = False
            self.player_first = False
            self.change_allowed = False
            
        def roll_dices(self):
            self.player_first = not self.player_first
            self.poker_dice_player = ["", "", "", "", ""]
            self.poker_dice_opponent = ["", "", "", "", ""]
            self.poker_dice_player_int = [0, 0, 0, 0, 0]
            self.poker_dice_opponent_int = [0, 0, 0, 0, 0]
            for i in range(0,5):
                self.poker_dice_player_int[i] = renpy.random.randint(1,6)
                self.poker_dice_player[i] = "gui/dice_" + str(self.poker_dice_player_int[i]) + ".png"
                self.poker_dice_opponent_int[i] = renpy.random.randint(1,6)
                self.poker_dice_opponent[i] = "gui/dice_" + str(self.poker_dice_opponent_int[i]) + ".png"
            renpy.call(self.game.on_dice_roll())
                
        def switch_dice(self, index):
            if (self.change_allowed):
                if (self.poker_dice_player[index] == "gui/dice_unknown.png"):
                    self.poker_dice_player[index] = "gui/dice_" + str(self.poker_dice_player_int[index]) + ".png"
                else:
                    self.poker_dice_player[index] = "gui/dice_unknown.png"
                
        def change_player_dices(self):
            for i in range(0,5):
                if (self.poker_dice_player[i] == "gui/dice_unknown.png"):
                    self.poker_dice_player_int[i] = renpy.random.randint(1,6)
                    self.poker_dice_player[i] = "gui/dice_" + str(self.poker_dice_player_int[i]) + ".png"
                if (self.poker_dice_opponent_int[i] == 0):
                    self.poker_dice_opponent_int[i] = renpy.random.randint(1,6)
                    self.poker_dice_opponent[i] = "gui/dice_" + str(self.poker_dice_opponent_int[i]) + ".png"
                    
        def change_opponent_dices(self):
            buckets = self.get_buckets(self.poker_dice_opponent_int)
            tier = self.get_tier(buckets)
            prob = renpy.random.randint(1,6)
            changed = 0
            if prob == 1:
                changed = renpy.random.randint(2,4)
                i = 0
                while i < changed:
                    self.poker_dice_opponent_int[i] = renpy.random.randint(1,6)
                    i = i + 1
            elif (tier == 7):
                changed = 0
            elif (tier == 6):
                value = buckets.index(1) + 1
                index = self.poker_dice_opponent_int.index(value)
                self.poker_dice_opponent_int[index] = renpy.random.randint(1,6)
                changed = 1
            elif (tier == 5):
                changed = 0
            elif (tier == 4):
                changged = 0
            elif (tier == 3):
                for i in range(6):
                    if (buckets[i] == 1):
                        index = self.poker_dice_opponent_int.index(i + 1)
                        self.poker_dice_opponent_int[index] = renpy.random.randint(1,6)
                        changed += 1
            elif (tier == 2):
                value = buckets.index(1) + 1
                index = self.poker_dice_opponent_int.index(value)
                self.poker_dice_opponent_int[index] = renpy.random.randint(1,6)
                changed = 1
            elif (tier == 1):
                for i in range(6):
                    if (buckets[i] == 1):
                        index = self.poker_dice_opponent_int.index(i + 1)
                        self.poker_dice_opponent_int[index] = renpy.random.randint(1,6)
                        changed += 1
            else:
                for i in range(5):
                    self.poker_dice_opponent_int[i] = renpy.random.randint(1,6)
                    changed += 1
            for i in range(5):
                self.poker_dice_opponent[i] = "gui/dice_" + str(self.poker_dice_opponent_int[i]) + ".png"
            renpy.call(self.game.on_oponent_switch(changed))
        
        def fold_player(self):
            self.player_folded = True
            self.opponent_folded = False
            renpy.jump(self.game.on_player_folded())
            
        def fold_opponent(self):
            self.player_folded = False
            self.opponent_folded = True
            
        def call_player(self):
            self.player_folded = False
            self.player_called = True
            if (self.opponent_called):
                renpy.jump("poker_dice_end_round")
            else:
                if (self.decide_opponent()):
                    renpy.jump("poker_dice_end_round")
                else:
                    renpy.jump(self.game.opponent_fold())
                
        def call_opponent(self):
            self.opponent_folded = False
            self.opponent_called = True
            if (self.player_called):
                renpy.jump("poker_dice_end_round")
            else:
                renpy.jump(self.game.opponent_call())
                
        def get_buckets(self, dice_int):
            buckets = [0, 0, 0, 0, 0, 0]
            for i in range(5):
                buckets[dice_int[i] - 1] += 1
            return buckets
            
        def get_tier(self, buckets):
            tier = 0
            if (5 in buckets):
                tier = 7
            elif (4 in buckets):
                tier = 6
            elif (3 in buckets and 2 in buckets):
                tier = 5
            elif (3 in buckets):
                tier = 3
            elif (buckets.count(2) == 2):
                tier = 2
            elif (2 in buckets):
                tier = 1
            elif (buckets.index(0) == 0 or buckets.index(0) == 5):
                tier = 4
            return tier
                
        def decide_opponent(self):
            if (self.opponent_folded):
                return True
            buckets = self.get_buckets(self.poker_dice_opponent_int)
            tier = self.get_tier(buckets)
            prob = renpy.random.randint(1,6)
            if (tier >= 2):
                return prob >= 2
            elif (tier == 1 and self.player_called and buckets.index(2) <= 3):
                return False
            else:
                return True
                
        def get_player_points(self, player_tier, player_buckets, opponent_tier, opponent_buckets):
            if (player_tier > opponent_tier):
                return 1
            if (opponent_tier > player_tier):
                return -1
            tier = player_tier #=opponent_tier
            if (tier == 7): #5 of the same
                player_number = player_buckets.index(5)
                opponent_number = opponent_buckets.index(5)
                if (player_number > opponent_number):
                    return 1
                if (opponent_number > player_number):
                    return -1
                return 0
            if (tier == 6): #4 of the same
                player_number = player_buckets.index(4)
                opponent_number = opponent_buckets.index(4)
                if (player_number > opponent_number):
                    return 1
                if (opponent_number > player_number):
                    return -1
                player_additional = player_buckets.index(1)
                opponent_additional = opponent_buckets.index(1)
                if (player_additional > opponent_additional):
                    return 1
                if (opponent_additional > player_additional):
                    return -1
                return 0
            if (tier == 5): #full house
                player_number = player_buckets.index(3)
                opponent_number = opponent_buckets.index(3)
                if (player_number > opponent_number):
                    return 1
                if (opponent_number > player_number):
                    return -1
                player_additional = player_buckets.index(2)
                opponent_additional = opponent_buckets.index(2)
                if (player_additional > opponent_additional):
                    return 1
                if (opponent_additional > player_additional):
                    return -1
                return 0
            if (tier == 4): #straight
                player_number = player_buckets.index(0)
                opponent_number = opponent_buckets.index(0)
                if (player_number < opponent_number):
                    return 1
                if (opponent_number < player_number):
                    return -1
                return 0
            if (tier == 3): #3 of the same
                player_number = player_buckets.index(3)
                opponent_number = opponent_buckets.index(3)
                if (player_number > opponent_number):
                    return 1
                if (opponent_number > player_number):
                    return -1
                for i in range(6):
                    if (player_buckets[5 - i] > opponent_buckets[5 - i]):
                        return 1
                    if (opponent_buckets[5 - i] > player_buckets[5 - i]):
                        return -1
                return 0
            if (tier == 2): #double 2's
                player_number = 5 - player_buckets[::-1].index(2)
                opponent_number = 5 - opponent_buckets[::-1].index(2)
                if (player_number > opponent_number):
                    return 1
                if (opponent_number > player_number):
                    return -1
                player_additional = player_buckets.index(2)
                opponent_additional = opponent_buckets.index(2)
                if (player_additional > opponent_additional):
                    return 1
                if (opponent_additional > player_additional):
                    return -1
                player_weakest = player_buckets.index(1)
                opponent_weakest = opponent_buckets.index(1)
                if (player_weakest > opponent_weakest):
                    return 1
                if (opponent_weakest > player_weakest):
                    return -1
                return 0
            if (tier == 1): #2 of the same
                player_number = player_buckets.index(2)
                opponent_number = opponent_buckets.index(2)
                if (player_number > opponent_number):
                    return 1
                if (opponent_number > player_number):
                    return -1
                for i in range(6):
                    if (player_buckets[5 - i] > opponent_buckets[5 - i]):
                        return 1
                    if (opponent_buckets[5 - i] > player_buckets[5 - i]):
                        return -1
                return 0
            #high number
            player_number = player_buckets.index(0)
            opponent_number = opponent_buckets.index(0)
            if (player_number < opponent_number):
                return 1
            if (opponent_number < player_number):
                return -1
            return 0
            
        def end_round(self):
            player_buckets = self.get_buckets(self.poker_dice_player_int)
            opponent_buckets = self.get_buckets(self.poker_dice_opponent_int)
            player_tier = self.get_tier(player_buckets)
            opponent_tier = self.get_tier(opponent_buckets)
            player_point = self.get_player_points(player_tier, player_buckets, opponent_tier, opponent_buckets)
            if (player_point > 0):
                renpy.jump(self.game.on_player_win())
            elif (player_point < 0):
                renpy.jump(self.game.on_player_loose())
            else:
                renpy.jump(self.game.on_game_tie())
            
screen engine_poker_dice_hidden:
    hbox:
        xpos 10
        ypos 50
        spacing 0
        image "gui/dice_unknown.png"
        image "gui/dice_unknown.png"
        image "gui/dice_unknown.png"
        image "gui/dice_unknown.png"
        image "gui/dice_unknown.png"
        
screen engine_poker_dice_player:
    hbox:
        xpos 10
        ypos 400
        spacing 0
        image dice_poker_delegate.poker_dice_player[0]
        image dice_poker_delegate.poker_dice_player[1]
        image dice_poker_delegate.poker_dice_player[2]
        image dice_poker_delegate.poker_dice_player[3]
        image dice_poker_delegate.poker_dice_player[4]
        
screen engine_poker_dice_player_active:
    hbox:
        xpos 10
        ypos 400
        spacing 0
        imagebutton:
            idle dice_poker_delegate.poker_dice_player[0]
            action Jump("poker_dice_switch_0")
        imagebutton:
            idle dice_poker_delegate.poker_dice_player[1]
            action Jump("poker_dice_switch_1")
        imagebutton:
            idle dice_poker_delegate.poker_dice_player[2]
            action Jump("poker_dice_switch_2")
        imagebutton:
            idle dice_poker_delegate.poker_dice_player[3]
            action Jump("poker_dice_switch_3")
        imagebutton:
            idle dice_poker_delegate.poker_dice_player[4]
            action Jump("poker_dice_switch_4")
        
screen engine_poker_dice_opponent:
    hbox:
        xpos 10
        ypos 50
        spacing 0
        image dice_poker_delegate.poker_dice_opponent[0]
        image dice_poker_delegate.poker_dice_opponent[1]
        image dice_poker_delegate.poker_dice_opponent[2]
        image dice_poker_delegate.poker_dice_opponent[3]
        image dice_poker_delegate.poker_dice_opponent[4]
        
screen engine_poker_dice_decision:
    vbox:
        xpos 10
        ypos 314
        spacing 0
        imagebutton:
            idle "gui/call.png"
            action Jump("poker_dice_call")
        imagebutton:
            idle "gui/fold.png"
            action Jump("poker_dice_fold")
            
screen engine_poker_dice_end_switch:
    vbox:
        xpos 10
        ypos 350
        spacing 0
        imagebutton:
            idle "gui/roll.png"
            action Jump("poker_dice_end_switch")
            
label poker_dice_start_round:
    $dice_poker_delegate.roll_dices()
    jump poker_dice_start_switch
        
label poker_dice_switch_0:
    $dice_poker_delegate.switch_dice(0)
    show screen engine_poker_dice_player
    jump wait
        
label poker_dice_switch_1:
    $dice_poker_delegate.switch_dice(1)
    show screen engine_poker_dice_player
    jump wait
        
label poker_dice_switch_2:
    $dice_poker_delegate.switch_dice(2)
    show screen engine_poker_dice_player
    jump wait
        
label poker_dice_switch_3:
    $dice_poker_delegate.switch_dice(3)
    show screen engine_poker_dice_player
    jump wait
        
label poker_dice_switch_4:
    $dice_poker_delegate.switch_dice(4)
    show screen engine_poker_dice_player
    jump wait

label poker_dice_fold:
    if (dice_poker_delegate.player_folded):
        player "{i}I folded the last game, so I can't do that now.{/i}"
    else:
        hide screen engine_poker_dice_decision
        $dice_poker_delegate.fold_player()
    jump wait

label poker_dice_call:
    hide screen engine_poker_dice_decision
    $dice_poker_delegate.call_player()
    jump wait
    
label poker_dice_start_switch:
    hide screen engine_poker_dice_decision
    show screen engine_poker_dice_hidden
    show screen engine_poker_dice_player
    player "Let's choose which dices to switch..."
    if (not dice_poker_delegate.player_first):
        $dice_poker_delegate.change_opponent_dices()
    $dice_poker_delegate.change_allowed = True
    hide screen engine_poker_dice_player
    show screen engine_poker_dice_player_active
    show screen engine_poker_dice_end_switch
    jump wait
    
label poker_dice_end_switch:
    hide screen engine_poker_dice_player_active
    show screen engine_poker_dice_player
    hide screen engine_poker_dice_end_switch
    player "I'm ready!"
    $dice_poker_delegate.change_player_dices()
    if (dice_poker_delegate.player_first):
        $dice_poker_delegate.change_opponent_dices()
    show screen engine_poker_dice_decision
    jump wait
    
label poker_dice_end_round:
    player "Let's see who wins. Show your dices!"
    hide screen engine_poker_dice_hidden
    show screen engine_poker_dice_opponent
    $dice_poker_delegate.end_round()
    jump wait