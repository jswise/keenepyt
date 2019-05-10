# KeenePYT
Materials for a workshop at Northeast Arc User Group (NEARC), Keene, New Hampshire, USA in the spring of 2019.

This workshop is for ArcGIS Pro users who want to package their Python geoprocessing tools and distribute them to other users.

## Getting started

### Download Miniconda.

Get the [Miniconda](https://docs.conda.io/en/latest/miniconda.html
) Python 3.7 64-bit installer for Windows (Miniconda3-latest-Windows-x86_64.exe).

Even though ArcGIS Pro comes with conda, we'll make a separate conda installation for building packages.

### Create a folder.

Create the folder **C:\Projects\NEARC\code**.

You can put it somewhere else if you must, but this we'll be easier if we're all doing it the same way.

### Download this repository.

#### If you have Git installed on your computer:

Open a command prompt, navigate to **C:\Projects\NEARC\code**, and enter this command:

`git clone https://github.com/jswise/keenepyt.git`

#### If you don't have Git:

Click the **Clone or download** button above, and download the zip file.

Extract the zip file in **C:\Projects\NEARC\code**.

Rename the **keenepyt-master** folder to just **keenepyt**. You should now have the folder **C:\Projects\NEARC\code\keenepyt** with stuff in it.

Better yet, get [Git](https://git-scm.com/)!

### Install conda in your folder.

After you download Miniconda, navigate to **C:\Projects\NEARC\code\keenepyt\batch** and run **install-conda.bat**.

This will create a standalone conda installation in **C:\Projects\NEARC\conda**.

### Create dev and test environments.

In **C:\Projects\NEARC\code\keenepyt\batch**, run **create-dev-envs.bat**.

This will clone your default Python environment, _arcgispro-py3_, to two new environments, _dev_ and _localtest_.

### Create the production environment.

In **C:\Projects\NEARC\code\keenepyt\batch**, run **create-main-env.bat**.

This will clone your default Python environment to another new environment, _main_.