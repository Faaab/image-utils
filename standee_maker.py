from PIL import Image, ImageOps
import os
import typer

app = typer.Typer()

def process_image(image_path: str):
    # Load the image
    image = Image.open(image_path)
    
    # Add a 20px black border
    bordered_image = ImageOps.expand(image, border=20, fill='black')
    
    # Rotate the image 180 degrees
    rotated_image = bordered_image.rotate(180)
    
    # Calculate the size for the new image
    width, height = bordered_image.size
    new_height = height * 2
    
    # Create a new blank image to accommodate both bordered and rotated images
    new_image = Image.new('RGB', (width, new_height))
    
    # Paste the rotated image on top
    new_image.paste(rotated_image, (0, 0))
    
    # Paste the bordered image below the rotated image
    new_image.paste(bordered_image, (0, height))
    
    # Construct the new filename
    directory, filename = os.path.split(image_path)
    new_filename = f"STANDEE_{filename}"
    new_image_path = os.path.join(directory, new_filename)
    
    # Save the resulting image
    new_image.save(new_image_path)
    print(f"Saved processed image as: {new_image_path}")

@app.command()
def main(image_path: str):
    process_image(image_path)

if __name__ == "__main__":
    app()
