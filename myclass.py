class car:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def add_num(self):
        return self.a + self.b

    def sub_num(self):
        return self.a - self.b


def print_Hello():
    print("First number 1000")


if __name__ == "__main__":
    print(car.sub_num())
    print("Hello Class")
