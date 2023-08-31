def mul(a):
    def helper(b):
        return a * b
    return helper

if __name__ == '__main__':
    mul5 = mul(5)
    print(mul5(3))
    print(mul5(12))
