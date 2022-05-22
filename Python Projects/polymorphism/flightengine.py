class Flight:
    def __init__(self,engine):
        self.engine=engine

    def startEngine(self):
        self.engine.start();

class AirbusEngine:
    def start(self):
        print("Starting Airbus engine")

class BoingEngine:
    def start(self):
        print("Starting BoingEngine engine")

ae = AirbusEngine()
f = Flight(ae)
f.startEngine()

be = BoingEngine()
f1 = Flight(be)
f1.startEngine()


class Flight:
  def __init__(self,engine):
    self.engine = engine

  def engine(self):
    self.engine.start()

class Airbusengine:
  def start(self):
    print("Air bus engine started")

class Boingengine:
  def start(self):
    print("Boing engine started")


abe = Airbusengine()
f = Flight(abe)
f.engine()

boing = Boingengine()
f1 = Flight(boing)
f1.engine()