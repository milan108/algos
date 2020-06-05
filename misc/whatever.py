import math
def main():
    assert(divide(32, 2) == 32 // 2)
    assert(divide(180 , 9) == 180 // 9)
    assert(divide(365, 5) == 365 // 5)
    assert(divide(21, 3) == 21 // 3)
    print(divide(360000000, 12))
    #print(divide_alt(360000000, 12))

def divide(dividend, divisor, quotient = 0):
    if dividend > 0:
        factors = [1,2,3,5,10,100,1000]
        factor = 1
        for i in factors:
            if multiply(divisor,i) <= dividend:
                factor = i
        accumulator = multiply(divisor, factor)
        i,j = 0,0
        while i < dividend:
            j += 1
            i += accumulator
        if i > dividend:
            j -= 1
            i -= accumulator
        quotient += multiply(factor, j)
        quotient = divide(dividend - i, divisor, quotient)
    return quotient

# from algorist wiki
def divide_alt(num, den):
	quotient = 0
	quot_accumulator = 1
	den_accumulator = den

	while num >= den:
		if num < den_accumulator:
			den_accumulator = den
			quot_accumulator = 1

		num = num - den_accumulator
		quotient = quotient + quot_accumulator
		quot_accumulator = quot_accumulator + quot_accumulator
		den_accumulator = den_accumulator + den_accumulator
	
	return quotient
def multiply(x,  y):
    product = 0
    for _ in range(0, y):
        product += x
    return product

if __name__ == '__main__':
    main()