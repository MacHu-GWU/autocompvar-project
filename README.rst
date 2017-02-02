.. image:: https://travis-ci.org/MacHu-GWU/autocompvar-project.svg?branch=master

.. image:: https://img.shields.io/pypi/v/autocompvar.svg

.. image:: https://img.shields.io/pypi/l/autocompvar.svg

.. image:: https://img.shields.io/pypi/pyversions/autocompvar.svg


Welcome to autocompvar Documentation
===============================================================================
In most of the case, put constant value in your code. Because when you see the value, you don't know what does that mean in behind. A better way is to define a constant, and use that constant variable. 

But sometimes, you have a great amount of constant, and you need to put that in your code anywhere. It's really hard to remember all constant name. Especially, sometimes they are nested.

``autocompvar`` allows developer to create a Constant def script from data, and then you don't need to remember anything anymore.

Let's see an example.


Example
-------------------------------------------------------------------------------
You have a game client.

	ItemType
	|--- Weapon: subclass_id=1, name=weapon
		|--- Sword: id=1, name=sword
		|--- Dagger: id=2, name=dagger
	|--- Armor: subclass_id=2, name=armor
		|--- Plate: id=1, name=plate
		|--- Cloth: id=2, name=cloth

ideally, you want this:

	>>> from itemtype import itemtype
	
	# when you type itemtype.name, it gives you all available subclass
	# when you type itemtype.name____weapon, it gives you all attributes
	>>> itemtype.name____weapon.subclass_id
	1

	>>> itemtype.name____weapon.name____dagger.id
	2

	# or you can use a function interface to program that
	>>> itemtype.name____armor.getattr_by_id(2).name
	cloth


**Quick Links**
-------------------------------------------------------------------------------
- `GitHub Homepage <https://github.com/MacHu-GWU/autocompvar-project>`_
- `Online Documentation <http://pythonhosted.org/autocompvar>`_
- `PyPI download <https://pypi.python.org/pypi/autocompvar>`_
- `Install <install_>`_
- `Issue submit and feature request <https://github.com/MacHu-GWU/autocompvar-project/issues>`_
- `API reference and source code <http://pythonhosted.org/autocompvar/py-modindex.html>`_


.. _install:

Install
-------------------------------------------------------------------------------

``autocompvar`` is released on PyPI, so all you need is:

.. code-block:: console

	$ pip install autocompvar

To upgrade to latest version:

.. code-block:: console

	$ pip install --upgrade autocompvar