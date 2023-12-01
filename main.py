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
                        metavar="PATH",
                        help="Path to directory for output files")

    parser.add_argument("--output-http",
                        metavar="URL",
                        help="Post output files to this HTTP endpoint as binary payload")

    parser.add_argument("--output-s3",
                        metavar="BUCKET",
                        help="Upload output files to this S3 bucket (requires AWS credentials)")

    parser.add_argument("--zip",
                        action="store_true",
                        help="Produce zip archive as output")

    # Parse command-line arguments
    args = parser.parse_args()

    # only specify one of --output-http, --output-s3, or --output-dir
    if sum([args.output_http is not None, args.output_s3 is not None, args.output_dir is not None]) > 1:
        parser.error("Please select only one of --output-dir, --output-http, or --output-s3")

    # Anonymize DICOM study
    anonymize_dicom_study(args.input_path, args.zip, **vars(args))


if __name__ == "__main__":
    main()
