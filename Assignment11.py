import tkinter as tk
from tkinter import ttk
import webbrowser

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    course = course_combobox.get()
    source = source_combobox.get()

    faq_urls = {
        "instagram_ads": "https://example.com/faq/instagram_ads",
        "youtube_ads": "https://example.com/faq/youtube_ads",
        "other": "https://example.com/faq/default",
    }

    faq_page_url = faq_urls.get(source, "https://example.com/faq/default")

    webbrowser.open(faq_page_url)


root = tk.Tk()
root.title("Course Inquiry Form")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Select a Course:").pack()
course_combobox = ttk.Combobox(root, values=["Course 1", "Course 2", "Course 3"])
course_combobox.pack()

tk.Label(root, text="Where did you hear about us?").pack()
source_combobox = ttk.Combobox(root, values=["Instagram Ads", "YouTube Ads", "Other"])
source_combobox.pack()

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

root.mainloop()
