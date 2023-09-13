import subprocess
import os


class Programm():
    def __init__(self):
        self.link = input('Enter yt video link: ')
        self.name_output = input('Enter video title: ')
        self.resolution = input('Select resolution 2160/1440/1080/720/480/360/240/144: ')
        self.file_name = f'{self.name_output}.mp4'


    def download_audio(self):
        command = ['yt-dlp', '-f ba[ext=m4a]','-oaudio.m4a' , self.link]
        subprocess.call(command)

    def download_video(self):
        command = ['yt-dlp', f'-f "bv[height<=?{self.resolution}]', '-ovideo.webm', self.link]
        subprocess.call(command)

    def audio_plus_video(self):
        subprocess.call(f'ffmpeg -i video.webm -i audio.m4a -c copy {self.name_output}.mp4')

    
    def check_width_and_height(self):
        subprocess.call(f'ffmpeg -v error -show_entries stream=width,height -of default=noprint_wrappers=1 {self.file_name}')

    @staticmethod
    def clear_temporary():
        os.remove('audio.m4a')
        os.remove('video.webm')


def execute_main():
    app = Programm()
    app.download_audio()
    app.download_video()
    app.audio_plus_video()
    app.check_width_and_height()
    app.clear_temporary()



if __name__ == '__main__':
    execute_main()
