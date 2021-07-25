import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import sqlite3

# 连接数据库
cn = sqlite3.connect('student.db')
cur = cn.cursor()

# 登录信息验证
def verify():
    s1 = c1.get()
    s2 = e1.get()
    s3 = e2.get()
    if s2 == '' or s3 == '':
        y1 = mb.showinfo('登录', '请输入账户与密码')
        print(y1)
    else:
        cur.execute('select * from verify where mold=? and name=? and password=?', (s1, s2, s3,))
        lg = cur.fetchone()
        if lg:
            y2 = mb.showinfo('登录', '登录成功')
            print(y2)
            if s1 == '学生':
                rt.destroy()
                student(s2)
            elif s1 == '教师':
                rt.destroy()
                teacher(s2)
        else:
            y3 = mb.showinfo('登录', '用户名或密码错误，请检查！')
            print(y3)
    return 0

# 注册页面
def login():
    def close():
        rt1.destroy()

    def into():
        s7 = var7.get()
        s6 = var6.get()
        s4 = c2.get()
        s5 = var5.get()
        if s4 == '' or s5 == '' or s6 == '' or s7 == '':
            y4 = mb.showinfo('注册', '请输入账户与密码')
            print(y4)
        else:
            if s6 == s7:
                if s5.isdigit():
                    if 0 <= int(s5) < 100000:
                        cur.execute('select * from verify where name=?', (s5,))
                        lg = cur.fetchone()
                        if lg:
                            y6 = mb.showinfo('注册', '用户名已存在')
                            print(y6)
                        else:
                            if s4 == '教师':
                                cur.execute('insert into verify values(?,?,?)', (s5, s6, s4,))
                                cn.commit()
                                y8 = mb.showinfo('注册', '注册成功')
                                print(y8)
                                rt1.destroy()
                            elif s4 == '学生':
                                cur.execute('insert into verify values(?,?,?)', (s5, s6, s4,))
                                cur.execute('insert into students values(?,0 ,0 ,0 ,0 ,0 , 0)', (s5,))
                                cur.execute('insert into score values(?,0,0,0,0,0,0)', (s5,))
                                cn.commit()
                                print(s4 + s5 + s6)
                                y8 = mb.showinfo('注册', '注册成功')
                                print(y8)
                                rt1.destroy()
                    else:
                        y7 = mb.showinfo('注册', '账号格式错误')
                        print(y7)
                else:
                    y8 = mb.showinfo('注册', '账号格式错误')
                    print(y8)
            else:
                y5 = mb.showinfo('注册', '两次输入密码不同')
                print(y5)

    rt1 = tk.Toplevel()
    rt1.title("账号注册")
    rt1.geometry('400x400')
    rt1.update()
    curx1 = rt1.winfo_width()
    cury1 = rt1.winfo_height()
    scnx1 = rt1.winfo_screenwidth()
    scny1 = rt1.winfo_screenheight()
    tm1 = '%dx%d+%d+%d' % (curx1, cury1, (scnx1 - curx1) / 2 + 400, (scny1 - cury1) / 2)
    rt1.geometry(tm1)
    rt1.resizable(False, False)
    var4 = tk.StringVar()
    c2 = ttk.Combobox(rt1, textvariable=var4, font=("宋体", 20), state='readonly')
    c2['values'] = ("学生", "教师")
    c2["state"] = "readonly"
    c2.set("学生")
    c2.current(0)
    c2.place(x=40, y=40)

    b14 = tk.Label(rt1, text="账号", font=("宋体", 20))
    b14.place(x=40, y=100)
    var5 = tk.StringVar()
    e13 = tk.Entry(rt1, textvariable=var5, width=15, font=("宋体", 20))
    e13.place(x=120, y=100)

    b15 = tk.Label(rt1, text="密码", font=("宋体", 20))
    b15.place(x=40, y=160)
    var6 = tk.StringVar()
    e14 = tk.Entry(rt1, textvariable=var6, width=15, font=("宋体", 20), show='*')
    e14.place(x=120, y=160)
    e14.focus_set()

    b6 = tk.Label(rt1, text="确认密码", font=("宋体", 20))
    b6.place(x=20, y=220)
    var7 = tk.StringVar()
    e6 = tk.Entry(rt1, textvariable=var7, width=15, font=("宋体", 20), show='*')
    e6.place(x=130, y=220)
    e6.focus_set()

    bu3 = tk.Button(rt1, text="注册", width=7, height=1, font=("华文行楷", 20), command=lambda: into())
    bu3.place(x=60, y=300)
    bu4 = tk.Button(rt1, text="返回", width=7, height=1, font=("华文行楷", 20), command=lambda: close())
    bu4.place(x=200, y=300)
    b5 = tk.Label(rt1, text="注意：账号为学号或教师编号，由1~5位阿拉伯数字组成", font=("宋体", 10), width=45, height=2)
    b5.place(x=40, y=360)
    rt1.mainloop()
    return 0

# 修改密码
def xiugaimima(s):
    def into(s):
        s1 = e1.get()
        s2 = e2.get()
        s3 = e3.get()
        print(s)
        cur.execute('select * from verify where name=?',(s,))
        tm4 = cur.fetchone()
        print(tm4[1])
        if s1 == '' or s2 == '' or s3 == '':
            y1 = mb.showinfo('密码修改', '请输入密码')
            print(y1)
        else:
            if s2 == s3:
                if s1 == tm4[1]:
                    cur.execute('update verify set password=? where name=?', (s2, s,))
                    cn.commit()
                    lg = cur.fetchone()
                    y3 = mb.showinfo('密码修改', '密码修改成功')
                    print(y3)
                    rt7.destroy()
                    return 1
                else:
                    y3 = mb.showinfo('密码修改', '原密码错误')
                    print(y3)
            else:
                y2 = mb.showinfo('密码修改', '两次输入密码不同')
                print(y2)
    def close():
        rt7.destroy()
    rt7 = tk.Tk()
    rt7.title("密码修改")
    rt7.geometry('400x300')
    rt7.update()
    curx = rt7.winfo_width()
    cury = rt7.winfo_height()
    scnx = rt7.winfo_screenwidth()
    scny = rt7.winfo_screenheight()
    tm3 = '%dx%d+%d+%d' % (curx, cury, (scnx - curx) / 2, (scny - cury) / 2)
    rt7.geometry(tm3)
    rt7.resizable(False, False)
    b1 = tk.Label(rt7, text="旧密码:", font=("宋体", 20))
    b1.place(x=40, y=40)
    var1 = tk.StringVar()
    e1 = tk.Entry(rt7, textvariable=var1, width=15, font=("宋体", 20), show='*')
    e1.place(x=160, y=40)

    b2 = tk.Label(rt7, text="新密码:", font=("宋体", 20))
    b2.place(x=40, y=100)
    var2 = tk.StringVar()
    e2 = tk.Entry(rt7, textvariable=var2, width=15, font=("宋体", 20), show='*')
    e2.place(x=160, y=100)

    b3 = tk.Label(rt7, text="确认密码:", font=("宋体", 20))
    b3.place(x=40, y=160)
    var3 = tk.StringVar()
    e3 = tk.Entry(rt7, textvariable=var3, width=15, font=("宋体", 20), show='*')
    e3.place(x=160, y=160)

    bu3 = tk.Button(rt7, text="确定", width=7, height=1, font=("华文行楷", 20), command=lambda: into(s))
    bu3.place(x=60, y=230)
    bu4 = tk.Button(rt7, text="取消", width=7, height=1, font=("华文行楷", 20), command=lambda: close())
    bu4.place(x=200, y=230)
    rt7.mainloop()

# 学生个人信息修改
def xinxixiugei(s):
    def close():
        rt6.destroy()
    def tijiao():
        s1 = e1.get()
        s2 = c2.get()
        s3 = c3.get()
        s4 = e4.get()
        s5 = e5.get()
        s6 = c6.get()
        if s1 == '' or s2 == '' or s3 == '' or s4== '' or s5 == '' or s6 == '':
            y2 = mb.showinfo('信息修改', '信息修改成功')
            print(y2)
        else:
            if s5.isdigit():
                if 9999999999 < int(s5) < 100000000000:
                    cur.execute('update students set name=?, sex=?, age=?, grade=?, phone=?, college=? where id=?', (s1,s2,s3,s4,s5,s6,s,))
                    cur.execute('update score set name=?, grade=? where id=?',(s1, s4, s,))
                    cn.commit()
                    y1 = mb.showinfo('信息修改', '信息修改成功')
                    print(y1)
                    rt6.destroy()
                else:
                    y3 = mb.showinfo('信息修改', '电话号码位数错误')
                    print(y3)
            else:
                y3 = mb.showinfo('信息修改', '电话号码格式错误')
                print(y3)
    rt6 = tk.Tk()
    rt6.title("学生个人信息修改")
    rt6.geometry('500x400')
    rt6.update()
    curx = rt6.winfo_width()
    cury = rt6.winfo_height()
    scnx = rt6.winfo_screenwidth()
    scny = rt6.winfo_screenheight()
    tm6 = '%dx%d+%d+%d' % (curx, cury, (scnx - curx) / 2, (scny - cury) / 2)
    rt6.geometry(tm6)
    rt6.resizable(False, False)
    cur.execute('select * from students where id=?', (s,))
    tm1 = cur.fetchone()

    b1 = tk.Label(rt6, text="姓名：", font=("宋体", 20))
    b1.place(x=40, y=40)
    var1 = tk.StringVar()
    e1 = tk.Entry(rt6, textvariable=var1, width=10, font=("宋体", 20))
    e1.place(x=120, y=40)
    e1.insert(0,tm1[1])

    b2 = tk.Label(rt6, text="性别：", font=("宋体", 20))
    b2.place(x=40, y=100)
    var2 = tk.StringVar()
    c2 = ttk.Combobox(rt6, textvariable=var2, width=9, font=("宋体", 20))
    c2['values'] = ("男", "女")
    c2["state"] = "readonly"
    c2.current(0)
    c2.set(tm1[2])
    c2.place(x=120, y=100)

    b3 = tk.Label(rt6, text="年龄：", font=("宋体", 20))
    b3.place(x=40, y=160)
    var3 = tk.StringVar()
    c3 = ttk.Combobox(rt6, textvariable=var3, width=9, font=("宋体", 20))
    c3['values'] = ("17", "18", "19", "20", '21', '22', '23', '24', '25')
    c3["state"] = "readonly"
    c3.current(2)
    c3.set(tm1[3])
    c3.place(x=120, y=160)

    b4 = tk.Label(rt6, text="班级：", font=("宋体", 20))
    b4.place(x=40, y=220)
    var4 = tk.StringVar()
    e4 = tk.Entry(rt6, textvariable=var4, width=10, font=("宋体", 20))
    e4.insert(0,tm1[4])
    e4.place(x=120, y=220)

    b5 = tk.Label(rt6, text="电话：", font=("宋体", 20))
    b5.place(x=40, y=280)
    var5 = tk.StringVar()
    e5 = tk.Entry(rt6, textvariable=var5, width=10, font=("宋体", 20))
    e5.insert(0, tm1[5])
    e5.place(x=120, y=280)

    b6 = tk.Label(rt6, text="学院：", font=("宋体", 20))
    b6.place(x=40, y=340)
    var6 = tk.StringVar()
    c6 = ttk.Combobox(rt6, textvariable=var6, width=9, font=("宋体", 20))
    c6['values'] = ("电子与信息工程学院", "机械工程学院", '数学学院')
    c6["state"] = "readonly"
    c6.current(0)
    c6.set(tm1[6])
    c6.place(x=120, y=340)

    b7 = tk.Label(rt6, text='学号：'+tm1[0],font=('华文行楷',20))
    b7.place(x=300,y=40)
    bu7 = tk.Button(rt6, text="提交信息", width=16, height=1, font=("宋体", 15), command=lambda: tijiao())
    bu7.place(x=300, y=100)
    bu8 = tk.Button(rt6, text="退出", width=10, height=1, font=("宋体", 15), command=lambda: close())
    bu8.place(x=300, y=200)
    rt6.mainloop()
    return 0

# 学生端页面
def student(s2):
    def xinxixiugeixisheng(s):
        rt3.destroy()
        xinxixiugei(s)
        student(s2)
    def close():
        rt3.destroy()
    rt3 = tk.Tk()
    rt3.title("学生信息表")
    rt3.geometry('800x600')
    rt3.update()
    rt3.resizable(False, False)
    curx = rt3.winfo_width()
    cury = rt3.winfo_height()
    scnx = rt3.winfo_screenwidth()
    scny = rt3.winfo_screenheight()
    tm1 = '%dx%d+%d+%d' % (curx, cury, (scnx - curx) / 2, (scny - cury) / 2)
    rt3.geometry(tm1)

    b1 = tk.Label(rt3, text="学生信息端", font=("宋体", 40), width=31, height=2, bg='#42b7d5')
    b1.place(x=0, y=0)
    cv = tk.Canvas(rt3, width=800, height=600, bd=2)
    cv.place(x=0, y=120)
    cv.create_line((70, 70), (750, 70), width=3, fill='green')
    cv.create_line((70, 110), (750, 110), width=2, fill='green')
    cv.create_line((70, 150), (750, 150), width=3, fill='green')
    cv.create_line((70, 70), (70, 150), width=3, fill='green')
    cv.create_line((145, 70), (145, 150), width=1, fill='green')
    cv.create_line((215, 70), (215, 150), width=1, fill='green')
    cv.create_line((265, 70), (265, 150), width=1, fill='green')
    cv.create_line((315, 70), (315, 150), width=1, fill='green')
    cv.create_line((435, 70), (435, 150), width=1, fill='green')
    cv.create_line((555, 70), (555, 150), width=1, fill='green')
    cv.create_line((750, 70), (750, 150), width=3, fill='green')
    cur.execute('select * from students where id=?', (s2,))
    tm = cur.fetchone()
    l1 = tk.Label(cv, text='学生信息', font=('楷体', 16, 'bold'))
    l1.place(x=20, y=30)
    lb1 = tk.Label(cv, text='学号', font=('仿宋', 13))
    lb1.place(x=80, y=80)
    lb2 = tk.Label(cv, text='姓名', font=('仿宋', 13))
    lb2.place(x=150, y=80)
    lb3 = tk.Label(cv, text='性别', font=('仿宋', 13))
    lb3.place(x=220, y=80)
    lb4 = tk.Label(cv, text='年龄', font=('仿宋', 13))
    lb4.place(x=270, y=80)
    lb5 = tk.Label(cv, text='班级', font=('仿宋', 13))
    lb5.place(x=320, y=80)
    lb7 = tk.Label(cv, text='电话', font=('仿宋', 13))
    lb7.place(x=440, y=80)
    lb9 = tk.Label(cv, text='所在学院', font=('仿宋', 13))
    lb9.place(x=560, y=80)
    lb11 = tk.Label(cv, text=tm[0], font=('仿宋', 13))
    lb11.place(x=80, y=120)
    lb12 = tk.Label(cv, text=tm[1], font=('仿宋', 13))
    lb12.place(x=150, y=120)
    lb13 = tk.Label(cv, text=tm[2], font=('仿宋', 13))
    lb13.place(x=220, y=120)
    lb14 = tk.Label(cv, text=tm[3], font=('仿宋', 13))
    lb14.place(x=270, y=120)
    lb15 = tk.Label(cv, text=tm[4], font=('仿宋', 13))
    lb15.place(x=320, y=120)
    lb16 = tk.Label(cv, text=tm[5], font=('仿宋', 13))
    lb16.place(x=440, y=120)
    lb17 = tk.Label(cv, text=tm[6], font=('仿宋', 13))
    lb17.place(x=560, y=120)

    cur.execute('select * from score where id=?', (s2,))
    tm1 = cur.fetchone()
    cv.create_line((70, 240), (450, 240), width=3, fill='green')
    cv.create_line((70, 290), (450, 290), width=2, fill='green')
    cv.create_line((70, 330), (450, 330), width=3, fill='green')
    cv.create_line((70, 240), (70, 330), width=3, fill='green')
    cv.create_line((140, 240), (140, 330), width=1, fill='green')
    cv.create_line((240, 240), (240, 330), width=1, fill='green')
    cv.create_line((340, 240), (340, 330), width=1, fill='green')
    cv.create_line((450, 240), (450, 330), width=3, fill='green')
    l21 = tk.Label(cv, text='公共课成绩信息', font=('楷体', 16, 'bold'))
    l21.place(x=20, y=200)
    lb21 = tk.Label(cv, text='高数', font=('仿宋', 13))
    lb21.place(x=80, y=250)
    lb22 = tk.Label(cv, text='大学物理', font=('仿宋', 13))
    lb22.place(x=150, y=250)
    lb23 = tk.Label(cv, text='大学体育', font=('仿宋', 13))
    lb23.place(x=250, y=250)
    lb24 = tk.Label(cv, text='思修', font=('仿宋', 13))
    lb24.place(x=350, y=250)
    lb31 = tk.Label(cv, text=tm1[3], font=('仿宋', 13))
    lb31.place(x=80, y=300)
    lb32 = tk.Label(cv, text=tm1[4], font=('仿宋', 13))
    lb32.place(x=150, y=300)
    lb33 = tk.Label(cv, text=tm1[5], font=('仿宋', 13))
    lb33.place(x=250, y=300)
    lb34 = tk.Label(cv, text=tm1[6], font=('仿宋', 13))
    lb34.place(x=350, y=300)

    bu3 = tk.Button(rt3, text="学生个人信息修改", width=16, height=1, font=("宋体", 15), command=lambda: xinxixiugeixisheng(s2))
    bu3.place(x=100, y=500)
    bu4 = tk.Button(rt3, text="密码修改", width=16, height=1, font=("宋体", 15), command=lambda: xiugaimima(s2))
    bu4.place(x=350, y=500)
    bu5 = tk.Button(rt3, text="安全退出", width=16, height=1, font=("宋体", 15), command=lambda: close())
    bu5.place(x=550, y=500)
    rt3.mainloop()
    return 0

def teacher(ss):
    def close():
        rt4.destroy()
    def chenji():
        s = e35.get()

        def chenji2():
            def close():
                rt6.destroy()
            def tijiao():
                s1 = e1.get()
                s2 = e2.get()
                s3 = e3.get()
                s4 = e4.get()
                if s1 == '' or s2 == '' or s3 == '' or s4 == '':
                    y2 = mb.showinfo('学生成绩录入', '请输入成绩信息')
                    print(y2)
                else:
                    if s1.isdigit() and s2.isdigit() and s3.isdigit() and s4.isdigit():
                        if 0 <= int(s1) <= 100 and 0 <= int(s2) <= 100 and 0 <= int(s3) <= 100 and 0 <= int(s4) <= 100:
                            cur.execute('update score set gaoshu=?,wuli=?,tiyu=?,sixiu=? where id=?',(s1, s2, s3, s4, s,))
                            cn.commit()
                            y1 = mb.showinfo('学生成绩录入', '成绩录入成功')
                            print(y1)
                            rt6.destroy()
                        else:
                            y3 = mb.showinfo('学生成绩录入', '成绩不在正确区间')
                            print(y3)

                    else:
                        y3 = mb.showinfo('学生成绩录入', '成绩格式错误')
                        print(y3)

            rt6 = tk.Tk()
            rt6.title("学生成绩录入")
            rt6.geometry('500x400')
            rt6.update()
            curx = rt6.winfo_width()
            cury = rt6.winfo_height()
            scnx = rt6.winfo_screenwidth()
            scny = rt6.winfo_screenheight()
            tm6 = '%dx%d+%d+%d' % (curx, cury, (scnx - curx) / 2+500, (scny - cury) / 2)
            rt6.geometry(tm6)
            rt6.resizable(False, False)
            cur.execute('select * from score where id=?', (s,))
            tm1 = cur.fetchone()

            b1 = tk.Label(rt6, text="高数：", font=("宋体", 20))
            b1.place(x=40, y=40)
            var1 = tk.StringVar()
            e1 = tk.Entry(rt6, textvariable=var1, width=10, font=("宋体", 20))
            e1.place(x=120, y=40)
            e1.insert(0, tm1[3])

            b2 = tk.Label(rt6, text="物理：", font=("宋体", 20))
            b2.place(x=40, y=100)
            var2 = tk.StringVar()
            e2 = tk.Entry(rt6, textvariable=var2, width=10, font=("宋体", 20))
            e2.insert(0, tm1[4])
            e2.place(x=120, y=100)

            b3 = tk.Label(rt6, text="体育：", font=("宋体", 20))
            b3.place(x=40, y=160)
            var3 = tk.StringVar()
            e3 = tk.Entry(rt6, textvariable=var3, width=10, font=("宋体", 20))
            e3.insert(0, tm1[5])
            e3.place(x=120, y=160)

            b4 = tk.Label(rt6, text="思修：", font=("宋体", 20))
            b4.place(x=40, y=220)
            var4 = tk.StringVar()
            e4 = tk.Entry(rt6, textvariable=var4, width=10, font=("宋体", 20))
            e4.insert(0, tm1[6])
            e4.place(x=120, y=220)

            b7 = tk.Label(rt6, text='学号：' + tm1[0], font=('华文行楷', 20))
            b7.place(x=300, y=40)
            b8 = tk.Label(rt6, text='姓名：' + tm1[1], font=('华文行楷', 20))
            b8.place(x=300, y=100)
            b9 = tk.Label(rt6, text='班级：' + tm1[2], font=('华文行楷', 20))
            b9.place(x=300, y=160)
            bu7 = tk.Button(rt6, text="提交信息", width=16, height=1, font=("宋体", 15), command=lambda: tijiao())
            bu7.place(x=300, y=220)
            bu8 = tk.Button(rt6, text="退出", width=16, height=1, font=("宋体", 15), command=lambda: close())
            bu8.place(x=300, y=260)
            rt6.mainloop()
        if s.isdigit():
            if 0 <= int(s) < 100000:
                cur.execute('select * from score where id=?', (s,))
                lg = cur.fetchone()
                if lg:
                    chenji2()
                else:
                    y6 = mb.showinfo('提示', '该学生不存在')
                    print(y6)
            else:
                y4 = mb.showinfo('提示', '学号位数错误')
                print(y4)
        else:
            y5 = mb.showinfo('提示', '学号格式错误')
            print(y5)
    def table(s):
        rt5 = tk.Toplevel()
        rt5.title("学生信息表")
        rt5.geometry()
        rt5.update()
        rt5.resizable(False, False)
        cv1 = tk.Canvas(rt5, width=800, height=800)
        cv1.place(x=0, y=0)
        cur.execute(s)
        tm = cur.fetchall()
        tree = ttk.Treeview(rt5, columns=['id', 'name', 'sex', 'age', 'grade', 'phone', 'college'], show='headings')
        tree.column('id', width=100, anchor='center')
        tree.column('name', width=100, anchor='center')
        tree.column('sex', width=100, anchor='center')
        tree.column('age', width=100, anchor='center')
        tree.column('grade', width=100, anchor='center')
        tree.column('phone', width=100, anchor='center')
        tree.column('college', width=100, anchor='center')
        tree.heading('id', text='学号')
        tree.heading('name', text='姓名')
        tree.heading('sex', text='性别')
        tree.heading('age', text='年龄')
        tree.heading('grade', text='班级')
        tree.heading('phone', text='电话')
        tree.heading('college', text='所在学院')
        for each in tm:
            tree.insert('', 'end', values=each)
        tree.grid()
        rt5.mainloop()
    def table2(s):
        rt5 = tk.Toplevel()
        rt5.title("学生成绩表")
        rt5.geometry()
        rt5.update()
        rt5.resizable(False, False)
        cv1 = tk.Canvas(rt5, width=800, height=800)
        cv1.place(x=0, y=0)
        cur.execute(s)
        tm = cur.fetchall()
        tree = ttk.Treeview(rt5, columns=['id', 'name', 'grade', 'gaoshu', 'wuli', 'tiyu', 'sixiu'], show='headings')
        tree.column('id', width=100, anchor='center')
        tree.column('name', width=100, anchor='center')
        tree.column('grade', width=100, anchor='center')
        tree.column('gaoshu', width=100, anchor='center')
        tree.column('wuli', width=100, anchor='center')
        tree.column('tiyu', width=100, anchor='center')
        tree.column('sixiu', width=100, anchor='center')
        tree.heading('id', text='学号')
        tree.heading('name', text='姓名')
        tree.heading('grade', text='班级')
        tree.heading('gaoshu', text='高数')
        tree.heading('wuli', text='物理')
        tree.heading('tiyu', text='体育')
        tree.heading('sixiu', text='思修')
        for each in tm:
            tree.insert('', 'end', values=each)
        tree.grid()
        rt5.mainloop()
    # 班级学生查询
    def banjichaxun():
        s1 = e1.get()
        if s1 == '':
            y3 = mb.showinfo('学生信息查询', '请输入班级信息！')
            print(y3)
        else:
            s2 = "select * from students where grade='{}'".format(s1)
            table(s2)

    # 学院学生查询
    def xueyuanchaxun():
        s1 = c1.get()
        s2 = "select * from students where college='{}'".format(s1)
        table(s2)
    # 学生个人信息查询
    def gerenchaxun():
        s1 = e31.get()
        if s1 == '':
            y3 = mb.showinfo('学生个人信息查询', '请输入学号或姓名！')
            print(y3)
        else:
            if s1.isdigit():
                s2 = "select * from students where id='{}'".format(s1)
            else:
                s2 = "select * from students where name='{}'".format(s1)
            table(s2)
    # 班级成绩查询
    def banjichenji():
        s1 = e11.get()
        if s1 == '':
            y3 = mb.showinfo('班级成绩查询', '请输入班级信息！')
            print(y3)
        else:
            s2 = "select * from score where grade='{}'".format(s1)
            table2(s2)

    # 学生成绩查询
    def gerenchenji():
        s1 = e21.get()
        if s1 == '':
            y3 = mb.showinfo('学生个人成绩查询', '请输入学号或姓名！')
            print(y3)
        else:
            if s1.isdigit():
                s2 = "select * from score where id='{}'".format(s1)
            else:
                s2 = "select * from score where name='{}'".format(s1)
            table2(s2)

    # 教师端学生个人信息修改
    def xinxixiugai1():
        s = e34.get()
        if s=='':
            y7 = mb.showinfo('提示', '请输入学号')
            print(y7)
        else:
            if s.isdigit():
                if 0 < int(s) < 100000:
                    cur.execute('select * from score where id=?', (s,))
                    lg = cur.fetchone()
                    if lg:
                        xinxixiugei(s)
                    else:
                        y6 = mb.showinfo('提示', '该学生不存在')
                        print(y6)
                else:
                    y4 = mb.showinfo('提示', '学号位数错误')
                    print(y4)
            else:
                y5 = mb.showinfo('提示', '学号格式错误')
                print(y5)
    # 教师端删除学生个人信息
    def delete():
        s = e36.get()
        if s == '':
            y7 = mb.showinfo('提示', '请输入学号')
            print(y7)
        else:
            if s.isdigit():
                if 0 < int(s) < 100000:
                    cur.execute('select * from score where id=?', (s,))
                    lg = cur.fetchone()
                    if lg:
                        cur.execute('delete from students where id=?',(s,))
                        cur.execute('delete from verify where name=?', (s,))
                        cur.execute('delete from score where id=?', (s,))
                        cn.commit()
                        y9 = mb.showinfo('提示', '学生信息删除成功')
                        print(y9)
                    else:
                        y6 = mb.showinfo('提示', '该学生不存在')
                        print(y6)
                else:
                    y4 = mb.showinfo('提示', '学号位数错误')
                    print(y4)
            else:
                y5 = mb.showinfo('提示', '学号格式错误')
                print(y5)

    rt4 = tk.Tk()
    rt4.title("教师管理端")
    rt4.geometry('800x600')
    rt4.update()
    curx = rt4.winfo_width()
    cury = rt4.winfo_height()
    scnx = rt4.winfo_screenwidth()
    scny = rt4.winfo_screenheight()
    tm = '%dx%d+%d+%d' % (curx, cury, (scnx - curx) / 2, (scny - cury) / 2)
    rt4.geometry(tm)
    rt4.resizable(False, False)
    b1 = tk.Label(rt4, text="", font=("华文行楷", 30), width=50, height=2, bg='#42b7d5')
    b1.place(x=0, y=0)
    b2 = tk.Label(rt4, text="教师管理端", font=("华文行楷", 30), width=16, height=2, bg='#42b7d5')
    b2.place(x=0, y=0)
    bu1 = tk.Button(rt4, text="全部学生信息", width=22, height=1, font=("宋体", 20), command=lambda: table('select * from students'))
    bu1.place(x=60, y=120)
    var1 = tk.StringVar()
    e1 = tk.Entry(rt4, textvariable=var1, width=10, font=("宋体", 20))
    e1.place(x=60, y=200)
    bu2 = tk.Button(rt4, text="班级学生信息查询", width=16, height=1, font=("宋体", 15), command=lambda: banjichaxun())
    bu2.place(x=210, y=200)
    var2 = tk.StringVar()
    c1 = ttk.Combobox(rt4, textvariable=var2, width=8, font=("宋体", 20))
    c1['values'] = ("电子与信息工程学院", "机械工程学院", '数学学院')
    c1["state"] = "readonly"
    c1.current(0)
    c1.place(x=60, y=280)
    bu13 = tk.Button(rt4, text="学院学生信息查询", width=16, height=1, font=("宋体", 15), command=lambda: xueyuanchaxun())
    bu13.place(x=210, y=280)
    bu11 = tk.Button(rt4, text="全部学生成绩", width=22, height=1, font=("宋体", 20),command=lambda: table2('select * from score'))
    bu11.place(x=450, y=120)
    var11 = tk.StringVar()
    e11 = tk.Entry(rt4, textvariable=var11, width=10, font=("宋体", 20))
    e11.place(x=450, y=200)
    bu12 = tk.Button(rt4, text="班级学生成绩查询", width=16, height=1, font=("宋体", 15), command=lambda: banjichenji())
    bu12.place(x=600, y=200)
    var12 = tk.StringVar()
    e21 = tk.Entry(rt4, textvariable=var12, width=10, font=("宋体", 20))
    e21.place(x=450, y=280)
    bu13 = tk.Button(rt4, text="学生个人成绩查询", width=16, height=1, font=("宋体", 15), command=lambda: gerenchenji())
    bu13.place(x=600, y=280)
    var32 = tk.StringVar()
    e31 = tk.Entry(rt4, textvariable=var32, width=10, font=("宋体", 20))
    e31.place(x=60, y=360)
    bu33 = tk.Button(rt4, text="学生个人信息查询", width=16, height=1, font=("宋体", 15), command=lambda: gerenchaxun())
    bu33.place(x=210, y=360)
    var35 = tk.StringVar()
    e35 = tk.Entry(rt4, textvariable=var35, width=10, font=("宋体", 20))
    e35.place(x=450, y=360)
    bu35 = tk.Button(rt4, text="学生个人成绩录入", width=16, height=1, font=("宋体", 15), command=lambda: chenji())
    bu35.place(x=600, y=360)

    var34 = tk.StringVar()
    e34 = tk.Entry(rt4, textvariable=var34, width=10, font=("宋体", 20))
    e34.place(x=60, y=440)
    bu34 = tk.Button(rt4, text="学生个人信息修改", width=16, height=1, font=("宋体", 15), command=lambda: xinxixiugai1())
    bu34.place(x=210, y=440)
    var36 = tk.StringVar()
    e36 = tk.Entry(rt4, textvariable=var36, width=10, font=("宋体", 20))
    e36.place(x=450, y=440)
    bu36 = tk.Button(rt4, text="学生信息删除", width=16, height=1, font=("宋体", 15), command=lambda: delete())
    bu36.place(x=600, y=440)
    bu4 = tk.Button(rt4, text="修改密码", width=10, height=1, font=("宋体", 15), command=lambda: xiugaimima(ss))
    bu4.place(x=250, y=540)
    bu5 = tk.Button(rt4, text="安全退出", width=10, height=1, font=("宋体", 15), command=lambda: close())
    bu5.place(x=450, y=540)
    rt4.mainloop()

    return 0

# 登陆界面
rt = tk.Tk()
rt.title("学生管理系统登录")
rt.geometry('870x600')
rt.update()
curx = rt.winfo_width()
cury = rt.winfo_height()
scnx = rt.winfo_screenwidth()
scny = rt.winfo_screenheight()
tm = '%dx%d+%d+%d' % (curx, cury, (scnx - curx) / 2, (scny - cury) / 2)
rt.geometry(tm)
rt.resizable(False, False)

p1 = tk.PanedWindow(rt, width=870, height=120, bg='green')
p1.place(x=0, y=0)
b1 = tk.Label(rt, text="兰州城市学院学生管理信息系统", font=("宋体", 40), width=31, height=2, bg='#42b7d5')
b1.place(x=60, y=0)
imgla1 = tk.PhotoImage(file="001.gif")
b2 = tk.Label(rt, image=imgla1, width=90, height=110, bg='blue')
b2.place(x=0, y=0)
p1.add(b2)
p1.add(b1)

imgla2 = tk.PhotoImage(file="002.gif")
b3 = tk.Label(rt, image=imgla2, width=400, height=400)
b3.place(x=40, y=160)

p2 = tk.PanedWindow(rt, width=390, height=480, bg='#aad542')
p2.place(x=480, y=120)

var3 = tk.StringVar()
c1 = ttk.Combobox(p2, textvariable=var3, font=("宋体", 20))
c1['values'] = ("学生", "教师")
c1["state"] = "readonly"
c1.current(0)
c1.place(x=40, y=40)

b4 = tk.Label(p2, text="账号", font=("宋体", 20))
b4.place(x=40, y=120)
var1 = tk.StringVar()
e1 = tk.Entry(p2, textvariable=var1, width=15, font=("宋体", 20))
e1.place(x=120, y=120)

b5 = tk.Label(p2, text="密码", font=("宋体", 20))
b5.place(x=40, y=200)
var2 = tk.StringVar()
e2 = tk.Entry(p2, textvariable=var2, width=15, font=("宋体", 20), show='*')
e2.place(x=120, y=200)

bu1 = tk.Button(p2, text="登录", width=7, height=1, font=("华文行楷", 20), command=lambda: verify())
bu1.place(x=60, y=300)
bu2 = tk.Button(p2, text="注册", width=7, height=1, font=("华文行楷", 20), command=lambda: login())
bu2.place(x=200, y=300)
b5 = tk.Label(p2, text="注意：账号为学号或教师编号，由1~5位阿拉伯数字组成", font=("宋体", 10), width=45, height=2, bg='red')
b5.place(x=40, y=400)
rt.mainloop()