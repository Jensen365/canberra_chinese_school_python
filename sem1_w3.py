import random
heath_points=[60,80,100]
heroes=["knight","wizard","archor"]
hero=random.choice(heroes)
point=random.choice(heath_points)
damage=random.randiant(10,30)
hp_Left=point-damage
print(hero)
print(point)