COLOUR_TO_CODE = {
    "absolutezero": "#0048ba",
    "acidgreen": "#b0bf1a",
    "aliceblue": "#f0f8ff",
    "alizarincrimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antiqueWhite": "#faebd7",
    "apricot": "#fbceb1",
    "aqua": "#00ffff"
}

print(COLOUR_TO_CODE)

# Prompt the user for colour names and print the corresponding hex codes
colour = input("Enter Colour: ").lower()
while colour != "":
    try:
        print(COLOUR_TO_CODE[colour])
    except KeyError:
        print("Invalid colour")
    colour = input("Enter Colour: ").lower()
