# SpiderForbes

This repository contains two tasks:

1. Write a web crawler to crawl all news from www.forbes.com/business. Save each piece of the article as one txt document.
   - Use [scrapy](https://docs.scrapy.org/en/latest/) framework to realize page jump and dynamic infinite loading.
   - Crawled 62 [articles](https://github.com/martyLY/SpiderForbes/tree/main/SpiderForbes/spiders).

2. Choose 1 article(0_.json) from step 1 output, which talks about any companies. Write codes to do the following pre-processing steps, the specific operation on [one](https://github.com/martyLY/SpiderForbes/blob/main/SpiderForbes/pre_process.py) and [two](https://github.com/martyLY/SpiderForbes/blob/main/SpiderForbes/preprocess.sh).
   - Remove all company names in the article: Use [Stanford NLP](https://stanfordnlp.github.io) NER module to recognize entity as 'Organization', then remove
   - Lowercase the words
   - Remove punctuation and remove numbers
   - Tokenization
   - Remove stop words 
   - Stemming and lemmatization
   - BPE
  
