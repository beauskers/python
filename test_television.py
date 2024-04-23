import pytest
from television import *

tv = Television()


def test_init():
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0], '


def test_power():
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0], '
    tv.power()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0], '
    tv.power()


def test_mute():
    tv.mute()
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0], '

    tv.mute()
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0], '

    tv.power()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0], '

    tv.volume_up()
    tv.mute()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0], '
    tv.mute()
    tv.volume_down()
    tv.power()


def test_channel_up():
    tv.channel_up()
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0], '

    tv.power()
    tv.channel_up()
    assert str(tv) == 'Power = [True], Channel = [1], Volume = [0], '

    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0], '
    tv.power()


def test_channel_down():
    tv.channel_down()
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0], '

    tv.power()
    tv.channel_down()
    assert str(tv) == 'Power = [True], Channel = [3], Volume = [0], '
    tv.channel_up()
    tv.power()


def test_volume_up():
    tv.volume_up()
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [0], '

    tv.power()
    tv.volume_up()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [1], '

    tv.mute()
    tv.volume_up()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [2], '

    tv.volume_up()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [2], '
    tv.power()


def test_volume_down():
    tv.volume_down()
    assert str(tv) == 'Power = [False], Channel = [0], Volume = [2], '

    tv.power()
    tv.volume_down()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [1], '

    tv.mute()
    tv.volume_down()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0], '

    tv.volume_down()
    assert str(tv) == 'Power = [True], Channel = [0], Volume = [0], '
