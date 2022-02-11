# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Onnxruntime(Package):
    """ONNX Runtime: cross-platform, high performance ML 
    inferencing and training accelerator"""

    homepage = "www.onnxruntime.ai"
    url      = "https://github.com/microsoft/onnxruntime/archive/refs/tags/v1.9.1.tar.gz"
    git      = "https://github.com/microsoft/onnxruntime.git"
    
    #version('1.9.1', sha256='21632fe1354abdec6d513ea8fe88aa83b1bc05d801a82642cf816b580b5cda7c')
    version('1.9.1', tag='v1.9.1')

    depends_on('python', type='build')
    depends_on('flatbuffers +python')

    def setup_run_environment(self, env):
        lib_dir = self.prefix.RelWithDebInfo

        #env.prepend_path('CPATH', self.prefix.include)
        env.prepend_path('LIBRARY_PATH', lib_dir)
        env.prepend_path('LD_LIBRARY_PATH', lib_dir)

    def install(self, spec, prefix):
        bash = which('bash')
        bash('build.sh', '--build_dir=%s' % prefix, '--config=RelWithDebInfo', '--build_shared_lib', '--parallel=0', '--disable_ml_ops', '--skip_tests')

