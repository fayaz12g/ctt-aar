import os
import math
from functions import *

def create_patch_files(patch_folder, ratio_value, scaling_factor, visual_fixes):

    visual_fixesa = visual_fixes[0]
    scaling_factor = float(scaling_factor)
    ratio_value = float(ratio_value)
    print(f"The scaling factor is {scaling_factor}.")
    hex_value1, hex_value2= ctt_hex23(ratio_value)
    version_variables = ["1.3.0"]
    for version_variable in version_variables:
        file_name = f"main-{version_variable}.pchtxt"
        file_path = os.path.join(patch_folder, file_name)

        if version_variable == "1.3.0":
            nsobidid = "8F75C9B8B7FF69D96D6FBD6533A5930120985B2D"
            replace1 = "0045fd90"
            replace2 = "0045fd94"
            visual_fix = visual_fixesa

        patch_content = f'''@nsobid-{nsobidid}

@flag print_values
@flag offset_shift 0x100

@enabled
0038e928 DE719C52 
0038e92c 1E03A872
0038e930 C003271E
@disabled

{visual_fix}

// Generated using ctt-aar by Fayaz (github.com/fayaz12g/ctt-aar)
// Made possible by Fl4sh_#9174'''
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as patch_file:
            patch_file.write(patch_content)
        print(f"Patch file created: {file_path}")
