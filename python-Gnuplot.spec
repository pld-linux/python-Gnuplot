%include 	/usr/lib/rpm/macros.python

%define		module Gnuplot

Summary:	A Python interface to the gnuplot plotting program
Summary(pl):	Interfejs dla Pythona do programu tworz±cego wykresy - gnuplot
Name:		python-%{module}
Version:	1.5
Release:	6
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/gnuplot-py/%{module}-%{version}.tar.gz
# Source0-md5:	94da6c11af51d5872c498e59fd31c9a0
URL:		http://gnuplot-py.sourceforge.net/
BuildRequires:	python >= 2.2.1
BuildRequires:	python-numpy
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	gnuplot
Requires:	python-numpy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnuplot.py is a Python package that allows you to create graphs from
within Python using the gnuplot plotting program.

%description -l pl
Gnuplot.py jest modu³em Pythona pozwalaj±cym na tworzenie wykresów z
poziomu Pythona u¿ywaj±c do tego programu gnuplot.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT

mv -f doc html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE.txt README.txt NEWS.txt CREDITS.txt TODO.txt Gnuplot.html html
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
