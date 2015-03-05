Name:       sailfishos-android-leftswipe-patch

# >> macros
BuildArch: noarch
# << macros

Summary:    Disable left swipe for Android apps
Version:    0.0.2
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   sailfish-version >= 1.1.2
Requires:   sailfish-version < 1.1.3

%description
Disable left swipe for Android apps.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-android-leftswipe-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-android-leftswipe-patch
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-android-leftswipe-patch
# >> files
# << files
