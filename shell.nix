{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = with pkgs; [
    (python312.withPackages(pypkgs: with pypkgs; [
      flet
      croniter
      python-crontab
      ruff
    ]))
  ];
}