import nltk

from gensim.models import Word2Vec
from nltk.corpus import stopwords

import re

paragraph=""" Nature is one of the most beautiful and precious gifts of God to humanity. 
              It includes everything around us, such as trees, plants, flowers, mountains, rivers, oceans, forests, animals, birds, and the sky. 
              Nature makes our planet beautiful, peaceful, and full of life. The green forests provide fresh air,
              while rivers and lakes supply water to humans, animals, and plants. The sun gives us light and warmth, 
              and the moon and stars make the night sky look wonderful. Colorful flowers spread fragrance and beauty everywhere, 
              while birds sing sweet songs that make us feel happy and relaxed. Nature plays a very important role in maintaining the balance 
              of our environment. Trees absorb carbon dioxide and release oxygen, helping us breathe fresh air. Rain provides water for agriculture and 
              supports the growth of plants and crops. Mountains, forests, and oceans provide homes for thousands of species of animals and plants. 
              Spending time in nature can reduce stress, improve our mood, and help us feel calm and refreshed. However, human activities such as deforestation, 
              air pollution, water pollution, plastic waste, and excessive use of natural resources are damaging the environment. Climate change is also affecting weather patterns, 
              wildlife, and ecosystems around the world. If we continue to harm nature, future generations may face serious environmental problems. Therefore, it is our responsibility 
              to protect and preserve nature. We should plant more trees, save water and electricity, reduce plastic use, recycle waste, and keep our surroundings clean. We should also 
              protect forests and wildlife and encourage others to care for the environment. Small actions taken by each person can make a big difference in protecting our planet. 
              Nature teaches us the importance of peace, patience, beauty, and balance. It provides us with food, water, air, and many other resources that are essential for life."""


text = re.sub(r'\[[0-9]*\]',' ',paragraph)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

sentances=nltk.sent_tokenize(text)

sentances=[nltk.word_tokenize(sentance) for sentance in sentances]

for i in range(len(sentances)):
    sentances[i]=[word for word in sentances[i] if word not in stopwords.words('english')]

model=Word2Vec(sentances, min_count=1)


words = model.wv.key_to_index

vector = model.wv['nature']

similar = model.wv.most_similar('Nature')

similar = model.wv.most_similar('birds', topn=5)

similar = model.wv.most_similar('trees')

similar = model.wv.most_similar('son')









































similar = model.ww.most_similar('birds')

similar = model.ww.most_similar('Trees')

similar = model.ww.most_similar('water')
