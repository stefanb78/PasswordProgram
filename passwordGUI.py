import tkinter as tk
window = tk.Tk()
window.geometry('400x150')
Label = tk.Label(window, text="Login System:").grid(row=0, column=0)
usernameLabel = tk.Label(window, text="Username:").grid(row=1, column=0)

usernameEntry = tk.Entry(window, textvariable=tk.StringVar())
usernameEntry.grid(row=1, column=1)

passwordLabel = tk.Label(window, text="Password:").grid(row=2, column=0)
passwordEntry = tk.Entry(window, textvariable=tk.StringVar())
passwordEntry.grid(row=2, column=1)

print(passwordEntry)

def getInput():
    
    a = usernameEntry.get()
    b = passwordEntry.get()
    global params
    params = [a, b]
    window.destroy
    print(params)
    
    return 
    
b = tk.Button(window, text = "Log in", command = getInput).grid(row=3, column=0)

print(passwordEntry)
print(usernameEntry)

window.mainloop()
