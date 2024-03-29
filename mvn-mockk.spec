#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-mockk
Version  : 1.8.13
Release  : 2
URL      : https://github.com/mockk/mockk/archive/1.8.13.tar.gz
Source0  : https://github.com/mockk/mockk/archive/1.8.13.tar.gz
Source1  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk-agent-api/1.8.13/mockk-agent-api-1.8.13.jar
Source2  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk-agent-api/1.8.13/mockk-agent-api-1.8.13.pom
Source3  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk-agent-common/1.8.13/mockk-agent-common-1.8.13.jar
Source4  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk-agent-common/1.8.13/mockk-agent-common-1.8.13.pom
Source5  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk-agent-jvm/1.8.13/mockk-agent-jvm-1.8.13.jar
Source6  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk-agent-jvm/1.8.13/mockk-agent-jvm-1.8.13.pom
Source7  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk-common/1.8.13/mockk-common-1.8.13.jar
Source8  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk-common/1.8.13/mockk-common-1.8.13.pom
Source9  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk-dsl-jvm/1.8.13/mockk-dsl-jvm-1.8.13.jar
Source10  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk-dsl-jvm/1.8.13/mockk-dsl-jvm-1.8.13.pom
Source11  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk-dsl/1.8.13/mockk-dsl-1.8.13.jar
Source12  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk-dsl/1.8.13/mockk-dsl-1.8.13.pom
Source13  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk/1.8.13/mockk-1.8.13.jar
Source14  : https://repo.gradle.org/gradle/libs-releases/io/mockk/mockk/1.8.13/mockk-1.8.13.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-mockk-data = %{version}-%{release}
Requires: mvn-mockk-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-mvn
BuildRequires : gradle

%description
<div class="helpmasha">
<img src="doc/heart.png" width="40px" align="top" />
<a href="https://salveazaoinima.ro/en/campaigns/maria-pilipenco/">Help</a> my kid <a href="/MASHA">Masha</a> with a stem cell theraphy
</div>

%package data
Summary: data components for the mvn-mockk package.
Group: Data

%description data
data components for the mvn-mockk package.


%package license
Summary: license components for the mvn-mockk package.
Group: Default

%description license
license components for the mvn-mockk package.


%prep
%setup -q -n mockk-1.8.13

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-mockk
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-mockk/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-agent-api/1.8.13
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-agent-api/1.8.13/mockk-agent-api-1.8.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-agent-api/1.8.13
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-agent-api/1.8.13/mockk-agent-api-1.8.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-agent-common/1.8.13
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-agent-common/1.8.13/mockk-agent-common-1.8.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-agent-common/1.8.13
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-agent-common/1.8.13/mockk-agent-common-1.8.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-agent-jvm/1.8.13
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-agent-jvm/1.8.13/mockk-agent-jvm-1.8.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-agent-jvm/1.8.13
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-agent-jvm/1.8.13/mockk-agent-jvm-1.8.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-common/1.8.13
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-common/1.8.13/mockk-common-1.8.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-common/1.8.13
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-common/1.8.13/mockk-common-1.8.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-dsl-jvm/1.8.13
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-dsl-jvm/1.8.13/mockk-dsl-jvm-1.8.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-dsl-jvm/1.8.13
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-dsl-jvm/1.8.13/mockk-dsl-jvm-1.8.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-dsl/1.8.13
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-dsl/1.8.13/mockk-dsl-1.8.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-dsl/1.8.13
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk-dsl/1.8.13/mockk-dsl-1.8.13.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk/1.8.13
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk/1.8.13/mockk-1.8.13.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk/1.8.13
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/io/mockk/mockk/1.8.13/mockk-1.8.13.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/io/mockk/mockk-agent-api/1.8.13/mockk-agent-api-1.8.13.jar
/usr/share/java/.m2/repository/io/mockk/mockk-agent-api/1.8.13/mockk-agent-api-1.8.13.pom
/usr/share/java/.m2/repository/io/mockk/mockk-agent-common/1.8.13/mockk-agent-common-1.8.13.jar
/usr/share/java/.m2/repository/io/mockk/mockk-agent-common/1.8.13/mockk-agent-common-1.8.13.pom
/usr/share/java/.m2/repository/io/mockk/mockk-agent-jvm/1.8.13/mockk-agent-jvm-1.8.13.jar
/usr/share/java/.m2/repository/io/mockk/mockk-agent-jvm/1.8.13/mockk-agent-jvm-1.8.13.pom
/usr/share/java/.m2/repository/io/mockk/mockk-common/1.8.13/mockk-common-1.8.13.jar
/usr/share/java/.m2/repository/io/mockk/mockk-common/1.8.13/mockk-common-1.8.13.pom
/usr/share/java/.m2/repository/io/mockk/mockk-dsl-jvm/1.8.13/mockk-dsl-jvm-1.8.13.jar
/usr/share/java/.m2/repository/io/mockk/mockk-dsl-jvm/1.8.13/mockk-dsl-jvm-1.8.13.pom
/usr/share/java/.m2/repository/io/mockk/mockk-dsl/1.8.13/mockk-dsl-1.8.13.jar
/usr/share/java/.m2/repository/io/mockk/mockk-dsl/1.8.13/mockk-dsl-1.8.13.pom
/usr/share/java/.m2/repository/io/mockk/mockk/1.8.13/mockk-1.8.13.jar
/usr/share/java/.m2/repository/io/mockk/mockk/1.8.13/mockk-1.8.13.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-mockk/LICENSE
