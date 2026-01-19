# version numbers
%global masterver 3
%global minorver 0
%global patchver 0
# -------
# simplever is a minified version of the main version numbers, if it has a patch number higher than 0, it should be explicitly added here
%global simplever %{masterver}.%{minorver}
%global lib gtk3
%global header astal
%global gir Astal-%{simplever}
%global libheader lib%{header}
%global libdir %{_builddir}/astal-main/lib/astal/%{lib}


Name: astal3
Version: %{masterver}.%{minorver}.%{patchver}
Release: 1%{?dist}
Summary: GTK3 building blocks for creating custom desktop shells
License: LGPL-2.1
BuildArch: x86_64
URL: https://github.com/Aylur/astal

Source0: https://github.com/Aylur/astal/archive/refs/heads/main.tar.gz

#-- BUILD DEPENDENCIES ---------------------------------------------------------#
BuildRequires: rpmspectool
BuildRequires: rpmdevtools
BuildRequires: rpm-build
BuildRequires: meson
BuildRequires: valadoc
BuildRequires: gobject-introspection-devel
BuildRequires: gtk3-devel
BuildRequires: gtk-layer-shell-devel
BuildRequires: astal-io

#-- APPLICATION DEPENDENCIES ---------------------------------------------------#
Requires: vala
Requires: gobject-introspection
Requires: gtk3
Requires: gtk-layer-shell
Requires: astal-io

#-- OPTIONAL DEPENDENCIES ------------------------------------------------------#
#-- none... -----#

%description
%{summary}

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup
spectool %{name}.spec -g -S -C %{_sourcedir}
tar -xf %{_sourcedir}/main.tar.gz --directory %{_builddir}

%build
cd %{libdir}
meson setup build
meson compile -C build

%install
%meson_install -C %{libdir}/build --destdir %{buildroot}

# %post

#-- FILES ---------------------------------------------------------------------#
%files
/usr/local/lib64/%{libheader}.so.%{version}
/usr/local/include/%{header}.h
/usr/local/share/vala/vapi/%{header}-%{simplever}.vapi
/usr/local/share/gir-1.0/%{gir}.gir
/usr/local/lib64/girepository-1.0/%{gir}.typelib
/usr/local/lib64/pkg-config/%{header}-%{simplever}.pc
/usr/local/lib64/%{libheader}.so.%{masterver}
/usr/local/lib64/%{libheader}.so

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Sun Jan 18 2026 João Dias <joaovodias@gmail.com> - 0.0.1-1
- Initial release for Fedora copr

