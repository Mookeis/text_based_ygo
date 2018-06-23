from Deck import Deck
from ExtraDeck import ExtraDeck
from YGOPricesAPI import YGOPricesAPI

deck = Deck(list())
extra = ExtraDeck(list())
card_list = YGOPricesAPI().get_names()
