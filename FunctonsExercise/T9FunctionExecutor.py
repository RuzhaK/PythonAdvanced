def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2




def func_executor(*args):
    results=[]
    for func_definition in args:
        func, func_args=func_definition
        return_value=func(*func_args)
        results.append(return_value)
    return results

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
