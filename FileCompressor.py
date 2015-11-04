import os
import os.path as osp
import shutil
from PipelineModule import PipelineModule

class FileCompressor(PipelineModule):

    def __init__(self, *args, **kwargs):
        super(FileCompressor, self).__init__(*args, **kwargs)


    def run(self, data):
        path, fn = data
        self.out_path = osp.join(self.working_dir, fn + '.tar.gz')
        cmd = 'tar czf %s -C %s %s' % (self.out_path, path.rsplit('/', 1)[0], path.rsplit('/',1)[1])
        print '>>>>> ', cmd
        ret = os.system(cmd)
        if ret != 0:
            return None
        return self.out_path, fn


    def close(self):
        try:
            if not self.save and self.out_path:
                os.remove(self.out_path)
        except (AttributeError, OSError) as e:
            pass
