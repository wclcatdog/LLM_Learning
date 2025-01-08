from moviepy.editor import VideoFileClip


def convert_mp4_to_gif(mp4_file_path, gif_file_path, start_time, end_time, fps=10):
    """
    Converts an MP4 video file to a GIF file.

    :param mp4_file_path: Path to the MP4 video file.
    :param gif_file_path: Path to save the GIF file.
    :param start_time: Start time of the clip in seconds.
    :param end_time: End time of the clip in seconds.
    :param fps: Frames per second for the GIF.
    """
    # Load the video file
    video = VideoFileClip(mp4_file_path).subclip(start_time, end_time)

    # Write the video to a GIF file
    video.write_gif(gif_file_path, fps=fps)


# Example usage
mp4_file_path = 'video3.mp4'  # Replace with your MP4 file path
gif_file_path = 'output32.gif'  # Replace with your desired GIF file path
start_time = 0  # Start time in seconds
end_time = 5  # End time in seconds

convert_mp4_to_gif(mp4_file_path, gif_file_path, start_time, end_time)