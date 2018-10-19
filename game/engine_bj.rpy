init python:
    class EngineBlackJack:
        # 'game' object should have the following methods returning call labels:
        # on_player_start()
        # on_opponent_start()
        # on_opponent_second()
        # on_game_end()
        # on_opponen_hit()
        # on_opponent_stay()
        # on_opponent_win()
        # on_player_win()
        # on_draw()

        def __init__(self, game):
            self.game = game
            self.player_folded = False
            self.opponent_folded = False
            self.player_called = False
            self.opponent_called = False
            self.player_first = False
            self.player_score = 0
            self.opponent_score = 0
            self.shuffle()

        def shuffle(self):
            self.full_deck = ["2_c.png", "3_c.png", "4_c.png", "5_c.png", "6_c.png", "7_c.png", "8_c.png", "9_c.png", "10_c.png", "j_c.png", "q_c.png", "k_c.png", "a_c.png",
                              "2_d.png", "3_d.png", "4_d.png", "5_d.png", "6_d.png", "7_d.png", "8_d.png", "9_d.png", "10_d.png", "j_d.png", "q_d.png", "k_d.png", "a_d.png",
                              "2_h.png", "3_h.png", "4_h.png", "5_h.png", "6_h.png", "7_h.png", "8_h.png", "9_h.png", "10_h.png", "j_h.png", "q_h.png", "k_h.png", "a_h.png",
                              "2_s.png", "3_s.png", "4_s.png", "5_s.png", "6_s.png", "7_s.png", "8_s.png", "9_s.png", "10_s.png", "j_s.png", "q_s.png", "k_s.png", "a_s.png"]

            for i in range(1, 100):
                p1 = renpy.random.randint(0, 51)
                p2 = renpy.random.randint(0, 51)
                temp = self.full_deck[p1]
                self.full_deck[p1] = self.full_deck[p2]
                self.full_deck[p2] = temp

            self.current_index = 0

        def calculate_score(self, deck):
            score = 0
            for card in deck:
                if card.startswith("2"):
                    score += 2
                elif card.startswith("3"):
                    score += 3
                elif card.startswith("4"):
                    score += 4
                elif card.startswith("5"):
                    score += 5
                elif card.startswith("6"):
                    score += 6
                elif card.startswith("7"):
                    score += 7
                elif card.startswith("8"):
                    score += 8
                elif card.startswith("9"):
                    score += 9
                elif card.startswith("10"):
                    score += 10
                elif card.startswith("j"):
                    score += 10
                elif card.startswith("q"):
                    score += 10
                elif card.startswith("k"):
                    score += 10
                elif card.startswith("a"):
                    if score <= 10:
                        score += 11
                    else:
                        score += 1
            return score

        def deal(self):
            self.player_first = not self.player_first
            self.player_deck = [self.full_deck[self.current_index], self.full_deck[self.current_index+2]]
            self.opponent_deck = [self.full_deck[self.current_index+1], self.full_deck[self.current_index+3]]
            self.current_index = self.current_index+4
            self.player_score = self.calculate_score(self.player_deck)
            self.opponent_score = self.calculate_score(self.opponent_deck)
            if (self.player_first):
                #call player game
                renpy.jump(self.game.on_player_start())
            else:
                #call opponent game
                renpy.jump(self.game.on_opponent_start())

        def hit(self):
            self.player_deck.append(self.full_deck[self.current_index])
            self.current_index = self.current_index+1
            self.player_score = self.calculate_score(self.player_deck)
            if (self.player_score > 21):
                self.end_game()

        def stay(self):
            if self.player_first:
                #call opponent game
                renpy.jump(self.game.on_opponent_second())
            else:
                self.end_game()

        def opponent_stay(self):
            if self.player_first:
                self.end_game()
            else:
                renpy.jump(self.game.on_player_second())

        def opponent_play(self):
            target = 19
            if self.player_first:
                target = self.player_score + 2
            if target > 21:
                target = 21
            self.opponent_score = self.calculate_score(self.opponent_deck)
            if (self.opponent_score <= target):
                #call opponent hit
                renpy.jump(self.game.on_opponent_hit())
            if (self.opponent_score <= 21):
                #call opponent stay
                renpy.jump(self.game.on_opponent_stay())
            self.end_game()

        def opponent_hit(self):
            self.opponent_deck.append(self.full_deck[self.current_index])
            self.current_index += 1
            self.opponent_score = self.calculate_score(self.opponent_deck)
            renpy.jump("bj_opponent_play")

        def end_game(self):
            if (self.opponent_score > 21):
                renpy.jump(self.game.on_opponent_bust())
            elif (self.player_score > 21):
                renpy.jump(self.game.on_player_bust())
            elif (self.opponent_score > self.player_score):
                #call opponent win
                renpy.jump(self.game.on_opponent_win())
            elif (self.player_score > self.opponent_score):
                #call player win
                renpy.jump(self.game.on_player_win())
            else:
                #call draw
                renpy.jump(self.game.on_draw())

screen bj_opponent_cards_shown:
    hbox:
        xpos 10
        ypos 50
        spacing 5
        for card in bj_delegate.opponent_deck:
            image "cards/"+card

    hbox:
        xpos 10
        ypos 150
        text "Score: [bj_delegate.opponent_score]" style "calendar_text"

screen bj_player_cards:
    hbox:
        xpos 10
        ypos 350
        spacing 5
        for card in bj_delegate.player_deck:
            image "cards/"+card
    hbox:
        xpos 10
        ypos 450
        text "Score: [bj_delegate.player_score]" style "calendar_text"

screen bj_buttons:
    vbox:
        xpos 10
        ypos 264
        spacing 0
        imagebutton:
            idle "gui/hit.png"
            action Jump("bj_player_hit")
        imagebutton:
            idle "gui/stay.png"
            action Jump("bj_player_stay")

label bj_start_round:
    if (bj_delegate.current_index > 40):
        player "let's shuffle the deck."
        $bj_delegate.shuffle()
    $bj_delegate.deal()
    if (bj_delegate.player_first):
        jump bj_player_play
    else:
        jump bj_opponent_play

label bj_player_play:
    show screen bj_buttons
    jump wait

label bj_opponent_play:
    $bj_delegate.opponent_play()
    jump wait

label bj_opponent_hit:
    $bj_delegate.opponent_hit()
    jump wait

label bj_opponent_stay:
    $bj_delegate.opponent_stay()
    jump wait

label bj_player_hit:
    $bj_delegate.hit()
    jump wait

label bj_player_stay:
    hide screen bj_buttons
    $bj_delegate.stay()
    jump wait
