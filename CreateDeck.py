from YGOPricesAPI import YGOPricesAPI
import Levenshtein as lvst

api = YGOPricesAPI()

card_list = api.get_names()

# card = input("Enter Card Name: ")
