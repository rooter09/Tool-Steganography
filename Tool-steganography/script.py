import PySimpleGUI as sg
from PIL import Image
import numpy as np
from pydub import AudioSegment
import wave
from scipy.io import wavfile


# Function to embed message in image (unchanged)
def embed_message_in_image(image_path, message, output_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    
    data = np.array(image)
    message += '\0'  # Null character to indicate the end of the message
    binary_message = ''.join(format(ord(i), '08b') for i in message)

    data_flat = data.flatten()
    for i in range(len(binary_message)):
        data_flat[i] = (data_flat[i] & 0xFE) | int(binary_message[i])

    data = data_flat.reshape(image.size[1], image.size[0], 3)
    encoded_image = Image.fromarray(data)
    encoded_image.save(output_path)

# Function to extract message from image
def extract_message_from_image(image_path):
    image = Image.open(image_path)
    data = np.array(image)

    # Flatten the image data and read the LSB of each pixel
    binary_message = ''
    for pixel in data.flatten():
        binary_message += str(pixel & 1)  # Get the least significant bit

    # Split the binary message into chunks of 8 bits (1 byte)
    binary_message = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]

    # Convert the binary chunks back to characters
    message = ''.join(chr(int(i, 2)) for i in binary_message)

    # Remove the null-terminator to get the original message
    return message.split('\0')[0]  # Split at null character and return the part before it

# Create UI layout (same as previous)
layout = [
    [sg.Text("Steganography Tool - Embed and Extract Messages from Images or Audio")],
    [sg.Text("Select Image or Audio File:"), sg.Input(), sg.FileBrowse(key="file_path")],
    [sg.Text("Enter Message:"), sg.InputText(key="message")],
    [sg.Button("Embed Message"), sg.Button("Extract Message"), sg.Button("Save Image")],
    [sg.Text("Output:"), sg.Multiline("", size=(50, 10), key="output")],
]

# Create the window
window = sg.Window("Steganography Tool", layout)

# Event loop
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == "Embed Message":
        file_path = values["file_path"]
        message = values["message"]
        if file_path and message:
            if file_path.lower().endswith(('png', 'jpg', 'jpeg')):
                output_image_path = sg.popup_get_file("Save Encoded Image", save_as=True, file_types=(("PNG Files", "*.png"), ("JPEG Files", "*.jpg")))
                if output_image_path:
                    embed_message_in_image(file_path, message, output_image_path)
                    window["output"].update(f"Message successfully embedded in image. Saved to: {output_image_path}")
            elif file_path.lower().endswith(('wav',)):
                output_audio_path = sg.popup_get_file("Save Encoded Audio", save_as=True, file_types=(("WAV Files", "*.wav"),))
                if output_audio_path:
                    embed_message_in_audio(file_path, message, output_audio_path)
                    window["output"].update(f"Message successfully embedded in audio. Saved to: {output_audio_path}")
            else:
                window["output"].update("Invalid file format. Please choose an image or audio file.")

    elif event == "Extract Message":
        file_path = values["file_path"]
        if file_path:
            if file_path.lower().endswith(('png', 'jpg', 'jpeg')):
                extracted_message = extract_message_from_image(file_path)
                window["output"].update(f"Extracted message: {extracted_message}")
            elif file_path.lower().endswith(('wav',)):
                extracted_message = extract_message_from_audio(file_path)
                window["output"].update(f"Extracted message: {extracted_message}")
            else:
                window["output"].update("Invalid file format. Please choose an image or audio file.")

    elif event == "Save Image":
        file_path = values["file_path"]
        if file_path.lower().endswith(('png', 'jpg', 'jpeg')):
            save_path = sg.popup_get_file("Save Image As", save_as=True, file_types=(("PNG Files", "*.png"), ("JPEG Files", "*.jpg")))
            if save_path:
                image = Image.open(file_path)
                image.save(save_path)
                window["output"].update(f"Image saved to: {save_path}")
        else:
            window["output"].update("Please select an image file to save.")

window.close()
