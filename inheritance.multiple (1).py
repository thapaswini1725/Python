class A:
    def display_A(self):
        print("Iam from class A")
class B(A):
    def display_B(self):
        print("Iam from class B")
s=B()
s.display_A()
s.display_B()
        
