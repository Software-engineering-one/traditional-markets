from tkinter import*

def click_button1():
   sublabel = Label(tkin, text = "1. 별점 및 평가 입력 2. 별점 및 평가 조회")
   sublabel.pack()
   button3 = Button(tkin, text = "1. 별점 및 평가 입력", command = click_button3)
   button3.pack()
   button4 = Button(tkin, text = "2. 별점 및 평가 조회", command = click_button4)
   button4.pack()
   if button3:
        click_button3
   else:
       click_button4

def click_button2():
    sublabel2 = Label(tkin, text = "피드백 게시판 조회")
    sublabel2.pack()
    for star, eval in rate.items():
        total_Label = Label(tkin, text = star)
        total_Label.pack()
        total_Label2 = Label(tkin, text = eval)
        total_Label2.pack()


def click_button3():
    consumer_Label = Label(tkin, text = "별점 및 평가를 입력하세요")
    consumer_Label.pack()
    consumer_label2 = Label(tkin, text = "별점:")
    consumer_label2.pack()
    consumer_entry = Entry(tkin)
    consumer_entry.pack()
    consumer_label3 = Label(tkin, text = "평가:")
    consumer_label3.pack()
    consumer_entry2 = Entry(tkin)
    consumer_entry2.pack()
    star = consumer_entry.get()
    eval = consumer_entry2.get()
    starandevalcheck = Button(tkin, text = "별점 및 평가 입력 완료", command = starandeval(star, eval))
    starandevalcheck.pack()

def starandeval(star, eval):
    rate[star] = eval
    click_button1

def click_button4(star, eval):
    for star, eval in rate.items():
        total_Label = Label(tkin, text = star)
        total_Label.pack()
        total_Label2 = Label(tkin, text = eval)
        total_Label2.pack()

   
tkin = Tk()
tkin.title("운영관리")
rate = dict()
for j in range(9):
    mainlabel = Label(tkin, text = "소비자 또는 소상공인 유무를 확인하세요")
    mainlabel.pack()
    button1 = Button(tkin, text = "1. 소비자", command = click_button1)
    button1.pack()
    button2 = Button(tkin, text = "2. 소상공인", command= click_button2)
    button2.pack()
    user = int(input())
    star = 0
    eval = 0
    for i in range(5):
      if button1:
          click_button1
      else:
           click_button2
           break
      break

tkin.mainloop()