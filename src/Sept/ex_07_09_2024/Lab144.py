
class MathOperations:
    def div(self,a,b):
        return a/b

    @staticmethod
    def sum(a,b):
        return a+b

object_ref = MathOperations()
output = object_ref.div(10,5)
print(output)

print(MathOperations.sum(4,5))
# print(MathOperations.div(4,5))