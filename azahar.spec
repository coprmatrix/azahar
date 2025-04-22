Name: azahar
Version: 2120rc1
Release: 0
Summary: An open-source 3DS emulator project based on Citra.
URL: https://github.com/azahar-emu/azahar
License: MIT
BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: cmake(fmt)
BuildRequires: rpm_macro(cmake)
BuildRequires: rpm_macro(cmake_build)
BuildRequires: rpm_macro(cmake_install)
BuildRequires: pkgconfig
BuildRequires: boost-devel
BuildRequires: pkgconfig(libusb)
BuildRequires: pkgconfig(soundtouch)
BuildRequires: pkgconfig(libcryptopp)
BuildRequires: pkgconfig(fmt)
BuildRequires: cmake(dynarmic)
BuildRequires: pkgconfig(inih)
BuildRequires: cmake(zstd)
BuildRequires: pkgconfig(libenet)
BuildRequires: pkgconfig(catch2)
BuildRequires: cmake(cubeb)
BuildRequires: cmake(SDL2)
BuildRequires: cmake(nlohmann_json)
BuildRequires: pkgconfig(openssl)
BuildRequires: cmake(httplib)
BuildRequires: cmake(cpp-jwt)
BuildRequires: pkgconfig(lodepng)
BuildRequires: cmake(OpenAL)
BuildRequires: cmake(glslang)
BuildRequires: cmake(VulkanMemoryAllocator)
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtmultimedia-devel
BuildRequires: cmake(tsl-robin-map)

Source: %{name}-%{version}.tar.gz

%description
%{summary}.

%prep
%autosetup

%build
flags=(
USE_SYSTEM_LODEPNG
USE_SYSTEM_OPENAL
USE_SYSTEM_GLSLANG
USE_SYSTEM_VMA
USE_SYSTEM_VULKAN_HEADERS
USE_SYSTEM_SDL2
USE_SYSTEM_QT
USE_SYSTEM_MOLTENVK
USE_SYSTEM_BOOST
USE_SYSTEM_LIBUSB
USE_SYSTEM_SOUNDTOUCH
USE_SYSTEM_CRYPTOPP
USE_SYSTEM_FMT
USE_SYSTEM_XBYAK
USE_SYSTEM_DYNARMIC
USE_SYSTEM_INIH
#USE_SYSTEM_FFMPEG_HEADERS
USE_SYSTEM_ZSTD
USE_SYSTEM_ENET
USE_SYSTEM_CATCH2
USE_SYSTEM_CUBEB
USE_SYSTEM_JSON
USE_SYSTEM_OPENSSL
USE_SYSTEM_CPP_HTTPLIB
USE_SYSTEM_CPP_JWT
)

declare -a system
for flag in "${flags[@]}"
do
  system+=("-D${flag}=ON")
done

%cmake "${system[@]}" -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install
%cmake_install
rm -rfv %{buildroot}%{_libdir}
%files
%_bindir/*
%_datadir/*/*
