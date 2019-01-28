from conans import ConanFile, MSBuild


class SayConan(ConanFile):
    name = "say"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "say/*", "*.sln"

    def build(self):
        ms = MSBuild(self)
        ms.build("say.sln")

    def package(self):
        self.copy("*.h", dst="include", src="say")
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["say"]
