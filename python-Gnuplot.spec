%include 	/usr/lib/rpm/macros.python

%define		module Gnuplot

Summary:	A Python interface to the gnuplot plotting program
Summary(pl):	Interfejs dla Pythona do programu tworz±cego wykresy - gnuplot
Name:		python-%{module}
Version:	1.5
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://prdownloads.ysourceforge.net/gnuplot-py/%{module}-%{version}.tar.gz
URL:		http://gnuplot-py.sourceforge.net/
Requires:	gnuplot
%requires_eq	python
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
gzip -9nf ANNOUNCE.txt README.txt NEWS.txt CREDITS.txt TODO.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz Gnuplot.html html
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
