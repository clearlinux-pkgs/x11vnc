#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : x11vnc
Version  : 00f2b16442b23a06bae6135d953a9b0e76ee4d62
Release  : 8
URL      : https://github.com/LibVNC/x11vnc/archive/00f2b16442b23a06bae6135d953a9b0e76ee4d62.tar.gz
Source0  : https://github.com/LibVNC/x11vnc/archive/00f2b16442b23a06bae6135d953a9b0e76ee4d62.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: x11vnc-bin = %{version}-%{release}
Requires: x11vnc-data = %{version}-%{release}
Requires: x11vnc-license = %{version}-%{release}
Requires: x11vnc-man = %{version}-%{release}
BuildRequires : cairo-dev
BuildRequires : libXinerama-dev
BuildRequires : libXtst-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(libvncclient)
BuildRequires : pkgconfig(libvncserver)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xrandr)
BuildRequires : sed
Patch1: norc4.patch

%description
[![Build Status](https://travis-ci.org/LibVNC/x11vnc.svg?branch=master)](https://travis-ci.org/LibVNC/x11vnc)

%package bin
Summary: bin components for the x11vnc package.
Group: Binaries
Requires: x11vnc-data = %{version}-%{release}
Requires: x11vnc-license = %{version}-%{release}
Requires: x11vnc-man = %{version}-%{release}

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
%setup -q -n x11vnc-00f2b16442b23a06bae6135d953a9b0e76ee4d62
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542434590
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1542434590
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/x11vnc
cp misc/LICENSE %{buildroot}/usr/share/package-licenses/x11vnc/misc_LICENSE
cp misc/enhanced_tightvnc_viewer/COPYING %{buildroot}/usr/share/package-licenses/x11vnc/misc_enhanced_tightvnc_viewer_COPYING
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
/usr/share/package-licenses/x11vnc/misc_LICENSE
/usr/share/package-licenses/x11vnc/misc_enhanced_tightvnc_viewer_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/x11vnc.1
