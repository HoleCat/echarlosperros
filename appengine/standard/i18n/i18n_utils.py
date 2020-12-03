#!/usr/bin/env python
#
# Copyright 2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A small module for i18n of webapp2 and jinja2 based apps.

The idea of this example, especially for how to translate strings in
Javascript is originally from an implementation of Django i18n.
"""
from __future__ import print_function

import gettext
import json
import os

import jinja2

import webapp2

from webob import Request

try:
    basestring
except NameError:
    basestring = str


def _get_plural_forms(js_translations):
    """Extracts the parameters for what constitutes a plural.

    Args:
        js_translations: GNUTranslations object to be converted.

    Returns:
        A tuple of:
            A formula for what constitutes a plural
            How many plural forms there are
    """
    plural = None
    n_plural = 2
    if '' in js_translations._catalog:
        for l in js_translations._catalog[''].split('\n'):
            if l.startswith('Plural-Forms:'):
                plural = l.split(':', 1)[1].strip()
                print('plural is {}'.format(plural))
    if plural is not None:
        for raw_element in plural.split(';'):
            element = raw_element.strip()
            if element.startswith('nplurals='):
                n_plural = int(element.split('=', 1)[1])
            elif element.startswith('plural='):
                plural = element.split('=', 1)[1]
                print('plural is now {}'.format(plural))
    else:
        n_plural = 2
        plural = '(n == 1) ? 0 : 1'
    return plural, n_plural


def convert_translations_to_dict(js_translations):
    """Convert a GNUTranslations object into a dict for jsonifying.

    Args:
        js_translations: GNUTranslations object to be converted.

    Returns:
        A dictionary representing the GNUTranslations object.
    """
    plural, n_plural = _get_plural_forms(js_translations)

    translations_dict = {'plural': plural, 'catalog': {}, 'fallback': None}
    if js_translations._fallback is not None:
        translations_dict['fallback'] = convert_translations_to_dict(
            js_translations._fallback
        )
    for key, value in js_translations._catalog.items():
        if key == '':
            continue
        if isinstance(key, basestring):
            translations_dict['catalog'][key] = value
        elif isinstance(key, tuple):
            if key[0] not in translations_dict['catalog']:
                translations_dict['catalog'][key[0]] = [''] * n_plural
            translations_dict['catalog'][key[0]][int(key[1])] = value
    return translations_dict


class BaseHandler(webapp2.RequestHandler):
    """A base handler for installing i18n-aware Jinja2 environment."""

    @webapp2.cached_property
    def jinja2_env(self):
        """Cached property for a Jinja2 environment.

        Returns:
            Jinja2 Environment object.
        """

        jinja2_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                os.path.join(os.path.dirname(__file__), 'templates')),
            extensions=['jinja2.ext.i18n'])
        jinja2_env.install_gettext_translations(
            self.request.environ['i18n_utils.active_translation'])
        jinja2_env.globals['get_i18n_js_tag'] = self.get_i18n_js_tag
        return jinja2_env

    def get_i18n_js_tag(self):
        """Generates a Javascript tag for i18n in Javascript.

        This instance method is installed to the global namespace of
        the Jinja2 environment, so you can invoke this method just
        like `{{ get_i18n_js_tag() }}` from anywhere in your Jinja2
        template.

        Returns:
            A 'javascript' HTML tag which contains functions and
            translation messages for i18n.
        """

        template = self.jinja2_env.get_template('javascript_tag.jinja2')
        return template.render({'javascript_body': self.get_i18n_js()})

    def get_i18n_js(self):
        """Generates a Javascript body for i18n in Javascript.

        If you want to load these javascript code from a static HTML
        file, you need to create another handler which just returns
        the code generated by this function.

        Returns:
            Actual javascript code for functions and translation
            messages for i18n.
        """

        try:
            js_translations = gettext.translation(
                'jsmessages', 'locales', fallback=False,
                languages=self.request.environ[
                    'i18n_utils.preferred_languages'],
                codeset='utf-8')
        except IOError:
            template = self.jinja2_env.get_template('null_i18n_js.jinja2')
            return template.render()

        translations_dict = convert_translations_to_dict(js_translations)
        template = self.jinja2_env.get_template('i18n_js.jinja2')
        return template.render(
            {'translations': json.dumps(translations_dict, indent=1)})


class I18nMiddleware(object):
    """A WSGI middleware for i18n.

    This middleware determines users' preferred language, loads the
    translations files, and install it to the builtin namespace of the
    Python runtime.
    """

    def __init__(self, app, default_language='en', locale_path=None):
        """A constructor for this middleware.

        Args:
            app: A WSGI app that you want to wrap with this
                middleware.
            default_language: fallback language; ex: 'en', 'ja', etc.
            locale_path: A directory containing the translations
                file. (defaults to 'locales' directory)
        """

        self.app = app
        if locale_path is None:
            locale_path = os.path.join(
                os.path.abspath(os.path.dirname(__file__)), 'locales')
        self.locale_path = locale_path
        self.default_language = default_language

    def __call__(self, environ, start_response):
        """Called by WSGI when a request comes in.

        Args:
            environ: A dict holding environment variables.
            start_response: A WSGI callable (PEP333).

        Returns:
            Application response data as an iterable. It just returns
            the return value of the inner WSGI app.
        """
        req = Request(environ)
        preferred_languages = list(req.accept_language)
        if self.default_language not in preferred_languages:
            preferred_languages.append(self.default_language)
        translation = gettext.translation(
            'messages', self.locale_path, fallback=True,
            languages=preferred_languages, codeset='utf-8')
        translation.install(unicode=True, names=['gettext', 'ngettext'])
        environ['i18n_utils.active_translation'] = translation
        environ['i18n_utils.preferred_languages'] = preferred_languages

        return self.app(environ, start_response)
