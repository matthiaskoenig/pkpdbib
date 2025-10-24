.. image:: https://github.com/matthiaskoenig/pkpdbib/raw/develop/docs/images/favicon/pkpdbib-100x100-300dpi.png
   :align: left
   :alt: pkpdbib logo

pkpdbib: python utilities for metadata and COMBINE archives
==============================================================
|icon1| |icon2| |icon3| |icon4| |icon5| |icon6| |icon7|


.. |icon1| image:: https://github.com/matthiaskoenig/pkpdbib/workflows/CI-CD/badge.svg
   :target: https://github.com/matthiaskoenig/pkpdbib/workflows/CI-CD
   :alt: GitHub Actions CI/CD Status
.. |icon2| image:: https://img.shields.io/pypi/v/pkpdbib.svg
   :target: https://pypi.org/project/pkpdbib/
   :alt: Current PyPI Version
.. |icon3| image:: https://img.shields.io/pypi/pyversions/pkpdbib.svg
   :target: https://pypi.org/project/pkpdbib/
   :alt: Supported Python Versions
.. |icon4| image:: https://img.shields.io/pypi/l/pkpdbib.svg
   :target: http://opensource.org/licenses/LGPL-3.0
   :alt: GNU Lesser General Public License 3
.. |icon5| image:: https://zenodo.org/badge/10.5281/zenodo.11076700.svg
   :target: https://doi.org/10.5281/zenodo.11076700
   :alt: Zenodo DOI
.. |icon6| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Black
.. |icon7| image:: http://www.mypy-lang.org/static/mypy_badge.svg
   :target: http://mypy-lang.org/
   :alt: mypy

pkpdbib is a collection of python utilities for working with
pharmacokinetics/pharmacodynamics (PK/PD) literature with source code available from 
`https://github.com/matthiaskoenig/pkpdbib <https://github.com/matthiaskoenig/pkpdbib>`__.
 
If you have any questions or issues please `open an issue <https://github.com/matthiaskoenig/pkpdbib/issues>`__.

How to cite
===========

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.11076700.svg
   :target: https://doi.org/10.5281/zenodo.11076700
   :alt: Zenodo DOI

Contributing
============

Contributions are always welcome!

License
=======

* Source Code: `LGPLv3 <http://opensource.org/licenses/LGPL-3.0>`__
* Documentation: `CC BY-SA 4.0 <http://creativecommons.org/licenses/by-sa/4.0/>`__

The pkpdbib source is released under both the GPL and LGPL licenses version 2 or
later. You may choose which license you choose to use the software under.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License or the GNU Lesser General Public
License as published by the Free Software Foundation, either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

Funding
=======
Matthias König (MK) was supported by the Federal Ministry of Education and Research 
(BMBF, Germany) within the research network Systems Medicine of the Liver 
(**LiSyM**, grant number 031L0054). MK is supported by the Federal Ministry of 
Education and Research (BMBF, Germany) within ATLAS by grant number 031L0304B and 
by the German Research Foundation (DFG) within the Research Unit Program FOR 5151 
QuaLiPerF (Quantifying Liver Perfusion-Function Relationship in Complex Resection 
- A Systems Medicine Approach) by grant number 436883643 and by grant number 
465194077 (Priority Programme SPP 2311, Subproject SimLivA).

Installation
============
`pkpdbib` is available from `pypi <https://pypi.python.org/pypi/pkpdbib>`__ and 
can be installed via:: 

    pip install pkpdbib

Develop version
---------------
The latest develop version can be installed via::

    pip install git+https://github.com/matthiaskoenig/pkpdbib.git@develop

Or via cloning the repository and installing via::

    git clone https://github.com/matthiaskoenig/pkpdbib.git
    cd pkpdbib
    pip install -e .

To install for development use::

    pip install -e .[development]


Documentation
=============
Retrieve PDFs via Sci-hub

- Open the zotero library, select items without PDF attachment, right click -> Export items -> BetterBibTeX JSON -> <substance>.json

Run script ::

    scidownl domain.update
    scihub_pdfs -j <substance>.json

© 2021-2025 Matthias König
