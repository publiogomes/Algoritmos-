#Primeira versão usando o laço For
def triangular(n):
    for i in range(3,n+1):
        if (i-2)*(i-1)*(i)==n:
                return True
        return False
    '''
    #Segunda versão usando o laço While
    def triangular_(n):
        i = 3
        while i<=n:
            if (i-2)*(i-1)*(i)==n:
                return True
            i=i+1
            return False
            '''

