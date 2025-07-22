# 아래에 코드를 작성하시오.


# 요구사항
# 3432번 문제에서 작성한 코드에서 이어서 작성한다.

# MovieTheater 클래스는 좌석을 예약하는 reserve_seat 메서드를 가진다.
# reserve_seat 메서드는 예약 가능한 좌석이 있는 경우, reserved_seats를 1 증가시키고 예약 성공 메시지를 반환한다.
# 예약 가능한 좌석이 없는 경우, 예약 실패 메시지를 반환한다.
# MovieTheater 클래스는 현재 예약 상태를 출력하는 current_status 메서드를 가진다.
# current_status 메서드는 총 좌석 수와 예약된 좌석 수를 출력한다.


class MovieTheater :
    def __init__(self,name,total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0

    def __str__(self):
        return f'{self.name}'
    
    def reserve_seat(self) :
        if self.reserved_seats < self.total_seats :
            self.reserved_seats += 1
            print("좌석 예약이 완료되었습니다.")
        else : 
            print("예약이 가능한 좌석이 없습니다.")

    def current_status(self) : 
        print(f"총 좌석 수: {self.total_seats}")
        print(f"예약된 좌석 수: {self.reserved_seats}")


mt1 = MovieTheater('메가박스',50)
mt2 = MovieTheater('CGV', 120)
mt1.reserve_seat()
mt1.reserve_seat()
mt1.reserve_seat()

mt1.current_status()
