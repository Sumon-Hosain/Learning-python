class Human():
    def __init__(self,f,l,a):
        self.frist_name=f
        self.last_name=l
        self.age=a
    def full_name(self):
        print(f'Full name: {self.frist_name} {self.last_name}')    #accessing Variable under class
    

H=Human('Sumon','Hosain',18)         
H.full_name()
