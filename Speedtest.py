from tkinter import *
from tkinter import ttk
import speedtest_cli
import threading

root = Tk()
root["bg"] = "#fafafa"
root.geometry("300x400")
root.title("Speedtest")
root.iconbitmap("icon.ico")
root.resizable(False, False)
style = ttk.Style()
style.configure("TButton", font=("Comic Sans MS", 20))

#Start speedtest
def speedtest():
    downloadText.config(text="Download Speed:\n-")
    uploadText.config(text="Upload Speed:\n-")
    pingText.config(text="Ping:\n-")
    st = speedtest_cli.Speedtest()
    errorText.place_forget()
    analyzingText.place(anchor=CENTER, relx=0.5, rely=0.92)
    downloadSpeed = round(st.download() / (10 ** 6), 2)
    uploadSpeed = round(st.upload() / (10 ** 6), 2)
    pingSpeed = round(st.results.ping)
    downloadText.config(text="Download Speed:\n" + str(downloadSpeed) + " Mbps")
    uploadText.config(text="Upload Speed:\n" + str(uploadSpeed) + " Mbps")
    pingText.config(text="Ping:\n" + str(pingSpeed) + " Ms")
    analyzingText.place_forget()

#Start speedtest with checking on errors
def speedtestChecked():
    try:
        speedtest()
    except Exception:
        analyzingText.place_forget()
        errorText.place(anchor=CENTER, relx=0.5, rely=0.92)

def startSpeedtestThread():
    speedtestThread = threading.Thread(target=speedtestChecked)
    speedtestThread.start()

#GUI objects
speedtestButton = ttk.Button(root, text="Start Speedtest", style="TButton", command=startSpeedtestThread)
speedtestButton.pack(side=BOTTOM, pady=60)
analyzingText = Label(text="Analyzing...", bg="#fafafa", font=("Comic Sans MS", 17))
errorText = Label(text="Error occurred!", bg="#fafafa", font=("Comic Sans MS", 17), fg="#a83636")
downloadText = Label(text="Download Speed:\n-", bg="#fafafa", font=("Comic Sans MS", 17))
uploadText = Label(text="Upload Speed:\n-", bg="#fafafa", font=("Comic Sans MS", 17))
pingText = Label(text="Ping:\n-", bg="#fafafa", font=("Comic Sans MS", 17))
downloadText.place(anchor=CENTER, relx=0.5, rely=0.13)
uploadText.place(anchor=CENTER, relx=0.5, rely=0.35)
pingText.place(anchor=CENTER, relx=0.5, rely=0.57)

root.mainloop()