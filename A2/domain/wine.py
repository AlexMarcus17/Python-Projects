

class Wine:
    def __init__(self, name, type, country, price, prod, exp):
        self.__name = name
        self.__type = type
        self.__country = country
        self.__price = price
        self.__prod = prod
        self.__exp = exp
    def getprice(self):
        return self.__price
    def getcountry(self):
        return self.__country
    def getname(self):
        return self.__name
    def gettype(self):
        return self.__type
    def getprod(self):
        return self.__prod
