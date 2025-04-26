import argparse
import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_path: str, output_path: str = None) -> str:
    """
    Converts an MP4 file to MP3 format.
    
    Args:
        input_path (str): Path to the input MP4 file.
        output_path (str, optional): Path to save the output MP3 file. 
            If not provided, saves in the same directory as the input file.
    
    Returns:
        str: Path to the converted MP3 file.
    
    Raises:
        FileNotFoundError: If input file does not exist.
        ValueError: If input file is not in MP4 format.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if not input_path.lower().endswith('.mp4'):
        raise ValueError("Input file must be an MP4 file.")
    
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + '.mp3'
    elif not output_path.lower().endswith('.mp3'):
        output_path += '.mp3'
    
    video_clip = VideoFileClip(input_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path)
    audio_clip.close()
    video_clip.close()
    
    return output_path

def main():
    parser = argparse.ArgumentParser(description="Convert MP4 files to MP3 format.")
    parser.add_argument("input", help="Path to the input MP4 file.")
    parser.add_argument("-o", "--output", help="Path to save the output MP3 file.")
    args = parser.parse_args()
    
    try:
        output_path = convert_mp4_to_mp3(args.input, args.output)
        print(f"Successfully converted to: {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
