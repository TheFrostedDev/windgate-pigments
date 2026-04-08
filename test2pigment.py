import mixbox
from math import floor

class PigmentColours():
    _ROUND_OFFSET = (0.2, 0.16, 0.25) # found by mapping in frgb colour space and comparing with test values

    _RED_FLOWER      = mixbox.rgb_to_latent((198, 57,  57))
    _YELLOW_FLOWER   = mixbox.rgb_to_latent((198, 170, 57))
    _BLUE_FLOWER     = mixbox.rgb_to_latent((57,  57,  198))
    _WHITE_FLOWER    = mixbox.rgb_to_latent((198, 198, 198))
    _FLOWERS = (_RED_FLOWER, _YELLOW_FLOWER, _BLUE_FLOWER, _WHITE_FLOWER)

    _BRICKCOLOURS_BY_NAMES = {'White': ('White', 1, (242, 243, 243)), 'Grey': ('Grey', 2, (161, 165, 162)), 'Light yellow': ('Light yellow', 3, (249, 233, 153)), 'Medium stone grey': ('Medium stone grey', 194, (163, 162, 165)), 'Brick yellow': ('Brick yellow', 5, (215, 197, 154)), 'Light green (Mint)': ('Light green (Mint)', 6, (194, 218, 184)), 'Light reddish violet': ('Light reddish violet', 9, (232, 186, 200)), 'Pastel Blue': ('Pastel Blue', 11, (128, 187, 219)), 'Light orange brown': ('Light orange brown', 12, (203, 132, 66)), 'Nougat': ('Nougat', 18, (204, 142, 105)), 'Bright red': ('Bright red', 21, (196, 40, 28)), 'Med. reddish violet': ('Med. reddish violet', 22, (196, 112, 160)), 'Bright blue': ('Bright blue', 23, (13, 105, 172)), 'Bright yellow': ('Bright yellow', 24, (245, 205, 48)), 'Earth orange': ('Earth orange', 25, (98, 71, 50)), 'Black': ('Black', 26, (27, 42, 53)), 'Dark grey': ('Dark grey', 27, (109, 110, 108)), 'Dark green': ('Dark green', 28, (40, 127, 71)), 'Medium green': ('Medium green', 29, (161, 196, 140)), 'Lig. Yellowich orange': ('Lig. Yellowich orange', 36, (243, 207, 155)), 'Bright green': ('Bright green', 37, (75, 151, 75)), 'Dark orange': ('Dark orange', 38, (160, 95, 53)), 'Light bluish violet': ('Light bluish violet', 39, (193, 202, 222)), 'Transparent': ('Transparent', 40, (236, 236, 236)), 'Tr. Red': ('Tr. Red', 41, (205, 84, 75)), 'Tr. Lg blue': ('Tr. Lg blue', 42, (193, 223, 240)), 'Tr. Blue': ('Tr. Blue', 43, (123, 182, 232)), 'Tr. Yellow': ('Tr. Yellow', 44, (247, 241, 141)), 'Light blue': ('Light blue', 45, (180, 210, 228)), 'Tr. Flu. Reddish orange': ('Tr. Flu. Reddish orange', 47, (217, 133, 108)), 'Tr. Green': ('Tr. Green', 48, (132, 182, 141)), 'Tr. Flu. Green': ('Tr. Flu. Green', 49, (248, 241, 132)), 'Phosph. White': ('Phosph. White', 50, (236, 232, 222)), 'Light red': ('Light red', 100, (238, 196, 182)), 'Medium red': ('Medium red', 101, (218, 134, 122)), 'Medium blue': ('Medium blue', 102, (110, 153, 202)), 'Light grey': ('Light grey', 103, (199, 193, 183)), 'Bright violet': ('Bright violet', 104, (107, 50, 124)), 'Br. yellowish orange': ('Br. yellowish orange', 105, (226, 155, 64)), 'Bright orange': ('Bright orange', 106, (218, 133, 65)), 'Bright bluish green': ('Bright bluish green', 107, (0, 143, 156)), 'Earth yellow': ('Earth yellow', 108, (104, 92, 67)), 'Bright bluish violet': ('Bright bluish violet', 110, (67, 84, 147)), 'Tr. Brown': ('Tr. Brown', 111, (191, 183, 177)), 'Medium bluish violet': ('Medium bluish violet', 112, (104, 116, 172)), 'Tr. Medi. reddish violet': ('Tr. Medi. reddish violet', 113, (229, 173, 200)), 'Med. yellowish green': ('Med. yellowish green', 115, (199, 210, 60)), 'Med. bluish green': ('Med. bluish green', 116, (85, 165, 175)), 'Light bluish green': ('Light bluish green', 118, (183, 215, 213)), 'Br. yellowish green': ('Br. yellowish green', 119, (164, 189, 71)), 'Lig. yellowish green': ('Lig. yellowish green', 120, (217, 228, 167)), 'Med. yellowish orange': ('Med. yellowish orange', 121, (231, 172, 88)), 'Br. reddish orange': ('Br. reddish orange', 123, (211, 111, 76)), 'Bright reddish violet': ('Bright reddish violet', 124, (146, 57, 120)), 'Light orange': ('Light orange', 125, (234, 184, 146)), 'Tr. Bright bluish violet': ('Tr. Bright bluish violet', 126, (165, 165, 203)), 'Gold': ('Gold', 333, (239, 184, 56)), 'Dark nougat': ('Dark nougat', 128, (174, 122, 89)), 'Silver': ('Silver', 131, (156, 163, 168)), 'Neon orange': ('Neon orange', 133, (213, 115, 61)), 'Neon green': ('Neon green', 134, (216, 221, 86)), 'Sand blue': ('Sand blue', 135, (116, 134, 157)), 'Sand violet': ('Sand violet', 136, (135, 124, 144)), 'Medium orange': ('Medium orange', 137, (224, 152, 100)), 'Sand yellow': ('Sand yellow', 138, (149, 138, 115)), 'Earth blue': ('Earth blue', 140, (32, 58, 86)), 'Earth green': ('Earth green', 141, (39, 70, 45)), 'Tr. Flu. Blue': ('Tr. Flu. Blue', 143, (207, 226, 247)), 'Sand blue metallic': ('Sand blue metallic', 145, (121, 136, 161)), 'Sand violet metallic': ('Sand violet metallic', 146, (149, 142, 163)), 'Sand yellow metallic': ('Sand yellow metallic', 147, (147, 135, 103)), 'Dark grey metallic': ('Dark grey metallic', 148, (87, 88, 87)), 'Black metallic': ('Black metallic', 149, (22, 29, 50)), 'Light grey metallic': ('Light grey metallic', 150, (171, 173, 172)), 'Sand green': ('Sand green', 151, (120, 144, 130)), 'Sand red': ('Sand red', 153, (149, 121, 119)), 'Dark red': ('Dark red', 154, (123, 46, 47)), 'Tr. Flu. Yellow': ('Tr. Flu. Yellow', 157, (255, 246, 123)), 'Tr. Flu. Red': ('Tr. Flu. Red', 158, (225, 164, 194)), 'Gun metallic': ('Gun metallic', 168, (117, 108, 98)), 'Red flip/flop': ('Red flip/flop', 176, (151, 105, 91)), 'Yellow flip/flop': ('Yellow flip/flop', 178, (180, 132, 85)), 'Silver flip/flop': ('Silver flip/flop', 179, (137, 135, 136)), 'Curry': ('Curry', 180, (215, 169, 75)), 'Fire Yellow': ('Fire Yellow', 190, (249, 214, 46)), 'Flame yellowish orange': ('Flame yellowish orange', 191, (232, 171, 45)), 'Reddish brown': ('Reddish brown', 192, (105, 64, 40)), 'Flame reddish orange': ('Flame reddish orange', 193, (207, 96, 36)), 'Royal blue': ('Royal blue', 195, (70, 103, 164)), 'Dark Royal blue': ('Dark Royal blue', 196, (35, 71, 139)), 'Bright reddish lilac': ('Bright reddish lilac', 198, (142, 66, 133)), 'Dark stone grey': ('Dark stone grey', 199, (99, 95, 98)), 'Lemon metalic': ('Lemon metalic', 200, (130, 138, 93)), 'Light stone grey': ('Light stone grey', 208, (229, 228, 223)), 'Dark Curry': ('Dark Curry', 209, (176, 142, 68)), 'Faded green': ('Faded green', 210, (112, 149, 120)), 'Turquoise': ('Turquoise', 211, (121, 181, 181)), 'Light Royal blue': ('Light Royal blue', 212, (159, 195, 233)), 'Medium Royal blue': ('Medium Royal blue', 213, (108, 129, 183)), 'Rust': ('Rust', 345, (143, 76, 42)), 'Brown': ('Brown', 217, (124, 92, 70)), 'Reddish lilac': ('Reddish lilac', 218, (150, 112, 159)), 'Lilac': ('Lilac', 321, (167, 94, 155)), 'Light lilac': ('Light lilac', 220, (167, 169, 206)), 'Bright purple': ('Bright purple', 221, (205, 98, 152)), 'Light purple': ('Light purple', 222, (228, 173, 200)), 'Light pink': ('Light pink', 223, (220, 144, 149)), 'Light brick yellow': ('Light brick yellow', 224, (240, 213, 160)), 'Warm yellowish orange': ('Warm yellowish orange', 225, (235, 184, 127)), 'Cool yellow': ('Cool yellow', 226, (253, 234, 141)), 'Dove blue': ('Dove blue', 232, (125, 187, 221)), 'Medium lilac': ('Medium lilac', 268, (52, 43, 117)), 'Slime green': ('Slime green', 301, (80, 109, 84)), 'Smoky grey': ('Smoky grey', 302, (91, 93, 105)), 'Dark blue': ('Dark blue', 303, (0, 16, 176)), 'Parsley green': ('Parsley green', 304, (44, 101, 29)), 'Steel blue': ('Steel blue', 305, (82, 124, 174)), 'Storm blue': ('Storm blue', 306, (51, 88, 130)), 'Lapis': ('Lapis', 307, (16, 42, 220)), 'Dark indigo': ('Dark indigo', 308, (61, 21, 133)), 'Sea green': ('Sea green', 309, (52, 142, 64)), 'Shamrock': ('Shamrock', 310, (91, 154, 76)), 'Fossil': ('Fossil', 311, (159, 161, 172)), 'Mulberry': ('Mulberry', 312, (89, 34, 89)), 'Forest green': ('Forest green', 313, (31, 128, 29)), 'Cadet blue': ('Cadet blue', 314, (159, 173, 192)), 'Electric blue': ('Electric blue', 315, (9, 137, 207)), 'Eggplant': ('Eggplant', 316, (123, 0, 123)), 'Moss': ('Moss', 317, (124, 156, 107)), 'Artichoke': ('Artichoke', 318, (138, 171, 133)), 'Sage green': ('Sage green', 319, (185, 196, 177)), 'Ghost grey': ('Ghost grey', 320, (202, 203, 209)), 'Plum': ('Plum', 322, (123, 47, 123)), 'Olivine': ('Olivine', 323, (148, 190, 129)), 'Laurel green': ('Laurel green', 324, (168, 189, 153)), 'Quill grey': ('Quill grey', 325, (223, 223, 222)), 'Crimson': ('Crimson', 327, (151, 0, 0)), 'Mint': ('Mint', 328, (177, 229, 166)), 'Baby blue': ('Baby blue', 329, (152, 194, 219)), 'Carnation pink': ('Carnation pink', 330, (255, 152, 220)), 'Persimmon': ('Persimmon', 331, (255, 89, 89)), 'Maroon': ('Maroon', 332, (117, 0, 0)), 'Daisy orange': ('Daisy orange', 334, (248, 217, 109)), 'Pearl': ('Pearl', 335, (231, 231, 236)), 'Fog': ('Fog', 336, (199, 212, 228)), 'Salmon': ('Salmon', 337, (255, 148, 148)), 'Terra Cotta': ('Terra Cotta', 338, (190, 104, 98)), 'Cocoa': ('Cocoa', 339, (86, 36, 36)), 'Wheat': ('Wheat', 340, (241, 231, 199)), 'Buttermilk': ('Buttermilk', 341, (254, 243, 187)), 'Mauve': ('Mauve', 342, (224, 178, 208)), 'Sunrise': ('Sunrise', 343, (212, 144, 189)), 'Tawny': ('Tawny', 344, (150, 85, 85)), 'Cashmere': ('Cashmere', 346, (211, 190, 150)), 'Khaki': ('Khaki', 347, (226, 220, 188)), 'Lily white': ('Lily white', 348, (237, 234, 234)), 'Seashell': ('Seashell', 349, (233, 218, 218)), 'Burgundy': ('Burgundy', 350, (136, 62, 62)), 'Cork': ('Cork', 351, (188, 155, 93)), 'Burlap': ('Burlap', 352, (199, 172, 120)), 'Beige': ('Beige', 353, (202, 191, 163)), 'Oyster': ('Oyster', 354, (187, 179, 178)), 'Pine Cone': ('Pine Cone', 355, (108, 88, 75)), 'Fawn brown': ('Fawn brown', 356, (160, 132, 79)), 'Hurricane grey': ('Hurricane grey', 357, (149, 137, 136)), 'Cloudy grey': ('Cloudy grey', 358, (171, 168, 158)), 'Linen': ('Linen', 359, (175, 148, 131)), 'Copper': ('Copper', 360, (150, 103, 102)), 'Medium brown': ('Medium brown', 361, (86, 66, 54)), 'Bronze': ('Bronze', 362, (126, 104, 63)), 'Flint': ('Flint', 363, (105, 102, 92)), 'Dark taupe': ('Dark taupe', 364, (90, 76, 66)), 'Burnt Sienna': ('Burnt Sienna', 365, (106, 57, 9)), 'Institutional white': ('Institutional white', 1001, (248, 248, 248)), 'Mid gray': ('Mid gray', 1002, (205, 205, 205)), 'Really black': ('Really black', 1003, (17, 17, 17)), 'Really red': ('Really red', 1004, (255, 0, 0)), 'Deep orange': ('Deep orange', 1017, (255, 175, 0)), 'Alder': ('Alder', 1006, (180, 128, 255)), 'Dusty Rose': ('Dusty Rose', 1007, (163, 75, 75)), 'Olive': ('Olive', 1008, (193, 190, 66)), 'New Yeller': ('New Yeller', 1009, (255, 255, 0)), 'Really blue': ('Really blue', 1010, (0, 0, 255)), 'Navy blue': ('Navy blue', 1011, (0, 32, 96)), 'Deep blue': ('Deep blue', 1012, (33, 84, 185)), 'Cyan': ('Cyan', 1013, (4, 175, 236)), 'CGA brown': ('CGA brown', 1014, (170, 85, 0)), 'Magenta': ('Magenta', 1015, (170, 0, 170)), 'Pink': ('Pink', 1016, (255, 102, 204)), 'Teal': ('Teal', 1018, (18, 238, 212)), 'Toothpaste': ('Toothpaste', 1019, (0, 255, 255)), 'Lime green': ('Lime green', 1020, (0, 255, 0)), 'Camo': ('Camo', 1021, (58, 125, 21)), 'Grime': ('Grime', 1022, (127, 142, 100)), 'Lavender': ('Lavender', 1023, (140, 91, 159)), 'Pastel light blue': ('Pastel light blue', 1024, (175, 221, 255)), 'Pastel orange': ('Pastel orange', 1025, (255, 201, 201)), 'Pastel violet': ('Pastel violet', 1026, (177, 167, 255)), 'Pastel blue-green': ('Pastel blue-green', 1027, (159, 243, 233)), 'Pastel green': ('Pastel green', 1028, (204, 255, 204)), 'Pastel yellow': ('Pastel yellow', 1029, (255, 255, 204)), 'Pastel brown': ('Pastel brown', 1030, (255, 204, 153)), 'Royal purple': ('Royal purple', 1031, (98, 37, 209)), 'Hot pink': ('Hot pink', 1032, (255, 0, 191))}
    _BRICKCOLOURS_BY_BCID = {1: ('White', 1, (242, 243, 243)), 2: ('Grey', 2, (161, 165, 162)), 3: ('Light yellow', 3, (249, 233, 153)), 194: ('Medium stone grey', 194, (163, 162, 165)), 5: ('Brick yellow', 5, (215, 197, 154)), 6: ('Light green (Mint)', 6, (194, 218, 184)), 9: ('Light reddish violet', 9, (232, 186, 200)), 11: ('Pastel Blue', 11, (128, 187, 219)), 12: ('Light orange brown', 12, (203, 132, 66)), 18: ('Nougat', 18, (204, 142, 105)), 21: ('Bright red', 21, (196, 40, 28)), 22: ('Med. reddish violet', 22, (196, 112, 160)), 23: ('Bright blue', 23, (13, 105, 172)), 24: ('Bright yellow', 24, (245, 205, 48)), 25: ('Earth orange', 25, (98, 71, 50)), 26: ('Black', 26, (27, 42, 53)), 27: ('Dark grey', 27, (109, 110, 108)), 28: ('Dark green', 28, (40, 127, 71)), 29: ('Medium green', 29, (161, 196, 140)), 36: ('Lig. Yellowich orange', 36, (243, 207, 155)), 37: ('Bright green', 37, (75, 151, 75)), 38: ('Dark orange', 38, (160, 95, 53)), 39: ('Light bluish violet', 39, (193, 202, 222)), 40: ('Transparent', 40, (236, 236, 236)), 41: ('Tr. Red', 41, (205, 84, 75)), 42: ('Tr. Lg blue', 42, (193, 223, 240)), 43: ('Tr. Blue', 43, (123, 182, 232)), 44: ('Tr. Yellow', 44, (247, 241, 141)), 45: ('Light blue', 45, (180, 210, 228)), 47: ('Tr. Flu. Reddish orange', 47, (217, 133, 108)), 48: ('Tr. Green', 48, (132, 182, 141)), 49: ('Tr. Flu. Green', 49, (248, 241, 132)), 50: ('Phosph. White', 50, (236, 232, 222)), 100: ('Light red', 100, (238, 196, 182)), 101: ('Medium red', 101, (218, 134, 122)), 102: ('Medium blue', 102, (110, 153, 202)), 103: ('Light grey', 103, (199, 193, 183)), 104: ('Bright violet', 104, (107, 50, 124)), 105: ('Br. yellowish orange', 105, (226, 155, 64)), 106: ('Bright orange', 106, (218, 133, 65)), 107: ('Bright bluish green', 107, (0, 143, 156)), 108: ('Earth yellow', 108, (104, 92, 67)), 110: ('Bright bluish violet', 110, (67, 84, 147)), 111: ('Tr. Brown', 111, (191, 183, 177)), 112: ('Medium bluish violet', 112, (104, 116, 172)), 113: ('Tr. Medi. reddish violet', 113, (229, 173, 200)), 115: ('Med. yellowish green', 115, (199, 210, 60)), 116: ('Med. bluish green', 116, (85, 165, 175)), 118: ('Light bluish green', 118, (183, 215, 213)), 119: ('Br. yellowish green', 119, (164, 189, 71)), 120: ('Lig. yellowish green', 120, (217, 228, 167)), 121: ('Med. yellowish orange', 121, (231, 172, 88)), 123: ('Br. reddish orange', 123, (211, 111, 76)), 124: ('Bright reddish violet', 124, (146, 57, 120)), 125: ('Light orange', 125, (234, 184, 146)), 126: ('Tr. Bright bluish violet', 126, (165, 165, 203)), 127: ('Gold', 127, (220, 188, 129)), 128: ('Dark nougat', 128, (174, 122, 89)), 131: ('Silver', 131, (156, 163, 168)), 133: ('Neon orange', 133, (213, 115, 61)), 134: ('Neon green', 134, (216, 221, 86)), 135: ('Sand blue', 135, (116, 134, 157)), 136: ('Sand violet', 136, (135, 124, 144)), 137: ('Medium orange', 137, (224, 152, 100)), 138: ('Sand yellow', 138, (149, 138, 115)), 140: ('Earth blue', 140, (32, 58, 86)), 141: ('Earth green', 141, (39, 70, 45)), 143: ('Tr. Flu. Blue', 143, (207, 226, 247)), 145: ('Sand blue metallic', 145, (121, 136, 161)), 146: ('Sand violet metallic', 146, (149, 142, 163)), 147: ('Sand yellow metallic', 147, (147, 135, 103)), 148: ('Dark grey metallic', 148, (87, 88, 87)), 149: ('Black metallic', 149, (22, 29, 50)), 150: ('Light grey metallic', 150, (171, 173, 172)), 151: ('Sand green', 151, (120, 144, 130)), 153: ('Sand red', 153, (149, 121, 119)), 154: ('Dark red', 154, (123, 46, 47)), 157: ('Tr. Flu. Yellow', 157, (255, 246, 123)), 158: ('Tr. Flu. Red', 158, (225, 164, 194)), 168: ('Gun metallic', 168, (117, 108, 98)), 176: ('Red flip/flop', 176, (151, 105, 91)), 178: ('Yellow flip/flop', 178, (180, 132, 85)), 179: ('Silver flip/flop', 179, (137, 135, 136)), 180: ('Curry', 180, (215, 169, 75)), 190: ('Fire Yellow', 190, (249, 214, 46)), 191: ('Flame yellowish orange', 191, (232, 171, 45)), 192: ('Reddish brown', 192, (105, 64, 40)), 193: ('Flame reddish orange', 193, (207, 96, 36)), 195: ('Royal blue', 195, (70, 103, 164)), 196: ('Dark Royal blue', 196, (35, 71, 139)), 198: ('Bright reddish lilac', 198, (142, 66, 133)), 199: ('Dark stone grey', 199, (99, 95, 98)), 200: ('Lemon metalic', 200, (130, 138, 93)), 208: ('Light stone grey', 208, (229, 228, 223)), 209: ('Dark Curry', 209, (176, 142, 68)), 210: ('Faded green', 210, (112, 149, 120)), 211: ('Turquoise', 211, (121, 181, 181)), 212: ('Light Royal blue', 212, (159, 195, 233)), 213: ('Medium Royal blue', 213, (108, 129, 183)), 216: ('Rust', 216, (144, 76, 42)), 217: ('Brown', 217, (124, 92, 70)), 218: ('Reddish lilac', 218, (150, 112, 159)), 219: ('Lilac', 219, (107, 98, 155)), 220: ('Light lilac', 220, (167, 169, 206)), 221: ('Bright purple', 221, (205, 98, 152)), 222: ('Light purple', 222, (228, 173, 200)), 223: ('Light pink', 223, (220, 144, 149)), 224: ('Light brick yellow', 224, (240, 213, 160)), 225: ('Warm yellowish orange', 225, (235, 184, 127)), 226: ('Cool yellow', 226, (253, 234, 141)), 232: ('Dove blue', 232, (125, 187, 221)), 268: ('Medium lilac', 268, (52, 43, 117)), 301: ('Slime green', 301, (80, 109, 84)), 302: ('Smoky grey', 302, (91, 93, 105)), 303: ('Dark blue', 303, (0, 16, 176)), 304: ('Parsley green', 304, (44, 101, 29)), 305: ('Steel blue', 305, (82, 124, 174)), 306: ('Storm blue', 306, (51, 88, 130)), 307: ('Lapis', 307, (16, 42, 220)), 308: ('Dark indigo', 308, (61, 21, 133)), 309: ('Sea green', 309, (52, 142, 64)), 310: ('Shamrock', 310, (91, 154, 76)), 311: ('Fossil', 311, (159, 161, 172)), 312: ('Mulberry', 312, (89, 34, 89)), 313: ('Forest green', 313, (31, 128, 29)), 314: ('Cadet blue', 314, (159, 173, 192)), 315: ('Electric blue', 315, (9, 137, 207)), 316: ('Eggplant', 316, (123, 0, 123)), 317: ('Moss', 317, (124, 156, 107)), 318: ('Artichoke', 318, (138, 171, 133)), 319: ('Sage green', 319, (185, 196, 177)), 320: ('Ghost grey', 320, (202, 203, 209)), 321: ('Lilac', 321, (167, 94, 155)), 322: ('Plum', 322, (123, 47, 123)), 323: ('Olivine', 323, (148, 190, 129)), 324: ('Laurel green', 324, (168, 189, 153)), 325: ('Quill grey', 325, (223, 223, 222)), 327: ('Crimson', 327, (151, 0, 0)), 328: ('Mint', 328, (177, 229, 166)), 329: ('Baby blue', 329, (152, 194, 219)), 330: ('Carnation pink', 330, (255, 152, 220)), 331: ('Persimmon', 331, (255, 89, 89)), 332: ('Maroon', 332, (117, 0, 0)), 333: ('Gold', 333, (239, 184, 56)), 334: ('Daisy orange', 334, (248, 217, 109)), 335: ('Pearl', 335, (231, 231, 236)), 336: ('Fog', 336, (199, 212, 228)), 337: ('Salmon', 337, (255, 148, 148)), 338: ('Terra Cotta', 338, (190, 104, 98)), 339: ('Cocoa', 339, (86, 36, 36)), 340: ('Wheat', 340, (241, 231, 199)), 341: ('Buttermilk', 341, (254, 243, 187)), 342: ('Mauve', 342, (224, 178, 208)), 343: ('Sunrise', 343, (212, 144, 189)), 344: ('Tawny', 344, (150, 85, 85)), 345: ('Rust', 345, (143, 76, 42)), 346: ('Cashmere', 346, (211, 190, 150)), 347: ('Khaki', 347, (226, 220, 188)), 348: ('Lily white', 348, (237, 234, 234)), 349: ('Seashell', 349, (233, 218, 218)), 350: ('Burgundy', 350, (136, 62, 62)), 351: ('Cork', 351, (188, 155, 93)), 352: ('Burlap', 352, (199, 172, 120)), 353: ('Beige', 353, (202, 191, 163)), 354: ('Oyster', 354, (187, 179, 178)), 355: ('Pine Cone', 355, (108, 88, 75)), 356: ('Fawn brown', 356, (160, 132, 79)), 357: ('Hurricane grey', 357, (149, 137, 136)), 358: ('Cloudy grey', 358, (171, 168, 158)), 359: ('Linen', 359, (175, 148, 131)), 360: ('Copper', 360, (150, 103, 102)), 361: ('Medium brown', 361, (86, 66, 54)), 362: ('Bronze', 362, (126, 104, 63)), 363: ('Flint', 363, (105, 102, 92)), 364: ('Dark taupe', 364, (90, 76, 66)), 365: ('Burnt Sienna', 365, (106, 57, 9)), 1001: ('Institutional white', 1001, (248, 248, 248)), 1002: ('Mid gray', 1002, (205, 205, 205)), 1003: ('Really black', 1003, (17, 17, 17)), 1004: ('Really red', 1004, (255, 0, 0)), 1005: ('Deep orange', 1005, (255, 176, 0)), 1006: ('Alder', 1006, (180, 128, 255)), 1007: ('Dusty Rose', 1007, (163, 75, 75)), 1008: ('Olive', 1008, (193, 190, 66)), 1009: ('New Yeller', 1009, (255, 255, 0)), 1010: ('Really blue', 1010, (0, 0, 255)), 1011: ('Navy blue', 1011, (0, 32, 96)), 1012: ('Deep blue', 1012, (33, 84, 185)), 1013: ('Cyan', 1013, (4, 175, 236)), 1014: ('CGA brown', 1014, (170, 85, 0)), 1015: ('Magenta', 1015, (170, 0, 170)), 1016: ('Pink', 1016, (255, 102, 204)), 1017: ('Deep orange', 1017, (255, 175, 0)), 1018: ('Teal', 1018, (18, 238, 212)), 1019: ('Toothpaste', 1019, (0, 255, 255)), 1020: ('Lime green', 1020, (0, 255, 0)), 1021: ('Camo', 1021, (58, 125, 21)), 1022: ('Grime', 1022, (127, 142, 100)), 1023: ('Lavender', 1023, (140, 91, 159)), 1024: ('Pastel light blue', 1024, (175, 221, 255)), 1025: ('Pastel orange', 1025, (255, 201, 201)), 1026: ('Pastel violet', 1026, (177, 167, 255)), 1027: ('Pastel blue-green', 1027, (159, 243, 233)), 1028: ('Pastel green', 1028, (204, 255, 204)), 1029: ('Pastel yellow', 1029, (255, 255, 204)), 1030: ('Pastel brown', 1030, (255, 204, 153)), 1031: ('Royal purple', 1031, (98, 37, 209)), 1032: ('Hot pink', 1032, (255, 0, 191))}

    _BRICKCOLOURID_BY_ID = [1003, 1003, 332, 332, 332, 327, 327, 327, 1004, 1004, 1003, 1003, 1003, 339, 332, 327, 327, 21, 1004, 1004, 1003, 1003, 365, 365, 365, 365, 1014, 21, 21, 1004, 304, 304, 304, 365, 365, 1014, 1014, 1014, 1014, 1014, 313, 313, 1021, 1021, 365, 1014, 1014, 1014, 193, 1017, 313, 313, 1021, 1021, 1021, 1014, 1014, 12, 1017, 1017, 1020, 313, 1021, 1021, 310, 119, 1014, 1017, 1017, 1017, 1020, 1020, 1021, 1021, 119, 119, 119, 115, 1005, 1005, 1020, 1020, 1020, 1020, 1020, 119, 115, 115, 1009, 1009, 1020, 1020, 1020, 1020, 1020, 1009, 1009, 1009, 1009, 1009, 1003, 1003, 1003, 339, 332, 327, 327, 21, 1004, 1004, 1003, 149, 339, 339, 339, 154, 21, 21, 21, 1004, 26, 26, 141, 339, 365, 345, 21, 21, 21, 21, 304, 304, 304, 361, 192, 345, 1014, 193, 193, 331, 313, 313, 1021, 1021, 362, 345, 38, 193, 193, 193, 313, 313, 1021, 1021, 1021, 209, 209, 12, 105, 1017, 313, 313, 1021, 310, 310, 119, 119, 191, 191, 1017, 1020, 313, 1021, 310, 119, 119, 119, 115, 24, 24, 1020, 1020, 1021, 310, 119, 119, 115, 115, 190, 190, 1020, 1020, 1020, 1020, 1020, 119, 115, 115, 1009, 1009, 149, 149, 149, 339, 332, 327, 327, 21, 1004, 1004, 149, 149, 149, 339, 154, 350, 21, 21, 21, 1004, 26, 26, 361, 361, 154, 350, 1007, 21, 41, 331, 141, 141, 141, 361, 108, 345, 38, 41, 41, 331, 28, 28, 309, 301, 362, 362, 38, 133, 133, 133, 309, 309, 309, 37, 310, 209, 209, 12, 105, 105, 309, 309, 309, 310, 310, 119, 119, 1008, 191, 333, 1020, 309, 309, 310, 119, 119, 119, 115, 333, 24, 1020, 1020, 309, 310, 119, 119, 115, 115, 134, 190, 1020, 1020, 1020, 310, 119, 119, 115, 115, 134, 1009, 1011, 140, 312, 312, 316, 316, 316, 21, 1004, 1004, 1011, 140, 312, 312, 312, 312, 1007, 21, 41, 331, 140, 140, 140, 312, 355, 350, 1007, 41, 41, 331, 140, 140, 148, 148, 355, 344, 344, 41, 41, 331, 28, 28, 301, 301, 168, 176, 128, 123, 123, 331, 28, 28, 309, 310, 200, 200, 178, 18, 137, 137, 28, 28, 37, 310, 317, 200, 119, 180, 121, 121, 28, 28, 37, 310, 119, 119, 119, 1008, 121, 334, 1020, 28, 37, 310, 119, 119, 134, 134, 134, 334, 1020, 1020, 37, 310, 119, 119, 134, 134, 134, 157, 1011, 268, 308, 316, 316, 316, 316, 316, 1032, 1032, 1011, 268, 268, 312, 322, 124, 124, 124, 331, 331, 1011, 140, 268, 104, 104, 124, 124, 124, 331, 331, 1011, 306, 306, 302, 27, 344, 344, 338, 331, 331, 107, 306, 306, 27, 27, 153, 153, 338, 47, 331, 107, 28, 309, 210, 210, 138, 138, 18, 47, 337, 107, 28, 37, 210, 210, 318, 352, 352, 121, 225, 107, 28, 37, 210, 210, 323, 29, 352, 127, 334, 107, 1018, 37, 210, 210, 323, 328, 134, 334, 334, 1020, 1018, 1018, 210, 210, 323, 328, 157, 157, 157, 303, 308, 308, 308, 316, 316, 1015, 1015, 1032, 1032, 303, 308, 308, 308, 104, 198, 1015, 1015, 221, 1032, 196, 196, 196, 104, 104, 198, 124, 221, 221, 331, 196, 196, 110, 110, 219, 1023, 321, 221, 221, 331, 107, 196, 306, 305, 136, 136, 321, 22, 223, 337, 107, 107, 306, 151, 151, 179, 359, 223, 223, 337, 107, 107, 116, 116, 48, 318, 358, 352, 125, 337, 107, 107, 48, 48, 48, 29, 29, 346, 5, 1030, 107, 1018, 1018, 48, 48, 29, 328, 120, 226, 226, 1018, 1018, 1018, 48, 48, 29, 328, 44, 44, 44, 303, 303, 308, 308, 316, 1015, 1015, 1015, 1032, 1032, 303, 303, 308, 1031, 1031, 1015, 1015, 1015, 1032, 1032, 303, 1012, 110, 195, 104, 198, 321, 221, 221, 1032, 23, 1012, 110, 195, 219, 1023, 321, 221, 221, 1016, 23, 23, 195, 305, 112, 218, 218, 22, 22, 1016, 107, 107, 305, 305, 145, 146, 146, 343, 223, 337, 107, 116, 116, 116, 211, 131, 150, 111, 158, 337, 107, 1018, 116, 116, 211, 211, 319, 353, 100, 1030, 1018, 1018, 1018, 116, 211, 328, 328, 120, 120, 3, 1018, 1018, 1018, 116, 211, 328, 328, 1028, 120, 341, 303, 303, 1031, 1031, 1031, 1015, 1015, 1015, 1032, 1032, 303, 307, 1031, 1031, 1031, 1031, 1015, 1015, 1032, 1032, 307, 1012, 1012, 1031, 1031, 1031, 321, 221, 1016, 1016, 1012, 1012, 1012, 1012, 219, 1023, 321, 221, 1016, 1016, 315, 1012, 195, 305, 213, 218, 218, 22, 1016, 1016, 315, 315, 315, 102, 102, 146, 126, 343, 343, 330, 1013, 315, 116, 116, 102, 314, 220, 222, 222, 113, 1013, 1018, 116, 116, 211, 329, 319, 320, 9, 1025, 1018, 1018, 1018, 116, 211, 329, 118, 6, 347, 340, 1018, 1018, 1018, 1018, 1027, 1027, 1028, 1028, 1028, 1029, 1010, 1010, 1010, 1031, 1031, 1015, 1015, 1015, 1032, 1032, 307, 307, 307, 1031, 1031, 1031, 1015, 1015, 1032, 1032, 307, 307, 307, 1031, 1031, 1031, 1031, 1006, 1016, 1016, 307, 1012, 1012, 1031, 1031, 1023, 1006, 1006, 1016, 1016, 315, 315, 195, 305, 213, 218, 1006, 1006, 1016, 1016, 315, 315, 315, 102, 102, 43, 220, 343, 330, 330, 1013, 1013, 1013, 43, 43, 43, 220, 39, 342, 330, 1013, 1013, 232, 232, 232, 329, 212, 39, 325, 1025, 1018, 1018, 1018, 232, 232, 1027, 45, 336, 208, 50, 1019, 1018, 1018, 1027, 1027, 1027, 1027, 1028, 208, 1029, 1010, 1010, 1010, 1010, 1031, 1015, 1015, 1015, 1032, 1032, 1010, 1010, 1010, 1031, 1031, 1031, 1006, 1006, 1032, 1032, 1010, 307, 307, 1031, 1031, 1031, 1006, 1006, 1006, 1016, 1010, 1012, 1012, 1031, 1031, 1006, 1006, 1006, 1006, 1016, 315, 315, 195, 305, 1006, 1006, 1006, 1006, 1006, 1016, 1013, 315, 315, 102, 102, 1006, 1006, 1006, 1006, 330, 1013, 1013, 1013, 43, 43, 1026, 1026, 1026, 1026, 330, 1013, 1013, 1013, 43, 43, 212, 1024, 336, 143, 1025, 1019, 1019, 1019, 1024, 1024, 1024, 1024, 143, 335, 1001, 1019, 1019, 1019, 1019, 1027, 1027, 1024, 143, 1001, 1001]
    _IDS_BY_BRICKCOLOURID = {1003: [0, 1, 10, 11, 12, 20, 21, 100, 101, 102, 110], 332: [2, 3, 4, 14, 104, 204], 327: [5, 6, 7, 15, 16, 105, 106, 205, 206], 1004: [8, 9, 18, 19, 29, 108, 109, 119, 208, 209, 219, 308, 309], 339: [13, 103, 112, 113, 114, 123, 203, 213], 21: [17, 27, 28, 107, 116, 117, 118, 126, 127, 128, 129, 207, 216, 217, 218, 227, 307, 317], 365: [22, 23, 24, 25, 33, 34, 44, 124], 1014: [26, 35, 36, 37, 38, 39, 45, 46, 47, 55, 56, 66, 136], 304: [30, 31, 32, 130, 131, 132], 313: [40, 41, 50, 51, 61, 140, 141, 150, 151, 160, 161, 171], 1021: [42, 43, 52, 53, 54, 62, 63, 72, 73, 142, 143, 152, 153, 154, 162, 172, 182], 193: [48, 137, 138, 147, 148, 149], 1017: [49, 58, 59, 67, 68, 69, 159, 169], 12: [57, 157, 257], 1020: [60, 70, 71, 80, 81, 82, 83, 84, 90, 91, 92, 93, 94, 170, 180, 181, 190, 191, 192, 193, 194, 270, 280, 281, 290, 291, 292, 380, 390, 391, 490], 310: [64, 163, 164, 173, 183, 254, 263, 264, 273, 283, 293, 353, 363, 373, 383, 393], 119: [65, 74, 75, 76, 85, 165, 166, 174, 175, 176, 184, 185, 195, 265, 266, 274, 275, 276, 284, 285, 294, 295, 366, 374, 375, 376, 384, 385, 394, 395], 115: [77, 86, 87, 177, 186, 187, 196, 197, 277, 286, 287, 296, 297], 1005: [78, 79], 1009: [88, 89, 95, 96, 97, 98, 99, 198, 199, 299], 149: [111, 200, 201, 202, 210, 211, 212], 154: [115, 214, 224], 26: [120, 121, 220, 221], 141: [122, 230, 231, 232], 345: [125, 135, 145, 235], 361: [133, 222, 223, 233], 192: [134], 331: [139, 229, 239, 319, 329, 339, 349, 418, 419, 428, 429, 438, 439, 449, 529, 539], 362: [144, 244, 245], 38: [146, 236, 246], 209: [155, 156, 255, 256], 105: [158, 258, 259], 191: [167, 168, 268], 24: [178, 179, 279], 190: [188, 189, 289], 350: [215, 225, 325], 1007: [226, 316, 326], 41: [228, 237, 238, 318, 327, 328, 337, 338], 108: [234], 28: [240, 241, 340, 341, 350, 351, 360, 361, 370, 371, 381, 451, 461, 471], 309: [242, 250, 251, 252, 260, 261, 262, 271, 272, 282, 352, 452], 301: [243, 342, 343], 133: [247, 248, 249], 37: [253, 362, 372, 382, 392, 462, 472, 482], 1008: [267, 377], 333: [269, 278], 134: [288, 298, 386, 387, 388, 396, 397, 398, 487], 1011: [300, 310, 400, 410, 420, 430], 140: [301, 311, 320, 321, 322, 330, 331, 421], 312: [302, 303, 312, 313, 314, 315, 323, 413], 316: [304, 305, 306, 403, 404, 405, 406, 407, 504, 505, 604], 355: [324, 334], 148: [332, 333], 344: [335, 336, 435, 436], 168: [344], 176: [345], 128: [346], 123: [347, 348], 200: [354, 355, 365], 178: [356], 18: [357, 457], 137: [358, 359], 317: [364], 180: [367], 121: [368, 369, 378, 468], 334: [379, 389, 479, 488, 489], 157: [399, 497, 498, 499], 268: [401, 411, 412, 422], 308: [402, 501, 502, 503, 511, 512, 513, 602, 603, 612], 1032: [408, 409, 508, 509, 519, 608, 609, 618, 619, 629, 708, 709, 718, 719, 808, 809, 818, 819, 908, 909, 918, 919], 322: [414], 124: [415, 416, 417, 425, 426, 427, 526], 104: [423, 424, 514, 523, 524, 624], 306: [431, 432, 441, 442, 542, 552], 302: [433], 27: [434, 443, 444], 338: [437, 447], 107: [440, 450, 460, 470, 480, 540, 550, 551, 560, 561, 570, 571, 580, 650, 651, 660, 670], 153: [445, 446], 47: [448, 458], 210: [453, 454, 463, 464, 473, 474, 483, 484, 493, 494], 138: [455, 456], 337: [459, 549, 559, 569, 659, 669], 318: [465, 565], 352: [466, 467, 477, 567], 225: [469], 323: [475, 485, 495], 29: [476, 575, 576, 585, 595], 127: [478], 1018: [481, 491, 492, 581, 582, 590, 591, 592, 671, 680, 681, 682, 690, 691, 692, 771, 780, 781, 782, 790, 791, 792, 793, 880, 881, 882, 891, 892], 328: [486, 496, 586, 596, 685, 686, 695, 696], 303: [500, 510, 600, 601, 610, 611, 620, 700, 701, 710], 1015: [506, 507, 516, 517, 605, 606, 607, 615, 616, 617, 705, 706, 707, 716, 717, 805, 806, 807, 816, 817, 905, 906, 907], 198: [515, 525, 625], 221: [518, 527, 528, 537, 538, 627, 628, 637, 638, 727, 737], 196: [520, 521, 522, 530, 531, 541], 110: [532, 533, 622, 632], 219: [534, 634, 734], 1023: [535, 635, 735, 835], 321: [536, 546, 626, 636, 726, 736], 305: [543, 643, 652, 653, 743, 843, 943], 136: [544, 545], 22: [547, 647, 648, 747], 223: [548, 557, 558, 658], 151: [553, 554], 179: [555], 359: [556], 116: [562, 563, 661, 662, 663, 672, 673, 683, 693, 762, 763, 772, 773, 783], 48: [564, 572, 573, 574, 583, 584, 593, 594], 358: [566], 125: [568], 346: [577], 5: [578], 1030: [579, 679], 120: [587, 687, 688, 698], 226: [588, 589], 44: [597, 598, 599], 1031: [613, 614, 702, 703, 704, 712, 713, 714, 715, 723, 724, 725, 803, 804, 813, 814, 815, 823, 824, 825, 826, 833, 834, 904, 913, 914, 915, 923, 924, 925, 933, 934], 1012: [621, 631, 721, 722, 730, 731, 732, 733, 741, 831, 832, 931, 932], 195: [623, 633, 642, 742, 842, 942], 23: [630, 640, 641], 1016: [639, 649, 728, 729, 738, 739, 748, 749, 828, 829, 838, 839, 848, 849, 929, 939, 949], 112: [644], 218: [645, 646, 745, 746, 845], 145: [654], 146: [655, 656, 755], 343: [657, 757, 758, 857], 211: [664, 674, 675, 684, 694, 774, 784], 131: [665], 150: [666], 111: [667], 158: [668], 319: [676, 776], 353: [677], 100: [678], 3: [689], 1028: [697, 796, 797, 798, 897], 341: [699], 307: [711, 720, 810, 811, 812, 820, 821, 822, 830, 921, 922], 315: [740, 750, 751, 752, 761, 840, 841, 850, 851, 852, 940, 941, 951, 952], 213: [744, 844], 102: [753, 754, 764, 853, 854, 953, 954], 126: [756], 330: [759, 858, 859, 869, 959, 969], 1013: [760, 770, 860, 861, 862, 870, 871, 950, 960, 961, 962, 970, 971, 972], 314: [765], 220: [766, 856, 866], 222: [767, 768], 113: [769], 329: [775, 785, 875], 320: [777], 9: [778], 1025: [779, 879, 979], 118: [786], 6: [787], 347: [788], 340: [789], 1027: [794, 795, 885, 893, 894, 895, 896, 994, 995], 1029: [799, 899], 1010: [800, 801, 802, 900, 901, 902, 903, 910, 911, 912, 920, 930], 1006: [827, 836, 837, 846, 847, 916, 917, 926, 927, 928, 935, 936, 937, 938, 944, 945, 946, 947, 948, 955, 956, 957, 958], 43: [855, 863, 864, 865, 963, 964, 973, 974], 39: [867, 877], 342: [868], 232: [872, 873, 874, 883, 884], 212: [876, 975], 325: [878], 45: [886], 336: [887, 977], 208: [888, 898], 50: [889], 1019: [890, 980, 981, 982, 990, 991, 992, 993], 1026: [965, 966, 967, 968], 1024: [976, 983, 984, 985, 986, 996], 143: [978, 987, 997], 335: [988], 1001: [989, 998, 999]}

    square = lambda r255, g255, b255: f"\033[48;2;{r255};{g255};{b255}m   \033[0m"

    def __init__(self):
        self._id = None
        self._flowers = None
        self._recipe = None

        self._frgb = None
        self._rgb255 = None
    
        self._brickcolourid = None

    @classmethod
    def from_id(cls, id:int):
        new = cls()
        new._id = id
        return new
    
    @classmethod
    def from_rgb_float(cls, r:float, g:float, b:float):
        new = cls()
        new._frgb = (r, g, b)
        return new
    
    @classmethod
    def from_rgb255(cls, r255:int, g255:int, b255:int):
        new = cls()
        new._rgb255 = (r255, g255, b255)
        return new
    
    @classmethod
    def from_hex(cls, hex:str):
        new = cls()
        new._rgb255 = cls.hex_to_rgb255(hex)
        return new
    
    @classmethod
    def from_brickcolourname(cls, brickcolour:str):
        new = cls()
        new._brickcolourid = cls.brickcolourname_to_brickcolourid(brickcolour)
        return new
    
    @classmethod
    def from_brickcolourid(cls, brickcolourid:int):
        new = cls()
        new._brickcolourid = brickcolourid
        return new
    
    @classmethod
    def from_flowers(cls, red_flower:int, yellow_flower:int, blue_flower:int, white_flower:int):
        new = cls()
        new._flowers = (red_flower, yellow_flower, blue_flower, white_flower)
        return new

    @classmethod
    def from_recipe(cls, recipe:list[int]):
        new = cls()
        new._recipe = recipe
        return new
    
    # # Conversions
    # # USE frgb AS A BASE
    # # ALL COLOUR TYPES:
    # # flowers, recipe, id, frgb, rgb255, hex, brickcolour name, brickcolour id
    # VALIDATIONS

    @staticmethod
    def _validate_rgb255(func):
        """
        r255, g255, b255
        int 0-255
        """
        def wrapper(r255, g255, b255, *args, **kwargs):
            for val, name in zip((r255, g255, b255), ("r255", "g255", "b255")):
                if not isinstance(val, int):
                    raise TypeError(f"{name} must be an integer")
                if not (0 <= val <= 255):
                    raise ValueError(f"{name} must be in the range 0-255")
            return func(r255, g255, b255, *args, **kwargs)
        return wrapper
    
    @staticmethod
    def _validate_frgb(func):
        """
        r, g, b
        float 0-1
        """
        def wrapper(r, g, b, *args, **kwargs):
            for val, name in zip((r, g, b), ("r", "g", "b")):
                if not isinstance(val, float):
                    raise TypeError(f"{name} must be a float")
                if not (0 <= val <= 1):
                    raise ValueError(f"{name} must be in the range 0-1")
            return func(r, g, b, *args, **kwargs)
        return wrapper
    
    @staticmethod
    def _validate_hex(func):
        """
        hexv
        str len=6
        """
        def wrapper(hexv, *args, **kwargs):
            if not isinstance(hexv, str):
                raise TypeError(f"hexv must be a string")
            hexv = hexv.lstrip('#')
            if len(hexv) != 6:
                raise ValueError("Hex string must be 6 characters long")
            return func(hexv, *args, **kwargs)
        return wrapper
    
    @staticmethod
    def _validate_brickcolourname(func):
        """
        name
        str in list
        """
        def wrapper(name, *args, **kwargs):
            if not isinstance(name, str):
                raise TypeError(f"Brickcolour Name must be a string")
            if not name in PigmentColours._BRICKCOLOURS_BY_NAMES:
                raise ValueError("Brickcolour Name not found")
            return func(name, *args, **kwargs)
        return wrapper
    
    @staticmethod
    def _validate_brickcolourid(func):
        """
        bcid
        int in list
        """
        def wrapper(bcid, *args, **kwargs):
            if not isinstance(bcid, int):
                raise TypeError(f"Brickcolour ID must be an int")
            if not bcid in PigmentColours._BRICKCOLOURS_BY_BCID:
                raise ValueError("Brickcolour ID not found")
            return func(bcid, *args, **kwargs)
        return wrapper
    
    @staticmethod
    def _validate_ints(func):
        """
        any args (not kwargs)
        int or [int]
        """
        def wrapper(*args, **kwargs):
            def ismeowornot(x): # meow help
                if isinstance(x, int):
                    return True
                if isinstance(x, list) and all(isinstance(i, int) for i in x):
                    return True
                return False

            # Validate positional arguments
            for arg in args:
                if not ismeowornot(arg):
                    raise TypeError(f"Arg {arg} is not int or list of ints")

            # # Validate keyword arguments
            # for key, value in kwargs.items():
            #     if not ismeowornot(value):
            #         raise TypeError(f"Kwarg {key}:{value} is not int or list of ints")

            return func(*args, **kwargs)
        
        return wrapper


    # # completely analagous conversions
    
    # hex_to_rgb255 @staticmethod
    # rgb255_to_hex @staticmethod

    # brickcolourname_to_brickcolourid @staticmethod
    # brickcolourid_to_brickcolourname @staticmethod

    # # quantized conversions (top variant maps many:one), reverse maps one:one

    # frgb_to_rgb255 @staticmethod
    # rgb255_to_frgb @staticmethod
    
    # frgb_to_id @staticmethod
    # id_to_frgb @staticmethod

    # # one way quantized conversions
    
    # flowers_to_frgb @staticmethod

    # recipe_to_frgb @staticmethod

    # id_to_brickcolour @staticmethod

    # # multi-output reverses

    # brickcolour_to_ids @staticmethod

    @staticmethod
    @_validate_hex
    def hex_to_rgb255(hexv:str) -> tuple[int, int, int]:
        r255 = int(hexv[0:2], 16)
        g255 = int(hexv[2:4], 16)
        b255 = int(hexv[4:6], 16)
        return (r255, g255, b255)
    
    @staticmethod
    @_validate_rgb255
    def rgb255_to_hex(r255:int, g255:int, b255:int) -> str:
        return f"#{r255:02X}{g255:02X}{b255:02X}"


    @staticmethod
    @_validate_brickcolourname
    def brickcolourname_to_brickcolourid(name:str) -> int:
        return PigmentColours._BRICKCOLOURS_BY_NAMES[name][1]
    
    @staticmethod
    @_validate_brickcolourid
    def brickcolourid_to_brickcolourname(bcid:int) -> str:
        return PigmentColours._BRICKCOLOURS_BY_BCID[bcid][0]
    

    @staticmethod
    @_validate_frgb
    def frgb_to_rgb255(r:float, g:float, b:float) -> tuple[int, int, int]:
        r255 = floor(r*255+0.5)
        g255 = floor(g*255+0.5)
        b255 = floor(b*255+0.5)
        return (r255, g255, b255)

    @staticmethod
    @_validate_rgb255
    def rgb255_to_frgb(r255:int, g255:int, b255:int) -> tuple[float, float, float]:
        r = r255 / 255
        g = g255 / 255
        b = b255 / 255
        return (r, g, b)

    
    @staticmethod
    @_validate_frgb
    def frgb_to_id(r:float, g:float, b:float) -> int: ########################################################
        "the main thing (int, GBR order)"
        
        return int(floor(r*9+PigmentColours._ROUND_OFFSET[0]) + 10*floor(g*9+PigmentColours._ROUND_OFFSET[1]) + 100*floor(b*9+PigmentColours._ROUND_OFFSET[2]))

    @staticmethod
    @_validate_ints
    def id_to_frgb(id:int) -> tuple[float, float, float]:
        r = floor(id % 10) / 9
        g = floor((id % 100) / 10) / 9
        b = floor(id / 100) / 9
        return (r, g, b)
    
    @staticmethod
    @_validate_ints
    def id_to_rgb255(id:int) -> tuple[int, int, int]:
        return PigmentColours.frgb_to_rgb255(*PigmentColours.id_to_frgb(id))
    
    @staticmethod
    @_validate_ints
    def flowers_to_frgb(rc:int, yc:int, bc:int, wc:int) -> tuple[float, float, float]:
        counts = (rc, yc, bc, wc)
        tot = sum(counts)

        z_mix = [0.0] * mixbox.LATENT_SIZE
        for i in range(len(z_mix)):
            z_mix[i] = sum(counts[j]/tot*PigmentColours._FLOWERS[j][i] for j in range(4))
            
        return mixbox.latent_to_float_rgb(z_mix)

    @staticmethod
    @_validate_ints
    def recipe_to_frgb(ids:list[int]):
        arr = [PigmentColours.frgb_to_rgb255(*PigmentColours.id_to_frgb(col)) for col in ids]
        frac = 1/len(ids)

        n = mixbox.LATENT_SIZE
        z_mix = [0] * n

        for i, rgb255 in enumerate(arr):
            z_mix = [z_mix[i] + frac*mixbox.rgb_to_latent(rgb255)[i] for i in range(n)]

        return mixbox.latent_to_float_rgb(tuple(z_mix))

    @staticmethod
    @_validate_ints
    def id_to_brickcolourid(id:int) -> int:
        return PigmentColours._BRICKCOLOURID_BY_ID[id]
    
    @staticmethod
    @_validate_brickcolourid
    def brickcolourid_to_ids(brickcolourid) -> list[int]:
        return PigmentColours._IDS_BY_BRICKCOLOURID[brickcolourid]

    # property methods (@property)
        self._id = None
        self._flowers = None
        self._recipe = None

        self._frgb = None
        self._rgb255 = None
    
        self._brickcolourid = None

    @property
    def frgb(self) -> tuple[float, float, float]: # type: ignore
        if self._id:            return PigmentColours.id_to_frgb(self.id)
        if self._flowers:       return PigmentColours.flowers_to_frgb(*self.flowers)
        if self._recipe:        return PigmentColours.recipe_to_frgb(self.recipe)
        if self._frgb:          return self._frgb
        if self._rgb255:        return PigmentColours.rgb255_to_frgb(*self.rgb255)

    @property
    def id(self) -> int: # type: ignore
        if self._id:            return self._id
        if self.frgb:           return self.frgb_to_id(*self.frgb)

    @property
    def flowers(self) -> tuple[int, int, int, int]: # type: ignore
        if self._flowers:       return self._flowers

    @property
    def recipe(self) -> list[int]: # type: ignore
        if self._recipe:        return self._recipe

    @property
    def rgb255(self) -> tuple[int, int, int]: # type: ignore
        if self._rgb255:        return self._rgb255
        if self.frgb:           return PigmentColours.frgb_to_rgb255(*self.frgb)

    @property
    def brickcolourid(self) -> int: # type: ignore
        if self._brickcolourid: return self._brickcolourid
        if self.id:             return PigmentColours.id_to_brickcolourid(self.id)

    @property
    def brickcolourname(self) -> str: # type: ignore
        if self.brickcolourid:  return PigmentColours.brickcolourid_to_brickcolourname(self.brickcolourid)

    @property
    def ids(self) -> list[int]: # type: ignore
        if self.brickcolourid:  return PigmentColours.brickcolourid_to_ids(self.brickcolourid)

    @property
    def hex(self) -> str: # type: ignore
        if self.rgb255:         return PigmentColours.rgb255_to_hex(*self.rgb255)

    @property
    def colour_source(self) -> str: # type: ignore
        if self._id: return "id"
        if self._flowers: return "flowers"
        if self._recipe: return "recipe"
        if self._frgb: return "frgb"
        if self._rgb255: return "rgb255"
        if self._brickcolourid: return "brickcolourid"
        return ""
    
    @property
    def colour_source_value(self):
        if self._id: return self._id 
        if self._flowers: return self._flowers 
        if self._recipe: return self._recipe 
        if self._frgb: return self._frgb 
        if self._rgb255: return self._rgb255 
        if self._brickcolourid: return self._brickcolourid 

    # convert methods (instance methods)

    def _clear_colour_attr(self):
        self._id = None
        self._flowers = None
        self._recipe = None
        self._frgb = None
        self._rgb255 = None
        self._brickcolourid = None

    def to_id(self):
        new_id = self.id
        self._clear_colour_attr()
        self._id = new_id
    
    def to_frgb(self):
        new_frgb = self.frgb
        self._clear_colour_attr()
        self._frgb = new_frgb
        
    def to_rgb255(self):
        new_rgb255 = self.rgb255
        self._clear_colour_attr()
        self._rgb255 = new_rgb255
    
    def to_brickcolour(self):
        new_brickcolourid = self.brickcolourid
        self._clear_colour_attr()
        self._brickcolourid = new_brickcolourid

    ### OPERATIONS ###
    def __repr__(self):
        return f"{PigmentColours.square(*self.rgb255)} {self.hex} ({self.id} {self.brickcolourname}) - {self.colour_source_value} <PigmentColours ({self.colour_source})>"

    def __sub__(self, colour2):
        return PigmentColours.from_rgb_float(*(self.frgb[i] - colour2.frgb[i] for i in range(3)))

    def __eq__(self, colour2):
        return self.colour_source == colour2.colour_source and self.colour_source_value == colour2.colour_source_value

    @staticmethod
    def distance(colour1, colour2):
        res = colour1 - colour2
        r, g, b = res.frgb
        return (r**2+g**2+b**2)**0.5
    
    def distance_to_id(self):
        idcol = PigmentColours.from_id(self.id)

        return self.distance(self, idcol)
        

    ### PRINT FUNCTIONS ###
    def print_recip_result(self):
        idcol = PigmentColours.from_id(self.id)

        idsquare = PigmentColours.square(*idcol.rgb255)
        rawsquare = PigmentColours.square(*self.rgb255)
        dist = PigmentColours.distance(self, idcol)
        match self.colour_source:
            case "flowers":
                print(f"{idsquare} {self.id} {self.brickcolourname} - {rawsquare} {self.flowers} ~{dist:0.3f}")
            case "recipe":
                print(f"{idsquare} {self.id} {self.brickcolourname} - {rawsquare} {self.recipe} ~{dist:0.3f}")

    def print_colour(self):
        rawsquare = PigmentColours.square(*self.rgb255)
        print(f"{rawsquare} {self.hex} {self.id} {self.brickcolourname}")
