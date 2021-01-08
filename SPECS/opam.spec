Name:           opam
Version:        2.0.7
Release:        1%{?dist}
Summary:        Source-based OCaml package manager
License:        LGPLv2.1
URL:            https://github.com/ocaml/opam

Source0: https://github.com/ocaml/opam/releases/download/2.0.7/opam-full-2.0.7.tar.gz



BuildRequires:  curl
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  gcc gcc-c++

%description
Opam is a source-based package manager for OCaml. It supports multiple
simultaneous compiler installations, flexible package constraints, and
a Git-friendly development workflow.

%prep
%autosetup -n %{name}-full-%{version} -p1

%build
%configure
make lib-ext
make

%install
# The makefile looks like it tries to invoke ocamlfind but only if DESTDIR
# isn't set. If it is set (which it is) LIBINSTALLDIR must be set too
# for installing opam-installer metadata.
%make_install LIBINSTALL_DIR=%{buildroot}/%{_libdir}/ocaml

# However it looks like some (extra) documentation gets
# installed in the wrong place so... delete it.
rm -rf %{buildroot}%{_prefix}/doc

%files
%doc README.md CHANGES AUTHORS CONTRIBUTING.md
%{_bindir}/opam
%{_bindir}/opam-installer
%license LICENSE
%{_mandir}/man1/*.1*
%exclude /usr/doc/opam-installer/*

%changelog
* Fri Jan 08 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 2.0.7-1
- Update to 2.0.7, include some comments from the fedora package

* Wed Dec 04 2019 Christian Lindig <christian.lindig@citrix.com> - 2.0.5-1
- update for compatibility with OCaml 4.08

* Wed Oct 03 2018 Christian Lindig <christian.lindig@citrix.com> - 2.0.0-2
- update License, use mirror for Source0

* Fri Sep 28 2018 Christian Lindig <christian.lindig@citrix.com> - 2.0.0-1
- First packaging of Opam 2

* Tue Sep 04 2018 Christian Lindig <christian.lindig@citrix.com> - 1.2.2-4
- Add patch to compile with -unsafe-string

* Tue Oct 3 2017 Edwin Török <edvin.torok@citrix.com> - 1.2.2-3
- CP-24976: Apply upstream patch to fix jbuilder install location of C stubs

* Mon Feb 27 2017 Christian Lindig <christian.lindig@citrix.com> - * 1.2.2-2
- Download sources from Artifactory

* Thu Dec 8 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2.2-1
- Update to 1.2.2

* Fri Dec 26 2014 David Scott <dave.scott@citrix.com> - 1.2.0-1
- Update to 1.2.0

* Thu Oct 02 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.1.2-2
- Force a rebuild

* Fri Aug 01 2014 Euan Harris <euan.harris@citrix.com> - 1.1.2-1
- Initial package
