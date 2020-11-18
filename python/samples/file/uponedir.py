import os

'''
goes up one directory without using ..
'''

_path_ = os.path.realpath(__file__)
_base_, _file_ = os.path.split(_path_)

print(_base_)
print(_file_)

_uponed_ = _base_[:-_base_[::-1].find(os.path.sep)]
print(_uponed_)
