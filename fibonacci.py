def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence


num_terms = 10 
fib_sequence = fibonacci(num_terms)
print(fib_sequence)
