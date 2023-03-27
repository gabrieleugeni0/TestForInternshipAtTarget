def fibonacci(n):
    x0 = 0
    x1 = 1
    soma = 0
    seq = [0, 1]

    while soma < n:
        soma = x0 + x1
        seq.append(soma)
        x0 = x1
        x1 = soma
    
    return seq

if __name__ == '__main__':
    n = int(input('Digite um numero inteiro: '))
    sequencia = fibonacci(n)

    print(f'Sequencia de Fibonacci: {sequencia}')
    if n in sequencia:
        print(f'O valor {n} digitado pertence a sequencia de Fibonacci, sendo o {(sequencia.index(n)) + 1}o. termo.')
    else:
        print(f'O valor {n} digitado NAO pertence a sequencia de Fibonacci')
        