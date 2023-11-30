# main.py

import argparse
from anonymizer import anonymize_dicom_study


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Anonymize DICOM study")

    # Define command-line arguments
    parser.add_argument("input_path", help="Path to the input DICOM files")

    # Define command line options
    parser.add_argument("--output-dir", help="Output directory for anonymized DICOM files")
    parser.add_argument("--output-http", help="HTTP endpoint for anonymized DICOM files")
    parser.add_argument("--zip", action="store_true", help="Zip output")

    # Parse command-line arguments
    args = parser.parse_args()

    # Anonymize DICOM study
    anonymize_dicom_study(args.input_path, args.zip, **vars(args))


if __name__ == "__main__":
    main()
