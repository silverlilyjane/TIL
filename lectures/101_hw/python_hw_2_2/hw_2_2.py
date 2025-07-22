# 아래에 코드를 작성하시오.
# Product 클래스를 정의한다.
# Product의 인스턴스 수를 기록할 수 있는 클래스 변수 product_count를 정의하고, 0을 할당한다.
# 생성자 메서드를 정의한다.
# 생성자 메서드는 상품의 이름(name)과 가격(price)을 인자로 받는다.
# 각 인스턴스는 고유한 이름과 가격을 담을 수 있는 name과 price 변수를 가지고, 인자로 넘겨받은 값을 할당받는다.
# 인스턴스가 생성될 때마다 product_count가 1 증가해야 한다.
# 상품의 정보를 출력하는 display_info 인스턴스 메서드를 정의한다.
# 2개 이상의 인스턴스를 생성하고, 각 인스턴스의 정보를 출력한다.
# Product 클래스의 product_count를 출력한다.

class Product :
    product_count = 0 # 클래스 변수는 이 클래스로 만들어질 모든 인스턴스들이 공통으로 가지는 속성이다.


    # 인스턴스 메서드는 인스턴스가 쓸 것이다.
    # 그럼, 당연히 인스턴스에 대한 정보도 알고 있어야 할 것이다.
    # self라는 인자를 약속처럼 쓴다. -> 항상 첫번재 매개변수는 self
    # self가 없다면 파이썬은 어느 객체에 대해 작업하는지를 잘 모름
    def __init__(self,name,price) : # 인스턴스 메서드 만드는 방법과 동일하게 진행
        self.name = name
        self.price = price

        # product_count는 클래스 변수이다.
        # 따라서, 인스턴스가 직접적으로 클래스 변수를 변화시키지 않는다.
        #  그렇기 때문에 Product.product_count라고 쓴다.
        Product.product_count += 1

    def display_info(self) :
        return f"상품명: {self.name}, 상품가격: {self.price}"

# 인스턴스 생성과 할당 과정을 단계별로 나눠 보자면
# 1. 인스턴스 생성
# 2. 변수에 할당
product1 = Product('사과',1000)
print(product1.display_info())
# print(product1.display_info()) -> None 이 나온다. -> 함수가 끝나고 output이 return 이 없기 때문에 none이 나온다.
product2 = Product('바나나',1500)
print(product2.display_info())

print(f"총 상품 수: {Product.product_count}")