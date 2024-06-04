from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Sound:
    def __init__(self):
        self.off_on_click = True
        self.off_on_message = True
        self.background_music_player = QMediaPlayer()
        self.click_sound_player = QMediaPlayer()

    def play_background_music(self):
        url = QUrl.fromLocalFile(
            r"Sound\bgsound.wav"
        )
        content = QMediaContent(url)
        self.background_music_player.setMedia(content)
        self.background_music_player.setVolume(50)
        self.background_music_player.play()

    def stop_background_music(self):
        self.background_music_player.stop()

    def play_click_music(self):
        if self.off_on_click == True:
            url = QUrl.fromLocalFile(
                r"Sound\clicksound.wav"
            )
            content = QMediaContent(url)
            self.click_sound_player.setMedia(content)
            self.click_sound_player.setVolume(80)
            self.click_sound_player.play()

    def play_warn_music(self):
        if self.off_on_message == True:
            url = QUrl.fromLocalFile(
                r"Sound\warning.wav"
            )
            content = QMediaContent(url)
            self.background_music_player.setMedia(content)
            self.background_music_player.setVolume(30)
            self.background_music_player.play()

    def play_message_music(self):
        if self.off_on_message == True:
            url = QUrl.fromLocalFile(
                r"Sound\message.wav"
            )
            content = QMediaContent(url)
            self.background_music_player.setMedia(content)
            self.background_music_player.setVolume(50)
            self.background_music_player.play()

    def off_message_music(self):
        self.off_on_message = False

    def on_message_music(self):
        self.off_on_message = True

    def off_click_music(self):
        self.off_on_click = False

    def on_click_music(self):
        self.off_on_click = True
