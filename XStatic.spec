#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic
Version  : 1.0.2
Release  : 35
URL      : https://files.pythonhosted.org/packages/36/78/c0ffaf14216517a14d3daa67ff24fbb60b4703e95ce1059a48fd508e6b8c/XStatic-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/36/78/c0ffaf14216517a14d3daa67ff24fbb60b4703e95ce1059a48fd508e6b8c/XStatic-1.0.2.tar.gz
Summary  : XStatic base package with minimal support code
Group    : Development/Tools
License  : MIT
Requires: XStatic-python = %{version}-%{release}
Requires: XStatic-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
-------
        
        The goal of XStatic family of packages is to provide static file packages
        with minimal overhead - without selling you some dependencies you don't want.
        
        XStatic has some minimal support code for working with the XStatic-* packages.

%package python
Summary: python components for the XStatic package.
Group: Default
Requires: XStatic-python3 = %{version}-%{release}
Provides: xstatic-python

%description python
python components for the XStatic package.


%package python3
Summary: python3 components for the XStatic package.
Group: Default
Requires: python3-core
Provides: pypi(xstatic)

%description python3
python3 components for the XStatic package.


%prep
%setup -q -n XStatic-1.0.2
cd %{_builddir}/XStatic-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603409255
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
