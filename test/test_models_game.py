import os

import mock
import pytest
from PySide import QtGui

from pytwitcher import models, cache
from pytwitcherapi import session


thisdir = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture(scope="function")
def mockedsession():
    s = session.TwitchSession()
    s.request = mock.Mock()
    return s


@pytest.fixture(scope="function")
def filledcache(mockedsession, qtbot):
    c = cache.PixmapLoader(mockedsession)
    c['smallgamebox.png'] = QtGui.QPixmap(
        os.path.join(thisdir, 'smallgamebox.png'))
    c['mediumgamebox.png'] = QtGui.QPixmap(
        os.path.join(thisdir, 'mediumgamebox.png'))
    c['largegamebox.png'] = QtGui.QPixmap(
        os.path.join(thisdir,'largegamebox.png'))
    c['smallgamelogo.png'] = QtGui.QPixmap(
        os.path.join(thisdir,'smallgamelogo.png'))
    c['mediumgamelogo.png'] = QtGui.QPixmap(
        os.path.join(thisdir,'mediumgamelogo.png'))
    c['largegamelogo.png'] = QtGui.QPixmap(
        os.path.join(thisdir,'largegamelogo.png'))
    return c


@pytest.fixture(scope='function')
def mockedgame(mockedsession, filledcache):
    """Return a qtgame with a already filled cache."""
    box = {'small': 'smallgamebox.png',
           'medium': 'mediumgamebox.png',
           'large': 'largegamebox.png'}
    logo = {'small': 'smallgamelogo.png',
            'medium': 'mediumgamelogo.png',
            'large': 'largegamelogo.png'}
    g = models.QtGame(mockedsession, filledcache, 'TestGame',
                      box, logo, 424242, 10, 3)
    return g


@pytest.mark.parametrize('size,pixmap', [
    ('small', os.path.join(thisdir,'smallgamebox.png')),
    ('medium', os.path.join(thisdir,'mediumgamebox.png')),
    ('large', os.path.join(thisdir,'largegamebox.png')),
])
def test_get_box(size, pixmap, mockedgame, qtbot):
    b = mockedgame.get_box(size)
    pixmap = QtGui.QPixmap(pixmap)
    assert b.toImage() == pixmap.toImage()


@pytest.mark.parametrize('size,pixmap', [
    ('small', os.path.join(thisdir,'smallgamelogo.png')),
    ('medium', os.path.join(thisdir,'mediumgamelogo.png')),
    ('large', os.path.join(thisdir,'largegamelogo.png')),
])
def test_get_logo(size, pixmap, mockedgame, qtbot):
    b = mockedgame.get_logo(size)
    pixmap = QtGui.QPixmap(pixmap)
    assert b.toImage() == pixmap.toImage()
