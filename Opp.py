class Human():
    def __init__(self,n,a):
        self.Name=n
        self.Age=a

    def eat(self):
        print('Eating....')
    def walk(self):
        print('Walking...')

H=Human('Sumon',24)
print(H.Age)