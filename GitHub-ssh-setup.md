# Connect to GitHub with SSH (Windows)

## Generate a new SSH key

1. Open Bash Terminal.
2. Open to the .ssh directory by using this command.

 ```bash
    cd ~/.ssh
```

3. If the directory doesn't exist, create it using this command.

 ```bash
    mkdir ~/.ssh
```

4. Paste the text below, substituting in your GitHub email address to generate the key.

```bash
ssh-keygen -t rsa -b 4096 -C "your@email.com"
```

5. When you're prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.
6. At the prompt, leave the passphrase blank, press Enter.
7. locate the public key file in the .ssh directory. The file is named id_rsa.pub.
8. View and copy the contents of the file by using this command.

```bash
cat id_rsa.pub
```

9. Paste the key into the "New SSH key" section of your GitHub account settings.
10. Confirm the action by entering your GitHub password.

## Connect your repository to GitHub

1. Create a new repository on GitHub, make sure to leave the "Initialize this repository with a README" option unchecked.
2. Click the SSH button
3. Open Bash Terminal.
4. Change the current working directory to your local project.
5. Initialize the local directory as a Git repository.

```bash
git init
```

6. Add the files in your new local repository. This stages them for the first commit.

```bash
git add .
```

7. Commit the files that you've staged in your local repository.

```bash
git commit -m "First commit"
```

8. In the Command prompt, add the URL for the remote repository where your local repository will be pushed.

```bash
git remote add origin git@github.com:example_user/example_repo.git
```

10. Push the changes in your local repository to GitHub.

```bash
git push -u origin main
```

11. Enter your GitHub username and password if/when prompted.
