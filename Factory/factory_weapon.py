from time import sleep

# run first

class Weapon:
    def __init__(self, type, damage, distance, max_capacity:int):
        self.type = type
        self.damage = damage
        self.distance = distance
        self.max_capacity = max_capacity
        self.capacity = max_capacity

    def shoot(self):
        if self.capacity > 0:
            self.capacity -= 1
            # do damage code
            # calculate distance/hit code
            print(f"{self.type} shot one shot. ({self.capacity} shots left)")
        else:
            print(f"CLICK ({self.type} is empty.)")
    
    def reload(self):
        if self.capacity < self.max_capacity:
            self.capacity = self.max_capacity
            print(f"{self.type} was reloaded. ({self.capacity} shots)")
        else:
            print(f"{self.type} is already fully loaded!")
    
    def give_info(self):
        print(f"{self.type} has {self.damage} damage, {self.distance} distance and {self.max_capacity} capacity (currently {self.capacity})")

def weapon_factory(weapon_type):
    if weapon_type.lower() == "pistol":
        return Weapon("Pistol", 10, 50, 7)
    elif weapon_type.lower() == "shotgun":
        return Weapon("Shotgun", 100, 20, 5+1)
    elif weapon_type.lower() == "rifle":
        return Weapon("Rifle", 50, 100, 30)
    else:
        raise ValueError(f"Invalid weapon type: {weapon_type}")

#-------------

pistol = weapon_factory("pistol")
shotty = weapon_factory("shotgun")
kalash = weapon_factory("rifle")

while pistol.capacity > 0:
    pistol.shoot()
    sleep(0.5)
pistol.shoot()
sleep(1)
pistol.reload()
sleep(1)
pistol.give_info()
input("ENTER TO CONTINUE")

villain1 = weapon_factory("rifle")
villain2 = weapon_factory("shotgun")
while villain1.capacity > 0:
    sleep(0.1)
    villain1.shoot()
villain1.shoot()
sleep(1)
villain1.reload()
sleep(1)
villain1.give_info()


