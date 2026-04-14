class A:
    def show(self):
        print("Iam from parent class")
class B(A):
    def show(self):
        print("Iam from child class")
s=B()
s.show()
        
