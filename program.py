class program:
    import cell
    import time
    import organ

    processing : bool = False
    active : bool = True
    in_game : bool = False
    current_cell : cell.cell
    current_turn : int
    def __init__(self) -> None:
        self.commands : dict = {
        "START" : [self.start, "!!\nCOMMAND START:Starts the game/ restarts the game \n Takes no arguments\n!!"],
        "EXIT" : [self.end,"!!COMMAND EXIT:Forcibly exists the simulation. \n Takes no arguments!!"],
        "HELP" : [self.command_lis,"!!\nCOMMAND Help:Prints list of available commands. \n Can take the name of other commands as an argument \n EXAMPLE: HELP START\n!!"],
        "TURN" : [self.turn, "!!\nCOMMAND Turn: Passes a turn, printing the actions of each tick (turns are 4-9 ticks, depending on amount of atp generated and health/size of nucleus)\nCan only be used while the simulation is ongoing.\n!!"],
        "SHOW" : [self.show,"!!\nCOMMAND Show: Prints specific properties about the cell/organs\n Takes subject as an argument\nEXAMPLE: Show Atp\n!!"],
        "ORGANS" : [self.organ_list,"!!\nCOMMAND Organs: Prints names and types of present organs inside the cell.\n Takes organ name as an argument, printing out its attributes\n!!"],
        "ACT" : [self.act,"!!\nCOMMAND Act: Performs a pre programmed action from a predefined list.\n Takes an action as an argument\n!!"],
    }
        
    def intrude_message(self):
        print("ERROR")
        self.time.sleep(1)
        print("Start the simulation to use this command!")
    def start(self,arg=""):
        if self.in_game:
            print(f"are you sure ? Doing so will restart the simulation\n write \"Y\" to confirm.")
            inp2 = input()
            if inp2 != "Y":
                print("Cancelling...")
                self.processing = False
                return
            else:
                print("CONFIRMED")
                self.time.sleep(0.4)
        print("STARTING GAME")
        self.in_game = True
        self.current_turn = 0
        print(f"Select the name of your very new cell!")
        self.current_cell = self.cell.cell(input())
        self.current_cell.init_cell()
        self.current_cell.atp = 200
        self.time.sleep(0.5)
        print(f"Your new cell, {self.current_cell.cell_id} has been born!")
        self.time.sleep(0.5)
        print("Begin simulation")
        self.processing = False
        #This might be the worst  code known to man, but i dont care
    
    def end(self,arg=""):
        print("goodbye")
        self.processing = False
        exit()
    def command_lis(self,arg=""):
        if arg in self.commands:
            print(f"{self.commands[arg][1]}")
        else:
            print("present commands are:")
            for command in self.commands:
                print(f"{command}")
            print("\n!!Add an argument to the help command to get more information!!")
        self.processing = False
    def tick(self,arg=""):
        self.current_cell.tick_actor()
    def turn(self,arg=""):
        if not self.in_game:
            self.intrude_message()
            return
        i = 0
        while (i < 9):
            self.time.sleep(0.2)
            self.tick()
            i+=1
        self.processing = False
    def show(self,arg=""):
        if not self.in_game:
            self.intrude_message()
            return
        match arg:
            case "ATP":
                print(f"*Current Atp value is: {self.current_cell.atp}")
            case "ACTS":
                print(f"*Current Acts number is: {self.current_cell.acts}")
            case "PROTEIN":
                print(f"*Current Protein count is: {self.current_cell.protein}")
            case "WASTE":
                print(f"*Current Waste value is: {self.current_cell.waste}")
            case _:
                print("Available Inspectable Arguments are:")

        self.processing = False
        pass
    def organ_list(self, arg = ""):
        if not self.in_game:
            self.intrude_message()
            return
        organ_names = []
        for organ in self.current_cell.organs:
            organ_names.append(organ.organ_name.upper())
        if arg in organ_names:
            for organ in self.current_cell.organs:
                if organ.organ_name.upper() == arg:
                    print(f"Organ {organ.organ_name} : type_{organ.organ_id}:\n °- MAINTENANCE COST: {organ.main_cost} \n °- FUNCTION COST: {organ.func_cost} \n °- PRIORITY: {organ.priority} \n °- INTEGRITY: {organ.integrity} \n °- WASTE ACCUMULATION: {organ.waste} \n")
        else:
            print(f"*Organs inside cell, {self.current_cell.cell_id} are:")
            self.time.sleep(0.4)
            for organ in self.current_cell.organs:
                print(f"{organ.organ_name} : type_{organ.organ_id}")
            pass

            print("\n!!Add the name of an ORGANELLE as an argument, to inspect it!!")
        self.processing = False
    def act(self,arg = ""):
        match arg:
            case "CREATE":
                self.time.sleep(0.4)
                print("**************")
                print(f"_ORGANELLE CREATION MENU_\nAvailable types:mitachondria,membrane,ribosome \nCOMMAND: ORGANELLE_TYPE ORGANELLE_NAME")
                try:
                    INPUT = input()
                    arg1 = ""
                    for i in range(len(INPUT)):
                        if INPUT[i] == ' ':
                            break
                        arg1 += INPUT[i]
                    arg2 = ""
                    if len(arg1)+1 >= len(INPUT):
                        pass
                    else:
                        for i in range(len(arg1)+1,len(INPUT)):
                            if INPUT[i] == ' ':
                                break
                            arg2 += INPUT[i]
                    self.current_cell.create_organelle(arg2,arg1.upper())
                except:
                    print("ERROR WHILE PERFORMING ACTION")

            case "DELETE":
                self.time.sleep(0.4)
                print("**************")
                print(f"_ORGANELLE DELETION MENU_\nEnter name of organelle you wanted DELETED PERMANENTLY\nCOMMAND: ORGANELLE_NAME")
                try:
                    INPUT = input()
                    self.current_cell.delete_organelle(INPUT)
                except:
                    print("ERROR WHILE PERFORMING ACTION")
            case _:
                print(f"**LIST OF AVAILABLE ACTIONS:**\nCreate: Creates new organelle\nDelete: Delete an exisitng organelle")
        self.processing = False
    def Update(self):
        pass
        

    def main(self):
        print(f"Welcome to CELLSIMULATOR, type help for list of commands \n Type \"Start\" to create your very first cell")
        while self.active:
        
            inp = input()
            new_inp = inp.upper()
            num = len(new_inp)
            command = ""
            for i in range(num):
                if new_inp[i] == ' ':
                    break
                command += new_inp[i]
            arg1 = ""
            val = len(command)
            if val >= num:
                pass
            else:
                for i in range(len(command)+1,num):
                    if new_inp[i] == ' ':
                        break
                    arg1 += new_inp[i]
            if command in self.commands:
                if self.processing:
                    print("please wait")
                else:
                    self.processing = True
                    self.commands[command][0](arg1)
            else:
                self.time.sleep(0.2)
                print("Unkown command!")
prog = program()
prog.main()