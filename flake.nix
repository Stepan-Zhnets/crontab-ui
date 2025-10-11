{
  description = "Flake: Crontab-UI";
  
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-ubstable";
  };
  outputs = { self, nixpkgs, ... }: let
    pkgs = nixpkgs.legacyPackages."x86_64-linux";
    packageOverrides = pkgs.callPackage ./python-packages.nix {};
    python = pkgs.python3.override { inherit packageOverrides; };
  in {
    devShell.x86_64-linux.default = pkgs.mkShell {
      packages = [
        (python.withpackages(pypkgs: with pypkgs; [
          flet
          croniter
          python-crontab
          ruff
        ]))
      ];
    };
  };
}
