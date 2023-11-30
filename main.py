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
                        help="Output directory for output files (for local filesystem and S3 writer)")

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

    # if --output-http and --output-s3 are not specified, --output-dir is required
    if not args.output_http and not args.output_s3 and not args.output_dir:
        parser.error("Please specify --output-dir for local filesystem output")

    # if --output-http is specified, --output-dir is not allowed
    if args.output_http and args.output_dir:
        parser.error("--output-dir is not allowed for HTTP output")

    # setting --output-http and --output-s3 together is not allowed
    if args.output_http and args.output_s3:
        parser.error("Please select between HTTP or S3 output")

    # Anonymize DICOM study
    anonymize_dicom_study(args.input_path, args.zip, **vars(args))


if __name__ == "__main__":
    main()
