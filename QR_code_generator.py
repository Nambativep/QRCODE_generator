# Convert a text or a link to a QR_CODE IN PYTHON USING LIBRARIES
# Install all the libraries needed
# Create a function that collects a text and convert it to a QRCODE
# Save the QRCODE as an image
# Create a function that takes the image and converts its to a text
# Run the function


#import qr
#import redis
import qrcode
#from django.utils import text
from qr import add_data
import make


def generate_qrcode(text):
    # Create a variable qr and store
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=40,
        border=6,
    )

    qr = add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("img002.png")


""""
Ask the user to input their own URL and let the machine generate
the QRCODE based on the URL
"""

url = input("Enter your URL: ")
generate_qrcode(url)
