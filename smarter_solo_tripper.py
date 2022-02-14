from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def fibonacci(n: int, previous_fibs: dict):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1 or n == 2:
        return 1
    if str(n) in previous_fibs:
        return previous_fibs[str(n)]
    return fibonacci(n=n - 1, previous_fibs=previous_fibs) + fibonacci(n=n - 2, previous_fibs=previous_fibs)


def main():

    print("Hello world from rank", str(rank), "of", str(size))

    numbers = np.zeros(50)
    count = len(numbers)
    previous_fibs = {}

    for i in range(count):
        if rank == 0:
            print(f"Rank {rank} calculating {i+1}th Fibonacci number")
            numbers[i] = fibonacci(n=i + 1, previous_fibs=previous_fibs)
            previous_fibs[str(i)] = numbers[i]
    
    if rank == 0:
        print(f"The {count} first Fibonacci numbers are \n {numbers}")

if __name__ == "__main__":
    main()
