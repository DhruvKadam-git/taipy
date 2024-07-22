# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

"""# Taipy Graphical User Interface generator

The Taipy GUI package provides User Interface generation based on page templates. It can
run a web server that a web browser can connect to.

The pages are generated by a web server that allows web clients to connect, display and
interact with the page content through visual elements.

Each page can contain regular text and images, as well as Taipy controls that are
typically linked to some value that is managed by the whole Taipy application.

Here is how you can create your first Taipy User Interface:

   - Create a Python source file.
     Copy these two lines into a file called *taipy_app.py*.
     ```py title="taipy_app.py"
     from taipy import Gui
     Gui("# Hello Taipy!").run()
     ```
   - Install Taipy:
     ```
     pip install taipy
     ```
   - Run your application:
     ```
     python taipy_app.py
     ```

Your browser opens a new page, showing the content of your graphical
application.

!!! Note "Optional packages"

    There are Python packages that you can install in your environment to
    add functionality to Taipy GUI:

    - [`python-magic`](https://pypi.org/project/python-magic/): identifies image format
      from byte buffers so the [`image`](../../../userman/gui/viselements/generic/image.md) control can
      display them, and so that [`file_download`](../../../userman/gui/viselements/generic/file_download.md)
      can request the browser to display the image content when relevant.<br/>
      You can install that package with the regular `pip install python-magic` command
      (then potentially `pip install python-magic` on Windows),
      or install Taipy GUI using: `pip install taipy-gui[image]`.
    - [`pyarrow`](https://pypi.org/project/pyarrow/): can improve the performance of your
      application by reducing the volume of data transferred between the web server and the
      clients. This is relevant if your application uses large tabular data.<br/>
      You can install that package with the regular `pip install pyarrow` command,
      or install Taipy GUI using: `pip install taipy-gui[arrow]`.
    - [`simple-websocket`](https://pypi.org/project/simple-websocket/): enables the
      debugging of the WebSocket part of the server execution.<br/>
      You can install that package with the regular `pip install simple-websocket` command,
      or install Taipy GUI using: `pip install taipy-gui[simple-websocket]`.
    - [`pyngrok`](https://pypi.org/project/pyngrok/): enables use of [Ngrok](https://ngrok.com/)
      to access Taipy GUI application from the internet.<br/>
      You can install that package with the regular `pip install pyngrok` command,
      or install Taipy GUI using: `pip install taipy-gui[pyngrok]`.

"""

from importlib.util import find_spec

from ._init import *
from ._renderers import Html, Markdown
from ._renderers.json import JsonAdapter
from .gui_actions import (
    broadcast_callback,
    download,
    get_module_context,
    get_module_name_from_state,
    get_state_id,
    get_user_content_url,
    hold_control,
    invoke_callback,
    invoke_long_callback,
    navigate,
    notify,
    resume_control,
)
from .icon import Icon
from .page import Page
from .partial import Partial
from .state import State
from .utils import is_debugging

if find_spec("taipy") and find_spec("taipy.config"):
    from taipy.config import _inject_section

    from ._default_config import default_config
    from ._gui_section import _GuiSection

    _inject_section(
        _GuiSection,
        "gui_config",
        _GuiSection(property_list=list(default_config)),
        [("configure_gui", _GuiSection._configure)],
        add_to_unconflicted_sections=True,
    )
