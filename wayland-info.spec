%define		snap	20211213
%define		gitref	f7f4e42ed46200b4bf1c1df4d26ee8f4b532439a
Summary:	Utility for displaying information about Wayland compositor
Name:		wayland-info
Version:	0.0.1
Release:	0.%{snap}.1
License:	MIT
Group:		Applications
Source0:	https://gitlab.freedesktop.org/ofourdan/wayland-info/-/archive/%{gitref}/%{name}-%{gitref}.tar.bz2
# Source0-md5:	f7a397e761fcc39755d16b3b83a1a4f6
URL:		https://gitlab.freedesktop.org/ofourdan/wayland-info
BuildRequires:	meson >= 0.47
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	wayland-devel >= 1.17.0
BuildRequires:	wayland-protocols >= 1.18
Requires:	wayland >= 1.17.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wayland-info is a utility for displaying information about the Wayland
protocols supported by a Wayland compositor.

It can be used to check which Wayland protocols and versions are
advertised by the Wayland compositor.

wayland-info also provides additional information for a subset of
Wayland protocols it knows about, namely Linux DMABUF, presentation
time, tablet and XDG output protocols.

%prep
%setup -q -n %{name}-%{gitref}

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/wayland-info
%{_mandir}/man1/wayland-info.1*
