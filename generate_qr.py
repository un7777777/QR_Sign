#!/usr/bin/env python3
import qrcode
import sys

def generate_qr(url, output_file):
    img = qrcode.make(url)
    img.save(output_file)
    print(f"✅ QR code saved to: {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python generate_qr.py <url> <output_file>")
        sys.exit(1)

    form_url = sys.argv[1]
    output = sys.argv[2]
    generate_qr(form_url, output)

