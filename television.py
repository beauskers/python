class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self) -> None:
        """
        Create the Television object with the following attributes:
        status: Boolean, True if the television is on, False otherwise
        muted: Boolean, True if the television is muted, False otherwise
        volume: Integer, the volume of the television
        channel: Integer, the channel of the television
        previous_volume: Integer, the volume of the television before it was muted
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.min_volume
        self.__channel = Television.min_channel
        self.__previous_volume = None

    def power(self) -> None:
        """
        This method will turn the television on or off
        :return:
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        This method will mute or unmute the television
        :return:
        """
        if self.__status:
            if not self.__muted:
                self.__previous_volume = self.__volume
                self.__volume = Television.min_volume
                self.__muted = True
            else:
                self.__volume = self.__previous_volume
                self.__muted = False

    def channel_up(self) -> None:
        """
        This method will increase the channel of the television
        :return:
        """
        if self.__status:
            if self.__channel < Television.max_channel:
                self.__channel += 1
            else:
                self.__channel = Television.min_channel

    def channel_down(self) -> None:
        """
        This method will decrease the channel of the television
        :return:
        """
        if self.__status:
            if self.__channel > Television.min_channel:
                self.__channel -= 1
            else:
                self.__channel = Television.max_channel

    def volume_up(self) -> None:
        """
        This method will increase the volume of the television
        :return:
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume < Television.max_volume:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        This method will decrease the volume of the television
        :return:
        """
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume > Television.min_volume:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        This method will return a string for the Television object
        :return:
        """
        return f'Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}], '
