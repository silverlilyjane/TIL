# 학생들의 이름과 점수를 딕셔너리에 저장하시오.
#    "Alice" = 85,
#    "Bob" = 78,
#    "Charlie" = 92,
#    "David" = 88,
#    "Eve" = 95
# 모든 학생의 평균 점수를 계산하여 출력하시오.
# 80점 이상을 받은 학생들의 이름을 리스트 컴프리헨션을 사용하여 추출하시오.
# 학생들의 점수를 높은 순서대로 정렬하여 출력하시오.
# 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이를 계산하여 출력하시오.
# 각 학생의 점수가 평균 점수보다 높은지 낮은지를 판단하여, 낮은 학생의 이름과 성적을 함께 출력하시오.



'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

# 아래에 코드를 작성하시오.

scores = {
   "Alice" : 85,
   "Bob" : 78,
   "Charlie" : 92,
   "David" : 88,
   "Eve" : 95
}

avg = 0
sum = 0
# 80점이 넘는 학생 이름
list_over80 = [name for name,score in scores.items() if score >= 80]

# 평균을 구하기 전 점수들의 합
for name,score in scores.items() :
    sum += score

# 평균값
avg = sum / len(scores)

print(f"student type: {type(scores)}")
print(scores)
print(avg)
print(list_over80)

# 점수 순으로 정렬
sorted_scores = dict(sorted(scores.items(), key=lambda x:x[1], reverse=True))
for name,score in sorted_scores.items():
    print(f"{name}: {score}")


# 가장 높은 점수와 가장 낮은 점수의 차
max_score = max(scores.values())
min_score = min(scores.values())
print(max_score-min_score)


# 각 학생의 점수가 평균보다 낮은지 높은지 판단
for name,score in scores.items() : 
   if score >= avg : 
        print(f"{name} 학생의 점수({score})는 평균 이상입니다.")
   else : 
       print(f"{name} 학생의 점수({score})는 평균 이하입니다.")