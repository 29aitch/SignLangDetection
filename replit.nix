{pkgs}: {
  deps = [
    pkgs.python311Packages.openai
    pkgs.python311Packages.numpy
    pkgs.streamlit
  ];
}
