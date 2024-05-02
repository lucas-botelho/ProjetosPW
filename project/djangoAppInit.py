import os
import subprocess


def djangoAppInit(app_name):

    command = f'python manage.py startapp {app_name}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=os.path.abspath("./"))

    if result.returncode == 0:
        pySettings = os.path.abspath("./project/settings.py")
        with open(pySettings) as settingsFile:
            lines = settingsFile.readlines()

        isInInstalledApps = False
        for line in lines:
            if line.__contains__("INSTALLED_APPS"):
                isInInstalledApps = True
            
            if line.__eq__(']\n') and isInInstalledApps:
                lines.insert(lines.index(line), "    '" + app_name + "',\n" )
                break
        
        with open(pySettings, 'w') as file:
            file.writelines(lines)
      
appname = input("new app name=")

djangoAppInit(app_name=appname)

