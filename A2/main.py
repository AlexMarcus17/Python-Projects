from domain.wine import Wine
from repository.winerepo import WineRepo

w1 = Wine("Splash", "Rose", "Argentina", 110.0, "11.11.2011", "11.11.2029")
w2 = Wine("Morgon", "White", "France", 90.0, "12.02.2009", "11.11.2029")
w3 = Wine("Pinto", "White", "Italy", 150.0, "11.08.1997", "11.11.2029")
w4 = Wine("Pinto", "White", "Italy", 150.0, "11.08.2025", "11.11.2029")
repo = WineRepo()
repo.addwine(w1)
repo.addwine(w2)
repo.addwine(w3)
repo.addwine(w4)

for i in repo.getall():
    print(i.getname())

print(repo.getavgprice())

repo.addwine(w1)
repo.sort()
for i in repo.getall():
    print(i.getname())


