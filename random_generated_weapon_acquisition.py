#by deviousname
import random

class Random_Weapon_Generator():
    def __init__(self):
        self.bundle_of_list()
        self.combine_metal_and_enchantment()
        (vowel_or_not := random.choice(self.new_old))
        statement = f"{random.choice(self.you_and_me)} {random.choice(self.acquired)} {(a_or_num := random.choice(self.a_or_number))}{'n' if vowel_or_not[0] in ['a', 'e', 'i', 'o', 'u'] and a_or_num in ['a'] else ''} {vowel_or_not} {random.choice(self.list3_mix)} {random.choice(self.infusions)} {random.choice(self.weapons)}{'s' if a_or_num != 'a' else ''}!"
        print(statement)
        
    def bundle_of_list(self):
        self.you_and_me = ["You", "I", "We", "They"]
        self.acquired = ["scored", "acquired", "reacquired", "forged", "created", "stole", "bought", "borrowed"]
        self.a_or_number = ["a", random.randint(2,5)]
    
        self.new_old = ["new", "worn", "old", "dirty", "dusty", "musty", "pristine", "priceless"]
        self.list1_metals = ["steel", "iron", "bronze", "copper", "silver", "gold", "platinum", "titanium", "tungsten", "uranium", "plutonium", "iridium", "osmium", "rhenium", "rhodium", "palladium", "ruthenium"]
        self.list2_enchantments = ["titanscored", "elemental", "magical", "enchanted", "legendary", "mythical", "ancient"]
        self.list3_mix = [] #blank list to combine list with
        self.infusions = ['plated', 'scaled', 'alloy', 'armored', 'edged', 'infused', 'fused','encrusted','gilded','replica','toy']
        self.weapons = ["sword", "axe", "hammer", "mace", "spear", "dagger", "knife"]

    def combine_metal_and_enchantment(self):
        for item in self.list1_metals:
            item_list = item.split()
            item_list[0] = random.choice(self.list2_enchantments)
            item = " ".join(item_list)
            self.list3_mix.append(item)

rng_weapon = Random_Weapon_Generator()

            


