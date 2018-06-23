from YGOPricesAPI import YGOPricesAPI


class Card(object):
    def __init__(self, name):
        data = YGOPricesAPI().get_data(name).get("data")
        self.name = name
        self.text = data.get("text")
        self.card_type = data.get("card_type")
        self.type = data.get("type")
        self.attribute = data.get("family")
        self.level = data.get("level")

    def get_name(self):
        return self.name

    def get_text(self):
        return self.text

    def get_card_type(self):
        return self.card_type

    def get_type(self):
        return self.type

    def get_attribute(self):
        return self.attribute

    def get_level(self):
        return self.level

    def is_extra_deck(self):
        return (self.type is not None
                and ("Link" in self.type or "Xyz" in self.type or "Synchro" in self.type or "Fusion" in self.type))
