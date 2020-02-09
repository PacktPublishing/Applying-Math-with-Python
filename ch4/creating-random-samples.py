
import random

data = [0.1, 0.2, 0.4, -0.1, 0.2, 0.3, -0.2, 0.1, 0.0, 0.3]


sample1 = random.sample(data, 5) # Randomly select 5 entries from data



def data_generator():
    while True:
        yield random.random()


from collections import deque

class SampleSelector:
    
    def __init__(self, iterable, probability=0.2, max_number=5):
        self.max_number = max_number
        self.actual_number = 0
        self.selected = 0
        self.iterator = iterable
        self.rng = random.Random()
        self.probability = probability

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_number and self.selected == self.max_number:
            raise StopIteration

        for item in self.iterator:
            self.actual_number += 1
            if self.rng.random() < self.probability:
                self.selected += 1
                return item


selector = SampleSelector(data_generator())

for d in selector:
    print(d)


print("selected", selector.max_number, "from", selector.actual_number) 




