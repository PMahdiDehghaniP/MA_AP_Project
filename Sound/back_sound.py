from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl


class Sound:
    def __init__(self) -> None:
        pass

    def play_background_music(self):
        self.background_music = QSoundEffect()
        self.background_music.setSource(
            QUrl.fromLocalFile(
                r"F:\AP\pyqt6\1379416183 (online-audio-converter.com).wav"
            )
        )
        self.background_music.setLoopCount(QSoundEffect.Infinite)
        self.background_music.setVolume(0.5)
        self.background_music.play()

    def stop_background_music(self):
        self.background_music.stop()

    def play_click_music(self):
        self.background_music = QSoundEffect()
        self.background_music.setSource(
            QUrl.fromLocalFile(
                r"Sound\click_effect-86995 (online-audio-converter.com).wav"
            )
        )
        self.background_music.setVolume(0.8)
        self.background_music.play()
