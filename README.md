# L3T05 - Natural Language Processing
# Garden Path Sentences Analysis

## Overview
This task involves studying garden path sentences, which are sentences that initially lead the reader to interpret them in one way but then require the reader to re-parse them in a different way. The Python script `garden.py` is used to identify and analyze garden path sentences by tokenizing each sentence and performing named entity recognition (NER) using the spaCy library.

### Garden Path Sentences
- **Introduction**: Read about garden path sentences and study examples provided on Wikipedia to understand their structure and characteristics.
- **Identified Sentences**: Find at least 2 garden path sentences from the web or create your own. Store these sentences in a list called `gardenpathSentences`.
  - Example sentences:
    - "The old man the boats."
    - "The horse raced past the barn fell."

### Instructions
#### Setup and Installation
1. **Create Python Script**
   - Create a new Python file called `garden.py` and save it to your designated folder for this task.

2. **Adding Sentences**
   - Store the identified or created garden path sentences in a list called `gardenpathSentences` within the `garden.py` script.
   - Example:
     ```python
     gardenpathSentences = [
         "The old man the boats.",
         "The horse raced past the barn fell."
     ]
     ```

3. **Tokenization and Named Entity Recognition**
   - Tokenize each sentence in the list and perform named entity recognition using the spaCy library.
   - Examine how spaCy categorizes each sentence and print the meaning of entities using `spacy.explain` for entities that are not understood.

4. **Analysis**
   - Analyze the categorization and explanations provided by spaCy for each identified entity in the garden path sentences.

5. **Commenting on Entities**
   - At the bottom of the `garden.py` script, write a comment about two entities that you looked up.
     - For each entity, answer the following questions:
       - What was the entity and its explanation that you looked up?
       - Did the entity make sense in terms of the word associated with it?

### Running the Script
1. **Execute Python Script**
   - Run the `garden.py` script to tokenize sentences, perform named entity recognition, and analyze garden path sentences.

### Dependencies
- Python 3.x
Ensure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/).
- spaCy library
Install using the following   
``` pip install spaCy ```  
- Download the language model using the following  
```python -m spacy download en_core_web_sm```  



