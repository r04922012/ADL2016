import tf_glove, zipfile
import tensorflow as tf
import sys

model = tf_glove.GloVeModel(embedding_size = 100, context_size = 10)

with open(sys.argv[1],'r') as input_file:
	for line in input_file:
	  words = line.split(' ')
corpus = [words[1:]]

model.fit_to_corpus(corpus)
model.train(num_epochs = 150, log_dir = "tmp_glove")

with open('tmp_dir/tmp_glove.txt','w') as output:
	for word_index in xrange(len(model.words)):
	  output.write(model.words[word_index])
	  for embed_dimension in xrange(model.embeddings.shape[1]):
	    output.write(' {}'.format(model.embeddings[word_index][embed_dimension]))
	  output.write('\n')
