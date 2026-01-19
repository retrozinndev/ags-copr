%global lib gtk3
%global gir Astal-3.0


Name: astal3
Version: 0.0.1
Release: 1%{?dist}
Summary: GTK3 building blocks for creating custom desktop shells
License: LGPL-2.1
BuildArch: x86_64
URL: https://github.com/Aylur/astal

%global libdir %{_builddir}/lib/astal/%{lib}

Source0: https://github.com/Aylur/astal/archive/refs/heads/main.tar.gz

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
tar -xvzf %{SOURCE0} --directory %{_builddir}

%build
cd %{libdir}
meson setup build
meson compile -C build

%install
mkdir -p %{buildroot}%{_datadir}/gir-1.0
meson install -C %{libdir}/build --destdir %{buildroot}


# %post

#-- FILES ---------------------------------------------------------------------#
%files
%{_datadir}/gir-1.0/%{gir}.gir

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Sun Jan 18 2026 João Dias <joaovodias@gmail.com> - 0.0.1-1
- Initial release for Fedora copr
