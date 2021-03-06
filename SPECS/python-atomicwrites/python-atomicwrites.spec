%{!?python2_sitelib: %define python2_sitelib %(python2 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Summary:        Python Atomic file writes
Name:           python3-atomicwrites
Version:        1.2.1
Release:        4%{?dist}
License:        MIT
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://github.com/untitaker/python-atomicwrites
Source0:        https://pypi.python.org/packages/a1/e1/2d9bc76838e6e6667fde5814aa25d7feb93d6fa471bf6816daac2596e8b2/atomicwrites-%{version}.tar.gz
%define sha1    atomicwrites=fec341b1028177784ac97436c479a397ffeb20d7

%if %{with_check}
BuildRequires:  curl-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-attrs
BuildRequires:  python3-pytest
BuildRequires:  python3-six
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
BuildArch:      noarch

%description
Python Atomic file writes

%prep
%setup -q -n atomicwrites-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
easy_install_3=$(ls /usr/bin |grep easy_install |grep 3)
$easy_install_3 funcsigs pathlib2 pluggy more-itertools
cp tests/test_atomicwrites.py .
python3 test_atomicwrites.py

%files
%defattr(-,root,root)
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
*   Thu Jun 11 2020 Tapas Kundu <tkundu@vmware.com> 1.2.1-4
-   Mass removal python2
*   Mon Aug 26 2019 Shreyas B. <shreyasb@vmware.com> 1.2.1-3
-   Fixed make check
*   Mon Nov 12 2018 Tapas Kundu <tkundu@vmware.com> 1.2.1-2
-   Fixed make check
*   Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> 1.2.1-1
-   Update to version 1.2.1
*   Wed Jul 26 2017 Divya Thaluru <dthaluru@vmware.com> 1.1.5-2
-   Fixed rpm check errors
*   Fri Jul 07 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.1.5-1
-   Initial packaging for Photon
