Summary:	Command-line application to restore firmware files to iOS devices
Summary(pl.UTF-8):	Narzędzie linii poleceń do przywracania plików firmware w urządzeniach iOS
Name:		idevicerestore
Version:	1.0.0
%define	gitref	4b3e847e1d9a1210049a9e3f1d1caa38650c6617
%define	snap	20261006
%define	rel	1
Release:	4.%{snap}.%{rel}
License:	LGPL v2.1+
Group:		Applications
#Source0Download: https://libimobiledevice.org/
#Source0:	https://github.com/libimobiledevice/idevicerestore/releases/download/%{version}/%{name}-%{version}.tar.bz2
Source0:	https://github.com/libimobiledevice/idevicerestore/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	4c9908bc70e19fe5102a5ba153eeefe2
Patch0:		%{name}-sh.patch
URL:		https://libimobiledevice.org/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.0
BuildRequires:	libimobiledevice-devel >= 1.4.0
BuildRequires:	libimobiledevice-glue-devel >= 1.3.0
BuildRequires:	libirecovery-devel >= 1.3.0
BuildRequires:	libplist-devel >= 2.6.0
BuildRequires:	libtool >= 2:2
BuildRequires:	libtatsu-devel >= 1.0.4
BuildRequires:	libusbmuxd-devel >= 2.0.2
BuildRequires:	libzip-devel >= 1.0
BuildRequires:	openssl-devel >= 0.9.8
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	libimobiledevice >= 1.4.0
Requires:	libimobiledevice-glue >= 1.3.0
Requires:	libirecovery >= 1.3.0
Requires:	libplist >= 2.6.0
Requires:	libtatsu-devel >= 1.0.4
Requires:	libusbmuxd >= 2.0.2
Requires:	libzip >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The idevicerestore application is a full reimplementation of all
granular steps which are performed during the restore of a firmware to
a device.

In general, upgrades and downgrades are possible, however subject to
availability of SHSH blobs from Apple for signing the firmare files.

%description -l pl.UTF-8
Aplikacja idevicerestore to pełna reimplementacja wszystkich kroków
wykonywanych podczas przywracania firmware'u urządzenia.

W ogólności możliwe są upgrade'y i downgrade'y, ale zależy to od
dostępności blobów SHSH od Apple'a do podpisywania plików firmware'u.

%prep
%setup -q -n %{name}-%{gitref}
%patch -P0 -p1

echo "%{version}.%{snap}" > .tarball-version

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/idevicerestore
%{_mandir}/man1/idevicerestore.1*
