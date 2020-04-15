def Add(x,y):
    return x + y
def Sub(x,y):
    return x - y
def Mul(x,y):
    return x * y
def Div(x,y):
    return x / y

class calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def Add(self):
        return self.x + self.y

    def Sub(self):
        return self.x - self.y

    def Mul(self):
        return self.x * self.y

    def Div(self):
        return self.x / self.y