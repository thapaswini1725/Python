class A:
    def display_A(self):
        print("iam from class A")
class B(A):
    def display_B(self):
        print("iam from class B")
class C(B):
    def display_C(self):
        print("iam from class C")
s=C()
s.display_A()
s.display_B()
s.display_C()
        
