class Process:

    UNKNOWN_SIZE = -1
    
    def __init__(self, name, size, other_values={}):  # why the ={} here?
        self.name = name
        self.size = size
        self.other_values = other_values

class Flow:

    UNKNOWN_PROPORTION = -1
    UNKNOWN_AMOUNT = -1

    def __init__(self, origin, destination, amount, is_proportion=True):
        self.origin = origin
        self.destination = destination
        self.proportion = amount if is_proportion else -1  # why is 'propotion' not listed in the brackets after __init__?
        self.amount = amount if not is_proportion else -1

class System:

    def __init__(self, name):
        self.name = name
        self.processes = {}
        self.flows = []

    def add_process(self, *args):  # is '*args' just shorthand for the arguments of the Process class defined above?
        p = Process(*args)
        self.processes[p.name] = p
        return p

    def add_flow(self, *args):
        f = Flow(*args)
        self.flows.append(f)
        return f

    def is_flow(self, origin, destination):
        return len([f for f in self.flows if f.origin == origin and f.destination == destination]) > 0

    def get_flow(self, origin, destination):
        return [f for f in self.flows if f.origin == origin and f.destination == destination][0]

    def split_flow(self, origin, destination, names, amounts, are_proportional=True):
        overarching_flow = get_flow(origin, destination)
        for i in range(0, len(names)):
            if are_proportional:
                amounts = [proportion * destination.size for proportion in amounts]
            intermediate_process = self.add_process(names[i], amounts[i])
            pre_sub_flow = self.add_flow(origin, intermediate_process, amounts[i], False)
            post_sub_flow = self.add_flow(intermediate_process, destination, amounts[i], False)

    def solve_unknowns(self):
        any_changes_made = True
        while any_changes_made:
            any_changes_made = False
            # TODO: Populate both proportions and amounts where possible
            # TODO: Populate unknown Process sizes
        return False

    # TODO: Check balance
    # TODO: Add time series
