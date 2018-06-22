class ExtraDeck:
    def __init__(self):
        self.extra_list = list()
        self.max_count = 15

    def get_count(self):
        return len(self.extra_list)

    def is_full(self):
        return len(self.extra_list) == self.max_count

    def can_add_card(self, card):
        return len(list(filter(lambda x: x == card, self.extra_list))) != 3
