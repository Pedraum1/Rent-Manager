from src.Core.App import App

def test_app_can_instatiate():
    app = App()
    assert isinstance(app, App)

def test_can_app_run(monkeypatch):
    app = App()

    monkeypatch.setattr('builtins.input', lambda _: '3')
    app.run()
    
    assert True