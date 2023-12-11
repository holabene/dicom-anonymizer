# main.py

import argparse
from modify_dicom import process_files


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Anonymize DICOM study")

    # Define command-line arguments
    parser.add_argument("input_path", help="Path to the input DICOM files")
    parser.add_argument("output_path", help="Path to the output DICOM files. Also supports HTTP (POST) and S3 URLs")

    # Define command line options
    parser.add_argument("--zip", action="store_true", help="Produce zip archive as output")
    parser.add_argument("--keep-original-uids", action="store_true", help="Keep original UIDs in the output DICOM files")
    parser.add_argument("--keep-patient-data", action="store_true", help="Do not anonymize patient data")

    # Parse command-line arguments
    args = parser.parse_args()

    # Modify DICOM study
    process_files(args.input_path, args.output_path, args.zip, args.keep_original_uids, args.keep_patient_data)


if __name__ == "__main__":
    main()
