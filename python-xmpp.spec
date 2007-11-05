Name:		python-xmpp
Version:	1.0.0
Release:	%mkrel 1
URL:		http://pyxmpp.jajcus.net/
Summary:	PyXMPP -- Python Jabber/XMPP implementation
Source0:	http://pyxmpp.jajcus.net/downloads/pyxmpp-%{version}.tar.gz
Source1:	http://pyxmpp.jajcus.net/downloads/pyxmpp-%{version}.tar.gz.md5
Group:		System/Libraries 
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
