Summary:        DeskOS settings for GNOME
Name:           deskos-settings-gnome
Version:        0.2
Release:        1

Group:          System Environment/Base
License:        GPLv3+
Url:            https://github.com/deskosproject/deskos-settings-gnome-rpm
Source0:        org.deskos.gschema.override

Requires(post): dconf
Requires(post): glib2

%description
DeskOS settings for GNOME.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas

# GNOME override
install -m 0644 %{SOURCE0} %{buildroot}%{_datadir}/glib-2.0/schemas/org.deskos.gschema.override

%clean
rm -rf %{buildroot}

%pre

%post
# Reload changes
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null
dconf update

%postun
# Reload changes
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null
dconf update

%files
%defattr(-,root,root,-)
%{_datadir}/glib-2.0/schemas/org.deskos.gschema.override

%changelog
* Wed Aug 03 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.2-1
- Fixed favorite-apps
- Added font antialiasing config

* Thu May 12 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1-1
- Initial release
