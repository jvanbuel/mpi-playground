from mpi4py import MPI
from typing import Callable
import inspect

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


def integrate(f: Callable[[float], float], a: float, b: float, stepsize: float):
    steps = round((b - a) / stepsize)

    integral = 0
    for i in range(steps):
        integral += stepsize * (f(a + i * stepsize) + f(a + (i + 1) * stepsize)) / 2

    return integral


def main():

    f = lambda x: x**2
    a = 0
    b = 10
    stepsize = 0.0000001

    span = (b - a)/size
    left = a + rank * span
    right = a + (rank + 1) * span

    result = integrate(f=f, a=left, b=right, stepsize=stepsize)
    result = comm.reduce(result, op=MPI.SUM, root=0)
    if rank == 0:
        print(
            f"The integral of {inspect.getsource(f)} between {a} and {b} with stepsize {stepsize} is: {result}"
        )

    quit()


if __name__ == "__main__":
    main()
