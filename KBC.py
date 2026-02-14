questions = [
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1],
    ["how are you","fine","good","mast","notwell",1]
    
]


levels=[1000,2000,4000,16000,32000,640000,100000,200000,400000,500000,1000000,2000000]

money = 0

i=0
for i in range(0,len(questions)):

    question=questions[i]
    print(f"\n\nquestion for amount  {levels[i]}  and question is {question[0]}")
    print(f"a.{question[1]}       b.{question[2]}")
    print(f"c.{question[3]}       d.{question[4]}")

    reply = int(input("enter your answer(1-4) or 0 for quit\n"))

    if (reply==0):
        money=levels[i-1]
        break
    if (reply==question[-1]):
        print(f"correct answer , you won {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=1000000
        elif(i==14):
            money=10000000

           
    else:
        print("wrong answer")
        break

print(f"your take home money is {money}")