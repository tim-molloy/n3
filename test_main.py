from typer.testing import CliRunner
from gen import app as cli
from api import App, File


runner = CliRunner()


class TestGen:
    def test_column_data(self):
        result = runner.invoke(
            cli, ["--column-data", "('int_data', 'integer'), ('string_data', 'string')"]
        )
        assert result.exit_code == 0

    def test_rows(self):
        result = runner.invoke(
            cli,
            [
                "--rows",
                20,
                "--column-data",
                "('int_data', 'integer'), ('string_data', 'string')",
            ],
        )
        assert result.exit_code == 0

    def test_path(self):
        result = runner.invoke(
            cli,
            [
                "--output-path",
                "./data/",
                "--column-data",
                "('int_data', 'integer'), ('string_data', 'string')",
            ],
        )
        assert result.exit_code == 0


class TestApi:
    def test_get(self):
        with open("./data-file", "w") as file:
            file.write("Test")
        endpoint = File()
        response = endpoint.get()
        assert response == {"contents": "Test"}
