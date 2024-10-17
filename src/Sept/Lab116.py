a  = 10

class Pesrson:
    b = 11

    def print_infor(self):
        global a
        a = "Hello"
        print(self.b)

object_ref = Pesrson()
object_ref.print_infor()
print(a)