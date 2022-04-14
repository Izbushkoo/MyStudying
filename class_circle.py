import math


class Circle:

    circles_list = []
    count = 0

    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius
        self.circles_list.append(self)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def increasing(self):

        new_radius = math.sqrt(self.area() * 2 / math.pi)
        self.radius = new_radius

    def is_crossed_with_any_out_of_all(self):

        self.count = 0
        self_list = self.circles_list.copy()
        self_list.remove(self)
        dist_between_points_list = [self.check_cross(item)
                                    for item in self_list
                                    ]

        if all(dist_between_points_list):
            print("Cross every circle")
        elif not all(dist_between_points_list):
            print("Crosses at least one circle")
        elif self.count == 0:
            print("Don't cross any circle.")

    def is_crossed_with_one(self, other_circle):

        if self.check_cross(other_circle):
            print("Circle: X = {}, Y = {}, Radius = {} crosses "
                  "Circle: X = {}, Y = {}, Radius = {}"
                  .format(self.x, self.y, self.radius,
                          other_circle.x, other_circle.y,
                          other_circle.radius)
                  )
        else:
            print("Circle: X = {}, Y = {}, Radius = {} don't crosses "
                  "Circle: X = {}, Y = {}, Radius = {}"
                  .format(self.x, self.y, self.radius,
                          other_circle.x, other_circle.y,
                          other_circle.radius)
                  )

    def check_cross(self, other_circle):


        dist_between_two_point = math.sqrt(((self.x - other_circle.x) ** 2
                                            + (self.y - other_circle.y) ** 2)
                                           )
        if dist_between_two_point <= self.radius + other_circle.radius:
            self.count += 1
            return True
        return False

