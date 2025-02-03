from google.colab import drive
drive.mount('/content/drive')

import easyocr
import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import shutil

image_path = "/content/drive/MyDrive/images.jpeg"
reader=easyocr.Reader(['en'], gpu=False)
result=reader.readtext(image_path)
print(result)

top_left=tuple(result[0][0][0])
bottom_right=tuple(result[0][0][2])
text=result[0][1]
confidence=result[0][2]
img = cv2.imread(image_path)
img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
font=cv2.FONT_HERSHEY_SIMPLEX
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

#Databse
conn = sqlite3.connect("ocr_results.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS ocr_results (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        text TEXT,
                        confidence REAL
                    )''')

cursor.execute("INSERT INTO ocr_results (text, confidence) VALUES (?, ?)", (text, confidence))
conn.commit()
conn.close()
print("OCR result saved to database!")
shutil.move("ocr_results.db", "/content/drive/MyDrive/ocr_results.db")
print("Database saved to Google Drive!")

#Data from Database

shutil.copy("/content/drive/MyDrive/ocr_results.db", "ocr_results.db")
conn = sqlite3.connect("ocr_results.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM ocr_results")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
