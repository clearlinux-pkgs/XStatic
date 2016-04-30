#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic
Version  : 1.0.1
Release  : 13
URL      : https://pypi.python.org/packages/source/X/XStatic/XStatic-1.0.1.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic/XStatic-1.0.1.tar.gz
Summary  : XStatic base package with minimal support code
Group    : Development/Tools
License  : MIT
Requires: XStatic-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic
-------
The goal of XStatic family of packages is to provide static file packages
with minimal overhead - without selling you some dependencies you don't want.

%package python
Summary: python components for the XStatic package.
Group: Default

%description python
python components for the XStatic package.


%prep
%setup -q -n XStatic-1.0.1

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
