from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist


class Sound:
    def __init__(self):
        self.off_on_click = True
        self.off_on_message = True
        self.background_music_player = QMediaPlayer()
        self.click_sound_player = QMediaPlayer()
        self.warning_sound_player = QMediaPlayer()  # Player for warning sound
        self.message_sound_player = QMediaPlayer()  # Player for message sound

    def play_background_music(self):
        self.playlist = QMediaPlaylist()
        url = QUrl.fromLocalFile(r"Sound\bgsound.mp3")
        self.playlist.addMedia(QMediaContent(url))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.background_music_player.setPlaylist(self.playlist)
        self.background_music_player.setVolume(15)
        self.background_music_player.setPlaybackRate(1)
        self.background_music_player.play()

    def stop_background_music(self):
        self.background_music_player.stop()

    def play_click_music(self):
        if self.off_on_click:
            url = QUrl.fromLocalFile(r"Sound/clicksound.wav")
            content = QMediaContent(url)
            self.click_sound_player.setMedia(content)
            self.click_sound_player.setVolume(40)
            self.click_sound_player.play()

    def play_warn_music(self):
        if self.off_on_message:
            url = QUrl.fromLocalFile(r"Sound/warning.wav")
            content = QMediaContent(url)
            self.warning_sound_player.setMedia(content)
            self.warning_sound_player.setVolume(30)
            self.warning_sound_player.play()

    def play_message_music(self):
        if self.off_on_message:
            url = QUrl.fromLocalFile(r"Sound/message.wav")
            content = QMediaContent(url)
            self.message_sound_player.setMedia(content)
            self.message_sound_player.setVolume(50)
            self.message_sound_player.play()

    def off_message_music(self):
        self.off_on_message = False

    def on_message_music(self):
        self.off_on_message = True

    def off_click_music(self):
        self.off_on_click = False

    def on_click_music(self):
        self.off_on_click = True
