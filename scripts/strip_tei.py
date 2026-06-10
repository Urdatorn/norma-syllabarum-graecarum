import re

with open("norma_syllabify/pindar.txt", "r") as f:
    text = f.readlines()

cleaned = []
for line in text:
    clean = re.search(r"\[.*", line)
    if clean:
        clean = clean.group(0).replace("<l>", "").replace("</l>", "").replace("#", "")
        cleaned.append(clean)

for line in cleaned:
    print(line)
    
# overwrite old file with cleaned version
with open("norma_syllabify/pindar_fix.txt", "w") as f:
    for line in cleaned:
        f.write(line + "\n")