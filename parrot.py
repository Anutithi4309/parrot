class Parrot:
    species="bird"
    def __init__(self, name, age):
        self.name=name
        self.age=age
blu=Parrot("blu",10)
Woo=Parrot("Woo",15)
print("blu is a {}".format(blu.species))
print("Woo is a {}".format(Woo.species))
print("{}is {}years old".format(blu.name,blu.age))



print("{}is {}years old".format(Woo.name,Woo.age))


