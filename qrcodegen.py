import qrcode
import os
# Function to validate the QR code version
def validate_version(version):
    if not (1 <= version <= 40):
        raise ValueError("Version must be an integer between 1 and 40.")

# Data to encode
data = input('Enter the Data: ')

try:
    version = int(input('Enter the version (complexity) [1-40]: '))  # max value 40
    validate_version(version)
    box_size = int(input('Enter the Box size: '))  # max value 10

    # Creating an instance of QRCode class
    qr = qrcode.QRCode(version=version, box_size=box_size, border=5)

    # Adding data to the instance 'qr'
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    # Save the QR code image
    file_name = input("Name it as: ")  # image name
    img.save(f'{file_name}.png')

    print('QR code generated and saved in the gallery')

except ValueError as e:
    print(f"Value Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
