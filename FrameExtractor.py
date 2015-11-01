import os
import os.path as osp
from PipelineModule import PipelineModule

class FrameExtractor(PipelineModule):
    '''Extract frames by ffmpeg'''

    def __init__(self, fps=1, end_time=-1, *args, **kwargs):
        super(FrameExtractor, self).__init__(*args, **kwargs)
        self.fps = fps
        self.end_time = end_time


    def run(self, data):
        '''
        
        data[0]: input video path
        data[1]: output fileaname
        '''
        path, fn = data
        try:
            os.makedirs(osp.join(self.working_dir, fn))
        except:
            pass

        self.out_path = self.working_dir + '/' + fn
        cmd = 'ffmpeg -i %s ' % path
        cmd += '-threads 1 '
        cmd += '-r %d ' % self.fps
        if self.end_time > 0:
            cmd += '-t %d ' % self.end_time
        cmd += '-an -s qvga '
        cmd += '%s/frame-%%05d.jpg' % self.out_path
        ret = os.system(cmd)
        if ret != 0:
            self.out_path = None
            return None
        return self.out_path

