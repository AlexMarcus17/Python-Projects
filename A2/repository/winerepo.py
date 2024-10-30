from domain.wine import Wine
import unittest
class WineRepo:
    def __init__(self):
        self.__wines = []

    def getall(self):
        return self.__wines

    def addwine(self, wine):
        ok = True
        if wine.getname() == "":
            ok = False
        if not(wine.gettype() == "Red" or wine.gettype() == "Rose" or wine.gettype() == "White"):
            ok = False
        if wine.getprice()<0.0:
            ok = False
        dates = wine.getprod().split(".")
        if int(dates[2])>=2024:
            ok = False
        if ok:
            self.__wines.append(wine)
        else:
            print("Invalid data")

    def getavgprice(self):
        sum = 0
        c = 0

        for i in self.__wines:
            sum += i.getprice()
            c += 1
        if c == 0:
            sum = 0
        else:
            sum = sum/c
        return sum
    def sort(self):
        self.__wines = sorted(self.__wines, key= lambda wine: wine.getcountry())

