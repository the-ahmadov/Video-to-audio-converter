# Video-to-audio-converter
A python script to convert video files into mp3 audio files. As a heavy listener of music, I prefer keeping audio files on my phone than video files to consume less disk space. This tool helps in converting the video files present in my computer to mp3 audio files.


### Requirements:


##### This script needs Python 3+

If you don't have Python 3 installed, you just need to install python3 package :

```bash
$ sudo apt-get install python3
```
If you don't have ffmpeg installed, you just need to install ffmpeg package :

```bash
$ sudo apt-get install ffmpeg
```
If you don't have lame installed, you just need to install lame package :

```bash
$ sudo apt-get install lame
```


### Clone:
```bash
$ git clone https://github.com/adityashrm21/Video-to-audio-converter
$ cd ../Video-to-audio-converter
```

### Usage:

For single file
```bash
$ python3 video_to_audio.py <filename>
```

For all files in given folder name 
```bash
$ python3 video_to_audio.py <folder name>
```

Resulted audio files are saved in "audio folder"
