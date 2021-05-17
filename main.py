import matplotlib.pyplot as plt
from tqdm import tqdm

from collections import defaultdict
import re

with open('respones.txt', 'r') as f:
    raw = [ln.strip('\n').lower() for ln in f.readlines()]

responses = filter(lambda i: i != '', raw)


category_trigger_pairs = (
        ('Sheep', ['sheep', 'sheeeeeeeep', 'ram', 'sheeo']),
        ('Goat', ['goat']),
        ('Bovine', ['bovine', 'bull', 'buffalo', 'bison', 'cow', 'cattle', 'oxen', 'ruminant', 'yak', 'ox', 'buffalos']),
        ('Pokemon', ['pokemon', 'pokã©mon']),
        ('Sea-life', ['fish', 'sea', 'whale', 'ray', 'manatee', 'aquatic', 'starfish', 'fidh', 'ocean']),
        ('Food', ['dessert', 'food', 'meat', 'pudding', 'pancake', 'dish', 'cheese', 'soup', 'pastry', 'muffin', 'bakery', 'soufflã©', 'baked']),
        ('Deer-like', ['deer', 'moose', 'elk', 'antelope', 'gazelle']),
        ('Mustelid', ['weasel', 'ferret', 'furret']),
        ('Feline', ['cat', 'feline', 'leopard', 'lion', 'bobcat', 'catlike']),
        ('Reptile', ['reptile', 'lizard']),
        ('Rodent', ['rodent', 'rat', 'mouse', 'nutria', 'capybara', 'beaver', 'mice', 'hamster', 'marmoset', 'gerbil', 'mousy', 'capibara', 'rodant']),
        ('Bird', ['bird', 'birb', 'duck', 'quail', 'swan', 'puffin', 'penguin', 'seabird']),
        ('Insect', ['insect', 'butterfly', 'fly', 'moth', 'bug']),
        ('Primate', ['monkey', 'primate', 'lemur', 'ape', 'monkeys']),
        ('Made up', ['made up', 'fictional', 'made-up', 'fantasy', 'nothing', 'starwars']),
        ('Dog', ['dog']),
        ('Rabbit', ['rabbit']),
        ('Pig-like', ['pig', 'hog', 'warthog']),
        ('Badger', ['badger', 'bager', 'badgery']),
        ('Hedgehog', ['hedgehog']),
        ('Squirrel', ['squirrel', 'squirrell']),
        ('Racoon', ['racoon', 'raccon', 'raccoon']),
        ('Bear', ['bear']),
        ('Otter', ['otter']),
        ('Anteater', ['anteater']),
        ('Marsupial', ['kangaroo', 'marsupial', 'koala', 'maruspial']),
        ('Land Mollusc', ['snail', 'slug']),
        ('Elephant-like', ['elephant']),
        ('Armadillo', ['armadillo']),
        ('Horse-like', ['zebra', 'horse']),
        ('Amphibian', ['toad', 'frog', 'amphibian'])
)

counts = defaultdict(int)
uncategorised = []
for i in responses:
    categorised = False
    for category, triggers in category_trigger_pairs:
        for trigger in triggers:
            if re.search(f'\\b{re.escape(trigger)}\\b', i):
                counts[category] += 1
                categorised = True
                break

    if not categorised:
        uncategorised.append(i)

for category, count in counts.items():
    print(f'{category}, {count}')
