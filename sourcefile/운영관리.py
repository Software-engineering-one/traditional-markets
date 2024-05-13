
rate = dict()
for j in range(9):
    print("소비자 또는 소상공인 유무를 확인하세요")
    print("1. 소비자 2. 소상공인")
    user = int(input())
    star = 0
    eval = 0
    for i in range(5):
      if user == 1:
          print("1. 별점 및 평가 입력 2. 별점 및 평가 조회")
          starandeval = int(input())
          if starandeval == 1:
             print("별점 및 평가를 입력하세요:")
             star = float(input())
             eval = input()
             rate[star] = eval
          else:
              for star, eval in rate.items():
               print(star, eval)
              break
      else:
           print("피드백 게시판 조회")
           for star, eval in rate.items():
               print(star, eval)
           break
      break