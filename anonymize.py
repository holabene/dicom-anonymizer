import pydicom


def anonymize(ds: pydicom.Dataset) -> pydicom.Dataset:
    # Anonymize the DICOM file
    # List of tags from Orthanc source code

    ds.PatientName = "Anonymous"
    ds.PatientID = "AnonymousID"

    ds.pop((0x0008, 0x0020), None)  # Study Date
    ds.pop((0x0008, 0x0023), None)  # Content Date
    ds.pop((0x0008, 0x0030), None)  # Study Time
    ds.pop((0x0008, 0x0033), None)  # Content Time
    ds.pop((0x0008, 0x0050), None)  # Accession Number
    ds.pop((0x0008, 0x0090), None)  # Referring Physician's Name
    ds.pop((0x0008, 0x009c), None)  # Consulting Physician's Name
    ds.pop((0x0010, 0x0030), None)  # Patient's Birth Date
    ds.pop((0x0010, 0x0040), None)  # Patient's Sex
    ds.pop((0x0012, 0x0010), None)  # Clinical Trial Sponsor Name
    ds.pop((0x0012, 0x0020), None)  # Clinical Trial Protocol ID
    ds.pop((0x0012, 0x0021), None)  # Clinical Trial Protocol Name
    ds.pop((0x0012, 0x0030), None)  # Clinical Trial Site ID
    ds.pop((0x0012, 0x0031), None)  # Clinical Trial Site Name
    ds.pop((0x0012, 0x0040), None)  # Clinical Trial Subject ID
    ds.pop((0x0012, 0x0042), None)  # Clinical Trial Subject Reading ID
    ds.pop((0x0012, 0x0050), None)  # Clinical Trial Time Point ID
    ds.pop((0x0012, 0x0060), None)  # Clinical Trial Coordinating Center Name
    ds.pop((0x0012, 0x0081), None)  # Clinical Trial Protocol Ethics Committee Name
    ds.pop((0x0018, 0x0010), None)  # Contrast/Bolus Agent
    ds.pop((0x0018, 0x11bb), None)  # Acquisition Field Of View Label
    ds.pop((0x0018, 0x9367), None)  # X-Ray Source ID
    ds.pop((0x0018, 0x9369), None)  # Source Start DateTime
    ds.pop((0x0018, 0x936a), None)  # Source End DateTime
    ds.pop((0x0018, 0x9371), None)  # X-Ray Detector ID
    ds.pop((0x0020, 0x0010), None)  # Study ID
    ds.pop((0x0034, 0x0001), None)  # Flow Identifier Sequence
    ds.pop((0x0034, 0x0002), None)  # Flow Identifier
    ds.pop((0x0034, 0x0005), None)  # Source Identifier
    ds.pop((0x0034, 0x0007), None)  # Frame Origin Timestamp
    ds.pop((0x003a, 0x0314), None)  # Impedance Measurement DateTime
    ds.pop((0x0040, 0x0512), None)  # Container Identifier
    ds.pop((0x0040, 0x0513), None)  # Issuer of the Container Identifier Sequence
    ds.pop((0x0040, 0x0551), None)  # Specimen Identifier
    ds.pop((0x0040, 0x0562), None)  # Issuer of the Specimen Identifier Sequence
    ds.pop((0x0040, 0x0610), None)  # Specimen Preparation Sequence
    ds.pop((0x0040, 0x1101), None)  # Person Identification Code Sequence
    ds.pop((0x0040, 0x2016), None)  # Placer Order Number / Imaging Service Request
    ds.pop((0x0040, 0x2017), None)  # Filler Order Number / Imaging Service Request
    ds.pop((0x0040, 0xa027), None)  # Verifying Organization
    ds.pop((0x0040, 0xa073), None)  # Verifying Observer Sequence
    ds.pop((0x0040, 0xa075), None)  # Verifying Observer Name
    ds.pop((0x0040, 0xa088), None)  # Verifying Observer Identification Code Sequence
    ds.pop((0x0040, 0xa123), None)  # Person Name
    ds.pop((0x0040, 0xa730), None)  # Content Sequence
    ds.pop((0x0070, 0x0001), None)  # Graphic Annotation Sequence
    ds.pop((0x0070, 0x0084), None)  # Content Creator's Name
    ds.pop((0x3006, 0x0002), None)  # Structure Set Label
    ds.pop((0x3006, 0x0008), None)  # Structure Set Date
    ds.pop((0x3006, 0x0009), None)  # Structure Set Time
    ds.pop((0x3006, 0x0026), None)  # ROI Name
    ds.pop((0x3006, 0x00a6), None)  # ROI Interpreter
    ds.pop((0x300a, 0x0002), None)  # RT Plan Label
    ds.pop((0x300a, 0x0608), None)  # Treatment Position Group Label
    ds.pop((0x300a, 0x0611), None)  # RT Accessory Holder Slot ID
    ds.pop((0x300a, 0x0615), None)  # RT Accessory Device Slot ID
    ds.pop((0x300a, 0x0619), None)  # Radiation Dose Identification Label
    ds.pop((0x300a, 0x0623), None)  # Radiation Dose In-Vivo Measurement Label
    ds.pop((0x300a, 0x062a), None)  # RT Tolerance Set Label
    ds.pop((0x300a, 0x067c), None)  # Radiation Generation Mode Label
    ds.pop((0x300a, 0x067d), None)  # Radiation Generation Mode Description
    ds.pop((0x300a, 0x0734), None)  # Treatment Tolerance Violation Description
    ds.pop((0x300a, 0x0736), None)  # Treatment Tolerance Violation DateTime
    ds.pop((0x300a, 0x073a), None)  # Recorded RT Control Point DateTime
    ds.pop((0x300a, 0x0741), None)  # Interlock DateTime
    ds.pop((0x300a, 0x0742), None)  # Interlock Description
    ds.pop((0x300a, 0x0760), None)  # Override DateTime
    ds.pop((0x300a, 0x0783), None)  # Interlock Origin Description
    ds.pop((0x3010, 0x000f), None)  # Conceptual Volume Combination Description
    ds.pop((0x3010, 0x0017), None)  # Conceptual Volume Description
    ds.pop((0x3010, 0x001b), None)  # Device Alternate Identifier
    ds.pop((0x3010, 0x002d), None)  # Device Label
    ds.pop((0x3010, 0x0033), None)  # User Content Label
    ds.pop((0x3010, 0x0034), None)  # User Content Long Label
    ds.pop((0x3010, 0x0035), None)  # Entity Label
    ds.pop((0x3010, 0x0038), None)  # Entity Long Label
    ds.pop((0x3010, 0x0043), None)  # Manufacturer's Device Identifier
    ds.pop((0x3010, 0x0054), None)  # RT Prescription Label
    ds.pop((0x3010, 0x005a), None)  # RT Physician Intent Narrative
    ds.pop((0x3010, 0x005c), None)  # Reason for Superseding
    ds.pop((0x3010, 0x0077), None)  # Treatment Site
    ds.pop((0x3010, 0x007a), None)  # Treatment Technique Notes
    ds.pop((0x3010, 0x007b), None)  # Prescription Notes
    ds.pop((0x3010, 0x007f), None)  # Fractionation Notes
    ds.pop((0x3010, 0x0081), None)  # Prescription Notes Sequence

    ds.pop((0x0000, 0x1000), None)  # Affected SOP Instance UID
    ds.pop((0x0008, 0x0015), None)  # Instance Coercion DateTime
    ds.pop((0x0008, 0x0021), None)  # Series Date
    ds.pop((0x0008, 0x0022), None)  # Acquisition Date
    ds.pop((0x0008, 0x0024), None)  # Overlay Date
    ds.pop((0x0008, 0x0025), None)  # Curve Date
    ds.pop((0x0008, 0x002a), None)  # Acquisition DateTime
    ds.pop((0x0008, 0x0031), None)  # Series Time
    ds.pop((0x0008, 0x0032), None)  # Acquisition Time
    ds.pop((0x0008, 0x0034), None)  # Overlay Time
    ds.pop((0x0008, 0x0035), None)  # Curve Time
    ds.pop((0x0008, 0x0080), None)  # Institution Name
    ds.pop((0x0008, 0x0081), None)  # Institution Address
    ds.pop((0x0008, 0x0082), None)  # Institution Code Sequence
    ds.pop((0x0008, 0x0092), None)  # Referring Physician's Address
    ds.pop((0x0008, 0x0094), None)  # Referring Physician's Telephone Numbers
    ds.pop((0x0008, 0x0096), None)  # Referring Physician Identification Sequence
    ds.pop((0x0008, 0x009d), None)  # Consulting Physician Identification Sequence
    ds.pop((0x0008, 0x0201), None)  # Timezone Offset From UTC
    ds.pop((0x0008, 0x1010), None)  # Station Name
    ds.pop((0x0008, 0x1030), None)  # Study Description
    ds.pop((0x0008, 0x103e), None)  # Series Description
    ds.pop((0x0008, 0x1040), None)  # Institutional Department Name
    ds.pop((0x0008, 0x1041), None)  # Institutional Department Type Code Sequence
    ds.pop((0x0008, 0x1048), None)  # Physician(s) of Record
    ds.pop((0x0008, 0x1049), None)  # Physician(s) of Record Identification Sequence
    ds.pop((0x0008, 0x1050), None)  # Performing Physician's Name
    ds.pop((0x0008, 0x1052), None)  # Performing Physician Identification Sequence
    ds.pop((0x0008, 0x1060), None)  # Name of Physician(s) Reading Study
    ds.pop((0x0008, 0x1062), None)  # Physician(s) Reading Study Identification Sequence
    ds.pop((0x0008, 0x1070), None)  # Operators' Name
    ds.pop((0x0008, 0x1072), None)  # Operator Identification Sequence
    ds.pop((0x0008, 0x1080), None)  # Admitting Diagnoses Description
    ds.pop((0x0008, 0x1084), None)  # Admitting Diagnoses Code Sequence
    ds.pop((0x0008, 0x1110), None)  # Referenced Study Sequence
    ds.pop((0x0008, 0x1111), None)  # Referenced Performed Procedure Step Sequence
    ds.pop((0x0008, 0x1120), None)  # Referenced Patient Sequence
    ds.pop((0x0008, 0x2111), None)  # Derivation Description
    ds.pop((0x0008, 0x4000), None)  # Identifying Comments
    ds.pop((0x0010, 0x0021), None)  # Issuer of Patient ID
    ds.pop((0x0010, 0x0032), None)  # Patient's Birth Time
    ds.pop((0x0010, 0x0050), None)  # Patient's Insurance Plan Code Sequence
    ds.pop((0x0010, 0x0101), None)  # Patient's Primary Language Code Sequence
    ds.pop((0x0010, 0x0102), None)  # Patient's Primary Language Modifier Code Sequence
    ds.pop((0x0010, 0x1000), None)  # Other Patient IDs
    ds.pop((0x0010, 0x1001), None)  # Other Patient Names
    ds.pop((0x0010, 0x1002), None)  # Other Patient IDs Sequence
    ds.pop((0x0010, 0x1005), None)  # Patient's Birth Name
    ds.pop((0x0010, 0x1010), None)  # Patient's Age
    ds.pop((0x0010, 0x1020), None)  # Patient's Size
    ds.pop((0x0010, 0x1030), None)  # Patient's Weight
    ds.pop((0x0010, 0x1040), None)  # Patient's Address
    ds.pop((0x0010, 0x1050), None)  # Insurance Plan Identification
    ds.pop((0x0010, 0x1060), None)  # Patient's Mother's Birth Name
    ds.pop((0x0010, 0x1080), None)  # Military Rank
    ds.pop((0x0010, 0x1081), None)  # Branch of Service
    ds.pop((0x0010, 0x1090), None)  # Medical Record Locator
    ds.pop((0x0010, 0x1100), None)  # Referenced Patient Photo Sequence
    ds.pop((0x0010, 0x2000), None)  # Medical Alerts
    ds.pop((0x0010, 0x2110), None)  # Allergies
    ds.pop((0x0010, 0x2150), None)  # Country of Residence
    ds.pop((0x0010, 0x2152), None)  # Region of Residence
    ds.pop((0x0010, 0x2154), None)  # Patient's Telephone Numbers
    ds.pop((0x0010, 0x2155), None)  # Patient's Telecom Information
    ds.pop((0x0010, 0x2160), None)  # Ethnic Group
    ds.pop((0x0010, 0x2180), None)  # Occupation
    ds.pop((0x0010, 0x21a0), None)  # Smoking Status
    ds.pop((0x0010, 0x21b0), None)  # Additional Patient History
    ds.pop((0x0010, 0x21c0), None)  # Pregnancy Status
    ds.pop((0x0010, 0x21d0), None)  # Last Menstrual Date
    ds.pop((0x0010, 0x21f0), None)  # Patient's Religious Preference
    ds.pop((0x0010, 0x2203), None)  # Patient's Sex Neutered
    ds.pop((0x0010, 0x2297), None)  # Responsible Person
    ds.pop((0x0010, 0x2299), None)  # Responsible Organization
    ds.pop((0x0010, 0x4000), None)  # Patient Comments
    ds.pop((0x0012, 0x0051), None)  # Clinical Trial Time Point Description
    ds.pop((0x0012, 0x0071), None)  # Clinical Trial Series ID
    ds.pop((0x0012, 0x0072), None)  # Clinical Trial Series Description
    ds.pop((0x0012, 0x0082), None)  # Clinical Trial Protocol Ethics Committee Approval Number
    ds.pop((0x0016, 0x002b), None)  # Maker Note
    ds.pop((0x0016, 0x004b), None)  # Device Setting Description
    ds.pop((0x0016, 0x004d), None)  # Camera Owner Name
    ds.pop((0x0016, 0x004e), None)  # Lens Specification
    ds.pop((0x0016, 0x004f), None)  # Lens Make
    ds.pop((0x0016, 0x0050), None)  # Lens Model
    ds.pop((0x0016, 0x0051), None)  # Lens Serial Number
    ds.pop((0x0016, 0x0070), None)  # GPS Version ID
    ds.pop((0x0016, 0x0071), None)  # GPS Latitude Ref
    ds.pop((0x0016, 0x0072), None)  # GPS Latitude
    ds.pop((0x0016, 0x0073), None)  # GPS Longitude Ref
    ds.pop((0x0016, 0x0074), None)  # GPS Longitude
    ds.pop((0x0016, 0x0075), None)  # GPS Altitude Ref
    ds.pop((0x0016, 0x0076), None)  # GPS Altitude
    ds.pop((0x0016, 0x0077), None)  # GPS Time Stamp
    ds.pop((0x0016, 0x0078), None)  # GPS Satellites
    ds.pop((0x0016, 0x0079), None)  # GPS Status
    ds.pop((0x0016, 0x007a), None)  # GPS Measure Mode
    ds.pop((0x0016, 0x007b), None)  # GPS DOP
    ds.pop((0x0016, 0x007c), None)  # GPS Speed Ref
    ds.pop((0x0016, 0x007d), None)  # GPS Speed
    ds.pop((0x0016, 0x007e), None)  # GPS Track Ref
    ds.pop((0x0016, 0x007f), None)  # GPS Track
    ds.pop((0x0016, 0x0080), None)  # GPS Img Direction Ref
    ds.pop((0x0016, 0x0081), None)  # GPS Img Direction
    ds.pop((0x0016, 0x0082), None)  # GPS Map Datum
    ds.pop((0x0016, 0x0083), None)  # GPS Dest Latitude Ref
    ds.pop((0x0016, 0x0084), None)  # GPS Dest Latitude
    ds.pop((0x0016, 0x0085), None)  # GPS Dest Longitude Ref
    ds.pop((0x0016, 0x0086), None)  # GPS Dest Longitude
    ds.pop((0x0016, 0x0087), None)  # GPS Dest Bearing Ref
    ds.pop((0x0016, 0x0088), None)  # GPS Dest Bearing
    ds.pop((0x0016, 0x0089), None)  # GPS Dest Distance Ref
    ds.pop((0x0016, 0x008a), None)  # GPS Dest Distance
    ds.pop((0x0016, 0x008b), None)  # GPS Processing Method
    ds.pop((0x0016, 0x008c), None)  # GPS Area Information
    ds.pop((0x0016, 0x008d), None)  # GPS Date Stamp
    ds.pop((0x0016, 0x008e), None)  # GPS Differential
    ds.pop((0x0018, 0x1000), None)  # Device Serial Number
    ds.pop((0x0018, 0x1004), None)  # Plate ID
    ds.pop((0x0018, 0x1005), None)  # Generator ID
    ds.pop((0x0018, 0x1007), None)  # Cassette ID
    ds.pop((0x0018, 0x1008), None)  # Gantry ID
    ds.pop((0x0018, 0x1009), None)  # Unique Device Identifier
    ds.pop((0x0018, 0x100a), None)  # UDI Sequence
    ds.pop((0x0018, 0x1030), None)  # Protocol Name
    ds.pop((0x0018, 0x1400), None)  # Acquisition Device Processing Description
    ds.pop((0x0018, 0x4000), None)  # Acquisition Comments
    ds.pop((0x0018, 0x5011), None)  # Transducer Identification Sequence
    ds.pop((0x0018, 0x700a), None)  # Detector ID
    ds.pop((0x0018, 0x9185), None)  # Respiratory Motion Compensation Technique Description
    ds.pop((0x0018, 0x9373), None)  # X-Ray Detector Label
    ds.pop((0x0018, 0x937b), None)  # Multi-energy Acquisition Description
    ds.pop((0x0018, 0x937f), None)  # Decomposition Description
    ds.pop((0x0018, 0x9424), None)  # Acquisition Protocol Description
    ds.pop((0x0018, 0x9516), None)  # Start Acquisition DateTime
    ds.pop((0x0018, 0x9517), None)  # End Acquisition DateTime
    ds.pop((0x0018, 0x9937), None)  # Requested Series Description
    ds.pop((0x0018, 0xa003), None)  # Contribution Description
    ds.pop((0x0020, 0x3401), None)  # Modifying Device ID
    ds.pop((0x0020, 0x3406), None)  # Modified Image Description
    ds.pop((0x0020, 0x4000), None)  # Image Comments
    ds.pop((0x0020, 0x9158), None)  # Frame Comments
    ds.pop((0x0028, 0x4000), None)  # Image Presentation Comments
    ds.pop((0x0032, 0x0012), None)  # Study ID Issuer
    ds.pop((0x0032, 0x1020), None)  # Scheduled Study Location
    ds.pop((0x0032, 0x1021), None)  # Scheduled Study Location AE Title
    ds.pop((0x0032, 0x1030), None)  # Reason for Study
    ds.pop((0x0032, 0x1032), None)  # Requesting Physician
    ds.pop((0x0032, 0x1033), None)  # Requesting Service
    ds.pop((0x0032, 0x1060), None)  # Requested Procedure Description
    ds.pop((0x0032, 0x1066), None)  # Reason for Visit
    ds.pop((0x0032, 0x1067), None)  # Reason for Visit Code Sequence
    ds.pop((0x0032, 0x1070), None)  # Requested Contrast Agent
    ds.pop((0x0032, 0x4000), None)  # Study Comments
    ds.pop((0x0038, 0x0004), None)  # Referenced Patient Alias Sequence
    ds.pop((0x0038, 0x0010), None)  # Admission ID
    ds.pop((0x0038, 0x0011), None)  # Issuer of Admission ID
    ds.pop((0x0038, 0x0014), None)  # Issuer of Admission ID Sequence
    ds.pop((0x0038, 0x001e), None)  # Scheduled Patient Institution Residence
    ds.pop((0x0038, 0x0020), None)  # Admitting Date
    ds.pop((0x0038, 0x0021), None)  # Admitting Time
    ds.pop((0x0038, 0x0040), None)  # Discharge Diagnosis Description
    ds.pop((0x0038, 0x0050), None)  # Special Needs
    ds.pop((0x0038, 0x0060), None)  # Service Episode ID
    ds.pop((0x0038, 0x0061), None)  # Issuer of Service Episode ID
    ds.pop((0x0038, 0x0062), None)  # Service Episode Description
    ds.pop((0x0038, 0x0064), None)  # Issuer of Service Episode ID Sequence
    ds.pop((0x0038, 0x0300), None)  # Current Patient Location
    ds.pop((0x0038, 0x0400), None)  # Patient's Institution Residence
    ds.pop((0x0038, 0x0500), None)  # Patient State
    ds.pop((0x0038, 0x4000), None)  # Visit Comments
    ds.pop((0x0040, 0x0001), None)  # Scheduled Station AE Title
    ds.pop((0x0040, 0x0002), None)  # Scheduled Procedure Step Start Date
    ds.pop((0x0040, 0x0003), None)  # Scheduled Procedure Step Start Time
    ds.pop((0x0040, 0x0004), None)  # Scheduled Procedure Step End Date
    ds.pop((0x0040, 0x0005), None)  # Scheduled Procedure Step End Time
    ds.pop((0x0040, 0x0006), None)  # Scheduled Performing Physician's Name
    ds.pop((0x0040, 0x0007), None)  # Scheduled Procedure Step Description
    ds.pop((0x0040, 0x0009), None)  # Scheduled Procedure Step ID
    ds.pop((0x0040, 0x000b), None)  # Scheduled Performing Physician Identification Sequence
    ds.pop((0x0040, 0x0010), None)  # Scheduled Station Name
    ds.pop((0x0040, 0x0011), None)  # Scheduled Procedure Step Location
    ds.pop((0x0040, 0x0012), None)  # Pre-Medication
    ds.pop((0x0040, 0x0241), None)  # Performed Station AE Title
    ds.pop((0x0040, 0x0242), None)  # Performed Station Name
    ds.pop((0x0040, 0x0243), None)  # Performed Location
    ds.pop((0x0040, 0x0244), None)  # Performed Procedure Step Start Date
    ds.pop((0x0040, 0x0245), None)  # Performed Procedure Step Start Time
    ds.pop((0x0040, 0x0250), None)  # Performed Procedure Step End Date
    ds.pop((0x0040, 0x0251), None)  # Performed Procedure Step End Time
    ds.pop((0x0040, 0x0253), None)  # Performed Procedure Step ID
    ds.pop((0x0040, 0x0254), None)  # Performed Procedure Step Description
    ds.pop((0x0040, 0x0275), None)  # Request Attributes Sequence
    ds.pop((0x0040, 0x0280), None)  # Comments on the Performed Procedure Step
    ds.pop((0x0040, 0x0310), None)  # Comments on Radiation Dose
    ds.pop((0x0040, 0x050a), None)  # Specimen Accession Number
    ds.pop((0x0040, 0x051a), None)  # Container Description
    ds.pop((0x0040, 0x0555), None)  # Acquisition Context Sequence
    ds.pop((0x0040, 0x0600), None)  # Specimen Short Description
    ds.pop((0x0040, 0x0602), None)  # Specimen Detailed Description
    ds.pop((0x0040, 0x06fa), None)  # Slide Identifier
    ds.pop((0x0040, 0x1001), None)  # Requested Procedure ID
    ds.pop((0x0040, 0x1002), None)  # Reason for the Requested Procedure
    ds.pop((0x0040, 0x1004), None)  # Patient Transport Arrangements
    ds.pop((0x0040, 0x1005), None)  # Requested Procedure Location
    ds.pop((0x0040, 0x100a), None)  # Reason for Requested Procedure Code Sequence
    ds.pop((0x0040, 0x1010), None)  # Names of Intended Recipients of Results
    ds.pop((0x0040, 0x1011), None)  # Intended Recipients of Results Identification Sequence
    ds.pop((0x0040, 0x1102), None)  # Person's Address
    ds.pop((0x0040, 0x1103), None)  # Person's Telephone Numbers
    ds.pop((0x0040, 0x1104), None)  # Person's Telecom Information
    ds.pop((0x0040, 0x1400), None)  # Requested Procedure Comments
    ds.pop((0x0040, 0x2001), None)  # Reason for the Imaging Service Request
    ds.pop((0x0040, 0x2008), None)  # Order Entered By
    ds.pop((0x0040, 0x2009), None)  # Order Enterer's Location
    ds.pop((0x0040, 0x2010), None)  # Order Callback Phone Number
    ds.pop((0x0040, 0x2011), None)  # Order Callback Telecom Information
    ds.pop((0x0040, 0x2400), None)  # Imaging Service Request Comments
    ds.pop((0x0040, 0x3001), None)  # Confidentiality Constraint on Patient Data Description
    ds.pop((0x0040, 0x4005), None)  # Scheduled Procedure Step Start DateTime
    ds.pop((0x0040, 0x4008), None)  # Scheduled Procedure Step Expiration DateTime
    ds.pop((0x0040, 0x4010), None)  # Scheduled Procedure Step Modification DateTime
    ds.pop((0x0040, 0x4011), None)  # Expected Completion DateTime
    ds.pop((0x0040, 0x4025), None)  # Scheduled Station Name Code Sequence
    ds.pop((0x0040, 0x4027), None)  # Scheduled Station Geographic Location Code Sequence
    ds.pop((0x0040, 0x4028), None)  # Performed Station Name Code Sequence
    ds.pop((0x0040, 0x4030), None)  # Performed Station Geographic Location Code Sequence
    ds.pop((0x0040, 0x4034), None)  # Scheduled Human Performers Sequence
    ds.pop((0x0040, 0x4035), None)  # Actual Human Performers Sequence
    ds.pop((0x0040, 0x4036), None)  # Human Performer's Organization
    ds.pop((0x0040, 0x4037), None)  # Human Performer's Name
    ds.pop((0x0040, 0x4050), None)  # Performed Procedure Step Start DateTime
    ds.pop((0x0040, 0x4051), None)  # Performed Procedure Step End DateTime
    ds.pop((0x0040, 0x4052), None)  # Procedure Step Cancellation DateTime
    ds.pop((0x0040, 0xa078), None)  # Author Observer Sequence
    ds.pop((0x0040, 0xa07a), None)  # Participant Sequence
    ds.pop((0x0040, 0xa07c), None)  # Custodial Organization Sequence
    ds.pop((0x0040, 0xa192), None)  # Observation Date (Trial)
    ds.pop((0x0040, 0xa193), None)  # Observation Time (Trial)
    ds.pop((0x0040, 0xa307), None)  # Current Observer (Trial)
    ds.pop((0x0040, 0xa352), None)  # Verbal Source (Trial)
    ds.pop((0x0040, 0xa353), None)  # Address (Trial)
    ds.pop((0x0040, 0xa354), None)  # Telephone Number (Trial)
    ds.pop((0x0040, 0xa358), None)  # Verbal Source Identifier Code Sequence (Trial)
    ds.pop((0x0050, 0x001b), None)  # Container Component ID
    ds.pop((0x0050, 0x0020), None)  # Device Description
    ds.pop((0x0050, 0x0021), None)  # Long Device Description
    ds.pop((0x0070, 0x0086), None)  # Content Creator's Identification Code Sequence
    ds.pop((0x0088, 0x0200), None)  # Icon Image Sequence
    ds.pop((0x0088, 0x0904), None)  # Topic Title
    ds.pop((0x0088, 0x0906), None)  # Topic Subject
    ds.pop((0x0088, 0x0910), None)  # Topic Author
    ds.pop((0x0088, 0x0912), None)  # Topic Keywords
    ds.pop((0x0400, 0x0402), None)  # Referenced Digital Signature Sequence
    ds.pop((0x0400, 0x0403), None)  # Referenced SOP Instance MAC Sequence
    ds.pop((0x0400, 0x0404), None)  # MAC
    ds.pop((0x0400, 0x0550), None)  # Modified Attributes Sequence
    ds.pop((0x0400, 0x0551), None)  # Nonconforming Modified Attributes Sequence
    ds.pop((0x0400, 0x0552), None)  # Nonconforming Data Element Value
    ds.pop((0x0400, 0x0561), None)  # Original Attributes Sequence
    ds.pop((0x0400, 0x0600), None)  # Instance Origin Status
    ds.pop((0x2030, 0x0020), None)  # Text String
    ds.pop((0x2200, 0x0002), None)  # Label Text
    ds.pop((0x2200, 0x0005), None)  # Barcode Value
    ds.pop((0x3006, 0x0004), None)  # Structure Set Name
    ds.pop((0x3006, 0x0006), None)  # Structure Set Description
    ds.pop((0x3006, 0x0028), None)  # ROI Description
    ds.pop((0x3006, 0x0038), None)  # ROI Generation Description
    ds.pop((0x3006, 0x0085), None)  # ROI Observation Label
    ds.pop((0x3006, 0x0088), None)  # ROI Observation Description
    ds.pop((0x3008, 0x0054), None)  # First Treatment Date
    ds.pop((0x3008, 0x0056), None)  # Most Recent Treatment Date
    ds.pop((0x3008, 0x0105), None)  # Source Serial Number
    ds.pop((0x3008, 0x0250), None)  # Treatment Date
    ds.pop((0x3008, 0x0251), None)  # Treatment Time
    ds.pop((0x300a, 0x0003), None)  # RT Plan Name
    ds.pop((0x300a, 0x0004), None)  # RT Plan Description
    ds.pop((0x300a, 0x0006), None)  # RT Plan Date
    ds.pop((0x300a, 0x0007), None)  # RT Plan Time
    ds.pop((0x300a, 0x000e), None)  # Prescription Description
    ds.pop((0x300a, 0x0016), None)  # Dose Reference Description
    ds.pop((0x300a, 0x0072), None)  # Fraction Group Description
    ds.pop((0x300a, 0x00b2), None)  # Treatment Machine Name
    ds.pop((0x300a, 0x00c3), None)  # Beam Description
    ds.pop((0x300a, 0x00dd), None)  # Bolus Description
    ds.pop((0x300a, 0x0196), None)  # Fixation Device Description
    ds.pop((0x300a, 0x01a6), None)  # Shielding Device Description
    ds.pop((0x300a, 0x01b2), None)  # Setup Technique Description
    ds.pop((0x300a, 0x0216), None)  # Source Manufacturer
    ds.pop((0x300a, 0x02eb), None)  # Compensator Description
    ds.pop((0x300a, 0x0676), None)  # Equipment Frame of Reference Description
    ds.pop((0x300c, 0x0113), None)  # Reason for Omission Description
    ds.pop((0x300e, 0x0008), None)  # Reviewer Name
    ds.pop((0x3010, 0x0036), None)  # Entity Name
    ds.pop((0x3010, 0x0037), None)  # Entity Description
    ds.pop((0x3010, 0x004c), None)  # Intended Phase Start Date
    ds.pop((0x3010, 0x004d), None)  # Intended Phase End Date
    ds.pop((0x3010, 0x0056), None)  # RT Treatment Approach Label
    ds.pop((0x3010, 0x0061), None)  # Prior Treatment Dose Description
    ds.pop((0x4000, 0x0010), None)  # Arbitrary
    ds.pop((0x4000, 0x4000), None)  # Text Comments
    ds.pop((0x4008, 0x0042), None)  # Results ID Issuer
    ds.pop((0x4008, 0x0102), None)  # Interpretation Recorder
    ds.pop((0x4008, 0x010a), None)  # Interpretation Transcriber
    ds.pop((0x4008, 0x010b), None)  # Interpretation Text
    ds.pop((0x4008, 0x010c), None)  # Interpretation Author
    ds.pop((0x4008, 0x0111), None)  # Interpretation Approver Sequence
    ds.pop((0x4008, 0x0114), None)  # Physician Approving Interpretation
    ds.pop((0x4008, 0x0115), None)  # Interpretation Diagnosis Description
    ds.pop((0x4008, 0x0118), None)  # Results Distribution List Sequence
    ds.pop((0x4008, 0x0119), None)  # Distribution Name
    ds.pop((0x4008, 0x011a), None)  # Distribution Address
    ds.pop((0x4008, 0x0202), None)  # Interpretation ID Issuer
    ds.pop((0x4008, 0x0300), None)  # Impressions
    ds.pop((0x4008, 0x4000), None)  # Results Comments
    ds.pop((0xfffa, 0xfffa), None)  # Digital Signatures Sequence
    ds.pop((0xfffc, 0xfffc), None)  # Data Set Trailing Padding

    ds.remove_private_tags()

    return ds
