#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Alumni Survey Project LDA
#Cooper Project
#February 2017

import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

filename = '/Users/jessicamarshall/Desktop/DataScienceIS/CUProject/datasets/value_cooper.xlsx'
data = pd.read_excel(filename, header = None, squeeze = 1)
#data_list = list(data.values.flatten())

a = data.isnull().values.any()
if a == True:
    print(a)

n_features = 1000;     #to start, can change
n_topics = 3;
n_samples = data.size
n_top_words = 15;

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()

####################

from sklearn.feature_extraction import text 

#stop_words = text.ENGLISH_STOP_WORDS.union('cooper')    

####### LDA ########  
    
# Use tf features for LDA.
print("Extracting tf features for LDA...")


#WITH FUNKY STOP WORDS
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=1, max_features=n_features, stop_words = text.ENGLISH_STOP_WORDS.union(['cooper', 'students', 'faculty', 'free', 'value', 'critical', 'thinking', 'education', 'work', 'school', 'skills', 'experience', 'union', 'learning', 'think', 'tuition', 'professors', 'time', 'student', 'learn', 'small', 'community', 'ability', 'learned', 'problem', 'solving', 'life', 'art', 'ideas', 'body', 'institution', 'quality', 'engineering', 'environment', 'career', 'peers', 'strong', 'different', 'debt', 'creative', 'rigor', 'rigorous', 'diverse', 'working', 'classes', 'people', 'exposure', 'focus', 'good', 'helped', 'great', 'class', 'did', 'like', 'world', 'new', 'technical', 'prepared', 'scholarship', 'hard', 'years', 'taught', 'way', 'unique', 'critically', 'freedom', 'program', 'allowed', 'challenging', 'lot', 'able', 'having', 'academic', 'professional', 'valued', 'classmates', 'ethic', 'real', 'field', 'high', 'study', 'architecture', 'undergraduate', 'opportunity', 'valuable', 'problems', 'nyc', 'research', 'design', 'really', 'diversity', 'commitment', 'intelligent', 'intellectual' 'graduate', 'dedication', 'access', 'passionate', 'culture', 'appreciate', 'amazing', 'better', 'experiences', 'understanding', 'opportunities', 'artists', 'foundation', 'major', 'degree', 'course', 'difficult', 'smart', 'institutions', 'graduate', 'intellectual', 'merit', 'city', 'development', 'lab', 'schools', 'pursue', 'teaching', 'job', 'succeed', 'arts', 'values', 'explore', 'communication', 'attended', 'college', 'knowledge', 'practical', 'colleagues', 'teamwork', 'group', 'future', 'resources', 'information', 'provide', 'engaged', 'approach', 'fundamentals', 'practice', 'dr', 'curriculum', 'educational', 'studies', 'artist', 'emphasis', 'tough', 'reputation', 'teachers', 'disciplines', 'engaging', 'talent', 'challenges', 'material', 'dedicated', 'excellent', 'support', 'unparalleled', 'challenged', 'truly', 'important', 'independent', 'best', 'interaction', 'didn', 've', 'talented', 'professor', 'leadership', 'teach', 'courses', 'projects', 'extremely', 'focused', 'helpful', 'independence', 'analytical', 'engagement', 'general', 'challenge', 'presentations', 'humanities', 'cu', 'perspective', 'computer', 'interdisciplinary', 'grad', 'especially', 'generally', 'humanities', 'incredible', 'brilliant', 'don', 'presentation', 'village', 'particularly', 'engineers', 'highly', 'importance', 'staff', 'civic', 'skill', 'demanding', 'artistic', 'atmosphere', 'graduating', 'fostered', 'fact', 'artistic', 'cost', 'writing', 'connections', 'critique', 'studio', 'discourse', 'instilled', 'thinker', 'curiosity', 'graduated', 'long', 'paid', 'coursework', 'background', 'provided', 'received', 'committed', 'higher', 'engineer', 'mentors', 'teacher', 'creativity', 'grateful', 'mission', 'breadth', 'status', 'collaboration', 'paying', 'shop', 'excellence', 'appreciation', 'programs', 'wealth', 'graduation', 'facilities', 'studios', 'undergrad', 'techniques', 'interviews', 'creatively', 'competitive', 'project', 'resume', 'invaluable']))

#NORMAL BORING STOP WORDS
#tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=n_features, stop_words = text.ENGLISH_STOP_WORDS)


tf = tf_vectorizer.fit_transform(data)
lda_stop_words = tf_vectorizer.get_stop_words()

print("Fitting LDA models with tf features, "
      "n_samples=", n_samples, " and n_features=", n_features)
lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=5,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
lda.fit(tf)

#outputs
print("\nTopics in LDA model:")
tf_feature_names = tf_vectorizer.get_feature_names()
lda_stop_words = tf_vectorizer.get_stop_words()
print_top_words(lda, tf_feature_names, n_top_words)
#print("\nStop words:")
#print(lda_stop_words)
####### NMF ########  

# Use tf-idf features for NMF.
#print("Extracting tf-idf features for NMF...")
#tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
#                                   max_features=n_features,
#                                   stop_words='english') 
#tfidf = tfidf_vectorizer.fit_transform(data)


#print("Fitting the NMF model with tf features, "
#      "n_samples=", n_samples, " and n_features=", n_features)
#nmf = NMF(n_components=n_topics, random_state=1,
#          alpha=.1, l1_ratio=.5).fit(tfidf)

#print("\nTopics in NMF model:")
#tfidf_feature_names = tfidf_vectorizer.get_feature_names()
#print_top_words(nmf, tfidf_feature_names, n_top_words)

