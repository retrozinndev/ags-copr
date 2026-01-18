%define lib gtk3
%define gir Astal-3.0
%define libdir %{_builddir}/lib/astal/%{lib}


Name: astal3
Version: 0.0.1
Release: 1%{?dist}
License: LGPL-2.1
Summary: GTK3 building blocks for creating custom desktop shells
URL: https://github.com/Aylur/astal
BuildArch: x86_64

Source0: https://github.com/retrozinndev/ags-copr/archive/refs/heads/main.tar.gz
Source1: https://github.com/Aylur/astal/archive/refs/heads/main.tar.gz

#-- APPLICATION DEPENDENCIES ---------------------------------------------------#
Requires: gobject-introspection
Requires: gtk3
Requires: gtk-layer-shell

#-- OPTIONAL DEPENDENCIES ------------------------------------------------------#
#-- none... -----#

#-- BUILD DEPENDENCIES ---------------------------------------------------------#
BuildRequires: meson
BuildRequires: vala
BuildRequires: valadoc
BuildRequires: gobject-introspection-devel
BuildRequires: gtk3-devel
BuildRequires: gtk-layer-shell-devel

%description
%{summary}

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
tar -xvzf %{SOURCE1} --directory %{_builddir}
cd %{libdir}
meson setup build
meson compile -C build

%install
mkdir -p %{buildroot}%{_datadir}/gir-1.0
cp -f %{libdir}/build/%{gir}.gir %{buildroot}%{_datadir}/gir-1.0/%{gir}.gir


# %post

#-- FILES ---------------------------------------------------------------------#
%files
%{_builddir}%{_datadir}/gir-1.0/%{gir}.gir

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Sun Jan 18 2026 João Dias <joaovodias@gmail.com> - 0.0.1-1
- Initial release for Fedora copr
