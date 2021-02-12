#! /usr/bin/python3
#Monte Carlo Analysis of Dragons Cards game in Hilda App
import random

dragons = list(["fire", "forest", "water", "stone", "metal"])

winner = [0, 1, -1, 1, -1]



def attack(player, ki):
    result = winner[(dragons.index(ki)-dragons.index(player)) % 5]
    return result


class Player(object):
    def __init__(self):
        self.lifes = 3
        self.draw_cards()

    def draw_cards(self):
        print("Draw cards")
        self.dragons = random.sample(dragons, 3)
        self.other = list()
        for dragon in dragons:
            if dragon not in self.dragons:
                self.other.append(dragon)

    def play_card(self, card):
        self.played_card = card
        self.dragons.remove(card)
        

    def draw_card(self):
        new_card = random.choice(self.other)
        self.dragons.append(new_card)
        self.other.remove(new_card)
        self.other.append(self.played_card)

    def __str__(self):
        return "cards: {}, lifes: {}".format(self.dragons, self.lifes)


class Ki(Player):
    def __init__(self):
        super().__init__()

    def play(self):
        print(self.dragons)
        card = random.choice(self.dragons)
        self.play_card(card)
        return card


class User(Player):

    def __init__(self):
        super().__init__()

    def play(self):
        print(self.dragons)
        card = random.choice(self.dragons)
        self.play_card(card)
        return card


class Game(object):

    def __init__(self):
        self.user = User()
        self.ki = Ki()

    def __str__(self):
        return "user: {}, ki: {}".format(self.user, self.ki)

    def user_win(self):
        self.ki.lifes -= 1
        self.user.draw_card()
        self.ki.draw_card()

    def ki_win(self):
        self.user.lifes -= 1
        self.user.draw_card()
        self.ki.draw_card()

    def dragon_panic(self):
        print("Dragon Panic!!!")
        for i in range(2):
            user_card = self.user.play()
            ki_card = self.ki.play()

            fun = {1: self.user_win,
                   -1: self.ki_win,
                   0: self.dragon_panic_draw}

            move = attack(user_card, ki_card)
            fun[move]()

            if self.user.lifes == 0 or self.ki.lifes == 0:
                return

        self.user.draw_cards()
        self.ki.draw_cards()

    def dragon_panic_draw(self):
        return

    def run(self):
        while self.user.lifes > 0 and self.ki.lifes > 0:
            print(self)
            user_card = self.user.play()
            ki_card = self.ki.play()

            fun = {1: self.user_win,
                   -1: self.ki_win,
                   0: self.dragon_panic}

            move = attack(user_card, ki_card)
            fun[move]()
        print(self)
        if self.ki.lifes > 0:
            global wins 
            wins += 1
        global games
        games += 1


wins, games = 0, 0
for i in range(10000):
    game = Game()
    game.run()
print("{}/{}".format(wins,games))