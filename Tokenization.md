## Tokens
**Tokens** are small units of data used to train Generative AI language models like GPT4 and help them understand adn generate language. This data may take the form of whole words, subwords, and other content.

By analyzing tokens, models can understand the structure and semantics of text. The process of making raw data like text trainable for language models is know as **Tokenization**. This may include splitting text into individual words.

Using the tokenized data, language models can learn patterns and relationships between small units of data in the context of large amounts of data. This helops the model predict and generate new content based on what it learned.

## Tokenize some Text

- Create a new `tokens.py` file
- Import the `tokenize` library with the following code:
```py
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
```

- Use the code below to perform a simple tokenization task:
```py
smaple_text = "I love programming"
tokens = word_tokenize(sample_text)

print('Tokens:', tokens)
```
Your uotput should return a list of strings that represent the tokens in the `sample_text`.