class Cat:
    def shout(self):
        print("喵喵喵～")
class Dog:
    def shout(self):
        print("汪汪汪！")

def test(obj):
    obj.shout()

cat = Cat()
dog = Dog()
test(cat)
test(dog)

