from brownie import project

# print(project.load("brownie_project"))
proj = project.load("brownie_project")
# name changed to: BrownieProject

# print(dir(proj))
print([it for it in dir(proj) if not it.startswith("_")])
# we have "Faucet" now.
print(dir(proj.Faucet), type(proj.Faucet))
print(proj.Faucet.signatures)
