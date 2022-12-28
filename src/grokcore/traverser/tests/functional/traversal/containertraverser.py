"""
Containers can also have an explicit traverser associated with them.
The behavior falls back to basic container traversal if the 'traverse'
method returns None:

  >>> getRootFolder()["herd"] = herd = Herd()
  >>> herd['manfred'] = Mammoth('Manfred')
  >>> herd['ellie'] = Mammoth('Ellie')

Let's first try to look up the special traversed item:

  >>> from zope.testbrowser.wsgi import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False
  >>> browser.open("http://localhost/herd/special")
  >>> print(browser.contents)
  special view
  >>> browser.open("http://localhost/herd/special/index")
  >>> print(browser.contents)
  special view

Even if we have a container item called 'special', we should still
get our special object:

  >>> herd['special'] = Mammoth('Special invisible mammoth')
  >>> browser.open("http://localhost/herd/special")
  >>> print(browser.contents)
  special view
  >>> browser.open("http://localhost/herd/special/index")
  >>> print(browser.contents)
  special view

The fall-back behavior should work for items that aren't traversed:

  >>> browser.open("http://localhost/herd/manfred")
  >>> print(browser.contents)
  <html>
  <body>
  <h1>Hello, Manfred!</h1>
  </body>
  </html>

  >>> browser.open("http://localhost/herd/ellie")
  >>> print(browser.contents)
  <html>
  <body>
  <h1>Hello, Ellie!</h1>
  </body>
  </html>

Also try traversing (an empty and therefore False in a Boolean sense) container
as a subitem of a container:

  >>> herd['subherd'] = Herd()
  >>> browser.open("http://localhost/herd/subherd/special")
  >>> print(browser.contents)
  special view

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
        if name == 'special':
            return Special()
        return None


class Mammoth(content.Model):
    def __init__(self, name):
        self.name = name


class Special(content.Model):
    pass


class SpecialIndex(view.View):
    grok.context(Special)
    grok.name('index')

    def render(self):
        return "special view"


grok.context(Mammoth)


class Index(view.View):
    pass


index = view.PageTemplate("""\
<html>
<body>
<h1>Hello, <span tal:replace="context/name/title" />!</h1>
</body>
</html>
""")
