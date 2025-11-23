import imageio
import os


class VideoWriterByImageIO:
    def __init__(self, video_path, fps=25, **kwargs):
        # NOTE:
        # In imageio, `format` is the *plugin name* (e.g. "FFMPEG", "TIFF"), not the file extension ("mp4").
        # Using "mp4" here can cause imageio to select the wrong plugin (e.g. TIFF), which then
        # does not understand video-only kwargs like `fps`, leading to errors such as:
        # "TiffWriter.write() got an unexpected keyword argument 'fps'".
        #
        # Default to the FFMPEG plugin for video writing, and let the container be inferred from
        # the file extension (".mp4" in your pipeline: see StreamSDK.setup()).
        video_format = kwargs.get("format", "FFMPEG")  # default: use FFMPEG plugin for video

        codec = kwargs.get("vcodec", "libx264")  # default is libx264 encoding
        quality = kwargs.get("quality")  # video quality
        pixelformat = kwargs.get("pixelformat", "yuv420p")  # video pixel format
        macro_block_size = kwargs.get("macro_block_size", 2)
        ffmpeg_params = ["-crf", str(kwargs.get("crf", 18))]

        os.makedirs(os.path.dirname(video_path), exist_ok=True)

        writer = imageio.get_writer(
            video_path,
            fps=fps,
            format=video_format,  # plugin name, not file extension
            codec=codec,
            quality=quality,
            ffmpeg_params=ffmpeg_params,
            pixelformat=pixelformat,
            macro_block_size=macro_block_size,
        )
        self.writer = writer

    def __call__(self, img, fmt="bgr"):
        if fmt == "bgr":
            frame = img[..., ::-1]
        else:
            frame = img
        self.writer.append_data(frame)

    def close(self):
        self.writer.close()
