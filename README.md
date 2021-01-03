# 🤓 Digital Humanities

Project on automating some very boring tasks...
Can we save Rodericus?


## 🧑‍🔧 Setup
1. Install [Docker](https://docs.docker.com/get-docker/);
2. Verify you can access to a shell 
   (
   [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/install/installing-windows-powershell?view=powershell-7.1) 
   on Windows).


## 🧐 What can I do?
Please, open your shell (for example, to open the PowerShell perform a 
right click on the windows icon and select the PowerShell) and type the
following command (you can copy-paste it) (most of the commands are in
Italian... sorry international guys!):

```shell script
docker run -t --rm ghcr.io/robin-castellani/digital-humanities/digital-humanities:0.0.2
```

The shell will show you what is happening, read carefully its output!

So, here you can use `commands` like `sostituisci` to do something.
When you don't know what a command do, type it along with `--help`; 
here is an example (the copy-paste is still valid):

```shell script
docker run -t --rm ghcr.io/robin-castellani/digital-humanities/digital-humanities:0.0.2 sostituisci --help
```

The help output will tell you what the command does and which options
it needs. In this case, `sostituisci` perform some substitutions given
a `.pdf` file and a `.csv` file containing the substitutions; its
output is saved into a `.txt` file. An option is `--file-pdf`: you need
to tell which `.pdf` file you want to read! Indeed, you have to type its
path. Look at this example (my `helloworld.pdf` file is located in 
`C:\Users\VForVendetta\Desktop\helloworld.pdf`):

```shell script
docker run -t --rm ghcr.io/robin-castellani/digital-humanities/digital-humanities:0.0.2 sostituisci --file-pdf "C:\Users\VForVendetta\Desktop\helloworld.pdf"
```

And so on...


## 👉 In practice, please!
- `sostituisci`
    1. Create a folder and put your original `.pdf` file inside;
    2. With a text editor, create a `.csv` file like this one:
        ```csv
           old_string|new_string
           old_string2|new_string2
        ```
       and put it in that folder;
    3. Open a shell;
    4. Use the command `cd` (that is, Change Directory) to move to 
        the folder with the `.pdf` and `.csv` file; for example, if your
        files are in `C:\Users\VForVendetta\Desktop`, type in the shell
        `cd "C:\Users\VForVendetta\Desktop"`;
    5. Type in the shell
        ```shell script
           sudo docker run -t --rm ghcr.io/robin-castellani/digital-humanities/digital-humanities:0.0.2 \
           sostituisci \
           --file-pdf <file-pdf.pdf> \
           --file-sostituzioni <file-substitutions.csv>
        ```
        of course, replace `<file-pdf.pdf>` with the actual name of your
        `.pdf` file (the same with `<file-substitutions.csv>`);
    6. Wait and the look at the result in the `result.txt` file.
