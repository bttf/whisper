import argparse
import whisper
import json
import sys
import multiprocessing
import builtins
import functools

# Force flushing of print statemets to stdout for real-time logging
original_print = builtins.print

def flushed_print(*args, **kwargs):
    kwargs['flush'] = True  # Force flushing
    original_print(*args, **kwargs)

builtins.print = flushed_print

def main(video_path, out_file):
    model = whisper.load_model('base')
    print ('Now transcribing the video', flush=True)
    result = model.transcribe(video_path, verbose=True)
    print('Transcription complete', flush=True)
    with open(out_file, 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    parser = argparse.ArgumentParser(description='Transcribe a video file.')
    parser.add_argument('video_path', type=str, help='The path to the video or audio file.')
    parser.add_argument('out_file', type=str, help='The path to the output json file.')
    
    args = parser.parse_args()
    main(args.video_path, args.out_file)
