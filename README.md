# QR_Sign

## Overview

This project provides a simple way to collect sign-in and sign-out data using Google Forms and Google Sheets.

Responses are stored automatically in a spreadsheet, so you can track arrival and departure times like a time clock.

## Usage
Run the following command in your terminal to generate a QR code that links to the Google Form:


``````
python generate_qr.py "https://docs.google.com/forms/d/e/1FAIpQLSe9pbj1XTVebFQGcyzUqZ9kA_LyCl73IqqsuUwkORYv-JHl1g/viewform" output.png
``````
Then scan the generated QR code with your phone to open the form.

Switch the URL to your own form, and change the output file name as needed.


### Link
Form URL: 
```
https://docs.google.com/forms/d/e/1FAIpQLSe9pbj1XTVebFQGcyzUqZ9kA_LyCl73IqqsuUwkORYv-JHl1g/viewform
```
Sheet URL: 
```
https://docs.google.com/spreadsheets/d/1_T2t0yBH_kDUyZKnGKiZk-lB_WAUVwGzB9MNgXPkcZ4/edit?resourcekey=&gid=1514144812#gid=1514144812
```