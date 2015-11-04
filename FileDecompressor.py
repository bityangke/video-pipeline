import os
import os.path as osp
import shutil
from PipelineModule import PipelineModule

class FileDecompressor(PipelineModule):
    '''Inverse of FileCompressor

    Input: path of a .tar.gz file
    Output: path of directory containing the files extracted from the .tar.gz file
    '''

    def __init__(self, *args, **kwargs):
        super(FileDecompressor, self).__init__(*args, **kwargs)


    def run(self, data):
        path, fn = data
        self.out_path = osp.join(self.working_dir, fn)
        cmd = 'tar xzf %s -C %s' % (path, self.working_dir)
        print '>>>>> ', cmd
        ret = os.system(cmd)
        if ret != 0:
            return None
        return self.out_path, fn


    def close(self):
        try:
            if not self.save and self.out_path:
                shutil.rmtree(self.out_path)
        except (AttributeError, OSError) as e:
            pass
