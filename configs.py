from enum import Enum


class SK:
    # entries ={}
    # outerScope = {}
    def print_all(self, more_print_line=False):
        print()
        if more_print_line:
            print("===PRINT_ALL>>>===")

        for x in self.global_scope:
            print("G|" + x + ": " + str(self.global_scope[x]))

        if self.local_scope:
            print("------------------------------------------------------------")

        for x in self.local_scope:
            print("L|" + x + ": " + str(self.local_scope[x]))

        if more_print_line:
            print("===PRINT_ALL<<<===")

    def nr_global_vars(self):
        return len(self.global_scope)

    def __repr__(self):
        return (
            "global: " + str(self.global_scope) + "\n local: " + str(self.local_scope)
        )

    def __init__(self) -> None:
        self.global_scope = {}
        self.local_scope = {}

    def lookup(self, var_name):
        if var_name in self.local_scope:
            return self.local_scope.get(var_name)
        return self.global_scope.get(var_name)

    def in_globals(self, var_name):
        return var_name in self.global_scope

    def in_locals(self, var_name):
        return var_name in self.local_scope

    def reset_locals(self):
        self.local_scope = {}

    # TODO: refctor to in selfscope
    def set_local_var(self, name, info):
        if not self.local_scope.get(name):
            self.local_scope[name] = info

    def set_global_var(self, name, info):
        if not self.global_scope.get(name):
            self.global_scope[name] = info

    def update_global_POS(self, name, position=None):
        if not position:
            self.global_scope[name]["POS"].append(self.global_scope[name]["POS"][-1] + 1)
        else:
            raise NotImplemented("def update_global_POS(self,name, position=None):")

    def get_global_addr(self, var_name):
        entry = self.global_scope.get(var_name)
        if not entry:
            raise Exception(f"{var_name} not in global!")
        return entry["addr"]

    def get_local_addr(self, var_name):
        entry = self.local_scope.get(var_name)
        if not entry:
            raise Exception(f"{var_name} not in local!")
        return entry["addr"]

    def get_local_or_global_addr(self, var_name):
        entry = self.local_scope.get(var_name)
        if not entry:
            entry = self.global_scope.get(var_name)
        if not entry:
            raise Exception(f"{var_name} not in local and global!")
        return entry["addr"]


class Configs(Enum):
    GENERATED_DIR = "/Users/dominik/HOME/DEV/Compiler/incc24/dom/arm/generated"
    GENERATED_IR_CODE_DIR = (
        "/Users/dominik/HOME/DEV/Compiler/incc24/dom/arm/generated/ir_code"
    )
    CODE_DIR = "/Users/dominik/HOME/DEV/Compiler/incc24/dom/arm/code"
    SHOW_IR_IN_ASM = True
    ADD_COMMENTS_IR_TO_ARM_EACH_LINE = False
    ENV_GLOBAL_NAME = "__global"
    ENV_LOCAL_NAME = "__local"
    # ENV = {}
    # ENV[ENV_GLOBAL_NAME] = {}
    # ENV[ENV_LOCAL_NAME] = {}
    ENV_SYMBOL_TABLE = SK()
    ENV = SK()
    STACK_SIZE_ARM = 16
