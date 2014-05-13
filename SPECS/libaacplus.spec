Name:		libaacplus
Version:	2.0.2
Release:	1%{?dist}
Summary:	The AAC+ (HE-AAC) codec based on 3GPP reference implementation.

License:	3GPP
URL:		http://tipok.org.ua/node/17
Source0:	libaacplus-2.0.2.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	libtool

%description
The AAC+ (HE-AAC) shared library which supports multiple bitrates.

This lib is needed for Darkice to be able to encode AAC+ streams.

%prep
%setup -q


%build
./autogen.sh --enable-shared --enable-static
./configure --prefix=/usr
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
ldconfig


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
/usr/share/man/man1/aacplus*
%{_bindir}/aacplusenc
/usr/lib/libaacplus.*
/usr/lib/pkgconfig/aacplus.*
/usr/include/aacplus*


%changelog
* Tue May 13 2014 Vlad Ionescu <vlad@vladionescu.com> - 2.0.2-1-el6
- Built for RHEL 6.5, to be distribuited via salt. Used to run Darkice @ WITR 89.7
