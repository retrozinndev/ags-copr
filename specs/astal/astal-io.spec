%global lib io
%global gir AstalIO-0.1


Name: astal-io
Version: 0.0.1
Release: 1%{?dist}
Summary: Building blocks for creating custom desktop shells
License: LGPL-2.1
BuildArch: x86_64
URL: https://github.com/Aylur/astal

%global libdir %{_builddir}/astal-main/lib/astal/%{lib}

Source0: https://github.com/Aylur/astal/archive/refs/heads/main.tar.gz

#-- BUILD DEPENDENCIES ---------------------------------------------------------#
BuildRequires: rpmspectool
BuildRequires: rpmdevtools
BuildRequires: rpm-build
BuildRequires: meson
BuildRequires: valadoc
BuildRequires: gobject-introspection-devel
BuildRequires: gtk3-devel
BuildRequires: glib2-devel
BuildRequires: gtk-layer-shell-devel

#-- APPLICATION DEPENDENCIES ---------------------------------------------------#
Requires: vala
Requires: gobject-introspection
Requires: glib2

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
%{_datadir}/gir-1.0/%{gir}.gir
%{_datadir}/girepository-1.0/%{gir}.typelib

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Sun Jan 19 2026 João Dias <joaovodias@gmail.com> - 0.0.1-1
- Initial release for Fedora copr

