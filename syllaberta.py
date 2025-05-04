import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("Ericu950/SyllaBERTa", trust_remote_code=True)
model = AutoModelForMaskedLM.from_pretrained("Ericu950/SyllaBERTa", trust_remote_code=True)

# Encode a sentence
text = "Κατέβην χθὲς εἰς Πειραιᾶ μετὰ Γλαύκωνος τοῦ Ἀρίστωνος"
tokens = tokenizer.tokenize(text)
print(tokens)

# Insert a mask at random
import random
tokens[random.randint(0, len(tokens)-1)] = tokenizer.mask_token
masked_text = tokenizer.convert_tokens_to_string(tokens)

# Predict masked token
inputs = tokenizer(masked_text, return_tensors="pt", padding=True, truncation=True)
inputs.pop("token_type_ids", None)
with torch.no_grad():
    outputs = model(**inputs)

# Fetch prediction
logits = outputs.logits
mask_token_index = (inputs['input_ids'] == tokenizer.mask_token_id).nonzero(as_tuple=True)[1]
top_tokens = logits[0, mask_token_index].topk(5, dim=-1).indices.squeeze(0)
predicted = tokenizer.convert_ids_to_tokens(top_tokens.tolist())

print("Top predictions:", predicted)
