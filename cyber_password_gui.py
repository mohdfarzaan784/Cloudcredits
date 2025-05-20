import tkinter as tk
import re
import random
import string
import pyperclip

def check_password_strength(event=None):
    password = entry.get()
    suggestions = []
    strength = ""
    recommended = ""

    if len(password) < 8:
        suggestions.append("⚠️ Use 8+ characters")
    if not re.search(r"[A-Z]", password):
        suggestions.append("⚠️ Add uppercase letters (A-Z)")
    if not re.search(r"[a-z]", password):
        suggestions.append("⚠️ Add lowercase letters (a-z)")
    if not re.search(r"\d", password):
        suggestions.append("⚠️ Add numbers (0-9)")
    if not re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>?,./]", password):
        suggestions.append("⚠️ Add special characters (!@#$...)")

    if len(suggestions) == 0:
        strength = "✅ Strong"
        color = "#00FF00"
    elif len(suggestions) <= 2:
        strength = "🟡 Medium"
        color = "#FFA500"
    else:
        strength = "❌ Weak"
        color = "#FF3333"

    result_label.config(text=f"🔐 Strength: {strength}", fg=color)
    suggestion_label.config(text="\n".join(suggestions))

    if strength != "✅ Strong":
        password_suggestion = generate_strong_password()
        recommended_label.config(text=f"🔁 Recommended: {password_suggestion}")
        copy_button.config(command=lambda: copy_password(password_suggestion))
    else:
        recommended_label.config(text="")
        copy_button.config(command=None)

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

def copy_password(password):
    pyperclip.copy(password)
    copy_button.config(text="✅ Copied!")

# GUI Setup
root = tk.Tk()
root.title("🧠 Cyber Password Tester")
root.geometry("600x480")
root.configure(bg="#0f1117")

font_heading = ("Consolas", 16, "bold")
font_body = ("Consolas", 11)

# UI Layout
tk.Label(root, text="Enter Your Password:", font=font_heading, fg="#00ffff", bg="#0f1117").pack(pady=10)
entry = tk.Entry(root, show="*", width=40, font=font_body, bg="#1a1c23", fg="#00ff00", insertbackground="white")
entry.pack()
entry.bind("<KeyRelease>", check_password_strength)

tk.Label(root, text="----------------------------------------------------", fg="#333", bg="#0f1117").pack(pady=5)

result_label = tk.Label(root, text="🔐 Strength: ", font=font_heading, bg="#0f1117", fg="#ffffff")
result_label.pack(pady=10)

suggestion_label = tk.Label(root, text="", font=font_body, justify="left", bg="#0f1117", fg="#00ff00", wraplength=550)
suggestion_label.pack(pady=5)

recommended_label = tk.Label(root, text="", font=font_body, bg="#0f1117", fg="#00cccc")
recommended_label.pack(pady=5)

copy_button = tk.Button(root, text="📋 Copy Password", font=font_body, bg="#222", fg="white", activebackground="#333")
copy_button.pack(pady=10)

tk.Label(root, text="🛡️ Designed for Cyber Security Projects", font=("Consolas", 10), fg="#555", bg="#0f1117").pack(side="bottom", pady=5)

root.mainloop()
