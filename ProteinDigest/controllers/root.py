# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from ProteinDigest import model
from ProteinDigest.controllers.secure import SecureController
from ProteinDigest.model import DBSession
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from ProteinDigest.lib.base import BaseController
from ProteinDigest.controllers.error import ErrorController

from ProteinDigest.model.protein_digest import *
import tw2.forms as twf

__all__ = ['RootController']


class SearchForm(twf.Form):
    class child(twf.TableLayout):
        seq = twf.TextField(label="Protein Sequence")
        enzyme = twf.SingleSelectField(label="Seach Mode",
                                       options=["Trypsin",
                                                "Trypsin (C-term to K/R, even before P)",
                                                "Lys C"],
                                       prompt_text=None)
        l_min = twf.TextField(label="Min. Length")
        l_max = twf.TextField(label="Max. Length")
        mw_min = twf.TextField(label="Min. Molecular Weight")
        mw_max = twf.TextField(label="Max. Molecular Weight")
        miss = twf.TextField(label="Miss Cleavage")

        css_class = 'table'
        attrs = {'style': 'width: 600px;'}

    action = '/digest'
    submit = twf.SubmitButton(value="Digest")


class RootController(BaseController):
    """
    The root controller for the ProteinDigest application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)
    error = ErrorController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "ProteinDigest"

    @expose('ProteinDigest.templates.index')
    def index(self):
        """Front page"""
        return dict(title="ProteinDigest",
                    form=SearchForm)

    @expose('ProteinDigest.templates.digest')
    def result(self, seq):
        protein_digest_results = protein_digest(seq=seq)
        title = "Results"
        return dict(title=title, results=protein_digest_results)