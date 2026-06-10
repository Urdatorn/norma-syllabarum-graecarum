import os

for file in os.listdir("norma_syllabify"):
    if file.endswith(".txt") and not file.endswith("_macrons.txt"):
        input_path = os.path.join("norma_syllabify", file)
        output_path = input_path
        with open(input_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()
            text = text.replace("^", "").replace("_", "")
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(text)
            
