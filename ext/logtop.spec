Summary: Display real time statistics of whatever you want.
Group: Development
Name: logtop
Version: 0.1
Release: 1
License: GPL Logtop is Copyright (c) Julien Pallard 2010. Packaged by James Hannah.
Source: https://github.com/jiphex/logtop/tarball/logtop-0.1.tar.gz
URL: https://github.com/jiphex/logtop/
BuildRequires: ncurses-devel
BuildRoot:%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Logtop displays real-time count of strings recieved in standard input.
I's useful for some cases, like :
  tail -f /var/log/apache2/access.log \
    | sed -u -r 's/^([^ ]+) ([^ ]+) ([^ ]+) \[([^]]+)] "([^ ]+) ([^"]+) HTTP\/([^"]+)" ([^ ]+) ([^ ]+) "([^"]+)" "([^"]+)"$/\6/g' \
    | logtop
To show the top pages requested on your apache visitors.

%prep
rm -rvf logtop-0.1/
%setup -q
%build
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%clean
rm -rf %{buildroot}
%files
%defattr(-,root,root,-)
%doc
%{_bindir}/*
%{_mandir}/man1/*

%changelog
