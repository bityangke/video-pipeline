import os

class PipelineModule(object):


    def __init__(self, working_dir='/tmp/', save=True, **kwargs):
        self.save = save
        self.working_dir = working_dir

        try:
            os.makedirs(working_dir)
        except:
            pass


    def close(self):
        pass
