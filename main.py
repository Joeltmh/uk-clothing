import setup

system = setup.uk_clothes_system()
solved = system.solve_unknowns()
if not solved:
    print("Could not solve the system.")
    exit(0)
