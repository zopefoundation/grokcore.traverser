"""
Containers can have an explicit traverser associated with them.  The
behaviour falls back to basic container traversal if the 'traverse'
method returns None. Normal behaviour also means that the standard
Zope 3 paradigm "items before views" is supported in the fallback.

  >>> getRootFolder()["herd"] = herd = Herd()
  >>> herd['manfred'] = Mammoth('Manfred')
  >>> herd['ellie'] = Mammoth('Ellie')

  >>> from zope.testbrowser.wsgi import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False

When we look up 'manfred', we'll get the Mammoth object as expected:

  >>> browser.open("http://localhost/herd/manfred")
  >>> print(browser.contents)
  Hello Manfred

When we look up 'ellie', we also get a Mammoth object and not the
Ellie view:

  >>> browser.open("http://localhost/herd/ellie")
  >>> print(browser.contents)
  Hello Ellie

We can, of course, get to the Ellie view explicitly:

  >>> browser.open("http://localhost/herd/@@ellie")
  >>> print(browser.contents)
  Hi, it's me, the Ellie view!

"""
import grokcore.component as grok
import grokcore.content as content
import grokcore.view as view

import grokcore.traverser


class Herd(content.Container):
    pass


class Traverser(grokcore.traverser.Traverser):
    grok.context(Herd)

    def traverse(self, name):
        # we don't really need to do anything here as we want to test
        # the fallback behaviour
        pass


class Ellie(view.View):
    grok.context(Herd)
    grok.name('ellie')

    def render(self):
        return "Hi, it's me, the Ellie view!"


class Mammoth(content.Model):
    def __init__(self, name):
        self.name = name


class MammothIndex(view.View):
    grok.context(Mammoth)
    grok.name('index')

    def render(self):
        return "Hello " + self.context.name.title()
