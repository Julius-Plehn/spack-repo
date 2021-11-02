# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install libtensorflow
#
# You can edit this file again by typing:
#
#     spack edit libtensorflow
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Libtensorflow(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-linux-x86_64-2.6.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('2.6.0', sha256='58ff05f77aa1d969f912857e8a4edb17cc5b8220eeff13aaf807dcc10716a45d')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    def setup_run_environment(self, env):
        lib_dir = self.prefix.lib

        env.prepend_path('CPATH', self.prefix.include)
        env.prepend_path('LIBRARY_PATH', lib_dir)
        env.prepend_path('LD_LIBRARY_PATH', lib_dir)

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        with working_dir(self.stage.source_path):
            install_tree('./', prefix)

