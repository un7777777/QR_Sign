#!/usr/bin/env python3
"""Simple script to download a QR code for a Google Form URL.

Usage:
    python3 generate_qr.py FORM_URL [output.png]

The script uses the Google Chart API to generate a 300x300 QR image.
Internet access is required.
"""
import sys
import urllib.parse
import urllib.request


def generate_qr(form_url: str, output_file: str = "form_qr.png") -> None:
    params = {
        "chs": "300x300",
        "cht": "qr",
        "chl": form_url,
    }
    url = "https://chart.googleapis.com/chart?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url) as resp:
        data = resp.read()
    with open(output_file, "wb") as f:
        f.write(data)
    print(f"Saved QR code to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate_qr.py FORM_URL [output.png]")
        sys.exit(1)
    form_url = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else "form_qr.png"
    generate_qr(form_url, output)
