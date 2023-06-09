#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-ypy_websocket
Version  : 0.12.1
Release  : 7
URL      : https://files.pythonhosted.org/packages/85/46/d7c070b3d791cbf8ed16c1a3763c3eadf987fbb90959059662e5d8131639/ypy_websocket-0.12.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/85/46/d7c070b3d791cbf8ed16c1a3763c3eadf987fbb90959059662e5d8131639/ypy_websocket-0.12.1.tar.gz
Summary  : WebSocket connector for Ypy
Group    : Development/Tools
License  : MIT
Requires: pypi-ypy_websocket-license = %{version}-%{release}
Requires: pypi-ypy_websocket-python = %{version}-%{release}
Requires: pypi-ypy_websocket-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Ypy-websocket
Ypy-websocket is an async WebSocket connector for Ypy.
[![Build Status](https://github.com/y-crdt/ypy-websocket/workflows/CI/badge.svg)](https://github.com/y-crdt/ypy-websocket/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

%package license
Summary: license components for the pypi-ypy_websocket package.
Group: Default

%description license
license components for the pypi-ypy_websocket package.


%package python
Summary: python components for the pypi-ypy_websocket package.
Group: Default
Requires: pypi-ypy_websocket-python3 = %{version}-%{release}

%description python
python components for the pypi-ypy_websocket package.


%package python3
Summary: python3 components for the pypi-ypy_websocket package.
Group: Default
Requires: python3-core
Provides: pypi(ypy_websocket)
Requires: pypi(aiosqlite)
Requires: pypi(anyio)
Requires: pypi(y_py)

%description python3
python3 components for the pypi-ypy_websocket package.


%prep
%setup -q -n ypy_websocket-0.12.1
cd %{_builddir}/ypy_websocket-0.12.1
pushd ..
cp -a ypy_websocket-0.12.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687275549
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . aiofiles
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . aiofiles
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ypy_websocket
cp %{_builddir}/ypy_websocket-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ypy_websocket/9465b3e2ebae3e9685ba948c32cb340bceb4b12c || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} aiofiles
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ypy_websocket/9465b3e2ebae3e9685ba948c32cb340bceb4b12c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
