import customtkinter as ctk
import pyshorteners as pshort

def shorten():
    shortener = pshort.Shortener()
    short_url = shortener.tinyurl.short(longUrl_entry.get())
    shortUrl_entry.insert(0, short_url)

def clear():
    longUrl_entry.delete(0, ctk.END)
    shortUrl_entry.delete(0, ctk.END)

root = ctk.CTk()
root.geometry("750x450")
root.title("TinyLink - URL Link Shortener App")
root.config(background="#edeaea")

title_label = ctk.CTkLabel(root, text="TinyLink", font=ctk.CTkFont(size=28, weight="bold" ), text_color='#088ccd')
title_label.pack(pady=(30,0))

text_label = ctk.CTkLabel(root, text="Makes long url links to short url links", font=ctk.CTkFont(size=15, weight='bold'))
text_label.pack(pady=(0,20))

# Long URL Label and Entry
longUrl_frame = ctk.CTkFrame(root, bg_color='#edeaea')
longUrl_frame.pack(pady=(20,30))

longUrl_label = ctk.CTkLabel(longUrl_frame, text="Long Url", font=ctk.CTkFont(size=18))
longUrl_label.pack(side="left", padx=(5,0))

longUrl_entry = ctk.CTkEntry(longUrl_frame, placeholder_text="Enter Long Url", width=400, border_color='#088ccd')
longUrl_entry.pack(side="right", padx=(10, 0))

# Short URL Label and Entry
shortUrl_frame = ctk.CTkFrame(root, width=300)
shortUrl_frame.pack()

shortUrl_label = ctk.CTkLabel(shortUrl_frame, text="Short Url", font=ctk.CTkFont(size=18))
shortUrl_label.pack(side="left", padx=(5,0))

shortUrl_entry = ctk.CTkEntry(shortUrl_frame, placeholder_text="Resulting Short Url", width=400, border_color='#088ccd')
shortUrl_entry.pack(side="right", padx=(10, 0))

# Buttons
button_frame = ctk.CTkFrame(root, bg_color='#edeaea')
button_frame.pack(pady=30)

shortButton = ctk.CTkButton(button_frame, text="Convert to short url", width=25, font=ctk.CTkFont(size=20), text_color='#fff', command=shorten)
shortButton.pack(side="left", padx=(0, 10))

clearButton = ctk.CTkButton(button_frame, text="Clear the entries", width=25, font=ctk.CTkFont(size=20), text_color="#fff", command=clear)
clearButton.pack(side="right", padx=(10, 0))

root.mainloop()