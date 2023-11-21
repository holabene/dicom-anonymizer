# main.py

import argparse
from anonymizer import anonymize_dicom_study


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Anonymize DICOM study")

    # Define command-line arguments
    parser.add_argument("zip_file_path", help="Path to the input DICOM study ZIP file")
    parser.add_argument("output_dir", help="Path to the output directory for anonymized DICOM files")

    # Parse command-line arguments
    args = parser.parse_args()

    # Anonymize DICOM study
    anonymize_dicom_study(args.zip_file_path, args.output_dir)


if __name__ == "__main__":
    main()
