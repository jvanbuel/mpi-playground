from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
elements = np.zeros(size)


def fibonacci(n: int):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1 or n == 2:
        return 1
    return fibonacci(n=n - 1) + fibonacci(n=n - 2)


def main():

    print("Hello world from rank", str(rank), "of", str(size))

    numbers = np.zeros(40)
    count = len(numbers)

    for i in range(count):
        if rank == i % size:
            print(f"Rank {rank} calculating {i+1}th Fibonacci number")
            numbers[i] = fibonacci(n=i + 1)
            comm.bcast(numbers[i], root=rank)

        numbers[i] = comm.bcast(numbers[i], root=(i % size))

    if rank == 1:
        print(f"The {count} first Fibonacci numbers are \n {numbers}")



if __name__ == "__main__":
    main()
