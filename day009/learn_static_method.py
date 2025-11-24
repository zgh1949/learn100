class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 静态方法
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

def main():
    a, b, c = 3, 4, 5
    print(Triangle.is_valid(a, b, c))


if __name__ == "__main__":
    main()
