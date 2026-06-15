import argostranslate.package

available_packages = argostranslate.package.get_available_packages()

package = next(
    p for p in available_packages
    if p.from_code == "en" and p.to_code == "es"
)

path = package.download()
argostranslate.package.install_from_path(path)