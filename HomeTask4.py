def normalize_text(text):
    return text.lower()

def fix_misspelling(text):
    return text.replace("iz", "is")

def count_whitespace_characters(text):
    return text.count(' ')

def create_additional_sentence(text):
    last_words = [sentence.split()[-1] for sentence in text.split('.') if sentence.strip()]
    return " ".join(last_words) + "."

text = """tHis iz your homeWork, copy these Text to variable.

 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

normalized_text = normalize_text(text)
normalized_text = fix_misspelling(normalized_text).capitalize()

print("Normalized text:", normalized_text)

num_whitespace_characters = count_whitespace_characters(normalized_text)
print("Whitespace character count:", num_whitespace_characters)

additional_sentence = create_additional_sentence(normalized_text)
print("Additional sentence to be added:", additional_sentence)