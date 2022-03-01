# Dev environment for NixOS
with import <nixpkgs> {};

let
  python = python39;
  pythonPackages = pkgs.python39Packages;
in
pkgs.mkShell {
  name = "pip-env";
  buildInputs = with python39Packages; [
    virtualenv
    mypy
    black
    wheel
    jsonpickle
    networkx
    coverage
    pytest
    pygame
    pygame-gui
    pyyaml
    termcolor
    pre-commit
  ];
  src = null;
  shellHook = ''
    # Allow the use of wheels.
    SOURCE_DATE_EPOCH=$(date +%s)

    VENV=env
    if test ! -d $VENV; then
      virtualenv $VENV
    fi
    source ./$VENV/bin/activate

   export PYTHONPATH=`pwd`/$VENV/${python.sitePackages}/:$PYTHONPATH
  '';
}

