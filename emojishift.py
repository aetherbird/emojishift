#!/usr/bin/python3

input_forstring = input("Define Input > ")
print(f"\n\nTranslation Level: \n\n1. Light: Letters and text only\n2. Standard: Apply glyphs and letters\n3. Deep: Apply maximum glyphing\n\n")
input_parse_level = input("Select your translation level (default 2):")
if not input_parse_level:
    input_parse_level = "2"

if input_parse_level not in ["1", "2", "3"]:
    print("Invalid input, defaulting to standard parse (2)")
    input_parse_level = "2"

string_to_shift = str(input_forstring)

alpha_translation_dict_std = {
    "a": "🇦",
    "b": "🇧",
    "c": "🇨",
    "d": "🇩",
    "e": "🇪",
    "f": "🇫",
    "g": "🇬",
    "h": "🇭",
    "i": "🇮",
    "j": "🇯",
    "k": "🇰",
    "l": "🇱",
    "m": "🇲",
    "n": "🇳",
    "o": "🇴",
    "p": "🇵",
    "q": "🇶",
    "r": "🇷",
    "s": "🇸",
    "t": "🇹",
    "u": "🇺",
    "v": "🇻",
    "w": "🇼",
    "x": "🇽",
    "y": "🇾",
    "z": "🇿"
}

def light_parse(string_to_shift):
    for in_a, out_a in alpha_translation_dict_std.items():
        string_to_shift = string_to_shift.replace(in_a, out_a)
    return string_to_shift

def standard_parse(string_to_shift):
    for in_a, out_a in alpha_translation_dict_std.items():
        string_to_shift = string_to_shift.replace(in_a, out_a)
    return string_to_shift

def deep_parse(string_to_shift):
    for in_a, out_a in alpha_translation_dict_std.items():
        string_to_shift = string_to_shift.replace(in_a, out_a)
    return string_to_shift

if input_parse_level == "1":
    string_to_shift = light_parse(string_to_shift)
elif input_parse_level == "2":
    string_to_shift = standard_parse(string_to_shift)
elif input_parse_level == "3":
    string_to_shift = deep_parse(string_to_shift)

print(f" > {string_to_shift}")

