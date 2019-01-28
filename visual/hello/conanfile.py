from conans import ConanFile, MSBuild


class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "src/*"
    requires = "say/0.1@user/testing"

    generators = "visual_studio"
    exports_sources = "hello/*", "*.sln"

    def build(self):
        ms = MSBuild(self)
        ms.build("hello.sln")

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
