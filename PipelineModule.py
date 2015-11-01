class PipelineModule(object):


    def __init__(self, working_dir='/tmp/', save=True, **kwargs):
        self.save = save
        self.working_dir = working_dir


    def close(self):
        pass
