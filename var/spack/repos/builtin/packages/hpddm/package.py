# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Hpddm(Package):
    """High-performance unified framework for domain decomposition methods."""

    homepage = "https://github.com/hpddm/hpddm"
    url = "https://github.com/hpddm/hpddm"
    git = "https://github.com/hpddm/hpddm.git"

    maintainers("corentin-dev")

    version("main", branch="main")

    version("2.2.3", commit="54228a5288a38cf1a144df13c96b00ac9240179c")
    version("2.2.2", commit="ff61cf3ced922c2f896ebe1fff1a42f1f2805a3a")
    version("2.2.1", commit="382ee53a2fb9dcb3ff32424a2cbe6dc3cea89514")
    version("2.2.0", commit="5641877b44006c012c7fda0593d44e11c19c1c5b")
    version("2.1.3", commit="32025e4ee75a16fa67399d26dd86910c03910dba")
    version("2.1.2", commit="e58205623814f59bf2aec2e2bab8eafcfbd22466")
    version("2.1.1", commit="a02ebf482871ee07965ac785f6cf3d9978173b9b")
    version("2.1.0", commit="2096feeca21992be559cfe44de0a196878b19285")
    version("2.0.8", commit="91e49a61e229462a44acbc0440a9c855b77ff2fd")
    version("2.0.7", commit="5f2a51beb150eace12bafd884a922c8a0aa332a4")
    version("2.0.6", commit="ce6ce80b62e9bc71efedf8b9cb6ffb00dfd6e44e")
    version("2.0.5", commit="21c972f2488edbbd4948c937d7c929b38de9def7")
    version("2.0.4", commit="90c799d97bd0d3fa738cb288e5111f131b39753b")
    version("2.0.3", commit="8f545f4217c263fa5c5980b08fa10d68598b5305")
    version("2.0.2", commit="f94ef3fe56078cc59809f8b8ef568c0e98818e80")
    version("2.0.1", commit="7d809610de85db8d0c4a53d94ccb188a484ef0f7")
    version("2.0.0", commit="e7d921ec93b84f41984530822adda1f6fc8b611a")

    depends_on("mpi")
    depends_on("blas")
    depends_on("lapack")
    depends_on("mumps")
    depends_on("hypre")
    depends_on("scalapack")
    depends_on("arpack-ng")
    depends_on("python")

    def configure(self):
        makefile_inc = []
        # cflags = [
        makefile_inc.append("SOLVER ?= MUMPS")
        makefile_inc.append("SUBSOLVER ?= MUMPS")
        makefile_inc.append("EIGENSOLVER ?= ARPACK")
        makefile_inc.append("MPICXX ?= mpic++")
        makefile_inc.append("MPICC ?= mpicc")
        makefile_inc.append("MPIF90 ?= mpif90")
        makefile_inc.append("MPIRUN ?= mpirun -np")

        makefile_inc.append("override CXXFLAGS += -std=c++11 -O3 -fPIC")
        makefile_inc.append("override CFLAGS += -std=c99 -O3")
        makefile_inc.append("INCS =")
        makefile_inc.append("LIBS =")

        makefile_inc.append("HPDDMFLAGS ?= -DHPDM_NUMBERING='C'")

        makefile_inc.append("MUMPS_INCS = ")
        makefile_inc.append("PYTHON_INCS = ")
        makefile_inc.append("BLAS_LIBS = -lopenblas")
        makefile_inc.append("ARPACK_LIBS = -larpack")
        makefile_inc.append("SCALAPACK_LIBS = -lscalapack")
        makefile_inc.append(
            " ".join(
                [
                    "MUMPS_LIBS",
                    "=",
                    "-lcmumps",
                    "-ldmumps",
                    "-lsmumps",
                    "-lzmumps",
                    "-lmumps_common",
                    "-lpord",
                    "-fopenmp",
                ]
            )
        )
        makefile_inc.append("HYPRE_LIBS = -lHYPRE")
        makefile_inc.append("PYTHON_LIBS = -lpython3")

        with working_dir("."):
            with open("Makefile.inc", "w") as fh:
                fh.write("\n".join(makefile_inc))

    def patch(self):
        self.configure()

    def install(self, spec, prefix):
        make()
        install_tree("include", prefix.include)
        # make('install')
