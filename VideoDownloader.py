import os
from PipelineModule import PipelineModule

class VideoDownloader(PipelineModule):

    def __init__(self, *args, **kwargs):
        super(VideoDownloader, self).__init__(*args, **kwargs)


    def run(self, ytid):
        '''Returns output path and the filename...

        TODO: remove the need for this module to know what is needed in the next module
        '''
        ret = os.system('./youtube-dl -o "%s/yt-%s.mp4" -- "%s"' %
                            (self.working_dir, ytid, ytid))
        self.out_path = '%s/yt-%s.mp4' % (self.working_dir, ytid)
        return (self.out_path, 'yt-%s.mp4' % ytid)


    def close(self):
        if not self.save:
            os.remove(self.out_path)
