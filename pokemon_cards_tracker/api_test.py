
from pokemontcgsdk import Card
from pokemontcgsdk import Set

# set = Set.find('base1')
# print(set.name)

sets = Set.all()
# for set in sets:
#     print(f"{set.name} ({set.id})")

card = Card.find('sv10-1')
print(f"{card.name} ({card.id})")
