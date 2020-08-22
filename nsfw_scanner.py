import os, sys
import json
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
def image_scan():
# change this as you see fit
    file_path = "D:\\Code\\AI-assisted child protection\\HTML_cache\\images\\"
    relative_paths = os.listdir(file_path)
    unrelative_paths = []
    for path in relative_paths:
        new_path = "D:\\Code\\AI-assisted child protection\\HTML_cache\\images\\" + path
        unrelative_paths.append(new_path)
    for path_2 in unrelative_paths:

        # Read in the image_data
        image_data = tf.gfile.FastGFile(path_2, 'rb').read()

        # Loads label file, strips off carriage return
        label_lines = [line.rstrip() for line 
                    in tf.gfile.GFile("D:\\Code\\AI-assisted child protection\\retrained_labels.txt")]

    # Unpersists graph from file
        with tf.gfile.FastGFile("D:\\Code\\AI-assisted child protection\\retrained_graph.pb", 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')

        with tf.Session() as sess:
            # Feed the image_data as input to the graph and get first prediction
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
            predictions = sess.run(softmax_tensor, \
                    {'DecodeJpeg/contents:0': image_data})
    
            # Sort to show labels of first prediction in order of confidence
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
            f = open("D:\\Code\\AI-assisted child protection\\alert\\alert.txt","a")
            f.write("Image Results:\n")
            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                msg = '%s (score = %.5f)' % (human_string, score)
                print(msg)
                
                f.write(path_2.replace("D:\\Code\\AI-assisted child protection\\HTML_cache\\images\\","") + " " + msg + "\n")


image_scan()