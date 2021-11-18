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
#     spack install onnxruntime
#
# You can edit this file again by typing:
#
#     spack edit onnxruntime
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Onnxruntime(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/microsoft/onnxruntime/archive/refs/tags/v1.9.1.tar.gz"
    git      = "https://github.com/microsoft/onnxruntime.git"
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    
    #version('1.9.1', sha256='21632fe1354abdec6d513ea8fe88aa83b1bc05d801a82642cf816b580b5cda7c')
    version('1.9.1', tag='v1.9.1')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('python', type='build')
    depends_on('flatbuffers +python')

    def setup_run_environment(self, env):
        lib_dir = self.prefix.RelWithDebInfo

        #env.prepend_path('CPATH', self.prefix.include)
        env.prepend_path('LIBRARY_PATH', lib_dir)
        env.prepend_path('LD_LIBRARY_PATH', lib_dir)

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        bash = which('bash')
        #bash('build.sh', '--config RelWithDebInfo --build_shared_lib --parallel --build_dir %s' % prefix)
        bash('build.sh', '--build_dir=%s' % prefix, '--config=RelWithDebInfo', '--build_shared_lib', '--parallel=0', '--disable_ml_ops', '--skip_tests')
        #p = which('python')
        #p('tools/ci_build/build.py', '--build_dir=%s' % prefix, '--config=RelWithDebInfo', '--build_shared_lib', '--parallel=0', '--disable_ml_ops', '--skip_tests')

