from .. import Annotations, Categories

from dataclasses import dataclass, field
from typing import List


@dataclass
class Annotations_keypoint(Annotations):
    keypoints: List = field(metadata={'description': 'x,y,v...'})
    keypoints3d: List = field(metadata={'description': 'x,y,z,x,y,z...'})
    category_id: int = 0


@dataclass
class Categories_keypoint(Categories):
    supercategory: str
    keypoints: List[str]
    skeleton: List