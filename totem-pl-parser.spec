Name:		totem-pl-parser
Version:	2.28.3
Release:	1%{?dist}
Summary:	Totem Playlist Parser library

Group:		System Environment/Libraries
License:	LGPLv2+
Url:		http://www.gnome.org/projects/totem/
Source0:	http://download.gnome.org/sources/%{name}/2.28/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes:	totem-plparser

BuildRequires:	gtk2-devel
BuildRequires:	libxml2-devel
BuildRequires:	gettext
BuildRequires:	perl(XML::Parser) intltool

# Remove gmime dependency, and copy/paste instead
Patch0:		0001-Remove-compile-time-GMime-dependency.patch
Patch1:		totem-pl-parser-2.28.6-autoreconf.patch
BuildRequires:	libtool autoconf automake gnome-common

%description
A library to parse and save playlists, as used in music and movie players.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Obsoletes:	totem-devel < 2.21.90
Requires:       %{name} = %{version}-%{release}
Requires:	pkgconfig
Requires:	gtk2-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .gmime

# Those will not work on RHEL-6, as we do not have gobject-introspection-devel there
#autoreconf -i
#libtoolize -f
%patch1 -p1 -b .gmime-autotools

%build
%configure --enable-static=no
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LIB NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/totem-pl-parser

%changelog
* Tue Jun 01 2010 Bastien Nocera <bnocera@redhat.com> 2.28.3-1
- Rebase to 2.28.3
Related: rhbz#582850

* Thu Jan 14 2010 Bastien Nocera <bnocera@redhat.com> 2.28.2-3
- Fix pkg-config file
Related: rhbz#543948

* Wed Jan 13 2010 Bastien Nocera <bnocera@redhat.com> 2.28.2-2
- Remove gmime BR
Related: rhbz#543948

* Fri Dec 11 2009 Bastien Nocera <bnocera@redhat.com> 2.28.2-1
- Update to 2.28.2

* Thu Oct 15 2009 Bastien Nocera <bnocera@redhat.com> 2.28.1-2
- Fix crasher when parsing multiple XML-ish playlists in Rhythmbox

* Tue Sep 29 2009 Bastien Nocera <bnocera@redhat.com> 2.28.1-1
- Update to 2.28.1

* Mon Sep 21 2009 Bastien Nocera <bnocera@redhat.com> 2.28.0-2
- Update source URL

* Mon Sep 21 2009 Bastien Nocera <bnocera@redhat.com> 2.28.0-1
- Update to 2.28.0

* Tue Sep 15 2009 Bastien Nocera <bnocera@redhat.com> 2.27.92-1
- Update to 2.27.92

* Tue Sep 08 2009 Bastien Nocera <bnocera@redhat.com> 2.27.2-4
- Version Obsoletes for totem-devel (#520874)

* Tue Aug 11 2009 Bastien Nocera <bnocera@redhat.com> 2.27.2-3
- Fix URL

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Bastien Nocera <bnocera@redhat.com> 2.27.2-1
- Update to 2.27.2

* Wed May 06 2009 Bastien Nocera <bnocera@redhat.com> 2.27.1-1
- Update to 2.27.1

* Tue Mar 31 2009 - Bastien Nocera <bnocera@redhat.com> - 2.26.1-1
- Update to 2.26.1

* Mon Mar 16 2009 - Bastien Nocera <bnocera@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Tue Mar 03 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.92-1
- Update to 2.25.92

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.91-1
- Update to 2.25.91

* Tue Feb 03 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.90-1
- Update to 2.25.90

* Tue Feb 03 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.1-3
- Rebuild for new libcamel

* Tue Dec 09 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.1-2
- Add evolution-data-server-devel Requires for the devel package

* Mon Dec 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.1-1
- Update to 2.25.1

* Fri Dec 05 2008 Matthew Barnes <mbarnes@redhat.com> - 2.24.2-3
- Rebuild against newer libcamel.

* Fri Nov 14 2008 Matthias Clasen  <mclasen@redhat.com> - 2.24.2-2
- Rebuild

* Thu Oct 30 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.2-1
- Update to 2.24.2

* Tue Oct 21 2008 Matthias Clasen  <mclasen@redhat.com> - 2.24.1-2
- Rebuild

* Tue Oct 07 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Sun Sep 21 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Fri Aug 29 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Tue Aug  5 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.3-2
- Rebuild

* Mon Jul 14 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.3-1
- Update to 2.23.3
- Fixes crasher when totem_cd_detect_type() generates an error (#455014)

* Wed Jun 11 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.2-1
- Update to 2.23.2

* Tue May 13 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.1-2
- Rebuild

* Fri May 09 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.1-1
- Update to 2.23.1
- Remove gnome-vfs2 dependencies

* Wed May 07 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.2-3
- Rebuild for new libcamel

* Sun May  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.2-2
- Fix source url

* Tue Apr 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.2-1
- Update to 2.22.2

* Mon Mar 10 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.1-1
- Update to 2.22.1

* Mon Mar 10 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Sun Feb 24 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.92-1
- Update to 2.21.92

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.21.91-3
- Autorebuild for GCC 4.3

* Tue Jan 29 2008 - Matthew Barnes <mbarnes@redhat.com> - 2.21.21-2
- Rebuild against newer libcamel-1.2.

* Mon Jan 21 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.91-1
- Update to 2.21.91

* Mon Jan 07 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.90-1
- Update to 2.21.90

* Thu Dec 06 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.6-1
- First package

