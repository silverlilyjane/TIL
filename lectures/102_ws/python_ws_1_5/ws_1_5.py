# 아래에 코드를 작성하시오.


# movies리스트를 순회하며 영화 제목과 평점을 가진 딕셔너리 객체로 만들고 새로운 리스트에 담는다.
# get_high_rated_movies 함수를 정의하여, threshold 매개변수를 받아서 평점이 threshold 이상인 영화를 리스트로 반환한다.
# 사용자로부터 평점 기준을 입력받아, get_high_rated_movies 함수를 호출하여 해당 평점 이상인 영화를 출력한다.


def get_high_rated_movies(threshold) :
    high_list = []
    for movie in movies_rating :
        if movie['rating'] >= threshold :
            high_list.append(movie['title'])

    return high_list


movies = ['Inception', 'Interstellar', 'Dunkirk', 'Tenet']
ratings = [9, 8.5, 7.5, 6]

movies_rating = []

for i in range(len(movies)) :
    movies_rating.append({'title': movies[i], 'rating': ratings[i]})

print(movies_rating)

threshold = input("Enter the rating thresold: ")
threshold = int(threshold)
print(f"Movies with a rating of {float(threshold)} or higher:")
print("\n".join(get_high_rated_movies(threshold)))
## 수정완