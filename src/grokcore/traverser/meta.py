#############################################################################
#
# Copyright (c) 2006-2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Grokkers for Grok-configured components.

This `meta` module contains the actual grokker mechanisms for which the
Grok web framework is named.  A directive in the adjacent `meta.zcml`
file directs the `martian` library to scan this file, where it discovers
and registers the grokkers you see below.  The grokkers are then active
and available as `martian` recursively examines the packages and modules
of a Grok-based web application.

"""

import martian
import grokcore.traverser
import grokcore.component

from zope import interface, component
from zope.publisher.interfaces.http import IHTTPRequest
from zope.publisher.interfaces.browser import IBrowserPublisher

class TraverserGrokker(martian.ClassGrokker):
    """Grokker for subclasses of `grok.Traverser`."""
    martian.component(grokcore.traverser.Traverser)
    martian.directive(grokcore.component.context)

    def execute(self, factory, config, context, **kw):
        adapts = (context, IHTTPRequest)
        config.action(
            discriminator=('adapter', adapts, IBrowserPublisher, ''),
            callable=component.provideAdapter,
            args=(factory, adapts, IBrowserPublisher),
            )
        return True
