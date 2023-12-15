# -*- coding: utf-8 -*-
"""Main Controller"""

import tw2.forms as twf
from tg import expose
from tg import tmpl_context
from tgext.admin.controller import AdminController
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig

from ProteinDigest import model
from ProteinDigest.controllers.secure import SecureController
from ProteinDigest.lib.base import BaseController
from ProteinDigest.model import DBSession
from ProteinDigest.model.protein_digest import *

__all__ = ['RootController']

from formencode import validators, schema

class SearchFormValidator(schema.Schema):
    seq = validators.String(min=3,strip=True)
    l_min = validators.Int(min=0)
    l_max = validators.Int(min=1)
    mw_min = validators.Int(min=0)
    mw_min = validators.Int(min=1)

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

    action = '/double'
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

    # error = ErrorController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "ProteinDigest"

    @expose('ProteinDigest.templates.index')
    def index(self):
        """Front page"""
        return dict(title="ProteinDigest",
                    form=SearchForm)

    @expose('ProteinDigest.templates.double')
    def double(self, seq, enzyme, l_min, l_max, mw_min, mw_max, miss):
        protein_digest_result = protein_digest(seq, enzyme, l_min, l_max, mw_min, mw_max, int(miss))
        return dict(title="Double", results=protein_digest_result)
