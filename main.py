import argparse
import whisper

def main(video_path):
    model = whisper.load_model('base')
    result = model.transcribe(video_path)
    print(result['segments'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcribe a video file.')
    parser.add_argument('video_path', type=str, help='The path to the video or audio file.')
    
    args = parser.parse_args()
    main(args.video_path)
