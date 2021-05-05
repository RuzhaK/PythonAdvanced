from functools import lru_cache
import logging

logging.basicConfig(
    filename='demo-logs.log',
    level=logging.DEBUG
)
@lru_cache()
def div_numbers(a,b):
    return a/b

def fibonacci(n):
    if n==0:
        logging.debug("Calculating fibonacci of 0")
        return 0
    if n==1:
        logging.debug("Calculating fibonacci of 1")
        return 1
    prev_fib=fibonacci(n-1)
    logging.debug(f"prev_fibonacci={prev_fib}")
    two_prev_fib = fibonacci(n - 2)
    logging.debug(f"prev_fibonacci={two_prev_fib}")
    return prev_fib+two_prev_fib
n=int(input())
fibonacci(n)

# towa si samosazdawa demo-logs i tam pishe kakwo prawi
# lru - cache zabarzwa izpalnenieto kato keshira weche napraweni izchislenia