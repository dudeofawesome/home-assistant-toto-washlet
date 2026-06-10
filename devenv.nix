{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:

{
  # https://devenv.sh/packages/
  packages = [
    pkgs.esphome
  ];

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    version = "3.14";
  };

  # https://devenv.sh/services/
  # services.postgres.enable = true;
}
