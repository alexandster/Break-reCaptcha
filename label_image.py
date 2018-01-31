import tensorflow as tf
import argparse
import os.path
import re
import sys
import tarfile
import PIL

def checkImage (imageToCheck):
    image_path = imageToCheck

    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    label_lines = [line.rstrip() for line
                        in tf.gfile.GFile("./tf_files_galaxy/retrained_labels.txt")]

    with tf.gfile.FastGFile("./tf_files_galaxy/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})

    # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]

            if (human_string == "cars"):
                scoreCars = score

            print('%s (score = %.5f)' % (human_string, score))

    if scoreCars > .9:
        return True
    else:
        return False

<<<<<<< HEAD
def checkColumn (imageToCheck):
	image_path = imageToCheck

	image_data = tf.gfile.FastGFile(image_path, 'rb').read()

	label_lines = [line.rstrip() for line
	               in tf.gfile.GFile("./tf_files_galaxy/retrained_labels.txt")]

	with tf.gfile.FastGFile("./tf_files_galaxy/retrained_graph.pb", 'rb') as f:
		graph_def = tf.GraphDef()
		graph_def.ParseFromString(f.read())
		_ = tf.import_graph_def(graph_def, name='')

	with tf.Session() as sess:
		# Feed the image_data as input to the graph and get first prediction
		softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

		predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})

		# Sort to show labels of first prediction in order of confidence
		top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

		for node_id in top_k:
			human_string = label_lines[node_id]
			score = predictions[0][node_id]

			if (human_string == "cars"):
				scoreCars = score

			print('%s (score = %.5f)' % (human_string, score))

	if scoreCars > .5:
		return True
	else:
		return False

# print (checkImage ("./splitImage0/8.png"))
print (checkColumn ("./splitImage0/6Big.png"))
=======
# print (checkImage ("./splitImage0/3.png"))
>>>>>>> fdb7b9d144505de47cafd828a882035b1bab09e9
