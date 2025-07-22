# 아래에 코드를 작성하시오.

# 3x3 크기의 2차원 리스트를 생성하여 초기 좌석 배치를 표현하시오. 좌석은 'O'로 표시합니다.
# (0,2), (1,0), (1,2), (2,0), (2,2) 좌석을 예매 처리하시오. 예매된 좌석은 'X'로 표시합니다.
# 예매된 좌석을 포함하여 현재 좌석 배치를 출력하시오.


seats = []
for i in range(3) :
    seat = []
    for j in range(3) :
        seat.append('O')
    seats.append(seat)

#print(seats)

seats[0][2] = 'X'
seats[1][0] = 'X'
seats[1][2] = 'X'
seats[2][0] = 'X'
seats[2][2] = 'X'

print("현재 좌석 배치: ")
for seat in seats : 
    print(" ".join(seat))
