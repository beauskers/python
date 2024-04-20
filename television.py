class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self):
        """
        Create the Television object with the following attributes:
        status: Boolean, True if the television is on, False otherwise
        muted: Boolean, True if the television is muted, False otherwise
        volume: Integer, the volume of the television
        channel: Integer, the channel of the television
        previous_volume: Integer, the volume of the television before it was muted
        """
        self.status = False
        self.muted = False
        self.volume = Television.min_volume
        self.channel = Television.min_channel
        self.previous_volume = None

    def power(self):
        """
        This method will turn the television on or off
        :return:
        """
        if not self.status:
            self.status = True
        else:
            self.status = False

    def mute(self):
        """
        This method will mute or unmute the television
        :return:
        """
        if self.status:
            if not self.muted:
                self.previous_volume = self.volume
                self.volume = 0
                self.muted = True
            else:
                self.volume = self.previous_volume
                self.muted = False

    def channel_up(self):
        """
        This method will increase the channel of the television
        :return:
        """
        if self.status:
            if self.channel < Television.max_channel:
                self.channel += 1
            else:
                self.channel = Television.min_channel

    def channel_down(self):
        """
        This method will decrease the channel of the television
        :return:
        """
        if self.status:
            if self.channel > Television.min_channel:
                self.channel -= 1
            else:
                self.channel = Television.max_channel

    def volume_up(self):
        """
        This method will increase the volume of the television
        :return:
        """
        if self.status:
            if self.muted:
                self.mute()
            if self.volume < Television.max_volume:
                self.volume += 1

    def volume_down(self):
        """
        This method will decrease the volume of the television
        :return:
        """
        if self.status:
            if self.muted:
                self.mute()
            if self.volume > Television.min_volume:
                self.volume -= 1

    def __str__(self):
        """
        This method will return a string for the Television object
        :return:
        """
        return f'Power = [{self.status}], Channel = [{self.channel}], Volume = [{self.volume}], '
