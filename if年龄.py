age = int(input("请输入你的年龄: "))
print("")
if age < 0:
    print("你还没出生吧!")
elif 0 <=age<=12 :
    print("小屁孩。")
elif 13<=age<=19 :
    print("豆蔻。")
elif 13<=age<=19 :
    print("弱冠。")
elif 20<=age<=29 :
    print("而立。")
elif 30<=age<=39 :
    print("不惑。")
elif 40<=age<=49 :
    print("知命。")
elif 50<=age<=59 :
    print("花甲。")
elif 60<=age<=69 :
    print("古稀。")
elif 70<=age<=79 :
    print("豆蔻。")
elif 80<=age<=99 :
    print("耄耋。")
elif age>=100 :
    print("期颐。")

 
### 退出提示
input("点击 enter 键退出")
