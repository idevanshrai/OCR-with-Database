# OCR Text Detection with Database

This project demonstrates Optical Character Recognition (OCR) using **EasyOCR** in **Google Colab**, with extracted text stored in an **SQLite database**.

## Features
- Uses **EasyOCR** for text detection.
- Processes images uploaded via **Google Drive**.
- Visualizes detected text using **OpenCV**.
- Stores detected text in an **SQLite database** for easy retrieval.
- Runs entirely in **Google Colab**, eliminating local setup requirements.

## Setup and Dependencies
To run this project, install the required dependencies in your Colab notebook using pip:

```sh
!pip install easyocr
!pip install opencv-python-headless
```

Other required libraries (**sqlite3**, **matplotlib**, **numpy**) come pre-installed in Google Colab.

## Uploading Files using Google Drive
Since Google Colab does not retain files after runtime termination, we use **Google Drive** to upload and access images.

### Steps to Attach Google Drive:
1. Mount Google Drive in your Colab session.
2. Upload the image to Google Drive and access it using the file path.

## Storing Detected Text in SQLite
SQLite is used to store extracted text for future access. The database is created dynamically within the Colab session.

### How the Database Works:
1. A table `ocr_results` is created with columns for `id`, `image_name`, and `detected_text`.
2. Detected text from the image is stored in this table.
3. The database file is temporary in Colab but can be downloaded for future use.

## Running OCR on Images
Once the image is uploaded, **EasyOCR** extracts text and **SQLite** stores it. Refer to `code.ipynb` for full implementation details.

## How to Run the Project in Google Colab
1. Open Google Colab ([Google Colab](https://colab.research.google.com/)).
2. Mount Google Drive as shown above.
3. Upload your image to Google Drive.
4. Install dependencies using `pip install`.
5. Run the script in `code.ipynb` to extract text and store it in SQLite.
6. Query the database to retrieve stored text.

## Output Example
The output image will display detected text with bounding boxes, while the detected text is also saved in an SQLite database.

---

### Future Improvements
- Support for multiple languages.
- Exporting stored text in different formats (CSV, JSON, etc.).
- Web-based UI for user-friendly text extraction.

**Contributions & feedback are welcome!** 🚀

