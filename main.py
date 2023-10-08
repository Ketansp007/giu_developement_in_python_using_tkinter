from tkinter import  *
from NLPNowDB import *
from tkinter import  messagebox
from myapi import *

class NLPNow:

    def __init__(self):
        self.dbo = Database()
        self.root = Tk()
        self.api_call = MyApi()
        self.root.title('NLPNow')
        self.root.wm_iconbitmap('Resources/favicon.ico')
        self.root.geometry('350x530')
        self.root.configure(bg='#cb202d')
        self.login_page()
        self.root.mainloop()


    def login_page(self):

        self.clear_page()

        heading = Label(self.root,text='NLPNow',bg='#cb202d',fg ='white')
        heading.pack(pady= (30,30))
        heading.configure(font=('okra',30,'bold'))

        label1 = Label(self.root,text='Enter Your Email',bg='#cb202d',fg ='white')
        label1.pack(pady = (10,10))
        label1.configure(font=('okra',15,'bold'))

        self.log_email = Entry(self.root,width = 50)
        self.log_email.pack(pady = (5,10),ipady = 5)

        label2 = Label(self.root, text='Enter Password', bg='#cb202d', fg='white')
        label2.pack(pady=(10, 10))
        label2.configure(font=('okra', 15, 'bold'))

        self.log_pass = Entry(self.root, width=50,show='*')
        self.log_pass.pack(pady=(5, 10), ipady=5)

        button1 = Button(self.root,text = 'Login',width = 25, height=2,bd = 5 ,highlightcolor = '#cb202d',command=self.login)
        button1.pack(pady=(25,10))

        label3 = Label(self.root, text='Not a Member?', bg='#cb202d', fg='white')
        label3.pack(pady=(25, 10))
        label3.configure(font=('okra', 15, 'bold'))

        button2 = Button(self.root, text='Register Now', width=15, height=1,bd = 5 ,highlightcolor = '#cb202d',command=self.register_page)
        button2.pack(pady=(5, 10))

    def clear_page(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def register_page(self):
        self.clear_page()

        heading = Label(self.root, text='NLPNow', bg='#cb202d', fg='white')
        heading.pack(pady=(20, 20))
        heading.configure(font=('okra', 30, 'bold'))

        label0 = Label(self.root, text='Enter Your Name', bg='#cb202d', fg='white')
        label0.pack(pady=(10, 10))
        label0.configure(font=('okra', 15, 'bold'))

        self.reg_name = Entry(self.root, width=50)
        self.reg_name.pack(pady=(2, 10), ipady=5)

        label1 = Label(self.root, text='Enter Your Email', bg='#cb202d', fg='white')
        label1.pack(pady=(10, 10))
        label1.configure(font=('okra', 15, 'bold'))

        self.reg_email = Entry(self.root, width=50)
        self.reg_email.pack(pady=(2, 10), ipady=5)

        label2 = Label(self.root, text='Enter Password', bg='#cb202d', fg='white')
        label2.pack(pady=(10, 10))
        label2.configure(font=('okra', 15, 'bold'))

        self.reg_pass = Entry(self.root, width=50, show='*')
        self.reg_pass.pack(pady=(2, 10), ipady=5)

        button1 = Button(self.root, text='Register', width=25, height=2,bd = 5 ,highlightcolor = '#cb202d',command=self.registration)
        button1.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a Member?', bg='#cb202d', fg='white')
        label3.pack(pady=(10, 10))
        label3.configure(font=('okra', 15, 'bold'))

        button2 = Button(self.root, text='Login Now', width=15, height=1,bd = 5 ,highlightcolor = '#cb202d' ,command=self.login_page)
        button2.pack(pady=(1, 10))

    def registration(self):
        name = self.reg_name.get()
        email = self.reg_email.get()
        pass1 = self.reg_pass.get()

        res = self.dbo.add_data(name,email,pass1)
        if res == 1:
            messagebox.showinfo('Success','Registration Successful!!')
            self.clear_page()
            self.login_page()
        else:
            messagebox.showerror('Error','Email already exists!')

    def login(self):
        email = self.log_email.get()
        pass1 = self.log_pass.get()

        res = self.dbo.search(email,pass1)
        if res == 0:
            messagebox.showerror('Error', 'Incorrect Password!')
        elif res == -1:
            messagebox.showerror('Error', 'User Not Found! Please Register to continue.')
        else:
            messagebox.showinfo('Success', 'Login Successful!!')
            self.home_page()

    def home_page(self):
        self.clear_page()
        heading = Label(self.root, text='NLPNow',bg='#cb202d', fg='white')
        heading.pack(pady=(20, 20))
        heading.configure(font=('okra', 30, 'bold'))

        button0 = Button(self.root, text='Sentiment Analysis', width=20, height=2,bd = 5 ,highlightcolor = '#cb202d', command =self.sentiment_analysis_page)
        button0.pack(pady=(25, 10))
        button0.configure(font='okra',height=1)

        button1 = Button(self.root, text='Named Entity Recognition',width=25, height=2,bd = 5 ,highlightcolor = '#cb202d', command=self.name_entity_page)
        button1.pack(pady=(25, 10))
        button1.configure(font='okra', height=1)

        button2 = Button(self.root, text='Emotion Prediction', width=25, height=2,bd = 5 ,highlightcolor = '#cb202d', command=self.emotion_prediction_page)
        button2.pack(pady=(25, 10))
        button2.configure(font='okra', height=1)

        button3 = Button(self.root, text='Logout?', width=15, height=1, bd=5, highlightcolor='#cb202d',
                         command=self.login_page)
        button3.pack(pady=(70, 10))

    def sentiment_analysis_page(self):
        self.clear_page()

        heading = Label(self.root, text='NLPNow', bg='#cb202d', fg='white')
        heading.pack(pady=(20, 20))
        heading.configure(font=('okra', 30, 'bold'))

        heading1 = Label(self.root, text='Sentiment Analysis', bg='#cb202d', fg='white')
        heading1.pack(pady=(10, 10))
        heading1.configure(font=('okra', 20, 'bold'))

        label1 = Label(self.root, text='Enter the Text', bg='#cb202d', fg='white')
        label1.pack(pady=(10, 10))
        label1.configure(font=('okra', 15, 'bold'))

        self.sentiment_data = Entry(self.root, width=50)
        self.sentiment_data.pack(pady=(2, 10), ipady=10)

        button1 = Button(self.root, text='Analyze Sentiment', width=25, height=2, bd=5, highlightcolor='#cb202d',
                         command=self.analysis)
        button1.pack(pady=(25, 10))

        self.sentiment_result = Label(self.root, text='', bg='#cb202d', fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('okra', 15, 'bold'))

        button2 = Button(self.root, text='Go to Homepage', width=15, height=1, bd=5, highlightcolor='#cb202d',
                         command=self.home_page)
        button2.pack(pady=(15, 10))

    def analysis(self):

        res = self.api_call.sentiment_analysis(self.sentiment_data.get())
        txt = ''
        for i in res['sentiment']:
            txt = txt + i + ' -> ' + str(res['sentiment'][i]) + '\n'
        self.sentiment_result['text'] = txt

    def name_entity_page(self):
        self.clear_page()

        heading = Label(self.root, text='NLPNow', bg='#cb202d', fg='white')
        heading.pack(pady=(20, 20))
        heading.configure(font=('okra', 30, 'bold'))

        heading1 = Label(self.root, text='Name Entity Recognition', bg='#cb202d', fg='white')
        heading1.pack(pady=(10, 10))
        heading1.configure(font=('okra', 20, 'bold'))

        label1 = Label(self.root, text='Enter the Text', bg='#cb202d', fg='white')
        label1.pack(pady=(10, 10))
        label1.configure(font=('okra', 15, 'bold'))

        self.entity_data = Entry(self.root, width=50)
        self.entity_data.pack(pady=(2, 10), ipady=10)

        button1 = Button(self.root, text='Recognize Entity', width=25, height=2, bd=5, highlightcolor='#cb202d',
                         command=self.name_entity)
        button1.pack(pady=(20, 10))

        self.entity_result = Label(self.root, text='', bg='#cb202d', fg='white')
        self.entity_result.pack(pady=(5,5))
        self.entity_result.configure(font=('okra', 12, 'bold'))

        button2 = Button(self.root, text='Go to Homepage', width=15, height=1, bd=5, highlightcolor='#cb202d',
                         command=self.home_page)
        button2.pack(pady=(5, 10))

    def name_entity(self):
        res = self.api_call.name_entity(self.entity_data.get())
        txt =""
        for i in res['entities']:
            txt += i['category']+' -> '+i['name'] +'\n'
        self.entity_result['text'] = txt

    def emotion_prediction_page(self):
        self.clear_page()

        heading = Label(self.root, text='NLPNow', bg='#cb202d', fg='white')
        heading.pack(pady=(20, 20))
        heading.configure(font=('okra', 30, 'bold'))

        heading1 = Label(self.root, text='Emotion Prediction', bg='#cb202d', fg='white')
        heading1.pack(pady=(10, 10))
        heading1.configure(font=('okra', 20, 'bold'))

        label1 = Label(self.root, text='Enter the Text', bg='#cb202d', fg='white')
        label1.pack(pady=(10, 10))
        label1.configure(font=('okra', 15, 'bold'))

        self.emotion_data = Entry(self.root, width=50)
        self.emotion_data.pack(pady=(2, 10), ipady=10)

        button1 = Button(self.root, text='Predict Emotion', width=25, height=2, bd=5, highlightcolor='#cb202d',
                         command=self.predict_emotion)
        button1.pack(pady=(20, 10))

        self.emotion_result = Label(self.root, text='', bg='#cb202d', fg='white')
        self.emotion_result.pack(pady=(10,10))
        self.emotion_result.configure(font=('okra', 15, 'bold'))

        button2 = Button(self.root, text='Go to Homepage', width=15, height=1, bd=5, highlightcolor='#cb202d',
                         command=self.home_page)
        button2.pack(pady=(20, 10))

    def predict_emotion(self):
        res = self.api_call.emotion_rec(self.emotion_data.get())

        txt = ""
        n = 0
        for i in res['emotion']:
            if (res['emotion'][i]) > n:
                n = res['emotion'][i]
                txt = i
        self.emotion_result['text'] = txt


nlp1 = NLPNow()