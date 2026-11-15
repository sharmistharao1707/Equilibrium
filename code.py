import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import date

FILENAME = "mood_data.csv"

# Create CSV file with headers if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Mood", "Hours"])

# Function to save data
def save_data():
    mood = mood_var.get()
    hours = hours_entry.get()
    try:
        hours_float = float(hours)
        with open(FILENAME, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date.today(), mood, hours_float])
        messagebox.showinfo("Saved", "Your data has been saved!")
        hours_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for hours.")

# Function to analyze data
def analyze_data():
    mood_totals = {}
    mood_counts = {}
    try:
        with open(FILENAME, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                mood = row["Mood"]
                hours = float(row["Hours"])
                mood_totals[mood] = mood_totals.get(mood, 0) + hours
                mood_counts[mood] = mood_counts.get(mood, 0) + 1

        result_text = ""
        for mood in mood_totals:
            avg = mood_totals[mood] / mood_counts[mood]
            result_text += f"{mood}: {avg:.2f} hrs\n"

        if result_text == "":
            result_text = "No data available"
        result_label.config(text=result_text)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to analyze data: {e}")

# GUI setup
app = tk.Tk()
app.title("Mood → Productivity Tracker")
app.geometry("350x350")

tk.Label(app, text="Select Mood").pack(pady=5)
mood_var = tk.StringVar()
mood_var.set("Happy")
mood_menu = tk.OptionMenu(app, mood_var, "Happy", "Neutral", "Stressed", "Tired")
mood_menu.pack()

tk.Label(app, text="Study Hours").pack(pady=5)
hours_entry = tk.Entry(app)
hours_entry.pack()

tk.Button(app, text="Save Data", command=save_data).pack(pady=10)
tk.Button(app, text="Analyze Productivity", command=analyze_data).pack(pady=10)

result_label = tk.Label(app, text="", justify="left")
result_label.pack(pady=10)

app.mainloop()