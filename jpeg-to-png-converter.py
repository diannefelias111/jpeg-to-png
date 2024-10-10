import os
from PIL import Image

def is_valid_jpeg(file_path):
    """Check if the file is a valid JPEG image."""
    try:
        with Image.open(file_path) as img:
            return img.format == "JPEG"
    except:
        return False

def convert_jpeg_to_png(input_file, output_file):
    """Convert JPEG to PNG using Pillow."""
    with Image.open(input_file) as img:
        img.save(output_file, "PNG")

def main():
    print("JPEG to PNG Converter")
    input_file = input("Enter the path to the JPEG file: ")

    if is_valid_jpeg(input_file):
        print("Valid JPEG image. Converting to PNG...")
        
        # Generate output file name
        output_file = os.path.splitext(input_file)[0] + ".png"
        
        try:
            # Convert JPEG to PNG
            convert_jpeg_to_png(input_file, output_file)
            
            # Write PNG Image
            print(f"Conversion complete. PNG file saved as: {output_file}")
        except Exception as e:
            print(f"An error occurred during conversion: {str(e)}")
    else:
        # Display Error Message
        print("Error: Invalid JPEG file. Please provide a valid JPEG file path.")

if __name__ == "__main__":
    main()
