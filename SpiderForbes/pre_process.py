import json
import re
import nltk
import BeautifulSoup


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from stanfordcorenlp import StanfordCoreNLP

from pypbe import pyBPE


# nltk.download('all')



def read_parse_content(file_name):

    with open(file_name, 'r') as f:
        temp = json.loads(f.read())
        document = eval(temp)["_values"]["content"]
        soup = BeautifulSoup(document, "html.parser")
        for s in soup(['script', 'style']):
            s.decompose()
        document = ' '.join(soup.stripped_strings)
        document = re.sub('\n', ' ', document)
        # contents = str(content).split(".")
        document = document.strip()
        sentences = nltk.sent_tokenize(document)
        sentences = [sentence.strip() for sentence in sentences]
    return sentences


def clean_data_form_html(content):
    if content is not None:
        # Convert text to lowercase
        content = content.lower()
        # Remove numbers
        content = re.sub(r'\d+', '', content)
        # Remove punctuation
        content = re.sub(r'[^\w\s]', '', content)
        # Remove stop words
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(content)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        # Stemming
        stemmer = PorterStemmer()
        stemmed_sentence = []
        for word in filtered_sentence:
            stemmed_sentence.append(stemmer.stem(word))
        return stemmed_sentence

def remove_company(content):
    # tag sentences and use nltk's Named Entity Chunker
    tagged_sentence = nltk.pos_tag(content)
    ne_chunked_sent = nltk.ne_chunk(tagged_sentence)

    for tagged_tree in ne_chunked_sent:
        # extract only chunks having NE labels
        if hasattr(tagged_tree, 'label'):
            entity_name = ' '.join(c[0] for c in tagged_tree.leaves())  # get NE name
            entity_type = tagged_tree.label()  # get NE category
            if entity_type == "ORGANIZATION":
                content.remove(entity_name)

    return content

def bpe(content):
    # creates a vocab file sorted by frequency, one word per line
    pyBPE.create_vocab_file(content,"vocab")

    # Creates a BPE codes file
    pyBPE.create_bpe_file(content, 256,"code")

    bpe = pyBPE("vocab", "vocab")
    bpe.load()
    content = bpe.apply_bpe(content)

    return content

def preprocess(file_name):
    sentences = read_parse_content(file_name)
    cleaned_document = []

    for sentence in sentences:
        cleaned_sentence = clean_data_form_html(sentence)
        removed_company_sentence = remove_company(cleaned_sentence)
        # bpe(removed_company_sentence)
        cleaned_document.append(removed_company_sentence)

    return cleaned_document

if __name__ == '__main__':
    file_name = "spiders/0_.json"
    sentences = preprocess(file_name)







