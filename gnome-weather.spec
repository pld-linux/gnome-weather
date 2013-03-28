Summary:	A weather application for GNOME
Name:		gnome-weather
Version:	3.8.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-weather/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	f4e34d19aed2d780840cb7af02698482
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gobject-introspection-devel >= 1.36.0
BuildRequires:	gtk+3-devel >= 3.8.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig
Requires(post,postun):	glib2 >= 1:2.36.0
Requires:	gjs
Requires:	glib2 >= 1:2.36.0
Requires:	gtk+3 >= 3.8.0
Requires:	libgweather >= 3.8.0
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-weather/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-weather
%dir %{_libdir}/gnome-weather
%{_libdir}/gnome-weather/girepository-1.0
%attr(755,root,root) %{_libdir}/gnome-weather/libgd.so
%{_datadir}/gnome-weather
%{_datadir}/glib-2.0/schemas/org.gnome.Weather.Application.gschema.xml
%{_desktopdir}/gnome-weather.desktop
