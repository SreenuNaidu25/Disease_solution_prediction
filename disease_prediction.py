import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
import speech_recognition as sr
from PIL import Image
import pytesseract

# Set tesseract path if needed:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class DiseaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MediAid - Disease Info Assistant (Excel + Voice/Image)")
        self.root.geometry("720x600")
        self.root.configure(bg="#f0f4f7")

        self.load_data()
        self.create_widgets()

    def load_data(self):
        try:
            self.data = pd.read_excel(r"C:\Users\sreen\OneDrive\Desktop\diseases_data.xlsx")
        except FileNotFoundError:
            messagebox.showerror("File Error", "diseases_data.xlsx not found.")
            self.data = pd.DataFrame()

    def create_widgets(self):
        tk.Label(self.root, text="🩺 Disease Solution Finder",
                 font=("Helvetica", 18, "bold"), bg="#f0f4f7").pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Arial", 14), width=40)
        self.entry.pack(pady=10)

        btn_frame = tk.Frame(self.root, bg="#f0f4f7")
        btn_frame.pack()

        tk.Button(btn_frame, text="Search 🔍", font=("Arial", 12),
                  command=self.search_disease, bg="#4caf50", fg="white").grid(row=0, column=0, padx=10)

        tk.Button(btn_frame, text="🎤 Voice Input", font=("Arial", 12),
                  command=self.voice_input, bg="#2196f3", fg="white").grid(row=0, column=1, padx=10)

        tk.Button(btn_frame, text="🖼 Image Recognition", font=("Arial", 12),
                  command=self.image_input, bg="#673ab7", fg="white").grid(row=0, column=2, padx=10)

        self.output_text = tk.StringVar()
        tk.Label(self.root, textvariable=self.output_text,
                 wraplength=680, justify="left", font=("Arial", 12),
                 bg="#f0f4f7", anchor="w").pack(pady=20, fill="both", expand=True)

    def search_disease(self, disease_name=None):
        if disease_name is None:
            disease_name = self.entry.get().strip().lower()
        else:
            disease_name = disease_name.strip().lower()

        if self.data.empty:
            self.output_text.set("Data not loaded.")
            return

        result = self.data[self.data['Disease'].str.lower() == disease_name]
        if not result.empty:
            info = result.iloc[0]
            self.output_text.set(
                f"💊 Disease: {info['Disease']}\n\n"
                f"🩺 Symptoms:\n{info['Symptoms']}\n\n"
                f"📌 Causes:\n{info['Causes']}\n\n"
                f"🛡 Prevention:\n{info['Prevention']}\n\n"
                f"💉 Treatment:\n{info['Treatment']}"
            )
        else:
            self.output_text.set("Disease not found.")

    def voice_input(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                self.output_text.set("Listening... Please speak the disease name.")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, text)
                self.search_disease(text)
        except sr.UnknownValueError:
            self.output_text.set("Could not understand voice input.")
        except sr.RequestError:
            self.output_text.set("Could not connect to recognition service.")
        except Exception as e:
            self.output_text.set(f"Voice input failed: {e}")

    def image_input(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            try:
                image = Image.open(file_path)
                text = pytesseract.image_to_string(image)
                disease_name = text.strip().split()[0]  # Try to extract first word
                self.entry.delete(0, tk.END)
                self.entry.insert(0, disease_name)
                self.search_disease(disease_name)
            except Exception as e:
                self.output_text.set(f"Failed to read image: {e}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DiseaseApp(root)
    root.mainloop()
