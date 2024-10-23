from abc import abstractmethod


class Engine:
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Engine):
    def start(self):
        print("Car Started")

    def stop(self):
        print("Car stopped")

    def drive(self):
        self.start()
        self.stop()


car = Car()
car.drive()
