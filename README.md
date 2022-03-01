# AI12 - Nomad

## Makefile

The Makefile will automatically handle the virtual env. Type `make` to see the available commands. The Makefile only supports unix-based operating systems. If you're on Windows, consider using WSL2.

If you can't use WSL, try `pip install .` and then if everything has been installed correctly, try `pre-commit install`.

Now, if mypy or black doesn't work, you will not be abe to commit.

## Set up the CI

Because of Gitlab's limitations, we have to ensure that each fork is within the same `group`. Projects within the group will be able to access the CI dedicated to this project which is a requirement to make a Merge Request (MR).

1. Request to join the AI12-nomad Group https://gitlab.com/AI12-Nomad
2. Change the name of the fork and its URL to something unique (Settings -> Project Name, Settings -> Advanced -> Change Path)
3. Transfer the ownership to the AI12-nomad group. (Settings -> Advanced -> Transfert ownership)
4. Update your remotes with the new URL if necessary.

## Setup git

1. [Add an ssh key to your gitlab account](https://docs.gitlab.com/ee/ssh/)
2. `git clone git@gitlab.com:AI12-Nomad/ai12-nomad.git`
3. [Fork the repository](https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html#creating-a-fork)
4. Don't forget to change the {user_name} **without the curly brackets**!

Add the forked repository as a remote `git remote add fork  git@gitlab.com:AI12-Nomad/{fork_name}.git`

5. Consider disabling push on `origin`: `git remote set-url --push origin no_push`

## Setup your working environment

1. Setup the python virtual environment (venv) : `make install`
2. Enter the venv : `source env/bin/activate`
   Your prompt shoud now be preceded by "(env)".
3. to check that you're in the virtual environment : `which python3`
   If it returns a file in your project folder, it means you're in the virtual env.
4. to leave the venv : `deactivate`

## Contribute

1. To make changes start with creating a branch `git checkout -b my_feature origin/dev`.
2. Push to your fork using the same branch name. `git push fork my_feature`
   - Your code will need to be formatted in order to pass the pipeline validation.
     For that, you have ot run `make format` in your project before commiting your code.
3. [Create a Merge Request on gitlab](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html#when-you-use-git-commands-locally)

   - Wait for the pipeline to have validated your code, then ask for reviews.

## Run the applications

```sh
# In the venv:
make install #(pip install .)
nomad_server
nomad_client
```
