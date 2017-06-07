from decimal import Decimal

# set expression and unpacking
quarter, dime, nickel, penny = (Decimal(x) for x in ('0.25', '0.10', '0.05', '0.01'))
coinage = set([quarter, dime, nickel, penny])

def change(amount, coinage=coinage):
    returned_amount = Decimal('0')
    for coin in reversed(sorted(coinage)):
        while returned_amount + coin <= amount:
            yield coin
            returned_amount += coin

assert list(change(Decimal('0.75'))) == [quarter, quarter, quarter]
assert list(change(Decimal('0.35'))) == [quarter, dime]
assert list(change(Decimal('0.43'))) == [quarter, dime, nickel, penny, penny, penny]

from itertools import repeat, chain, takewhile
greedy = lambda items, predicate: chain.from_iterable(takewhile(predicate, repeat(x)) for x in reversed(sorted(items)))

def pred(amount, state=None):
    state = state or []
    def takecoin(item):
        if sum(state) + item <= amount:
            state.append(item)
            return True
        return False
    return takecoin

assert list(greedy(coinage, pred(Decimal('0.75')))) == [quarter, quarter, quarter]
assert list(greedy(coinage, pred(Decimal('0.35')))) == [quarter, dime]
assert list(greedy(coinage, pred(Decimal('0.43')))) == [quarter, dime, nickel, penny, penny, penny]

def primed(gen):
    def decorator(*args, **kwargs):
        instance = gen(*args, **kwargs)
        next(instance) # prime the generator
        return instance
    return decorator

@primed
def accept(amount, state=0):
    item = yield None
    while True:
        if state+item <= amount:
            state += item
            item = yield True
        else:
            item = yield False

assert list(greedy(coinage, accept(Decimal('0.75')).send)) == [quarter, quarter, quarter]
assert list(greedy(coinage, accept(Decimal('0.35')).send)) == [quarter, dime]
assert list(greedy(coinage, accept(Decimal('0.43')).send)) == [quarter, dime, nickel, penny, penny, penny]

mapping = {  1:  'i',   4: 'iv',    5:  'v',   9: 'ix',  10: 'x',
            40: 'ix',  50:  'x',   90: 'xc', 100:  'c', 400: 'cd',
           500:  'd', 900: 'cm', 1000:  'm',}
class numerals(list):
        def __format__(self, fmt):
                    return ''.join(mapping[x].upper() for x in self)

denominations = {1,5,10,25,100,500,1000,2000}
class purse(list):
    def __format__(self, fmt):
        return ' + '.join('{:d}x{}'.format(
                       sum(1 for _ in cs),
                       ('{:d}c' if c < 100 else '{:.0f}$').format(c if c < 100 else c/100))
                       for c,cs in groupby(self))

if __name__ == '__main__':
    from itertools import groupby
    from random import randint

    for _ in xrange(4):
        arabic = randint(1900,2200)
        roman = greedy(mapping,pred(arabic))
        print 'The year {} is written {}'.format(arabic, numerals(roman))

    for _ in xrange(4):
        amount = randint(0,1000)
        coins = greedy(denominations,pred(amount))
        print 'Your change for {:.2f}$ = {}'.format(amount/100, purse(coins))
