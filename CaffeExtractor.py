import glob
import os
import os.path as osp
import caffe
import numpy as np
from PipelineModule import PipelineModule

caffe.set_mode_gpu() # must use GPU if compiled with cudnn

class CaffeExtractor(PipelineModule):

    def __init__(self, layer, proto_path, caffemodel_path, mean_path, *args, **kwargs):
        super(CaffeExtractor, self).__init__(*args, **kwargs)
        self.net = caffe.Net(proto_path, caffemodel_path, caffe.TEST)

        self.layer = layer
        self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
        self.transformer.set_mean('data', np.load(mean_path).mean(1).mean(1))
        self.transformer.set_transpose('data', (2,0,1))
        self.transformer.set_channel_swap('data', (2,1,0))
        self.transformer.set_raw_scale('data', 255.0)


    def run(self, data):
        path, fn = data

        images = [caffe.io.load_image(ipath) for ipath in sorted(glob.glob(path + '/*'))]
        preproccesed_img = np.asarray([self.transformer.preprocess('data', im) for im in images])

        out = self.net.forward_all(data=preproccesed_img, blobs=[self.layer])
        X = []
        for j, path in enumerate(images):
            feat = out[self.layer][j]
            feat = feat.reshape((feat.shape[0], -1)).T
            X.append(feat)
        X = np.vstack(X)

        self.out_path = osp.join(self.working_dir, fn + '.npy')
        np.save(self.out_path, X)
        return self.out_path, fn


    def close(self):
        if not self.save:
            pass
