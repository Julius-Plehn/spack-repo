# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Extrap(AutotoolsPackage):
    """Extra-P is an automatic performance-modeling tool
    that supports the user in the identification of
    scalability bugs."""

    homepage = "https://www.scalasca.org/scalasca/software/extra-p/"
    url      = "http://apps.fz-juelich.de/scalasca/releases/extra-p/extrap-3.0.tar.gz"

    version('3.0', sha256='47ee80ba1b8e1a122aa250f026003e3ed4a674842d4fdc7e5e9465387d593a8f')

    depends_on('cubelib@4.3:')
    depends_on('python@3:')
    depends_on('py-pyqt5')
    depends_on('py-matplotlib')

    @run_after('install')
    def install_include(self):
        install_tree('include', self.prefix.include)

