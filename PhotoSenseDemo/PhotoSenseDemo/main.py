import streamlit
import subprocess
import sys
import streamlit.web.cli as stcli
import os


#%% Import the other libraries you need here
def main():
    """Function to run the Streamlit app from within the Python package after using cx_Freeze."""
    appname = 'photosensedemo.py'

    # Check if the app is running as a frozen executable (using cx_Freeze)
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # If frozen, use the temp folder where cx_Freeze unpacks files
        module_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(appname)))
    else:
        # If running from source code, use the current file path
        module_path = os.path.abspath(os.path.dirname(appname))

    # Update sys.argv for Streamlit (this is how Streamlit knows which file to run)
    sys.argv = ["streamlit", "run", os.path.join(module_path, appname), "--server.port=8502", "--global.developmentMode=false"]

    # Run the Streamlit app (this invokes Streamlit as if it's run from the command line)
    sys.exit(stcli.main())


if __name__ == "__main__":
    main()