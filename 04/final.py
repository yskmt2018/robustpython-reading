from typing import Final


VENDOR_NAME: Final = "Viafore's Auto-Dog"


def display_vendor_information():
    vendor_info = "Auto-Dog v1.0"
    # vendor_info += VENDOR_NAME でなければならないのに、コピペミスをした
    VENDOR_NAME += VENDOR_NAME
    print(vendor_info)
