# print("let's start the game")
# print("Here is your question:") 
# question=["Q.1 how many continents are there?"
# "Q.2 What is the capital of india?",
# "Q.3 Which course navgurukul teach?"]
# option=[["seven","eight","five"],
# ["chennai","chandigarh","mumbai"],
# ["counselling","software","tourism","agriculture"]]
# solution=[1,2,3]
# ans_list=[
# ["1.seven","2.eight"]
# ["2.chandigarh","3.delhi"]
# ["1.counselling","2.software"]]
# i=0
# count=0
# price=0
# while i<len(question):
#     print(question[i])
#     j=i
#     s_no=0
#     while s_no<len(option[i]):
#         a=option[j][s_no]
#         print(s_no+1,a)
#         s_no+1
#     if count==0:
#         lifeline=input("Do u want lifeline:-yes/no:")
#     if lifeline=="yes":
#         count+1
    #     print("select your option")
    #     sel_opt=0
    #     b=i
    #     while sel_opt<len(ans_list[i]):
    #         c=ans_list[b][sel_opt]
    #         sel_opt+=1
    #         print(c)
    #     ans1=int(input("choose your answer:"))
    #     if ans1==solution[i]:
    #         price+=1000
    #         print("correct answer,and your winning price is",price)
    #         print("congratulations")
    #         print("your next question is:")
    #     else:
    #         print("wrong answer")
    #         break
    # else:
    #     ans2=int(input("choose your answer:"))
    #     if ans2==solution[i]:
    #         price+=1000
    #         print("correct answer and your winning price is",price)
    #         print("congratulations")
    #         print("your next question is:-")
    #     else:
    #         print("wrong answer")
    #         break
    #     i+=1
        


# a=[12,45,23,67,78,90,45,32,100,70,30,62,73,29,83]
# i=0
# k=0
# b=[]
# while i<len(a):
#     j=0
#     c=[]
#     while j<5 and k!=len(a):
#         c.append(a[k])
#         j=j+1
#         k=k+1
#     b.append(c)
#     if k==len(a):
#         break
#     i=i+1
# print(b)


# # a=[1,2,3,4,5]
# # i=0
# # m=[]
# # while i<len(a)-1:
# #     b=[a[i],a[i+1]]
# #     m.append(b)
# #     i=i+1
# # print(m)





# # a=int(input("enter the number"))
# # b=int(input("enter the number"))
# # print(float(a/b))
# # print(a*b)
# # print(a**b)
# # print(str(a)*b)
# # print(str(a)+str(b))




# a= int(input("enter the num"))
# if a>12:
#     print("two girls extra",a-12)
# elif a<12:
#     print("we need girls",12-a)
# else:
#     print("equal")




# a=[1,2,3,4,5]
# b=[6,7,8,9,10]
# c=[]
# i=0
# while i<len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i=i+1
# j=0
# while i<len(c):
#     if c[i]<c[j]:
#         c[i],c[j]+c[j],c[i]
#         j=j+1
#     i=i+1
# print(c)
# a.extend(b)
# print(a)


# print("5"**5)

# print("5"*5)



print("Let's start the game")
print("Here is your question:")
question=["Q.1 How many continents are there?",
"Q.2 what is the capital of india?",
"Q.3 which course navgurukul teach?"]
option=[["seven","eight","nine","five"],
["chennai","chandigarh","delhi","mumbai"],
["counselling","software","tourism","agriculture"]]
solution=[1,3,2]
lifeline=[
["1.seven","2.eight"],
["2.chandigarh","3.delhi"],
["1.counselling","2.software"]]
i=0
count=0
price=0
while i<len(question):
    print(question[i])
    j=i
    s_no=0
    while s_no<len(option[i]):
        a=option[j][s_no]
        print(s_no+1,a)
        s_no+=1    
    lifeline1=input("Do u want lifeline:-yes/no : ")
    if lifeline1=="yes":
        if count==0:
            print("select your option") 
            sel_opt=0
            b=i
            while sel_opt<len(lifeline[i]):
                c=lifeline[b][sel_opt]
                sel_opt+=1
                print(c)
            ans=int(input("choose your answer : ")) 
            if ans==solution[i]:
                price+=1000
                print("correct answer, and your winning price is",price)
                print("congratulations")
                print("your next question is:")
            else:
                print("wrong answer")
                break 
            count+=1
        else:
            print("you already use lifeline")
            ans1=int(input("choose your answer : "))
            if ans1==solution[i]:
                price+=1000
                print("correct answer, and your winning price is",price) 
                print("congratulations")
            else:
                print("wrong answer")
                break
    else:
        ans2=int(input("choose your answer: "))
        if ans2==solution[i]:
            price+=1000
            print("correct answer and your winning price is",price)
            print("congratulations")
            # print("your next question is:-")   
        else:
            print("wrong answer") 
            break   
    i+=1