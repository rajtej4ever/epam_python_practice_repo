text= """tHis iz your homeWork, copy these Text to variable.



 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

normalized_text=text.lower()
normalized_text=normalized_text.replace("iz","is").capitalize()
print("Normalized text :",normalized_text)
count_whitespace_characters = normalized_text.count(' ')
print("White space character count:",count_whitespace_characters)

last_words = []
for sentence in normalized_text.split('.'):
    if sentence.strip():
        last_words.append(sentence.split()[-1])
additional_sentence_to_add = " ".join(last_words) + "."
print("Additional sentence to be added:", additional_sentence_to_add)