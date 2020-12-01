# based on work by The Fedora Project (2017)
# Copyright (c) 1998, 1999, 2000 Thai Open Source Software Center Ltd
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

%global libsepolver 3.1

Name:           secilc
Version:        3.0
Release:        1
Summary:        The SELinux CIL Compiler

License:        BSD
URL:            https://github.com/SELinuxProject/selinux/wiki
Source:         %{name}-%{version}.tar.bz2
Patch1:         dont_build_manpages.patch

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  libsepol-static >= %{libsepolver}

%description
The SELinux CIL Compiler is a compiler that converts the CIL language as
described on the CIL design wiki into a kernel binary policy file.
Please see the CIL Design Wiki at:
http://github.com/SELinuxProject/cil/wiki/
for more information about the goals and features on the CIL language.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
make -C %{name}/ %{?_smp_mflags} CFLAGS="%{optflags}" LIBSEPOL_STATIC=%{_libdir}/libsepol.a


%install
make -C %{name}/ %{?_smp_mflags} DESTDIR="%{buildroot}" SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" install


%files
%{_bindir}/secilc
%{_bindir}/secil2conf
%license %{name}/COPYING
