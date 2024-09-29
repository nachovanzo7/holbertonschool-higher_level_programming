
class CountedIterator:
    def __init__(self, lista):
        self.iterador = iter(lista)
        self.cont = 0

    def __next__(self):
        if self.iterador is not None:
            try:
                valor = next(self.iterador)
                self.cont += 1

                return valor

            except StopIteration:
                self.iterador = None
                raise
        else:
            raise StopIteration

    def get_count(self):
        return self.cont
