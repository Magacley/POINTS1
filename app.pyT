import os
import webbrowser

import hug
from hug import startup

import api


def project_configuration(directory, config_file: object, modules: object) -> object:
    pass


def server(
        directory: str = "~/DirFile/Files/DB",
        config_file: str = "http://localhost:63342/RealPoints/DirFile/admin/form.html?_ijt=edf21kfjft9s6hd5tv0fj6vrnv",
        open_browser: bool = False,
        port: int = 8000,  # None,
        host: str = '127.0.0.1',  # None,
        modules: list = api,   # None,
) -> None:
    """Runs a development webserver enabling you to browse documentation locally.

       - *directory*: The root folder of your project.
       - *config_file*: The [TOML](https://github.com/toml-lang/toml#toml) formatted
         config file you wish to use.
       - *open_browser*: If true a browser will be opened pointing at the documentation server
       - *port*: The port to expose your documentation on (defaults to: `8000`)
       - *host*: The host to expose your documentation on (defaults to `"127.0.0.1"`)
       - *modules*: One or more modules to render reference documentation for
    """
    # directory = directory if directory else os.getcwd()

    directory = os.makedirs(directory)\
        if directory else os.getcwd()
    api = hug.API("Doc Server")

    project_config = project_configuration(directory, config_file, modules=modules)

    with webbrowser.GenericBrowser(project_config) as doc_folder:
        @hug.static("/", api=api)
        def my_static_dirs():  # pragma: no cover
            return doc_folder

        @hug.startup(api=api)
        def custom_startup(*args, **kwargs):  # pragma: no cover
            # print(logo.ascii_art)
            if open_browser:
                webbrowser.open_new(f"http://{project_config['host']}:{project_config['port']}")

        api.http.serve(
            host=host or project_config["host"],
            port=port or project_config["port"],
            no_documentation=True,
            display_intro=False,
        )
        if '__main__' == __name__:
            startup()
