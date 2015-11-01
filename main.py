from VideoPipeline import VideoPipeline
from VideoDownloader import VideoDownloader
from FrameExtractor import FrameExtractor

def main():
    vp = VideoPipeline(n_job=2, log_dir='/tmp/')
    vp.add(VideoDownloader(working_dir='/tmp/', save=False))
    vp.add(FrameExtractor(fps=1, end_time=180, working_dir='/tmp/raw_frames/', save=True))

    urls = ['hLQl3WQQoQ0']
    vp.run(urls)

if __name__ == '__main__':
    main()
