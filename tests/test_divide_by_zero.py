from pituo.pituo import pituo


@pituo
def divide(a, b):
    return a / b


# err is not one
quotient, err = divide(5, 0)

if err is not None:
    print(err)
else:
    print(quotient)
