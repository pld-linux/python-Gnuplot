
%define		module	gnuplot
%define		dname	gnuplot-py

Summary:	A Python interface to the gnuplot plotting program
Summary(pl.UTF-8):	Interfejs dla Pythona do programu tworzącego wykresy - gnuplot
Name:		python-%{module}
Version:	1.7
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/gnuplot-py/%{dname}-%{version}.tar.gz
# Source0-md5:	724f9eee164d6ff763777b22a5851572
URL:		http://gnuplot-py.sourceforge.net/
BuildRequires:	python >= 2.2.1
BuildRequires:	python-Numeric
%pyrequires_eq	python-modules
Requires:	gnuplot
Requires:	python-Numeric
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnuplot.py is a Python package that allows you to create graphs from
within Python using the gnuplot plotting program.

%description -l pl.UTF-8
Gnuplot.py jest modułem Pythona pozwalającym na tworzenie wykresów z
poziomu Pythona używając do tego programu gnuplot.

%prep
%setup -q -n %{dname}-%{version}

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
%dir %{py_sitescriptdir}/Gnuplot
%{py_sitescriptdir}/Gnuplot/*.py[co]
