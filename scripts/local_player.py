'''Functions to control local player'''

from utilities.system.keyboard import VirtualKeyboard
import time


class LocalPlayer(object):
    '''Class to control local player using emulated hotkeys'''
    def __init__(self):
        self.keyboard = VirtualKeyboard()

        # Start by zeroing out volume
        self.zero_volume()

        # Volume Configs
        self.max_volume = 7
        self.volume_incrementor = 0

    def zero_volume(self):
        for i in range(30):
            time.sleep(0.05)
            self.keyboard.tap_key('sound_down')

    def increase_volume(self):
        if self.volume_incrementor < self.max_volume:
            self.volume_incrementor += 1
            self.keyboard.tap_key('sound_up')

    def play(self):
        # Skip to next track automatically
        self.keyboard.tap_key('play_pause')
        self.keyboard.tap_key('next')


if __name__ == '__main__':
    player = LocalPlayer()
    player.play()

    time_range = 1 * 60  # Seconds
    volume_steps = 8

    for i in range(volume_steps + 1):
        player.increase_volume()
        time.sleep(time_range / float(volume_steps))
