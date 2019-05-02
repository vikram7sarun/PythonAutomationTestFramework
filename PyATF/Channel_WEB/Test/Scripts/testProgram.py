class A:


    def __init__(self):
        print("I am Parent Class Constructor")

    def testM1(self):
        print("I am Parent Class M1")

    def testM2(self):
        print("I am Parent Class M2")

class B(A):
    def testM1(self):
        print("I am Child Class M1")


if __name__ == '__main__':
    ref = B()

    ref.testM1()
