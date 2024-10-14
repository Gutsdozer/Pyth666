class Bird:
    wings = True
    beak = True
    plumage = True

    def fly(self):
        print('Машу крыльями, лечу')

    def walk(self):
        pass



class Sparrow(Bird):
    size = 'small'

    def walk(self):
        print('Прыг скок')


class Duck(Bird):
    def walk(self):
        print('шагаю')


chizhik = Sparrow()
pyzhik = Sparrow()
pyzhik.size = 'medium'

print(chizhik.size)
print(pyzhik.size)
pyzhik.walk()
print(chizhik.wings)
print(chizhik.fly())

utka = Duck()