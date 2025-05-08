from sumy.nlp.tokenizers import Tokenizer
import nltk
nltk.download('punkt')
tokenizer = Tokenizer("en")

sentences = tokenizer.to_sentences("Hello, this is GeeksForGeeks! We are a computer science portal for " \
"geeks, offering a wide range of articles, tutorials, and resources on various topics in computer science "
"and programming. Our mission is to provide quality education and knowledge sharing to help you excel in " \
"your career and academic pursuits. Whether you're a beginner looking to learn the basics of coding or an " \
"experienced developer seeking advanced concepts, GeeksForGeeks has something for everyone. ")
for sentence in sentences:
    print(tokenizer.to_words(sentence))