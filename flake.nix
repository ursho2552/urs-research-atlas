{
  description = "Research Atlas: local-first research project showcase tool";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
  };

  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];

      forAllSystems = f:
        nixpkgs.lib.genAttrs systems (system:
          f nixpkgs.legacyPackages.${system}
        );
    in
    {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          packages = [
            pkgs.python312
            pkgs.git
          ];

          shellHook = ''
            echo "Research Atlas development shell"
            echo ""
            echo "First time setup:"
            echo "  python -m venv .venv"
            echo "  source .venv/bin/activate"
            echo "  pip install -r requirements.txt"
            echo ""
            echo "Then run:"
            echo "  python -m research_atlas.editor"
            echo "  python -m research_atlas.build"
            echo "  mkdocs serve"
          '';
        };
      });
    };
}
