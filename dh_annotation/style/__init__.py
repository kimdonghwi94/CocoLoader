from dataclasses import dataclass, asdict, field
from typing import List

import dh_annotation
import datetime


__now__ = datetime.datetime.now()


class DataJson:
    def __dict__(self):
        return asdict(self)


@dataclass
class Info(DataJson):
    description: str = ''
    version: str = dh_annotation.__version__
    year: str = __now__.strftime('%Y')
    contributor: str = dh_annotation.__author__
    date_created: str = __now__.strftime('%Y-%m-%d')


@dataclass(frozen=True)
class License(DataJson):
    id: int = 0
    name: str = 'Gnetworks'


@dataclass
class Images(DataJson):
    file_name: str
    id: str
    height: int
    width: int
    frame_index: int
    coco_url: str


@dataclass
class Annotations(DataJson):
    image_id: str
    id: int


@dataclass
class Categories(DataJson):
    id: str


@dataclass
class Videos(DataJson):
    id: str
    frame_rate: float
    width: int
    height: int
    camera_id: int
    file_name: str
    frame_index: int


@dataclass
class Coco(DataJson):
    info: Info = field(default_factory=lambda :Info)
    license_: List[License] = field(default_factory=lambda :[])
    images: List[Images] = field(default_factory=lambda :[])
    annotations: List[Annotations] = field(default_factory=lambda :[])
    categories: List[Categories] = field(default_factory=lambda :[])
    videos: List[Videos] = field(default_factory=lambda :[])