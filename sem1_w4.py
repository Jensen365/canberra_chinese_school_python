import random
heath_points=[60,80,100]
heroes=["knight","wizard","archor"]
hero=random.choice(heroes)
point=random.choice(heath_points)
damage=random.randint(10,30)
hp_Left=point-damage
print(hero)
print(point)
Enemy="Enemy1"
Enemy_hp=100
damage_to_enemy=random.randint(15,40)
Enemy_hp_left=Enemy_hp-damage_to_enemy
if hp_Left>=Enemy_hp_left:
    print("hero wins")
else:
    print("Enemy wins")