# QR_Sign

## Overview

This project provides a simple way to collect sign-in and sign-out data using **Google Forms** and **Google Sheets**. Parents can scan a QR code on Android or iOS devices to open the form. Responses are stored automatically in a spreadsheet, so you can track arrival and departure times like a time clock.

## Setup Steps

1. **Create a Google Form**
   - Go to [Google Forms](https://forms.google.com).
   - Add the following fields (English interface):
     - `Parent Name` – Short answer.
     - `Child Name` – Short answer (optional).
     - `Action` – Dropdown with options `Sign In` and `Sign Out`.
   - Ensure "Collect email addresses" is **off** unless required.
   - Link the form to a Google Spreadsheet via **Responses → Link to Sheets**.

2. **Generate the QR Code**
   - After the form is ready, copy its **public link**.
   - Ensure the link ends with `/viewform` so it opens the online questionnaire directly. Scanning the QR code will take parents straight to this form.
   - You can use any online QR generator or run the provided script:

     ```bash
     python3 generate_qr.py "FORM_LINK" output.png
     ```

   - The script downloads a QR image using the Google Chart API and saves it as `output.png`.
   - Print or display the generated QR code for parents to scan.

3. **Parents Sign In/Out**
   - Parents scan the QR code with their phone's camera.
   - Scanning the code automatically opens the online questionnaire in their browser.
   - The form opens in the browser (works on both Android and iOS).
   - They fill in their name, child name (if any), choose **Sign In** or **Sign Out**, and submit.
   - Each response is stored in the linked spreadsheet with a timestamp.

4. **Reviewing Data**
   - Open the linked Google Sheet to see all sign-in and sign-out records.
   - You can analyze times or create summaries directly in the sheet.

## QR Code Script

The repository includes `generate_qr.py` for convenience. It fetches a QR image from the Google Chart API. Internet access is required when running the script.

```bash
python3 generate_qr.py "https://example.com/my-form" qr.png
```

This will save a 300×300 QR code image as `qr.png`.

