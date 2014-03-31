Summary:	A weather application for GNOME
Name:		gnome-weather
Version:	3.12.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-weather/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	4a4c2a938d51b746b9a8daa7eaf33dc9
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.12
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel >= 1.40.0
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gobject-introspection-devel >= 1.36.0
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgweather-devel >= 3.10.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.36.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	gjs >= 1.40.0
Requires:	glib2 >= 1:2.36.0
Requires:	gtk+3 >= 3.12.0
Requires:	hicolor-icon-theme
Requires:	libgweather >= 3.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-weather is a small application that allows you to monitor the
current weather conditions for your city, or anywhere in the world,
and to access updated forecasts provided by various internet services.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4 -I libgd
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	GJS="/usr/bin/gjs" \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/org.gnome.Weather.Application/*.la

%find_lang org.gnome.Weather.Application

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f org.gnome.Weather.Application.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-weather
%dir %{_libdir}/org.gnome.Weather.Application
%{_libdir}/org.gnome.Weather.Application/girepository-1.0
%attr(755,root,root) %{_libdir}/org.gnome.Weather.Application/libgd.so
%{_datadir}/appdata/org.gnome.Weather.Application.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Weather.Application.service
%{_datadir}/gnome-shell/search-providers/org.gnome.Weather.Application.search-provider.ini
%{_datadir}/glib-2.0/schemas/org.gnome.Weather.Application.gschema.xml
%{_datadir}/org.gnome.Weather.Application
%{_desktopdir}/org.gnome.Weather.Application.desktop
%{_iconsdir}/hicolor/*/*/org.gnome.Weather.Application.png
