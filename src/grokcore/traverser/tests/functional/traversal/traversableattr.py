"""
Models can expose attributes using the grok.traversable directive.

  >>> getRootFolder()["traversefoo"] = Foo('foo')

  >>> from zope.testbrowser.wsgi import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False

As always, we can access a model with a view::
  >>> browser.open("http://localhost/traversefoo/")
  >>> print(browser.contents)
  foo

'foo' is an exposed attribute, so it should be accessible::
  >>> browser.open("http://localhost/traversefoo/foo")
  >>> print(browser.contents)
  foo

'bar' is an exposed method, and should also be accessible::
  >>> browser.open("http://localhost/traversefoo/bar")
  >>> print(browser.contents)
  bar

'bar' is also exposed under the name 'namedbar', and can also be accessed::
  >>> browser.open("http://localhost/traversefoo/namedbar")
  >>> print(browser.contents)
  bar

Finally, attributes which are not exposed, should not be visible:
  >>> browser.open("http://localhost/traversefoo/z")
  Traceback (most recent call last):
  ...
  zope.publisher.interfaces.NotFound: ...

"""
import grokcore.component as grok
import grokcore.content as content
import grokcore.view as view

import grokcore.traverser


class Bar(content.Model):
    def __init__(self, name):
        self.name = name


class BarIndex(view.View):
    grok.context(Bar)
    grok.name('index')

    def render(self):
        return self.context.name


class Foo(content.Model):
    grokcore.traverser.traversable('bar')
    grokcore.traverser.traversable('foo')
    grokcore.traverser.traversable(attr='bar', name='namedbar')

    def __init__(self, name):
        self.name = name

    foo = Bar('foo')

    def bar(self):
        return Bar('bar')
    z = "i'm not called"


class FooIndex(view.View):
    grok.context(Foo)
    grok.name('index')

    def render(self):
        return self.context.name
