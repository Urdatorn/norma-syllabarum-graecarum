import os

for file in os.listdir("norma_macronize"):
    if file.endswith(".txt"):
        input_path = os.path.join("norma_macronize", file)
        output_path = input_path
        with open(input_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()
            text = text.replace("[", "").replace("]", "").replace("{", "").replace("}", "")
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(text)
            
