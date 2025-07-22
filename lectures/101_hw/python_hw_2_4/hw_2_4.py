# 아래에 코드를 작성하시오.

# Animal 클래스를 정의한다.
    # Animal 클래스는 이름을 인자로 받는 생성자 메서드를 가진다.
    # Animal 클래스는 speak 메서드를 가진다. 이 메서드는 자식 클래스에서 오버라이딩된다.
# Dog와 Cat 클래스를 정의하고, Animal 클래스를 상속받는다.
    # Dog 클래스는 speak 메서드를 오버라이딩하여 "Woof!"를 반환한다.
    # Cat 클래스는 speak 메서드를 오버라이딩하여 "Meow!"를 반환한다.
# Flyer와 Swimmer 클래스를 정의한다.
    # Flyer 클래스는 fly 메서드를 가진다. 이 메서드는 "Flying"을 반환한다.
    # Swimmer 클래스는 swim 메서드를 가진다. 이 메서드는 "Swimming"을 반환한다.
# Duck 클래스를 정의하고, Flyer와 Swimmer 클래스를 다중 상속받는다.
    # Duck 클래스는 Animal 클래스를 상속받고, 이름을 인자로 받는 생성자 메서드를 가진다.
    # Duck 클래스는 speak 메서드를 오버라이딩하여 "Quack!"을 반환한다.
# make_animal_speak 함수를 정의한다.
    # 이 함수는 Animal 타입의 객체를 인자로 받아, 해당 객체의 speak 메서드를 호출하고 결과를 출력한다.
# 코드를 실행하고, 출력 결과를 확인한다.

# 오버라이딩 : 상속받은 메서드의 내용만 변경하는 것

class Animal :
    def __init__(self,name) : 
        self.name = name

    def speak(self) :
        '''
        여기다 설명을 넣으면 함수의 설명이 되네..?
         '''
        # 아무 기능도 하지 않을 speak 메서드를 왜 Animal 클래스에 정의 한걸까?
        # 나중에 만들 Dog, Cat 클래스가 Animal 클래스를 상속 받아서 각각 speak 메서드를 따라ㅗ 가지게 될 건데, 왜 굳이 Animal 클래스에 정의할까?
        # Animal class를 상속받을 자식 클래스들이 모두 speak 메서드를 각자의 역할로써 정의하고 있다.
        # 즉, 하위의 클래스들이 모두 공통적으로 speak 메서드를 가지고 있을 것이다라는 사실을 명시
        # 특별한 동작이 정의되어 있지 않다.
        pass


class Dog(Animal) :
    # 본인이 사용할 모양으로 오버라이딩 해서 사용하고 있다.
    def speak(self) :
        return "Woof!"


class Cat(Animal) : 
    def speak(self):
        return "Meow!"

    
class Flyer :
    def fly(self) :
        return "Flying"
    
class Swimmer :
    def swim(self):
        return "Swimming"
    
class Duck(Flyer,Swimmer,Animal) :
    def speak(self) : 
        return "Quack!"
    
# make_animal_speak 함수를 정의한다.
    # 이 함수는 Animal 타입의 객체를 인자로 받아, 해당 객체의 speak 메서드를 호출하고 결과를 출력한다.
# 코드를 실행하고, 출력 결과를 확인한다.

def make_animal_speak(instance) :
    print(instance.speak())

dog1 = Dog('치와와')
cat1 = Cat('페르시안 블루')
duck1 = Duck('거위')
flyer1 = Flyer()
swimmer1 = Swimmer()

make_animal_speak(dog1)
make_animal_speak(cat1)
make_animal_speak(duck1)
print(flyer1.fly())
print(swimmer1.swim())



