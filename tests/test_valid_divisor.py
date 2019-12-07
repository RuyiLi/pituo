from pituo.pituo import pituo


@pituo
def divide(a, b):
    return a / b


# err is None
quotient, err = divide(5, 1)

if err is not None:
    print(err)
else:
    print(quotient)
