class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = Television.min_volume
        self.channel = Television.min_channel
        self.previous_volume = None

    def power(self):
        if not self.status:
            self.status = True
        else:
            self.status = False

    def mute(self):
        if self.status:
            if not self.muted:
                self.previous_volume = self.volume
                self.volume = 0
                self.muted = True
            else:
                self.volume = self.previous_volume
                self.muted = False

    def channel_up(self):
        if self.status:
            if self.channel < Television.max_channel:
                self.channel += 1
            else:
                self.channel = Television.min_channel

    def channel_down(self):
        if self.status:
            if self.channel > Television.min_channel:
                self.channel -= 1
            else:
                self.channel = Television.max_channel

    def volume_up(self):
        if self.status:
            if self.muted:
                self.mute()
            if self.volume < Television.max_volume:
                self.volume += 1

    def volume_down(self):
        if self.status:
            if self.muted:
                self.mute()
            if self.volume > Television.min_volume:
                self.volume -= 1

    def __str__(self):
        return f'Power = [{self.status}], Channel = [{self.channel}], Volume = [{self.volume}], '
