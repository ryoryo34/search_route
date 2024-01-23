import networkx as nx

temples = ['鹿苑寺（金閣寺）', '南禅寺', '鞍馬寺', '慈照寺（銀閣寺）', '清水寺', '八坂神社','本願寺（西本願寺）', '天龍寺', '西芳寺（苔寺）', '宇治上神社']

def make_graph1():
    G=nx.Graph()
    G.add_nodes_from(temples)
    G.add_weighted_edges_from([
                           ('鹿苑寺（金閣寺）','南禅寺',28),
                          ('鹿苑寺（金閣寺）','鞍馬寺',26),
                          ('鹿苑寺（金閣寺）','慈照寺（銀閣寺）',25),
                          ('鹿苑寺（金閣寺）','清水寺',35),
                          ('鹿苑寺（金閣寺）','八坂神社',28),
                          ('鹿苑寺（金閣寺）','本願寺（西本願寺）',24),
                          ('鹿苑寺（金閣寺）','天龍寺',22),

                          ('南禅寺','鞍馬寺',35),
                          ('南禅寺','慈照寺（銀閣寺）',8),
                          ('南禅寺','清水寺',22),
                          ('南禅寺','八坂神社',14),
                          ('南禅寺','本願寺（西本願寺）',24),
                          ('南禅寺','宇治上神社',45),

                          ('鞍馬寺','慈照寺（銀閣寺）',40),
                          ('鞍馬寺','清水寺',55),
                          ('鞍馬寺','八坂神社',45),

                          ('慈照寺（銀閣寺）','清水寺',20),
                          ('慈照寺（銀閣寺）','八坂神社',15),
                          ('慈照寺（銀閣寺）','宇治上神社',50),

                          ('清水寺','八坂神社',12),
                          ('清水寺','本願寺（西本願寺）',16),
                          ('清水寺','宇治上神社',40),

                          ('八坂神社','本願寺（西本願寺）',18),
                          ('八坂神社','宇治上神社',40),

                          ('本願寺（西本願寺）','天龍寺',28),
                          ('本願寺（西本願寺）','宇治上神社',30),

                          ('天龍寺','西芳寺（苔寺）',12),
                        ])
    return G

def make_graph2():
    G=nx.Graph()
    G.add_nodes_from(temples)
    G.add_weighted_edges_from([
              ('鹿苑寺（金閣寺）','南禅寺',28),
              ('鹿苑寺（金閣寺）','鞍馬寺',26),
              ('鹿苑寺（金閣寺）','慈照寺（銀閣寺）',25),
              ('鹿苑寺（金閣寺）','清水寺',35),
              ('鹿苑寺（金閣寺）','八坂神社',28),
              ('鹿苑寺（金閣寺）','本願寺（西本願寺）',24),
              ('鹿苑寺（金閣寺）','天龍寺',22),
              ('鹿苑寺（金閣寺）','西芳寺（苔寺）',29),
              ('鹿苑寺（金閣寺）','宇治上神社',45),

              ('南禅寺','鞍馬寺',35),
              ('南禅寺','慈照寺（銀閣寺）',8),
              ('南禅寺','清水寺',22),
              ('南禅寺','八坂神社',14),
              ('南禅寺','本願寺（西本願寺）',24),
              ('南禅寺','天龍寺',30),
              ('南禅寺','西芳寺（苔寺）',32),
              ('南禅寺','宇治上神社',45),

              ('鞍馬寺','慈照寺（銀閣寺）',40),
              ('鞍馬寺','清水寺',55),
              ('鞍馬寺','八坂神社',45),
              ('鞍馬寺','本願寺（西本願寺）',38),
              ('鞍馬寺','天龍寺',42),
              ('鞍馬寺','西芳寺（苔寺）',50),
              ('鞍馬寺','宇治上神社',60),

              ('慈照寺（銀閣寺）','清水寺',20),
              ('慈照寺（銀閣寺）','八坂神社',15),
              ('慈照寺（銀閣寺）','本願寺（西本願寺）',21),
              ('慈照寺（銀閣寺）','天龍寺',31),
              ('慈照寺（銀閣寺）','西芳寺（苔寺）',35),
              ('慈照寺（銀閣寺）','宇治上神社',50),

              ('清水寺','八坂神社',12),
              ('清水寺','本願寺（西本願寺）',16),
              ('清水寺','天龍寺',28),
              ('清水寺','西芳寺（苔寺）',25),
              ('清水寺','宇治上神社',40),

              ('八坂神社','本願寺（西本願寺）',18),
              ('八坂神社','天龍寺',26),
              ('八坂神社','西芳寺（苔寺）',27),
              ('八坂神社','宇治上神社',40),

              ('本願寺（西本願寺）','天龍寺',28),
              ('本願寺（西本願寺）','西芳寺（苔寺）',18),
              ('本願寺（西本願寺）','宇治上神社',30),

              ('天龍寺','西芳寺（苔寺）',12),
              ('天龍寺','宇治上神社',43),

              ('西芳寺（苔寺）','宇治上神社',40),
                           ])
    return G