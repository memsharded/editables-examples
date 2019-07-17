import os
import shutil

def run(cmd):
    r = os.system(cmd)
    if r != 0:
        raise Exception("Failed: %s" % cmd)

shutil.rmtree("say/build", ignore_errors=True)
shutil.rmtree("hello/build", ignore_errors=True)

settings = "-s build_type=Debug -s arch=x86"
try:
    with open("say/src/say.cpp", "r") as f:
        say = f.read()

    run("cd say && conan link . say/0.1@user/testing --layout=layout")
    run("cd say && mkdir build && cd build && conan install .. %s" % settings)
    run("cd say/build && conan build ..")

    run("cd hello && mkdir build && cd build && conan install .. %s" % settings)
    run("cd hello/build && conan build ..")
    run("cd hello/build/bin && app")

    # Modify say 
    with open("say/src/say.cpp", "w") as f:
        f.write(say.replace("Release", "******* Release ******** ").replace("Debug", "***** Debug *****"))
    run("cd say/build && conan build ..")

    # Rebuild hello
    run("cd hello/build && conan build ..")
    run("cd hello/build/bin && app")

finally:
    run("conan link say/0.1@user/testing --remove")
    with open("say/src/say.cpp", "w") as f:
        f.write(say)



