class Deck:
    def __init__(self):
        self.deck_list = list()
        self.max_count = 60

    def get_count(self):
        return len(self.deck_list)

    def is_full(self):
        return len(self.deck_list) == self.max_count

    def can_add_card(self, card):
        return len(list(filter(lambda x: x == card, self.deck_list))) != 3
