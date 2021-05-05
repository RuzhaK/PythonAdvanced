import operator

def parse_expression(expr):
    n1,sign,n2=expr.split()
    op={
        '/':operator.truediv,
        '*':operator.mul,
        '+':operator.add,
        '-':operator.sub,
        '^':operator.pow,
    }[sign]
    return op,float(n1),float(n2)

def exec(op,n1,n2):
    return op(n1,n2)