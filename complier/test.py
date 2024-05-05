from complier.util import Util
class a:
    b=1
if __name__ == "__main__":
    a.b =2
    c = a()
    c.b += 1
    print(c.b)
    print(a.b)
