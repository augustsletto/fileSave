import random

class ChristmasGift:
    def __init__(self, _secret_gift, _price, gift_to, gift_from, christmas_rhyme):
        self._secret_gift = _secret_gift
        self._price = _price
        self.gift_to = gift_to
        self.gift_from = gift_from
        self.christmas_rhyme = christmas_rhyme
    
    def get_secret_gift(self):
        return self._secret_gift
    
    def get_price(self):
        return self._price
    
    
    
gift_1 = ChristmasGift("Kaffekopp", 20, "Emma", "August", "God jul här får du en kaffekopp")
gift_2 = ChristmasGift("Leksak", 300, "August", "Emma", "God jul här får du en Leksak")
gift_3 = ChristmasGift("Telefon", 8000, "Emma", "August", "God jul här får du en Telefon")
gift_4 = ChristmasGift("Smycke", 10000, "August", "Emma", "God jul här får du en Smycke")
gift_5 = ChristmasGift("Dator", 20000, "Emma", "August", "God jul här får du en Dator")


gift_bag = [gift_1, gift_2, gift_3, gift_4, gift_5]



user_input = input("Hey, who wants to look in to santas christmas sack?")

if user_input.lower() in ["santa claus", "mrs.claus"]:
    gift_chosen = random.choice(gift_bag)
    print(f"Till {gift_chosen.gift_to} från {gift_chosen.gift_from}: {gift_chosen.christmas_rhyme}")
    
else:
    gift_chosen = random.choice(gift_bag)
    print(f"Till {gift_chosen.gift_to} från {gift_chosen.gift_from} ges en gåva {gift_chosen.get_secret_gift()} till ett pris av {gift_chosen.get_price()}")
    