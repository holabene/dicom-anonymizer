# main.py

import argparse
from anonymizer import anonymize_dicom_study


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Anonymize DICOM study")

    # Define command-line arguments
    parser.add_argument("input_path", help="Path to the input DICOM files")

    # Define command line options
    parser.add_argument("--output-dir",
                        help="Output directory for output files (for local filesystem and S3 writer)")
    parser.add_argument("--output-http", help="Post output files to this HTTP endpoint")
    parser.add_argument("--output-s3", help="Upload output files to this S3 bucket")
    parser.add_argument("--zip", action="store_true", help="Produce zip archive for the output files")

    # Parse command-line arguments
    args = parser.parse_args()

    # Anonymize DICOM study
    anonymize_dicom_study(args.input_path, args.zip, **vars(args))


if __name__ == "__main__":
    main()
