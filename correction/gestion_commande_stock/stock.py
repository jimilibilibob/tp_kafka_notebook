class Stock:
    def __init__(self):
        self.stock = {
            "commestible":{
                "pain au chocolat" : 20,
                "croissant" : 20,
                "crêpe" : 20,
                "baguette" : 20,
                "baguette tradition" : 20,
                "brioche" : 20,
                "pain au raisin" : 20,
                "Chausson aux pommes" : 20
            },
            "boisson":{
                "lait" : 20,
                "café" : 20,
                "eau" : 20,
                "jus de pomme" : 20,
                "jus d'orange" : 20
            }
        }
    
    def get_stock(self):
        return self.stock
    
    def change_stock(self, add, article, qte):
        if article in self.stock["commestible"].keys():
            if add:
                self.stock["commestible"][article] += qte
            else: 
                self.stock["commestible"][article] -= qte
        if article in self.stock["boisson"].keys():
            if add:
                self.stock["boisson"][article] += qte
            else: 
                self.stock["boisson"][article] -= qte