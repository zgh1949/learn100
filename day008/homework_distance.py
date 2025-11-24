class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_x(self, x):
        self.x += x

    def move_y(self, y):
        self.y += y

    def move_by(self, x, y):
        self.x += x
        self.y += y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point: 'Point'): # 这里对自身的引用需要加引号
        return abs((self.x-point.x)**2+(self.y-point.y)**2)


if __name__ == "__main__":
    point_a = Point()
    point_a.move_x(1)
    point_a.move_y(1)

    point_b = Point(2, 2)
    point_b.move_by(3, 3)

    print(point_a.distance_to(point_b))
