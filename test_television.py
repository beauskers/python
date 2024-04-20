import pytest
from television import *

tv = Television()


def test_init():
    assert tv.status == False
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0], '


def test_power():
    assert tv.status == False
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel

    tv.power()
    assert tv.status == True
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel
    tv.power()


def test_mute():
    tv.mute()
    assert tv.status == False
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel

    tv.mute()
    assert tv.status == False
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel

    tv.power()
    assert tv.status == True
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel

    tv.volume_up()
    tv.mute()
    assert tv.status == True
    assert tv.muted == True
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel
    tv.mute()
    tv.volume_down()
    tv.power()


def test_channel_up():
    tv.channel_up()
    assert tv.status == False
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel

    tv.power()
    tv.channel_up()
    assert tv.status == True
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel + 1

    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert tv.status == True
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel
    tv.power()


def test_channel_down():
    tv.channel_down()
    assert tv.status == False
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel

    tv.power()
    tv.channel_down()
    assert tv.status == True
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.max_channel
    tv.channel_up()
    tv.power()


def test_volume_up():
    tv.volume_up()
    assert tv.status == False
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel

    tv.power()
    tv.volume_up()
    assert tv.status == True
    assert tv.muted == False
    assert tv.volume == Television.min_volume + 1
    assert tv.channel == Television.min_channel

    tv.mute()
    tv.volume_up()
    assert tv.status == True
    assert tv.muted == False
    assert tv.volume == Television.min_volume + 2
    assert tv.channel == Television.min_channel

    tv.volume_up()
    assert tv.status == True
    assert tv.muted == False
    assert tv.volume == Television.max_volume
    assert tv.channel == Television.min_channel
    tv.power()


def test_volume_down():
    tv.volume_down()
    assert tv.status == False
    assert tv.muted == False
    assert tv.volume == Television.max_volume
    assert tv.channel == Television.min_channel

    tv.power()
    tv.volume_down()
    assert tv.status == True
    assert tv.muted == False
    assert tv.volume == Television.max_volume - 1
    assert tv.channel == Television.min_channel

    tv.mute()
    tv.volume_down()
    assert tv.status == True
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel

    tv.volume_down()
    assert tv.status == True
    assert tv.muted == False
    assert tv.volume == Television.min_volume
    assert tv.channel == Television.min_channel
