import argparse
import whisper
import json

def main(video_path):
    model = whisper.load_model('base')
    result = model.transcribe(video_path, verbose=True)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcribe a video file.')
    parser.add_argument('video_path', type=str, help='The path to the video or audio file.')
    
    args = parser.parse_args()
    main(args.video_path)
