import os
from collections import defaultdict
from collections import OrderedDict

class TFIDFCaculator(object):
    def __init__(self, path):
        self.path = path
        self.tf_dict = {}
        self.df_dict = defaultdict(int)

    def build_tf_dict(self):
        for root, dirs, files in os.walk(self.path):
            for f in files:
                self.tf_dict[f] = defaultdict(int)
                with open(os.path.join(self.path, f), 'r') as fout:
                    data = fout.read()
                    words = [word.lower() for word in data.split()] 

                    for w in words:
                        self.tf_dict[f][w] += 1
                        
    def build_df_dict(self):
        all_keys = list(set([key for doc in self.tf_dict for key in self.tf_dict[doc]]))
        for key in all_keys:
            for root, dirs, files in os.walk(self.path):
                for f in files:
                    with open(os.path.join(self.path, f)) as fout:
                        data = fout.read()
                        words = [word.lower() for word in data.split()]  
                        if key in words:
                            self.df_dict[key] += 1
                            
    def get_tf_idf_dict(self, reverse = True):
        tf_idf_dict = {}
        
        for doc in self.tf_dict:
            tf_idf_dict[doc] = {}
            for key, value in self.tf_dict[doc].items():
                tf_idf_dict[doc][key] = float(value) / self.df_dict[key]
        
        for doc in tf_idf_dict:
            tf_idf_dict_by_doc = tf_idf_dict[doc]
            tf_idf_dict_by_doc = OrderedDict(sorted(tf_idf_dict_by_doc.items(), key = lambda x : x[1], reverse = reverse))
            tf_idf_dict[doc] = tf_idf_dict_by_doc
        return tf_idf_dict
            
            
path = os.getcwd() + '/data_set'            
tf_idf = TFIDFCaculator(path)            

tf_idf.build_tf_dict()
tf_idf.build_df_dict()

#print tf_idf.df_dict

for doc, tf_idf_dict in tf_idf.get_tf_idf_dict().items():
    print doc 
    print tf_idf_dict