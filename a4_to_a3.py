#!/usr/bin/env python3
import os
import tempfile

import typer
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, A4, landscape
from pdf2image import convert_from_path

app = typer.Typer()


def merge_pdf_to_a3(input_pdf_path: str, output_pdf_path: str):
    # Convert the PDF pages to images (keeping original A4 dimensions)
    images = convert_from_path(input_pdf_path, dpi=300, size=(int(A4[0]), int(A4[1])))

    if len(images) != 2:
        raise ValueError("The input PDF must have exactly 2 pages")

    # Create a temporary directory to save image files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save the images as temporary files
        image_paths = []
        for i, image in enumerate(images):
            temp_image_path = os.path.join(temp_dir, f"page_{i}.png")
            image.save(temp_image_path, "PNG")
            image_paths.append(temp_image_path)

        # Create a new PDF in A3 landscape size
        c = canvas.Canvas(output_pdf_path, pagesize=landscape(A3))

        # Get dimensions for A4 pages (width, height)
        a4_width, a4_height = A4

        # The canvas for A3 in landscape mode is essentially two A4 pages side by side
        a3_width, a3_height = landscape(A3)

        # Draw the first A4 image on the left half of the A3 page (X: 0 to A4 width)
        c.drawImage(image_paths[0], 0, 0, a4_width, a4_height)

        # Draw the second A4 image on the right half of the A3 page (X: A4 width to end)
        c.drawImage(image_paths[1], a4_width, 0, a4_width, a4_height)

        # Save the canvas
        c.save()

    print(f"Output A3 PDF saved to {output_pdf_path}")


@app.command()
def convert(
    input_pdf: str,
    output_pdf: str = typer.Option(None, help="Optional output PDF filename"),
):
    """
    Convert a two-page A4 PDF into a single-page A3 PDF in landscape mode.

    Arguments:
    - input_pdf: Path to the input PDF file.
    - output_pdf: (optional) Path to the output PDF file. If not provided, the script will create one.
    """
    if not output_pdf:
        # Generate a default output file name if not provided
        base_name = os.path.splitext(input_pdf)[0]
        output_pdf = f"{base_name}_merged_a3.pdf"

    merge_pdf_to_a3(input_pdf, output_pdf)


if __name__ == "__main__":
    app()
