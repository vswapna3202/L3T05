"""
This code processes garden path sentences using spaCy.
"""
# Import spacy, this will work if spaCy is installed
import spacy

# Load spaCy english model
nlp = spacy.load("en_core_web_sm")

# Store gardenpathSentences in a list
# Identified two gardenpathSentences and added more sentences to list
gardenpathSentences = [
    "The old man the boat.",
    "The complex houses married and single soldiers and their families.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",
]

# For every sentence in gardenPathSentence
for i, sentence in enumerate(gardenpathSentences):

    # Process the sentence using spaCy's NLP(natural language processing) pipeline
    doc = nlp(sentence)

    # Tokenization
    tokens = [token.orth_ for token in doc]

    # Named entity recognition (NER)
    entities = [(ent.orth_, ent.label_) for ent in doc.ents]

    print(f"\nSentence {i + 1} - Tokens: {tokens}")
    print(f"Named Entities: {entities}")

    # Explain entities
    for ent_orth, ent_label in entities:
        explanation = spacy.explain(ent_label)
        print(f"Explanation for entity '{ent_orth}' ({ent_label}): {explanation}")

# At the bottom of your file, write a comment about two entities that you looked up. For each entity
# answer the following questions:
# What was the entity and its explanation that you looked up?
# Did the entity make sense in terms of the word associated with it?
#
# Entity looked up was: 'PERSON'
# Explanation for entity : People including fictional
# Assessment: Yes, the entity 'PERSON' makes sense in terms of word associated with it i.e. 'Mary'
# and 'Jill' were identified as person in the sentences.
#
# Entity looked up was: 'GPE' (Geopolitical Entity)
# Explanation for entity: Countries, cities, states
# Assessment: Yes, the entity 'GPE' makes sense in terms of word associated with it i.e.
# 'Mississippi' is correctly identified as GPE in the sentences.
