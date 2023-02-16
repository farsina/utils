# (common.models.)__init__.py


from .posts import *
from .users import *


__all__ = (posts.__all__ +
            users.__all__)
