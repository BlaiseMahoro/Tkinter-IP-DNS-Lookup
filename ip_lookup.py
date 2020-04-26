import requests
from tkinter import *
from tkinter import ttk

def get_data():
    try:
        serch_txt = query.get()
        data_json = requests.get("https://salty-journey-20244.herokuapp.com/ip_api?address="+serch_txt).json()
        status = data_json['status']
        if status =="fail":
            err_label.config(text="Invalid input")
            err_label.update()
            ip_label.config(text="")
            ip_label.update()
            tz_label.config(text="")
            tz_label.update()
            country_label.config(text="")
            country_label.update()
            return 
        ip=data_json['query']
        country = data_json['country']
        timezone = data_json['timezone']
        err_label.config(text="")
        err_label.update()
        ip_label.config(text=ip)
        ip_label.update()
        tz_label.config(text=timezone)
        tz_label.update()
        country_label.config(text=country)
        country_label.update()
    except ValueError:
        pass


root = Tk()
root.title("IP/DNS LookUp")
root.geometry("500x300")
mainframe = ttk.Frame(root, padding="6 6 24 24")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

query = StringVar()


query_entry = ttk.Entry(mainframe, width=20, textvariable=query)
query_entry.grid(column=1, row=1, sticky=(W, E))
query_entry.focus()
ttk.Button(mainframe, text="Search", command=get_data).grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="IP:").grid(column=1, row=2, sticky=W)
ip_label = ttk.Label(mainframe, text="")
ip_label.grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="Country:").grid(column=1, row=3, sticky=W)
country_label = ttk.Label(mainframe, text="")
country_label.grid(column=2, row=3, sticky=W)
ttk.Label(mainframe, text="Timezone:").grid(column=1, row=4, sticky=W)
tz_label = ttk.Label(mainframe, text="")
tz_label.grid(column=2, row=4, sticky=W)
err_label=ttk.Label(mainframe, text="", background="red")
err_label.grid(column=1, row=5, sticky=W)
root.bind('<Return>', get_data)
#get_data('google.com')
#get_data('google.com')
root.mainloop()