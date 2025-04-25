#!/usr/bin/env python3
"""
PDF to PNG Converter

This script converts all PDF files in a given directory and its subdirectories to PNG images.
Dependencies:
- pdf2image (install via pip install pdf2image)
- poppler (for pdf2image to work)

Usage:
    python pdf2png.py [input_directory] [output_directory] [dpi]

If no directories are specified, the current directory will be used for both input and output.
Default DPI is 300 for high-quality images.
"""

import os
import sys
import argparse
from pdf2image import convert_from_path
from pathlib import Path

def pdf_to_png(input_dir='.', output_dir=None, dpi=300):
    """
    Convert all PDF files in the input directory and its subdirectories to PNG format.
    
    Args:
        input_dir (str): Directory containing PDF files
        output_dir (str): Directory to save the PNG files (defaults to input_dir)
        dpi (int): Resolution for the output images
    """
    if output_dir is None:
        output_dir = input_dir
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all PDF files in the input directory and its subdirectories
    pdf_files = list(Path(input_dir).glob('**/*.pdf'))
    
    if not pdf_files:
        print(f"No PDF files found in {input_dir} or its subdirectories")
        return
    
    print(f"Found {len(pdf_files)} PDF files. Converting...")
    
    # Process each PDF file
    for pdf_path in pdf_files:
        # Get relative path from input directory to preserve directory structure
        rel_path = pdf_path.relative_to(input_dir) if pdf_path.is_absolute() else pdf_path
        rel_dir = os.path.dirname(rel_path)
        
        # Create corresponding output directory if needed
        if rel_dir:
            out_dir = os.path.join(output_dir, rel_dir)
            os.makedirs(out_dir, exist_ok=True)
        else:
            out_dir = output_dir
            
        pdf_name = pdf_path.stem
        print(f"Converting {rel_path}...")
        
        try:
            # Convert PDF to list of images
            images = convert_from_path(str(pdf_path), dpi=dpi)
            
            # If PDF has only one page
            if len(images) == 1:
                output_file = os.path.join(out_dir, f"{pdf_name}.png")
                images[0].save(output_file, "PNG")
                print(f"  Saved {output_file}")
            # If PDF has multiple pages
            else:
                for i, image in enumerate(images):
                    output_file = os.path.join(out_dir, f"{pdf_name}_{i+1}.png")
                    image.save(output_file, "PNG")
                    print(f"  Saved {output_file}")
            
        except Exception as e:
            print(f"  Error converting {rel_path}: {str(e)}")
    
    print("Conversion complete!")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Convert PDF files to PNG images')
    parser.add_argument('input_dir', nargs='?', default='.', 
                        help='Directory containing PDF files (default: current directory)')
    parser.add_argument('output_dir', nargs='?', default=None,
                        help='Directory to save PNG files (default: same as input directory)')
    parser.add_argument('--dpi', type=int, default=300, 
                        help='DPI resolution for output images (default: 300)')
    
    args = parser.parse_args()
    
    # Run the conversion
    pdf_to_png(args.input_dir, args.output_dir, args.dpi)

if __name__ == "__main__":
    main()

