# Disease_solution_prediction MediAid - Disease Info Assistant (Excel + Voice/Image)
MediAid is a Python-based desktop application that helps users find information about diseases using text input, voice recognition, or image-based OCR. It utilizes a local Excel file (diseases_data.xlsx) as the data source, making it completely offline and privacy-preserving.

🚀 Features
🔍 Search for disease information by typing the name.

🎤 Voice-based search using microphone input.

🖼 Detect disease name from an image (e.g., prescription or note) using OCR.

📘 Displays symptoms, causes, prevention, and treatment for known diseases.

🧠 Fully offline — no internet required after setup.

🛠 Technologies Used
Tkinter - GUI framework

pandas - Excel data handling

speech_recognition - Voice input

pytesseract & Pillow - OCR from images

openpyxl - Excel engine for .xlsx

📂 Project Structure
bash
Copy
Edit
MediAid/
│
├── diseases_data.xlsx         # Disease database (Excel file)
├── mediAid_app.py             # Main application script
├── README.md                  # Documentation
📦 Installation Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/MediAid.git
cd MediAid
2. Install required packages
You can install the dependencies via pip:

bash
Copy
Edit
pip install pandas speechrecognition pillow pytesseract openpyxl
3. Install Tesseract-OCR (For Image Recognition)
Windows: Download from https://github.com/tesseract-ocr/tesseract

Add its path to environment variables or set it in the code:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
▶️ How to Run
bash
Copy
Edit
python mediAid_app.py
Then use the GUI to:

Type a disease name

Use microphone for voice input

Upload an image with disease name

📊 Data Format (diseases_data.xlsx)
Make sure your Excel file has these columns:

Disease	Symptoms	Causes	Prevention	Treatment

📝 Example Screenshot
(Add a screenshot here of the app UI if you want)

🤖 Future Improvements
Add support for multiple languages (voice & text).

Add spelling correction for more accurate search.

Use real-time camera feed for OCR input.

Export disease info as PDF or text.

🧑‍💻 Author
Sreenu Sreenu

📄 License
MIT License - feel free to use and modify
