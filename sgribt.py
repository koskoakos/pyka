import random


def fugtion():
    vocab = ['pyka', 'opuoha', 'me4', 'siriusa', 'pisun', 'zevsa']
    return '. '.join(' '.join(random.sample(vocab, random.randint(1, 6))) for _ in range(10))

