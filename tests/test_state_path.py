from atoffice_shell.chronoterm.state import default_state_path


def test_default_state_path_contains_app_folder() -> None:
    path = default_state_path()
    assert "AtOfficeShell" in str(path)
