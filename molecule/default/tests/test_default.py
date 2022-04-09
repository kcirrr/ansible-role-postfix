"""Role testing files using testinfra."""


def test_postfix_running_and_enabled(host):
    s = host.service("postfix")
    assert s.is_running
    assert s.is_enabled
    assert not s.is_masked


def test_postfix_config_file(host):
    f = host.file("/etc/postfix/main.cf")
    assert f.exists
    assert f.contains("smtpd_tls_dh1024_param_file")
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644
