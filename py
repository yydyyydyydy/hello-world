import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import Menu
import ctypes as C
import tkinter.scrolledtext as tkst
from ctypes.util import find_library
import tkinter.messagebox




#파일 열기 함수
def openfile():
    filename = filedialog.askopenfilename(initialdir = "C:/Users/PC02/source/repos/pysetup/pysetup", title = "파일을 선택해주세요", filetypes = (('RAW 파일','*.RAW'),('모든 파일',"*.*"))) #filename = 파일의 경로
    refilename = filename.replace('/', '\\')
    global bname
    bname = refilename.encode('utf-8')

    mid = Mid()

    

  

def clickOK():

    print(Margin)
    value = 2
    IEEE = C.CDLL('IEEE')
    name = C.c_char_p(bname)
    tole = C.c_double(Margin.get())
    solu = C.c_int(value)
    
    c_main = IEEE['main']
    IEEE.main.argtypes = [C.c_double, C.c_char_p, C.c_int]
    test =c_main(tole, name, solu)
    print(test)
    txt = open("Result.txt", 'r')
    data = txt.read()
    scrt.insert(tk.INSERT, data)                   
    scrt.see(tk.END)


    
    #tk.messagebox.showwarning("Warning","파일이 없습니다.")

    


if __name__ == '__main__':
    #제목과 사이즈
    win = tk.Tk()
    win.title("Power Flow Simulator")
    win.resizable(True, True)
    win.geometry("850x600+200+200")                     

    #내부 라벨
    labelGender = ttk.Label(win, text="Method:")   
    labelGender.grid(column=0, row=0)               
    labelMargin = ttk.Label(win, text="convergence:")         
    labelMargin.grid(column=1, row=0)                  

    #Method 형식
    Method = tk.StringVar()                                         
    MethodCombo = ttk.Combobox(win, width=80, textvariable=Method)   
    MethodCombo['values'] = ("Gauss-Seidel method", "Newton-Raphson method")                      
    MethodCombo.grid(column=0, row=1)
    MethodCombo.current(0)


    #계산 내용창
    scrt = tkst.ScrolledText(win, width=100, height=40, wrap=tk.WORD)
    scrt.grid(column=0, row=2, columnspan=3)
    scrt.focus_set()                                                
    
#메뉴창 형식, 파일
menu_bar = Menu(win)
file_menu = Menu(menu_bar, tearoff = 0)
file_menu.add_command(label = '파일 열기', command = openfile)
file_menu.add_separator()
file_menu.add_command(label = '종료', command = win.quit)
menu_bar.add_cascade(label = '파일', menu = file_menu)

#메뉴창 형식, 도움말
file_menu2 = Menu(menu_bar, tearoff = 0)
file_menu.add_separator()
file_menu2.add_command(label = '정보')
menu_bar.add_cascade(label = '도움말', menu = file_menu2)
win.config(menu = menu_bar)

class Mid():
    def __init__(self):

        win = tk.Tk()   

        global Margin
        global value

        # 탭 설정    
        win.title("계산 설정")  
        tabControl = ttk.Notebook(win)          
        tab1 = ttk.Frame(tabControl)            
        tabControl.add(tab1, text='오차 및 계산방법')      
        tabControl.pack(expand=1, fill="both")  

         #----------------------- 오차 라벨---------------------------------
        mighty = ttk.LabelFrame(tab1, text=' 오차 ')
        mighty.grid(column=0, row=0, padx=8, pady=4)

        
        Margin = tk.DoubleVar()
        MarginEntered = ttk.Entry(mighty, width=20, textvariable=Margin)  
        MarginEntered.grid(column=1, row=0, sticky=tk.W)
    

        # 오차 = : 라벨창
        a_label = ttk.Label(mighty, text="오차 : ")
        a_label.grid(column=0, row=0)

        #----------------------- 계산방식 라벨---------------------------------

        mighty = ttk.LabelFrame(tab1, text=' 계산 방식 ')
        mighty.grid(column=1, row=0, padx=8, pady=4)

        # 각 방식 라디오 버튼
        radVar = tk.IntVar()
        rad1 = tk.Radiobutton(mighty, text= "가우스 자이델 방식" , variable=radVar, value=1)
        rad1.grid(column=0, row=0, sticky=tk.W)   

        rad2 = tk.Radiobutton(mighty, text= "뉴턴 랩슨 방식" , variable=radVar, value=2)
        rad2.grid(column=1, row=0, sticky=tk.W)  

        action = ttk.Button(mighty, text="Calculate", command=clickOK)    
        action.grid(column=2, row=0)


        win.mainloop()
        


tk.mainloop()
