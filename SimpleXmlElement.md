# SimpleXMLElement #

SimpleXMLElement is a class to work with XML in a object oriented easy and simple way.  It's a resembles (was inspired) by the PHP SimpleXML extension (SimpleXMLElement).

It was implemented in python encapsulating xml.dom.minidom: see [source:simplexml.py]

The main difference is that no automatic type conversion is done (int, long, etc.).
It justs returns xml elements (textual), so they must be converted explicitly.

**Note**: Version 1.01a changes: method names (following python\_naming\_convention: `addChild` -> `add_child`), `__getitem__` behaviour (to access attributes) and added `__call__` to enhance search (instead of `__getitem__` that was limited, so replace `element['tag']` by `element('tag')`). See bellow.

## Usage ##

  * Create a SimpleXMLElement instance with the XML text string to parse
  * Navigate through the object:
    * XML Tags are converted to python attributes
    * Repetitive tags can be iterated
    * Call elements to search by name/ns: `element('tagname',ns=namespaces_uri,...)`
    * Use items notation to access to attributes: `element['attribute'] = value`
  * Modify tags with `add_child`, `add_attribute`, `add_comment`, etc.
  * Convert back to xml using `as_xml()`

## Methods: ##

SimpleXMLElement Constructor parameters:
  * text: xml text to parse
  * namespace: main tag xml namespace to be used (if any)
  * prefix: namespace prefix (if used)
  * elements, document: used internally, represents the xml.minidom objects

SimpleXMLElement supports some methods for introspection and updates:
  * add\_child(name,text=None,ns=True): Adding a child tag to a node. `text` is optional, `ns` enables the use of the namespace
  * add\_comment(data): Add an xml comment to this child
  * add\_attribute(name, value): Set an attribute value from a string
  * as\_xml(pretty=False): Return the XML representation of the document
  * get\_name(): Return the tag name of this node
  * attributes(): Return a dict of attributes for this tag
  * children(): Return xml children tags of this element
  * unmarshall(types): Convert to python values the current serialized xml element. `types` is a python structure {tag name: convertion function}, ie.: `types={'p': {'a': int,'b': int}, 'c': [{'d':str}]`}
  * marshall(name, value, add\_child=True, add\_comments=False, ns=False): Analize python value and add the serialized XML element using tag name. `add_child` controls the level where the tag must be added, `ns` enables the use of the namespace.

Also, SimpleXMLElement objects redefines the behavior for some python functions/statements:
  * repr: Return the XML representation of this tag
  * in: Search for a tag name in this element or child nodes
  * unicode: Returns the unicode text nodes of the current element
  * str: Returns the str text nodes of the current element
  * int: Returns the integer value of the current element
  * float: Returns the float value of the current element

## Example ##
```
>>> from pysimplesoap.simplexml import SimpleXMLElement
>>> span = SimpleXMLElement('<span><a href="google.com">google</a><prueba><i>1</i><float>1.5</float></prueba></span>')
>>> str(span.a)
'google'
>>> int(span.prueba.i)
1
>>> float(span.prueba.float)
1.5
>>>
>>> span = SimpleXMLElement('<span><a href="google.com">google</a><a>yahoo</a><a>hotmail</a></span>')
>>> for a in span.a: print str(a)
...     
google
yahoo
hotmail
>>> span.add_child('a','altavista')
'altavista'
>>> span.as_xml()
'<?xml version="1.0" encoding="utf8"?><span><a href="google.com">google</a><a>yahoo</a><a>hotmail</a><a>altavista</a></span>'
```