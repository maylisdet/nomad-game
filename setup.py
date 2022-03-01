from setuptools import setup, find_packages


with open("requirements.txt") as f:
    install_deps = f.read().splitlines()

extras = {"test": install_deps}


setup(
    name="Nomad",
    python_requires=">=3.7.3",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=install_deps,
    tests_require=install_deps,
    extras_require=extras,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "nomad_client = client.main:main",
            "nomad_server = server.main:main",
        ],
    },
    include_package_data=True,
)
