import logging
logging.basicConfig(filename='ketww.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s %(message)s')

def add(x, y):
    return x + y


def multi(x, y):
    return x * y


def sub(x, y):
    return x - y


num1 = 9
num2 = 2

add_result = add(num1, num2)
logging.info("asdassdassd")
print(fr"addition of {num1} and {num2}  is {add_result}")

multi_result = multi(num1, num2)
print(fr"multiplication of {num1} and {num2}  is {multi_result}")

sub_result = sub(num1, num2)
print(fr"subscription of {num1} and {num2}  is {sub_result}")