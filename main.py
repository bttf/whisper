import argparse
import whisper
import json
import sys
import multiprocessing

def main(video_path, out_file):
    model = whisper.load_model('base')
    result = model.transcribe(video_path, verbose=True)
    with open(out_file, 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    parser = argparse.ArgumentParser(description='Transcribe a video file.')
    parser.add_argument('video_path', type=str, help='The path to the video or audio file.')
    parser.add_argument('out_file', type=str, help='The path to the output json file.')
    
    args = parser.parse_args()
    main(args.video_path, args.out_file)
