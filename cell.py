from organ import organ,nucleus,mitachondria,membrane,ribosome
class cell:
    cell_id :str = ""
    dna = 0

    atp :int = 200
    acts: int = 8
    protein: int = 8
    waste :int = 0

    organs : list = []
    resources : dict


    def __init__(self, id):
        self.cell_id = id
    
    def ticker(self, subj: organ):
        for org in self.organs:
            if org != subj:
                org.tick_passed()
            else:
                if org.maintained:
                    self.use_atp(org.func_cost)
                    print(f"{org.organ_name} has done its function: {org.func_cost} has been used!")
                else:
                    self.use_atp(org.func_cost)
                    print(f"{org.organ_name} has been maintained: {org.main_cost} has been used!")
                org.tick_picked()
                
    def tick_actor(self):
        
        subj : organ = self.organs[0]
        score : float = 0
        for organ in self.organs:
            penatly = 1
            if organ.maintained:
                penatly = 2
                sc = (organ.priority + (organ.ticks_since_act*(1+(organ.priority*0.15)))) - penatly
            else:
                sc = (organ.priority + (organ.ticks_since_main*(0.85+(organ.priority*0.15)))) - penatly
            
            #print(f"{organ.organ_name} has importance score of {sc}")
            if sc > score:
                score = sc
                subj = organ
        self.ticker(subj)
    def increment_atp(self, val):
        self.atp += val
    def use_atp(self,val):
        self.atp -= val
    def increment_acts(self, val):
        self.acts += val
    def use_act(self,val):
        self.acts -= val
    def increment_protein(self, val):
        self.protein += val
    def use_protein(self,val):
        self.protein -= val
    def init_cell(self):
        nuc = nucleus("Nucleus",3,self)
        met = mitachondria("Mitochondria",4,self)
        rib = ribosome("Ribosome",2,self)
        mem = membrane("Membrane",1,self)
        self.organs = [nuc,met,rib,mem]