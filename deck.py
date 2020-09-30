from card import Card


class Deck:
    def __init__(self, screen):
        self.cards = []
        self.screen = screen
        for i in range(5):
            self.cards.append(Card([255, 0, 0], i, 30 * len(self.cards), 300, self.screen))
        for i in range(5):
            self.cards.append(Card([0, 255, 0], i, 30 * len(self.cards), 300, self.screen))
        for i in range(5):
            self.cards.append(Card([0, 0, 255], i, 30 * len(self.cards), 300, self.screen))

    def draw(self):
        for c in self.cards:
            c.draw()

    def get_pos(self, x, y):
        for c in self.cards:
            if c.get_x() <= x <= c.get_x() + 20 and c.get_y() <= y <= c.get_y() + 100:
                return c
