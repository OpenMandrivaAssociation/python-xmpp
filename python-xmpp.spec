Name:		python-xmpp
Version:	1.0.0
Release:	%mkrel 5
URL:		http://pyxmpp.jajcus.net/
Summary:	Python Jabber/XMPP implementation
Source0:	http://pyxmpp.jajcus.net/downloads/pyxmpp-%{version}.tar.gz
Source1:	http://pyxmpp.jajcus.net/downloads/pyxmpp-%{version}.tar.gz.md5
Group:		System/Libraries 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	LGPLv2
BuildRequires:	python-m2crypto dnspython python-libxml2 python-devel libxml2-devel
Requires:	python-m2crypto dnspython python-libxml2 python
%description
PyXMPP is a Python XMPP (RFC 3920,3921) and Jabber implementation. It
is based on libxml2 -- fast and fully-featured XML parser.

PyXMPP provides most core features of the XMPP protocol and several
JSF-defined extensions. PyXMPP provides building blocks for creating
Jabber clients and components. Developer uses them to setup XMPP streams,
handle incoming events and create outgoing stanzas (XMPP "packets").

Features

 * nearly complete XMPP Core (RFC 3920) protocol for client connections
   (includes SASL, TLS and Strinprep).
 * mostly complete XMPP IM (RFC 3921) protocol (lacks privacy lists)
 * XMPP error objects including translations to and from legacy codes
   for backward compatibility (JEP-0086).
 * legacy authentication ("digest" and "plain") (JEP-0078).
 * component protocol (JEP-0114).
 * Service Discovery (JEP-0030).
 * vCards -- both Jabber "vcard-temp" and RFC 2426
 * basic parts of the Multi-User Chat protocol (JEP-0045)
 * delayed delivery timestamps (JEP-0091).
 * Data Forms (JEP-0004).
 * In-Band Registration (JEP-0077).

%prep
%setup -q -n pyxmpp-%{version}

%build
%__python setup.py build
%__python -O -c "import compileall; compileall.compile_dir('build')"
%__python -c "import compileall; compileall.compile_dir('build')"

%install
%{__rm} -Rf %{buildroot}
%__python setup.py install --prefix %{buildroot}%{_prefix}

%files
%doc ChangeLog COPYING PKG-INFO README TODO examples doc
%{py_platsitedir}/pyxmpp
%{py_platsitedir}/pyxmpp-%{version}-*


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-5mdv2010.0
+ Revision: 442549
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-4mdv2009.0
+ Revision: 259868
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-3mdv2009.0
+ Revision: 247742
- rebuild
- fix no-buildroot-tag
- fix summary

* Mon Nov 05 2007 Nicolas Vigier <nvigier@mandriva.com> 1.0.0-1mdv2008.1
+ Revision: 106192
- import python-xmpp


