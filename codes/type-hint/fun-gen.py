
## PARA LAS FUNCIONES GEN, DEBEN IMPLEMENTARSE ITER Y NEXT

class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.n > self.max):
            raise StopIteration
        resultado = 2 ** self.n
        self.n += 1
        return resultado

def PowTwoGen(max=0):
    n = 0
    while n<max:
        yield 2**n
        n+=1


def todos_pares():
    n = 0
    while True:
        yield n
        n += 2



        ####

        
print("usando iterators: ")
powtwo1 = PowTwo(5)
powtwo1_iter = iter(powtwo1)

while True:
    try:
        print(next(powtwo1_iter))
    except StopIteration:
        print("concluyó el iterador powtwo1_iter")
        break

def powTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

print("usando generadores: ")
for value in powTwoGen(5):
    print(value)


