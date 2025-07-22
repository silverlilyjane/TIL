# 아래에 코드를 작성하시오.

# MovieTheater 클래스는 모든 영화관이 공통으로 가지는 total_movies변수를 가진다.
    # total_movies 변수를 MovieTheater 클래스에 클래스 변수로 추가한다.
    # MovieTheater 클래스는 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다
    # add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.
    # MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
# description 메서드는 아래 문장을 출력한다.
# '"이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다."
# "영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다."

class MovieTheater :
    total_movies = 0
    def __init__(self,name,total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def add_movie(cls) :
        cls.total_movies += 1
        print("영화가 성공적으로 추가되었습니다.")
    
    @staticmethod
    def description() :
        print("이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.")
        print("영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.")

    def reserve_seat(self) :
        if self.reserved_seats < self.total_seats :
            self.reserved_seats += 1
            print("좌석 예약이 완료되었습니다.")
        else : 
            print("예약이 가능한 좌석이 없습니다.")

    def current_status(self) : 
        print(f"총 좌석 수: {self.total_seats}")
        print(f"예약된 좌석 수: {self.reserved_seats}")


class VIPMovieTheater(MovieTheater) :
    def __init__(self,name,total_seats,vip_seats) :
        super().__init__(name,total_seats)
        self.vip_seats = vip_seats

    def reserve_vip_seat(self) :
        if self.vip_seats > 0 :
            self.vip_seats -= 1
            self.reserved_seats += 1
            print("VIP 좌석 예약이 완료되었습니다.")
        else : 
            print("예약 가능한 VIP 좌석이 없습니다.")

    def reserve_seat(self) :
        if self.vip_seats > 0 :
            self.reserve_vip_seat()
        else:
            super().reserve_seat()

mega1 = MovieTheater('메가박스',100)
mega1.reserve_seat()
mega1.reserve_seat()
cgv1 = MovieTheater('CGV',150)
cgv1.reserve_seat()
MovieTheater.add_movie()
MovieTheater.add_movie()
mega1.current_status()
cgv1.current_status()
print(f"총 영화 수: {MovieTheater.total_movies}")
MovieTheater.description()