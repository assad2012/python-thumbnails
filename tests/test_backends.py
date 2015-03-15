# -*- coding: utf-8 -*-
import unittest

from thumbnails.backends import ThumbnailBackend
from thumbnails.images import Thumbnail


class BackendTestCase(unittest.TestCase):
    def test_generate_filename(self):
        self.assertEqual(
            ThumbnailBackend.generate_filename('url', '100x200', 'center', None),
            ['0af', 'a360db703bd5c2fe7c83843ce7738a0a6d37b']
        )
        self.assertEqual(
            ThumbnailBackend.generate_filename('url', '200x200', 'center', None),
            ['851', '521c21fe9709802e9d4eb20a5fe84c18cd3ad']
        )

    def test_create_thumbnail_object(self):
        name = ['851', '521c21fe9709802e9d4eb20a5fe84c18cd3ad']
        self.assertTrue(isinstance(ThumbnailBackend.create_thumbnail_object(name), Thumbnail))

    def test_parse_size(self):
        self.assertEqual(ThumbnailBackend.parse_size('100'), (100, None))
        self.assertEqual(ThumbnailBackend.parse_size('100x200'), (100, 200))
        self.assertEqual(ThumbnailBackend.parse_size('1x10'), (1, 10))
        self.assertEqual(ThumbnailBackend.parse_size('x1000'), (None, 1000))