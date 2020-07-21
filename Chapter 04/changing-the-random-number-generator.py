
from numpy import random


seed_seq = random.SeedSequence()

print(seed_seq.entropy)
# 9219863422733683567749127389169034574


bit_gen = random.MT19937(seed_seq)

rng = random.Generator(bit_gen)




