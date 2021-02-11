#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : x11vnc
Version  : 0.9.16
Release  : 11
URL      : https://github.com/LibVNC/x11vnc/archive/0.9.16/x11vnc-0.9.16.tar.gz
Source0  : https://github.com/LibVNC/x11vnc/archive/0.9.16/x11vnc-0.9.16.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: x11vnc-bin = %{version}-%{release}
Requires: x11vnc-data = %{version}-%{release}
Requires: x11vnc-license = %{version}-%{release}
Requires: x11vnc-man = %{version}-%{release}
BuildRequires : cairo-dev
BuildRequires : libXtst-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(libvncclient)
BuildRequires : pkgconfig(libvncserver)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xi)
BuildRequires : sed
Patch1: 0001-no-rc4.patch
Patch2: 0002-Fix-build-with-fno-common.patch
Patch3: 0003-src-cursor-fix-xfc-NULL-pointer-dereference.patch
Patch4: CVE-2020-29074.patch

%description
[![Build Status](https://travis-ci.org/LibVNC/x11vnc.svg?branch=master)](https://travis-ci.org/LibVNC/x11vnc)

%package bin
Summary: bin components for the x11vnc package.
Group: Binaries
Requires: x11vnc-data = %{version}-%{release}
Requires: x11vnc-license = %{version}-%{release}

%description bin
bin components for the x11vnc package.


%package data
Summary: data components for the x11vnc package.
Group: Data

%description data
data components for the x11vnc package.


%package license
Summary: license components for the x11vnc package.
Group: Default

%description license
license components for the x11vnc package.


%package man
Summary: man components for the x11vnc package.
Group: Default

%description man
man components for the x11vnc package.


%prep
%setup -q -n x11vnc-0.9.16
cd %{_builddir}/x11vnc-0.9.16
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613014831
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1613014831
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/x11vnc
cp %{_builddir}/x11vnc-0.9.16/COPYING %{buildroot}/usr/share/package-licenses/x11vnc/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/x11vnc-0.9.16/misc/LICENSE %{buildroot}/usr/share/package-licenses/x11vnc/602bc8c6ce5e9f04bc1f31c0903947632222d8e0
cp %{_builddir}/x11vnc-0.9.16/misc/enhanced_tightvnc_viewer/COPYING %{buildroot}/usr/share/package-licenses/x11vnc/ab8577d3eb0eedf3f98004e381a9cee30e7224e1
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/Xdummy
/usr/bin/x11vnc

%files data
%defattr(-,root,root,-)
/usr/share/applications/x11vnc.desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/x11vnc/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/x11vnc/602bc8c6ce5e9f04bc1f31c0903947632222d8e0
/usr/share/package-licenses/x11vnc/ab8577d3eb0eedf3f98004e381a9cee30e7224e1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/x11vnc.1
