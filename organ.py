import cell
class organ:
    organ_name :str= ""
    organ_id : str = "organ"
    main_cost :int= 0
    func_cost :int= 0
    mother_cell : cell.cell

    priority : int=0
    ticks_since_main = 0
    ticks_since_act = 0



    integrity :int = 100
    waste :int = 0
    maintained : bool = False
    def __init__(self,name : str,prio : int, mother):
        self.organ_name = name
        self.priority = prio
        self.mother_cell = mother
    def act(self):
        pass
    def maintain(self):
        self.ticks_since_main = 0
        self.maintained = True
        
    def tick_passed(self):
        if self.maintained:
            self.ticks_since_act += 1
        else:
            self.ticks_since_main += 1
    def tick_picked(self):
        if self.maintained:
            self.ticks_since_act = 0
            self.act()
        else:
            self.maintain()
    def get_tick_cost(self):
        return self.main_cost
    
class nucleus(organ):
    DNA= []
    organ_id = "Nucleus"
    main_cost :int= 6
    func_cost :int= 8
    def act(self):
        self.mother_cell.increment_acts(1)
class mitachondria(organ):
    organ_id = "Mitachondria"
    main_cost :int= 4
    func_cost :int= 3
    def act(self):
        self.mother_cell.increment_atp(32)
class membrane(organ):
    organ_id = "Membrane"
    main_cost :int= 6
    func_cost :int= 4
    def act(self):
        pass
class ribosome(organ):
    organ_id = "Ribosome"
    main_cost :int= 3
    func_cost :int= 5
    def act(self):
        self.mother_cell.increment_protein(1)