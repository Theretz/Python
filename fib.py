#Top Recurso 

#Tempo: 0(2^0)
#Espaço: 0(n)
class solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

#Top Memorização

#Tempo: 0(n)
#s