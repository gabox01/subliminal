from datetime import timedelta

from babelfish import Language
import logging

from subliminal import region
from subliminal.core import execute

# configure the cache
region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})

# scan for videos newer than 2 weeks and their existing subtitles in a folder
videos = execute('/mnt/mybook/Shared Videos/',{Language('eng'), Language('hun')})

