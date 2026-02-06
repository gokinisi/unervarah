Last login: Sun Jan 11 10:54:28 on ttys002
# Step 1: Make sure you're in your project folder
cd ~/nervarah
^C%                                                                             krismac@Kristins-MacBook-Air ~ % # Step 1: Make sure you're in your project folder
cd ~/nervarah
quote> cd ~/nervarah
quote> python3 -m venv nervarah-env-new
quote> /Library/Developer/CommandLineTools/usr/bin/python3 -m venv nervarah-env-new
quote> 
quote> 
krismac@Kristins-MacBook-Air ~ % /Library/Developer/CommandLineTools/usr/bin/python3 -m venv nervarah-env-new
krismac@Kristins-MacBook-Air ~ % # Step 1: Make sure you're in your project folder
cd ~/nervarah
quote> 
krismac@Kristins-MacBook-Air ~ % cd ~ /nervarah
cd: no such file or directory: /nervarah
krismac@Kristins-MacBook-Air ~ % cd ~ APPS N+
cd: too many arguments
krismac@Kristins-MacBook-Air ~ % cd ~APPNcd
zsh: no such user or named directory: APPNcd
krismac@Kristins-MacBook-Air ~ % cd ~APPN
zsh: no such user or named directory: APPN
krismac@Kristins-MacBook-Air ~ % cd ~/APPN
cd: no such file or directory: /Users/krismac/APPN
krismac@Kristins-MacBook-Air ~ % cd ~/Desktop
krismac@Kristins-MacBook-Air Desktop % cd ~/Desktop
krismac@Kristins-MacBook-Air Desktop % ls
APPN
krismac@Kristins-MacBook-Air Desktop % streamlit run app.py
zsh: command not found: streamlit
krismac@Kristins-MacBook-Air Desktop % mv app.py motivation_app.py
streamlit run motivation_app.py
zsh: command not found: streamlit
krismac@Kristins-MacBook-Air Desktop % pip install streamlit
zsh: command not found: pip
krismac@Kristins-MacBook-Air Desktop % /Library/Developer/CommandLineTools/usr/bin/python3 -m pip install streamlit
Defaulting to user installation because normal site-packages is not writeable
Collecting streamlit
  Using cached streamlit-1.50.0-py3-none-any.whl.metadata (9.5 kB)
Collecting altair!=5.4.0,!=5.4.1,<6,>=4.0 (from streamlit)
  Using cached altair-5.5.0-py3-none-any.whl.metadata (11 kB)
Collecting blinker<2,>=1.5.0 (from streamlit)
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting cachetools<7,>=4.0 (from streamlit)
  Using cached cachetools-6.2.6-py3-none-any.whl.metadata (5.6 kB)
Collecting click<9,>=7.0 (from streamlit)
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Requirement already satisfied: numpy<3,>=1.23 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (1.24.3)
Collecting packaging<26,>=20 (from streamlit)
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pandas<3,>=1.4.0 (from streamlit)
  Using cached pandas-2.3.3-cp39-cp39-macosx_11_0_arm64.whl.metadata (91 kB)
Collecting pillow<12,>=7.1.0 (from streamlit)
  Using cached pillow-11.3.0-cp39-cp39-macosx_11_0_arm64.whl.metadata (9.0 kB)
Requirement already satisfied: protobuf<7,>=3.20 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (4.25.8)
Collecting pyarrow>=7.0 (from streamlit)
  Using cached pyarrow-21.0.0-cp39-cp39-macosx_12_0_arm64.whl.metadata (3.3 kB)
Requirement already satisfied: requests<3,>=2.27 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (2.32.5)
Collecting tenacity<10,>=8.1.0 (from streamlit)
  Using cached tenacity-9.1.2-py3-none-any.whl.metadata (1.2 kB)
Collecting toml<2,>=0.10.1 (from streamlit)
  Using cached toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)
Requirement already satisfied: typing-extensions<5,>=4.4.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (4.15.0)
Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)
  Using cached gitpython-3.1.46-py3-none-any.whl.metadata (13 kB)
Collecting pydeck<1,>=0.8.0b4 (from streamlit)
  Using cached pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)
Collecting tornado!=6.5.0,<7,>=6.0.3 (from streamlit)
  Using cached tornado-6.5.4-cp39-abi3-macosx_10_9_universal2.whl.metadata (2.8 kB)
Requirement already satisfied: jinja2 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)
Collecting jsonschema>=3.0 (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached jsonschema-4.25.1-py3-none-any.whl.metadata (7.6 kB)
Collecting narwhals>=1.14.2 (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached narwhals-2.15.0-py3-none-any.whl.metadata (13 kB)
Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)
  Using cached gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)
Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)
  Using cached smmap-5.0.2-py3-none-any.whl.metadata (4.3 kB)
Collecting python-dateutil>=2.8.2 (from pandas<3,>=1.4.0->streamlit)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas<3,>=1.4.0->streamlit)
  Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas<3,>=1.4.0->streamlit)
  Using cached tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)
Requirement already satisfied: charset_normalizer<4,>=2 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (2.6.3)
Requirement already satisfied: certifi>=2017.4.17 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (2026.1.4)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.3)
Collecting attrs>=22.2.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached attrs-25.4.0-py3-none-any.whl.metadata (10 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached referencing-0.36.2-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.7.1 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached rpds_py-0.27.1-cp39-cp39-macosx_11_0_arm64.whl.metadata (4.2 kB)
Requirement already satisfied: six>=1.5 in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.15.0)
Using cached streamlit-1.50.0-py3-none-any.whl (10.1 MB)
Using cached altair-5.5.0-py3-none-any.whl (731 kB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached cachetools-6.2.6-py3-none-any.whl (11 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached gitpython-3.1.46-py3-none-any.whl (208 kB)
Using cached gitdb-4.0.12-py3-none-any.whl (62 kB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Using cached pandas-2.3.3-cp39-cp39-macosx_11_0_arm64.whl (10.8 MB)
Using cached pillow-11.3.0-cp39-cp39-macosx_11_0_arm64.whl (4.7 MB)
Using cached pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)
Using cached smmap-5.0.2-py3-none-any.whl (24 kB)
Using cached tenacity-9.1.2-py3-none-any.whl (28 kB)
Using cached toml-0.10.2-py2.py3-none-any.whl (16 kB)
Using cached tornado-6.5.4-cp39-abi3-macosx_10_9_universal2.whl (443 kB)
Using cached jsonschema-4.25.1-py3-none-any.whl (90 kB)
Using cached attrs-25.4.0-py3-none-any.whl (67 kB)
Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Using cached narwhals-2.15.0-py3-none-any.whl (432 kB)
Using cached pyarrow-21.0.0-cp39-cp39-macosx_12_0_arm64.whl (31.2 MB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Using cached referencing-0.36.2-py3-none-any.whl (26 kB)
Using cached rpds_py-0.27.1-cp39-cp39-macosx_11_0_arm64.whl (354 kB)
Using cached tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Installing collected packages: pytz, tzdata, tornado, toml, tenacity, smmap, rpds-py, python-dateutil, pyarrow, pillow, packaging, narwhals, click, cachetools, blinker, attrs, referencing, pydeck, pandas, gitdb, jsonschema-specifications, gitpython, jsonschema, altair, streamlit
  Attempting uninstall: packaging
    Found existing installation: packaging 26.0
    Uninstalling packaging-26.0:
      Successfully uninstalled packaging-26.0
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━━━━ 22/25 [jsonschema]  WARNING: The script jsonschema is installed in '/Users/krismac/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╺━ 24/25 [streamlit]  WARNING: The script streamlit is installed in '/Users/krismac/Library/Python/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
tensorflow-macos 2.13.1 requires typing-extensions<4.6.0,>=3.6.6, but you have typing-extensions 4.15.0 which is incompatible.
Successfully installed altair-5.5.0 attrs-25.4.0 blinker-1.9.0 cachetools-6.2.6 click-8.1.8 gitdb-4.0.12 gitpython-3.1.46 jsonschema-4.25.1 jsonschema-specifications-2025.9.1 narwhals-2.15.0 packaging-25.0 pandas-2.3.3 pillow-11.3.0 pyarrow-21.0.0 pydeck-0.9.1 python-dateutil-2.9.0.post0 pytz-2025.2 referencing-0.36.2 rpds-py-0.27.1 smmap-5.0.2 streamlit-1.50.0 tenacity-9.1.2 toml-0.10.2 tornado-6.5.4 tzdata-2025.3
krismac@Kristins-MacBook-Air Desktop % /Library/Developer/CommandLineTools/usr/bin/python3 -m streamlit run motivation_app.py

      👋 Welcome to Streamlit!

      If you'd like to receive helpful onboarding emails, news, offers, promotions,
      and the occasional swag, please enter your email address below. Otherwise,
      leave this field blank.

      Email:  
/Users/krismac/Library/Python/3.9/lib/python/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(

  You can find our privacy policy at https://streamlit.io/privacy-policy

  Summary:
  - This open source library collects usage statistics.
  - We cannot see and do not store information contained inside Streamlit apps,
    such as text, charts, images, etc.
  - Telemetry data is stored in servers in the United States.
  - If you'd like to opt out, add the following to ~/.streamlit/config.toml,
    creating that file if necessary:

    [browser]
    gatherUsageStats = false


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.25:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
2026-01-30 15:48:56.902 Script compilation error
Traceback (most recent call last):
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 571, in _run_script
    code = self._script_cache.get_bytecode(script_path)
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_cache.py", line 68, in get_bytecode
    with open_python_file(script_path) as f:
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/source_util.py", line 54, in open_python_file
    return tokenize.open(filename)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/tokenize.py", line 392, in open
    buffer = _builtin_open(filename, 'rb')
IsADirectoryError: [Errno 21] Is a directory: '/Users/krismac/Desktop/motivation_app.py'
2026-01-30 15:48:56.908 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-01-30 15:49:13.347 Script compilation error
Traceback (most recent call last):
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 571, in _run_script
    code = self._script_cache.get_bytecode(script_path)
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_cache.py", line 68, in get_bytecode
    with open_python_file(script_path) as f:
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/source_util.py", line 54, in open_python_file
    return tokenize.open(filename)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/tokenize.py", line 392, in open
    buffer = _builtin_open(filename, 'rb')
IsADirectoryError: [Errno 21] Is a directory: '/Users/krismac/Desktop/motivation_app.py'
2026-01-30 15:49:13.348 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
# Still on Desktop
python3 -m venv mymotivationenv

source mymotivationenv/bin/activate
# Prompt should now show (mymotivationenv)

python -m pip install --upgrade pip
pip install streamlit
streamlit run motivation_app.py
^C  Stopping...
krismac@Kristins-MacBook-Air Desktop % # Still on Desktop
python3 -m venv mymotivationenv

source mymotivationenv/bin/activate
# Prompt should now show (mymotivationenv)

python -m pip install --upgrade pip
pip install streamlit
streamlit run motivation_app.py
zsh: command not found: #
zsh: number expected
Requirement already satisfied: pip in ./mymotivationenv/lib/python3.9/site-packages (21.2.4)
Collecting pip
  Using cached pip-25.3-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
Successfully installed pip-25.3
Collecting streamlit
  Using cached streamlit-1.50.0-py3-none-any.whl.metadata (9.5 kB)
Collecting altair!=5.4.0,!=5.4.1,<6,>=4.0 (from streamlit)
  Using cached altair-5.5.0-py3-none-any.whl.metadata (11 kB)
Collecting blinker<2,>=1.5.0 (from streamlit)
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting cachetools<7,>=4.0 (from streamlit)
  Using cached cachetools-6.2.6-py3-none-any.whl.metadata (5.6 kB)
Collecting click<9,>=7.0 (from streamlit)
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting numpy<3,>=1.23 (from streamlit)
  Using cached numpy-2.0.2-cp39-cp39-macosx_14_0_arm64.whl.metadata (60 kB)
Collecting packaging<26,>=20 (from streamlit)
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pandas<3,>=1.4.0 (from streamlit)
  Using cached pandas-2.3.3-cp39-cp39-macosx_11_0_arm64.whl.metadata (91 kB)
Collecting pillow<12,>=7.1.0 (from streamlit)
  Using cached pillow-11.3.0-cp39-cp39-macosx_11_0_arm64.whl.metadata (9.0 kB)
Collecting protobuf<7,>=3.20 (from streamlit)
  Using cached protobuf-6.33.5-cp39-abi3-macosx_10_9_universal2.whl.metadata (593 bytes)
Collecting pyarrow>=7.0 (from streamlit)
  Using cached pyarrow-21.0.0-cp39-cp39-macosx_12_0_arm64.whl.metadata (3.3 kB)
Collecting requests<3,>=2.27 (from streamlit)
  Using cached requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting tenacity<10,>=8.1.0 (from streamlit)
  Using cached tenacity-9.1.2-py3-none-any.whl.metadata (1.2 kB)
Collecting toml<2,>=0.10.1 (from streamlit)
  Using cached toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)
Collecting typing-extensions<5,>=4.4.0 (from streamlit)
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)
  Using cached gitpython-3.1.46-py3-none-any.whl.metadata (13 kB)
Collecting pydeck<1,>=0.8.0b4 (from streamlit)
  Using cached pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)
Collecting tornado!=6.5.0,<7,>=6.0.3 (from streamlit)
  Using cached tornado-6.5.4-cp39-abi3-macosx_10_9_universal2.whl.metadata (2.8 kB)
Collecting jinja2 (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jsonschema>=3.0 (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached jsonschema-4.25.1-py3-none-any.whl.metadata (7.6 kB)
Collecting narwhals>=1.14.2 (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached narwhals-2.15.0-py3-none-any.whl.metadata (13 kB)
Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)
  Using cached gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)
Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)
  Using cached smmap-5.0.2-py3-none-any.whl.metadata (4.3 kB)
Collecting python-dateutil>=2.8.2 (from pandas<3,>=1.4.0->streamlit)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas<3,>=1.4.0->streamlit)
  Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas<3,>=1.4.0->streamlit)
  Using cached tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting charset_normalizer<4,>=2 (from requests<3,>=2.27->streamlit)
  Using cached charset_normalizer-3.4.4-cp39-cp39-macosx_10_9_universal2.whl.metadata (37 kB)
Collecting idna<4,>=2.5 (from requests<3,>=2.27->streamlit)
  Using cached idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3<3,>=1.21.1 (from requests<3,>=2.27->streamlit)
  Using cached urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2017.4.17 (from requests<3,>=2.27->streamlit)
  Using cached certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)
Collecting MarkupSafe>=2.0 (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached markupsafe-3.0.3-cp39-cp39-macosx_11_0_arm64.whl.metadata (2.7 kB)
Collecting attrs>=22.2.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached attrs-25.4.0-py3-none-any.whl.metadata (10 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached referencing-0.36.2-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.7.1 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit)
  Using cached rpds_py-0.27.1-cp39-cp39-macosx_11_0_arm64.whl.metadata (4.2 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Using cached streamlit-1.50.0-py3-none-any.whl (10.1 MB)
Using cached altair-5.5.0-py3-none-any.whl (731 kB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached cachetools-6.2.6-py3-none-any.whl (11 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached gitpython-3.1.46-py3-none-any.whl (208 kB)
Using cached gitdb-4.0.12-py3-none-any.whl (62 kB)
Using cached numpy-2.0.2-cp39-cp39-macosx_14_0_arm64.whl (5.3 MB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Using cached pandas-2.3.3-cp39-cp39-macosx_11_0_arm64.whl (10.8 MB)
Using cached pillow-11.3.0-cp39-cp39-macosx_11_0_arm64.whl (4.7 MB)
Using cached protobuf-6.33.5-cp39-abi3-macosx_10_9_universal2.whl (427 kB)
Using cached pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)
Using cached requests-2.32.5-py3-none-any.whl (64 kB)
Using cached charset_normalizer-3.4.4-cp39-cp39-macosx_10_9_universal2.whl (209 kB)
Using cached idna-3.11-py3-none-any.whl (71 kB)
Using cached smmap-5.0.2-py3-none-any.whl (24 kB)
Using cached tenacity-9.1.2-py3-none-any.whl (28 kB)
Using cached toml-0.10.2-py2.py3-none-any.whl (16 kB)
Using cached tornado-6.5.4-cp39-abi3-macosx_10_9_universal2.whl (443 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Using cached urllib3-2.6.3-py3-none-any.whl (131 kB)
Using cached certifi-2026.1.4-py3-none-any.whl (152 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached jsonschema-4.25.1-py3-none-any.whl (90 kB)
Using cached attrs-25.4.0-py3-none-any.whl (67 kB)
Using cached jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Using cached markupsafe-3.0.3-cp39-cp39-macosx_11_0_arm64.whl (12 kB)
Using cached narwhals-2.15.0-py3-none-any.whl (432 kB)
Using cached pyarrow-21.0.0-cp39-cp39-macosx_12_0_arm64.whl (31.2 MB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Using cached referencing-0.36.2-py3-none-any.whl (26 kB)
Using cached rpds_py-0.27.1-cp39-cp39-macosx_11_0_arm64.whl (354 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Installing collected packages: pytz, urllib3, tzdata, typing-extensions, tornado, toml, tenacity, smmap, six, rpds-py, pyarrow, protobuf, pillow, packaging, numpy, narwhals, MarkupSafe, idna, click, charset_normalizer, certifi, cachetools, blinker, attrs, requests, referencing, python-dateutil, jinja2, gitdb, pydeck, pandas, jsonschema-specifications, gitpython, jsonschema, altair, streamlit
Successfully installed MarkupSafe-3.0.3 altair-5.5.0 attrs-25.4.0 blinker-1.9.0 cachetools-6.2.6 certifi-2026.1.4 charset_normalizer-3.4.4 click-8.1.8 gitdb-4.0.12 gitpython-3.1.46 idna-3.11 jinja2-3.1.6 jsonschema-4.25.1 jsonschema-specifications-2025.9.1 narwhals-2.15.0 numpy-2.0.2 packaging-25.0 pandas-2.3.3 pillow-11.3.0 protobuf-6.33.5 pyarrow-21.0.0 pydeck-0.9.1 python-dateutil-2.9.0.post0 pytz-2025.2 referencing-0.36.2 requests-2.32.5 rpds-py-0.27.1 six-1.17.0 smmap-5.0.2 streamlit-1.50.0 tenacity-9.1.2 toml-0.10.2 tornado-6.5.4 typing-extensions-4.15.0 tzdata-2025.3 urllib3-2.6.3

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.25:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
2026-01-30 15:49:54.425 Script compilation error
Traceback (most recent call last):
  File "/Users/krismac/Desktop/mymotivationenv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 571, in _run_script
    code = self._script_cache.get_bytecode(script_path)
  File "/Users/krismac/Desktop/mymotivationenv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_cache.py", line 68, in get_bytecode
    with open_python_file(script_path) as f:
  File "/Users/krismac/Desktop/mymotivationenv/lib/python3.9/site-packages/streamlit/source_util.py", line 54, in open_python_file
    return tokenize.open(filename)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/tokenize.py", line 392, in open
    buffer = _builtin_open(filename, 'rb')
IsADirectoryError: [Errno 21] Is a directory: '/Users/krismac/Desktop/motivation_app.py'
2026-01-30 15:49:54.430 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install streamlit
/Library/Developer/CommandLineTools/usr/bin/python3 -m streamlit run motivation_app.py
^C  Stopping...
(mymotivationenv) krismac@Kristins-MacBook-Air Desktop % /Library/Developer/CommandLineTools/usr/bin/python3 -m pip install streamlit
/Library/Developer/CommandLineTools/usr/bin/python3 -m streamlit run motivation_app.py
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: streamlit in /Users/krismac/Library/Python/3.9/lib/python/site-packages (1.50.0)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker<2,>=1.5.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools<7,>=4.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (6.2.6)
Requirement already satisfied: click<9,>=7.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (8.1.8)
Requirement already satisfied: numpy<3,>=1.23 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (1.24.3)
Requirement already satisfied: packaging<26,>=20 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (25.0)
Requirement already satisfied: pandas<3,>=1.4.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (2.3.3)
Requirement already satisfied: pillow<12,>=7.1.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (11.3.0)
Requirement already satisfied: protobuf<7,>=3.20 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (4.25.8)
Requirement already satisfied: pyarrow>=7.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (21.0.0)
Requirement already satisfied: requests<3,>=2.27 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (2.32.5)
Requirement already satisfied: tenacity<10,>=8.1.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (9.1.2)
Requirement already satisfied: toml<2,>=0.10.1 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions<5,>=4.4.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (4.15.0)
Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (3.1.46)
Requirement already satisfied: pydeck<1,>=0.8.0b4 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (0.9.1)
Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from streamlit) (6.5.4)
Requirement already satisfied: jinja2 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)
Requirement already satisfied: jsonschema>=3.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.1)
Requirement already satisfied: narwhals>=1.14.2 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.15.0)
Requirement already satisfied: gitdb<5,>=4.0.1 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)
Requirement already satisfied: smmap<6,>=3.0.1 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)
Requirement already satisfied: python-dateutil>=2.8.2 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from pandas<3,>=1.4.0->streamlit) (2025.3)
Requirement already satisfied: charset_normalizer<4,>=2 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (2.6.3)
Requirement already satisfied: certifi>=2017.4.17 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (2026.1.4)
Requirement already satisfied: MarkupSafe>=2.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.3)
Requirement already satisfied: attrs>=22.2.0 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.4.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in /Users/krismac/Library/Python/3.9/lib/python/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.27.1)
Requirement already satisfied: six>=1.5 in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.15.0)

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.25:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
2026-01-30 15:50:20.050 Script compilation error
Traceback (most recent call last):
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 571, in _run_script
    code = self._script_cache.get_bytecode(script_path)
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_cache.py", line 68, in get_bytecode
    with open_python_file(script_path) as f:
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/source_util.py", line 54, in open_python_file
    return tokenize.open(filename)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/tokenize.py", line 392, in open
    buffer = _builtin_open(filename, 'rb')
IsADirectoryError: [Errno 21] Is a directory: '/Users/krismac/Desktop/motivation_app.py'
2026-01-30 15:50:20.056 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-01-30 15:50:49.387 Script compilation error
Traceback (most recent call last):
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 571, in _run_script
    code = self._script_cache.get_bytecode(script_path)
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_cache.py", line 68, in get_bytecode
    with open_python_file(script_path) as f:
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/source_util.py", line 54, in open_python_file
    return tokenize.open(filename)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/tokenize.py", line 392, in open
    buffer = _builtin_open(filename, 'rb')
IsADirectoryError: [Errno 21] Is a directory: '/Users/krismac/Desktop/motivation_app.py'
2026-01-30 15:50:49.388 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-01-30 15:50:49.774 Script compilation error
Traceback (most recent call last):
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 571, in _run_script
    code = self._script_cache.get_bytecode(script_path)
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_cache.py", line 68, in get_bytecode
    with open_python_file(script_path) as f:
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/source_util.py", line 54, in open_python_file
    return tokenize.open(filename)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/tokenize.py", line 392, in open
    buffer = _builtin_open(filename, 'rb')
IsADirectoryError: [Errno 21] Is a directory: '/Users/krismac/Desktop/motivation_app.py'
2026-01-30 15:50:49.774 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
~/Library/Python/3.9/bin/streamlit run motivation_app.py
^C  Stopping...
(mymotivationenv) krismac@Kristins-MacBook-Air Desktop % ~/Library/Python/3.9/bin/streamlit run motivation_app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.25:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
2026-01-30 15:51:44.956 Script compilation error
Traceback (most recent call last):
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 571, in _run_script
    code = self._script_cache.get_bytecode(script_path)
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_cache.py", line 68, in get_bytecode
    with open_python_file(script_path) as f:
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/source_util.py", line 54, in open_python_file
    return tokenize.open(filename)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/tokenize.py", line 392, in open
    buffer = _builtin_open(filename, 'rb')
IsADirectoryError: [Errno 21] Is a directory: '/Users/krismac/Desktop/motivation_app.py'
2026-01-30 15:51:44.964 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-01-30 15:52:09.115 Script compilation error
Traceback (most recent call last):
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 571, in _run_script
    code = self._script_cache.get_bytecode(script_path)
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/runtime/scriptrunner/script_cache.py", line 68, in get_bytecode
    with open_python_file(script_path) as f:
  File "/Users/krismac/Library/Python/3.9/lib/python/site-packages/streamlit/source_util.py", line 54, in open_python_file
    return tokenize.open(filename)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/tokenize.py", line 392, in open
    buffer = _builtin_open(filename, 'rb')
IsADirectoryError: [Errno 21] Is a directory: '/Users/krismac/Desktop/motivation_app.py'
2026-01-30 15:52:09.116 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
^C  Stopping...
(mymotivationenv) krismac@Kristins-MacBook-Air Desktop % echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
streamlit run motivation_app.py
^C%                                                                             (mymotivationenv) krismac@Kristins-MacBook-Air Desktop % streamlit run motivation_app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.25:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
2026-01-30 15:52:39.399 Script compilation error
Traceback (most recent call last):
  File "/Users/krismac/Desktop/mymotivationenv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 571, in _run_script
    code = self._script_cache.get_bytecode(script_path)
  File "/Users/krismac/Desktop/mymotivationenv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_cache.py", line 68, in get_bytecode
    with open_python_file(script_path) as f:
  File "/Users/krismac/Desktop/mymotivationenv/lib/python3.9/site-packages/streamlit/source_util.py", line 54, in open_python_file
    return tokenize.open(filename)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/tokenize.py", line 392, in open
    buffer = _builtin_open(filename, 'rb')
IsADirectoryError: [Errno 21] Is a directory: '/Users/krismac/Desktop/motivation_app.py'
2026-01-30 15:52:39.408 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
ls
^C  Stopping...
(mymotivationenv) krismac@Kristins-MacBook-Air Desktop % streamlit run motivation_app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.25:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
2026-01-30 15:53:20.828 Script compilation error
Traceback (most recent call last):
  File "/Users/krismac/Desktop/mymotivationenv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 571, in _run_script
    code = self._script_cache.get_bytecode(script_path)
  File "/Users/krismac/Desktop/mymotivationenv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_cache.py", line 68, in get_bytecode
    with open_python_file(script_path) as f:
  File "/Users/krismac/Desktop/mymotivationenv/lib/python3.9/site-packages/streamlit/source_util.py", line 54, in open_python_file
    return tokenize.open(filename)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/tokenize.py", line 392, in open
    buffer = _builtin_open(filename, 'rb')
IsADirectoryError: [Errno 21] Is a directory: '/Users/krismac/Desktop/motivation_app.py'
2026-01-30 15:53:20.835 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
^C  Stopping...
(mymotivationenv) krismac@Kristins-MacBook-Air Desktop % ls
motivation_app.py	mymotivationenv
(mymotivationenv) krismac@Kristins-MacBook-Air Desktop % rm -rf motivation_app.py
(mymotivationenv) krismac@Kristins-MacBook-Air Desktop % mv motivation_app.py motivation_app_folder_backup
mv: rename motivation_app.py to motivation_app_folder_backup: No such file or directory
(mymotivationenv) krismac@Kristins-MacBook-Air Desktop % nano motivation_app.py

  UW PICO 5.09                File: motivation_app.py                 Modified  

import streamlit as st
import sqlite3
import os
from vonage import Client, Sms
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import random   

# Vonage credentials (replace with your own from dashboard.nexmo.com)
VONAGE_API_KEY = os.getenv84a6d565                          
VONAGE_API_SECRET = os.getenvUAtokW9%PCZXo1o$w                               
VONAGE_BRAND_NAME = os.getenv("VONAGE_BRAND_NAME", "nervarah")  # Your sender n$
        
vonage_client = Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
sms = Sms(vonage_client)
    
# Database setup
conn = sqlite3.connect('users.db')
c = conn.cursor()

^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Pg   ^K Cut Text  ^C Cur Pos   
^X Exit      ^J Justify   ^W Where is  ^V Next Pg   ^U UnCut Text^T To Spell  
