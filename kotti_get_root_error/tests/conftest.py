# -*- coding: utf-8 -*-

"""
Created on 2019-02-04
:author:  ()
"""

pytest_plugins = "kotti"

from pytest import fixture


@fixture(scope='session')
def custom_settings():
    import kotti_get_root_error.resources
    kotti_get_root_error.resources  # make pyflakes happy
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_get_root_error.kotti_configure'}
