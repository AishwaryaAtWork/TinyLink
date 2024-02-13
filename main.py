import customtkinter as ctk
import pyshorteners as pshort

def shorten():
    shortener = pshort.Shortener()
    short_url = shortener.tinyurl.short(longUrl_entry.get())
    shortUrl_entry.insert(0, short_url)

def clear():
    longUrl_entry.insert(0, "")
    shortUrl_entry.insert(0, "")

root = ctk.CTk()
root.geometry("750x450")
root.title("TinyLink - URL Link Shortener App")

longUrl_label = ctk.CTkLabel(root, text="Long Url", font=ctk.CTkFont(size=18, weight="bold"))
longUrl_label.pack(padx=10, pady=(50,10))

longUrl_entry = ctk.CTkEntry(root, placeholder_text="Enter Long Url", width=500)
longUrl_entry.pack(padx=10)

shortUrl_label = ctk.CTkLabel(root, text="Short Url", font=ctk.CTkFont(size=18, weight="bold"))
shortUrl_label.pack(padx=10, pady=(25,10))

shortUrl_entry = ctk.CTkEntry(root, placeholder_text="Resulting Short Url", width=500)
shortUrl_entry.pack(padx=10)

shortButton = ctk.CTkButton(root, text="Convert to short url", width=500, font=ctk.CTkFont(size=15), command=shorten)
shortButton.pack(pady=(30,10))

clearButton = ctk.CTkButton(root, text="Clear the enteries", width=500, font=ctk.CTkFont(size=15), command=clear)
clearButton.pack(pady=10)

root.mainloop()