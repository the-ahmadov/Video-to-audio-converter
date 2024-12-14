#!/usr/bin/env python3

import urllib.request
import urllib.error
import re
import sys
import time
import os
import shutil

def video_to_audio(filePath, output_dir):
    try:
        file, file_extension = os.path.splitext(filePath)
        file_name = os.path.basename(file)
        audio_wav_path = os.path.join(output_dir, f"{file_name}.wav")
        audio_mp3_path = os.path.join(output_dir, f"{file_name}.mp3")
        
        video_to_wav = f'ffmpeg -i "{filePath}" "{audio_wav_path}"'
        final_audio = f'lame "{audio_wav_path}" "{audio_mp3_path}"'
        
        os.system(video_to_wav)
        os.system(final_audio)
        
        os.remove(audio_wav_path)
        print(f"Successfully converted {filePath} into audio!")
    except OSError as err:
        print(err.reason)
        exit(1)

def main():
    if len(sys.argv) != 2:
        print('Command usage: python3 video_to_audio.py FileName_or_DirectoryName')
        exit(1)
    else:
        path = sys.argv[1]
        output_dir = "audio"
        
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Check if the specified path exists
        try:
            if os.path.exists(path):
                print("Path found!")
                # If it's a file, convert it to audio
                if os.path.isfile(path):
                    video_to_audio(path, output_dir)
                # If it's a directory, convert all files inside to audio
                elif os.path.isdir(path):
                    for fileName in os.listdir(path):
                        filePath = os.path.join(path, fileName)
                        if os.path.isfile(filePath):
                            video_to_audio(filePath, output_dir)
            else:
                print("Path not found!")
        except OSError as err:
            print(err.reason)
            exit(1)
        time.sleep(1)

# Install ffmpeg and/or lame if you get an error saying that the program is currently not installed 
if __name__ == '__main__':
    main()
