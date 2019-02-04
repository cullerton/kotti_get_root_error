# -*- coding: utf-8 -*-

"""
Created on 2019-02-04
:author:  ()
"""

from kotti.resources import File
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_get_root_error')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_get_root_error.kotti_configure

        to enable the ``kotti_get_root_error`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_get_root_error'
    settings['kotti.alembic_dirs'] += ' kotti_get_root_error:alembic'
    settings['kotti.available_types'] += ' kotti_get_root_error.resources.CustomContent'
    settings['kotti.fanstatic.view_needed'] += ' kotti_get_root_error.fanstatic.css_and_js'
    File.type_info.addable_to.append('CustomContent')


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('kotti_get_root_error:locale')
    config.add_static_view('static-kotti_get_root_error', 'kotti_get_root_error:static')

    config.scan(__name__)
