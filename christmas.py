class ChristmasGift:
    def __init__(self, _secret_gift, _price_gift, gift_to, gift_from, christmas_rhyme):
        self._secret_gift = _secret_gift
        self.price_gift = _price_gift
        self.gift_to = gift_to
        self.gift_from = gift_from
        self.christmas_rhyme = christmas_rhyme
        
        
    def get_secret_gift(self):
        return self._secret_gift
    
    def get_price(self):
        return self.price_gift
    
    
    
gift_1 = ChristmasGift("Kaffe", "299kr", "Emma", "August", "När morgonen är mörk och kall, är detta varmt och passar bra till alla fall.")
gift_2 = ChristmasGift("Boll", "99kr", "Mamma", "Pappa", "Med fart och studs, och kanske en spark, är detta roligt på en park.")
gift_3 = ChristmasGift("Dator", "12 299kr", "Sixten", "Pappa", "För spel, jobb, eller surf så lätt, denna gör allt på ett effektivt sätt.")
gift_4 = ChristmasGift("GTA6", "899kr", "August", "Emma", "Ett äventyr på skärm där spänning blir stor, ta dig an staden och låt fantasin få ord")
gift_5 = ChristmasGift("Smycke", "1299kr", "Emma", "August", "Något glittrigt att bära nära, vackert och fint, som bara du kan bära")



gifts_basket = [gift_1, gift_2, gift_3, gift_4, gift_5]



user_input = input("Hey, who wants to look into santas christmas sack?")


for gift in gifts_basket:
    if user_input.lower() in ["santa claus", "mrs.claus"]:
        print(f"Till {gift.gift_to} från {gift.gift_from} ges en gåva {gift._secret_gift} till ett pris av {gift.get_price()}:-")
    else:
        print(f"Från {gift.gift_from} till {gift.gift_to}: {gift.christmas_rhyme}")