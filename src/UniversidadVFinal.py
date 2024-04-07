from abc import ABCMeta, abstractmethod
from enum import Enum


class NotValidType(Exception):
    def __init__(self, mensaje="El tipo proporcionado no es válido"):
        self.message = mensaje
        super().__init__(self.message)

class TipoMiembro(Enum):
    Investigador    = 1
    Asociado        = 2
    Titular         = 3


class Sexo(Enum):
    Masculino   = 1
    Femenino    = 2

class AreaInvestigacion(Enum):  #OK
    InvestigacionOperativa           = 1
    ArquitecturaDeComputadores      = 2
    AprendizajeMaquina              = 3
    AprendizajeProfundo             = 4
    ComputacionAltasPrestaciones    = 5
    Software                        = 6

class Departamento(Enum):   #Ok
    DIIC = 1
    DITEC = 2
    DIS = 3


class Persona(metaclass = ABCMeta):
    def __init__(self, nombre : str, direccion : str ,  dni : str, sexo: Sexo):
        #Debemos comprobar en Persona que la información que llega para instanciar a cada estudiante, investigador o profesor es correcta
        self.nombre = nombre
        self._dni = dni
        self._sexo = sexo
        self._direccion = direccion

    @abstractmethod
    def devolver_datos(self):
        return f"Nombre : {self.nombre}, Dni: {self.__dni}, Direccion : {self.__direccion}, Sexo : {self.__sexo.name}"

    
class MiembroDepartamento:
    def __init__(self, identificador: str, tipo: TipoMiembro, departamento:Departamento):
        self.tipo = tipo
        self._departamento = departamento
        self.ID = identificador
            
    def cambioDepartamento(self, nuevo_departamento):
        #Esta comprobación debería hacerse con una excepción.... crearla más adelante
        if not isinstance(nuevo_departamento, Departamento):
            print("Departamento No válido")
            return
        self._departamento = nuevo_departamento

    def devolver_datos(self):
        return f", Miembro: {self.tipo.name}, Departamento: {self._departamento.name}"
    
    def devolverDepartamento(self):
        return self._departamento



class Asignatura:
    precio_credito = 16.5

    def __init__(self, nombre: str, codigo_asignatura : str, creditos: float, carrera : str, departamento : Departamento, curso: int):

        self.nombre = nombre
        self.codigo_asignatura = codigo_asignatura
        self.creditos = creditos
        self.carrera = carrera
        self._departamento = departamento
        self.curso = curso

    def devolverDepartamento(self):
        return self._departamento

    def __str__(self):
        return f"Nombre: {self.nombre}, Código asignatura: {self.codigo_asignatura} , Creditos: {self.creditos}, Carrera: {self.carrera}, Deparatamento: {self._departamento.name}, Curso: {self.curso}, Precio: {Asignatura.precio_credito * self.creditos}"
    


class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, dni: str, numero_expediente:str, sexo: Sexo):
        super().__init__(nombre, direccion, dni, sexo)
        self.numero_expediente = numero_expediente
        self.__listado_asignaturas = []
    
    def devolver_datos(self):                       
        return f"Nombre : {self.nombre}, Dni: {self._dni}, Direccion : {self._direccion}, Sexo : {self._sexo.name}, Número de Esxpediente : {self.numero_expediente}, Rol : Estudiante"
    
    def __str__(self):
        return f"{self.devolver_datos()}"

    def matricular(self, asignatura :Asignatura):
        self.__listado_asignaturas.append(asignatura)

    def desmatricular(self, asignatura:Asignatura):
        self.__listado_asignaturas.remove(asignatura)

    def mostrar_asignaturas(self):
        for a in self.__listado_asignaturas:
            print(a)
    
    def asignaturas(self):
        return self.__listado_asignaturas
    
    def devolver_dni(self):
        return self._dni



class ProfesorAsociado(Persona, MiembroDepartamento):
    def __init__(self, nombre: str, direccion: str, dni: str, identificador:str, sexo: Sexo, tipo: TipoMiembro, departamento: Departamento):
        Persona.__init__(self, nombre, direccion, dni, sexo)
        MiembroDepartamento.__init__(self, identificador, tipo, departamento)
        self.__listado_asignaturas = []


    def devolver_datos(self):   
        return f"Nombre : {self.nombre}, Dni: {self._dni}, Direccion : {self._direccion}, Sexo : {self._sexo.name}, Identificador : {self.ID}, Miembro: {self.tipo.name}, Departamento: {self._departamento.name}"

    def __str__(self):
        return f"{self.devolver_datos()}"
    
    def add_asignatura(self, asignatura :Asignatura):
        self.__listado_asignaturas.append(asignatura)

    def eliminar_asignatura(self, asignatura : Asignatura):
        self.__listado_asignaturas.remove(asignatura)
    
    def asignaturas(self):
        return self.__listado_asignaturas
    
    def mostrar_asignaturas(self):
        for a in self.__listado_asignaturas:
            print(a)

    def devolver_dni(self):
        return self._dni
    

class Investigador(Persona, MiembroDepartamento):
    def __init__(self, nombre: str, direccion: str, dni: str, identificador:str, sexo: Sexo, tipo:TipoMiembro,  departamento:Departamento, area_investigacion : AreaInvestigacion):
        Persona.__init__(self, nombre, direccion, dni, sexo)
        MiembroDepartamento.__init__(self,identificador, tipo, departamento)
        self.area_investigacion = area_investigacion

    def devolver_datos(self):   
        return f"Nombre : {self.nombre}, Dni: {self._dni}, Direccion : {self._direccion}, Sexo : {self._sexo.name}, Identificador : {self.ID}, Miembro: {self.tipo.name}, Departamento: {self._departamento.name}, Área Investigación : {self.area_investigacion.name}"
    
    def __str__(self):
        return f"{self.devolver_datos() }"
    
    def devolver_dni(self):
        return self._dni
    


class ProfesorTitular(Investigador):
    def __init__(self, nombre: str, direccion: str, dni: str, identificador:str, sexo: Sexo, tipo:TipoMiembro, departamento : Departamento, area_investigacion : AreaInvestigacion):

        super().__init__(nombre, direccion, dni, identificador,sexo, tipo, departamento, area_investigacion)
        self.__listado_asignaturas = []


    def devolver_datos(self):
        return super().devolver_datos()
    
    def __str__(self):
        return f"{self.devolver_datos()}"
    
    def add_asignatura(self, asignatura :Asignatura):
        self.__listado_asignaturas.append(asignatura)

    def eliminar_asignatura(self, asignatura : Asignatura):
        self.__listado_asignaturas.remove(asignatura)

    def asignaturas(self):
        return self.__listado_asignaturas

    def mostrar_asignaturas(self):
        for a in self.__listado_asignaturas:
            print(a)









class Universidad:
    def __init__(self, nombre : str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
        self.__listado_estudiantes = {}
        self.__listado_departamentos = {Departamento.DIIC :{'Asignaturas': {}, 
                                                            'Miembros': {TipoMiembro.Investigador:{}, 
                                                                         TipoMiembro.Asociado: {}, 
                                                                         TipoMiembro.Titular: {}}},
                                        Departamento.DITEC:{'Asignaturas': {}, 
                                                            'Miembros': {TipoMiembro.Investigador:{},
                                                                         TipoMiembro.Asociado: {}, 
                                                                         TipoMiembro.Titular: {}}},
                                        Departamento.DIS  :{'Asignaturas': {}, 
                                                            'Miembros': {TipoMiembro.Investigador:{}, 
                                                                         TipoMiembro.Asociado: {}, 
                                                                         TipoMiembro.Titular: {}}}}
        
    def __str__(self):
        pass
                    
    #Estos métodos se crean con la idea de poder tener el miembro de departamento, estudiante o asignatura cuando nos sea mas conveniente tenerlo, por los atributos que presentan.
    def devolver_miembro(self, identificador):      
        for departamento in self.__listado_departamentos:
            for tipo in  self.__listado_departamentos[departamento]['Miembros']:
                if identificador in self.__listado_departamentos[departamento]['Miembros'][tipo]:
                    return self.__listado_departamentos[departamento]['Miembros'][tipo][identificador]
        print("Miembro No encontrado")
        return None

    def devolver_estudiante(self, numero_expediente):   #Ok
        if numero_expediente not in self.__listado_estudiantes:
            print("Estudiante No encontrado")
            return None
        return self.__listado_estudiantes[numero_expediente]

    def devolver_asignatura(self, codigo_asignatura):    #Ok
        for departamento in self.__listado_departamentos:
            if codigo_asignatura in self.__listado_departamentos[departamento]["Asignaturas"]:
                return self.__listado_departamentos[departamento]["Asignaturas"][codigo_asignatura]
        print("Asignatura No encontrada")
        return None
    

    def add_estudiante(self, nombre_estudiante, direccion, dni, numero_expediente, sexo):          #OK
        #Aquí creo que esta primera comprobación debería de hacerse con el DNI ya que, podría darse el caso de que haya dos expedientes distintos, pero que presenten al mismo alumno...
        if numero_expediente in self.__listado_estudiantes:                    
            print("Estudiante ya añadido")
            return
        
        estudiante = Estudiante(nombre_estudiante, direccion, dni, numero_expediente, sexo)
        self.__listado_estudiantes[numero_expediente] = estudiante                                            


    def add_profesor(self, nombre, direccion, dni, identificador, sexo, tipo, departamento, area_investigacion = None): #OK, habría que comporbar que el tipo indicado es asociado o titular
        #Aquí creo que esta primera comprobación debería de hacerse con el DNI ya que, podría darse el caso de que haya dos expedientes distintos, pero que presenten al mismo alumno...
        
        if identificador in self.__listado_departamentos[departamento]['Miembros'][tipo]:
            print("Profesor ya añadido")
            return 
        
        if tipo.value == 2:
            profesor = ProfesorAsociado(nombre, direccion, dni, identificador, sexo, tipo, departamento)
        if tipo.value == 3:
            profesor = ProfesorTitular(nombre, direccion, dni, identificador, sexo, tipo, departamento, area_investigacion)

        self.__listado_departamentos[departamento]['Miembros'][tipo][identificador] = profesor

    
    def add_investigador(self, nombre, direccion, dni, identificador, sexo, departamento, area_investigacion): #OK , habría que comprobar que el tipo indicado es investigador
        
        if identificador in self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Investigador]:
            print("Investigador ya añadido")
            return
        
        self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Investigador][identificador] = Investigador(nombre, direccion, dni, identificador, sexo, TipoMiembro.Investigador, departamento, area_investigacion)

    
    def add_asignatura(self, nombre, codigo_asignatura, creditos, carrera, curso, departamento): #OK
        asignatura = self.devolver_asignatura(codigo_asignatura)
        if asignatura is not None:
            print("Asignatura ya añadida")
            return 

        self.__listado_departamentos[departamento]['Asignaturas'][codigo_asignatura] = Asignatura(nombre, codigo_asignatura, creditos, carrera, departamento, curso)
                   

    def mostrar_estudiantes(self):  #OK
        print("Estudiantes dados de alta:")
        for id in self.__listado_estudiantes:
            print(self.__listado_estudiantes[id])

    #Ojo que los 3 métodos siguientes tienen más complejidada temporal que hacer una única lista que vaya comprobando el tipo de Miembro que es cada elemento de la lista

    def mostrar_investigadores(self):   #OK
        for departamento in self.__listado_departamentos:
            for miembro in self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Investigador]:
                print(self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Investigador][miembro])


    
    def mostrar_profesores_titulares(self): #Ok
        for departamento in self.__listado_departamentos:
            for miembro in self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Titular]:
                print(self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Titular][miembro])

    def mostrar_profesores_asociados(self): #Ok
            for departamento in self.__listado_departamentos:
                for miembro in self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Asociado]:
                    print(self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Asociado][miembro])

    def mostrar_profesores(self):
        self.mostrar_profesores_titulares()
        self.mostrar_profesores_asociados()


    def mostrar_asignaturas_departamento(self, departamento):   #OK
        if not isinstance(departamento, Departamento):
            print("Departamento No válido")
            return
        for asignatura in self.__listado_departamentos[departamento]["Asignaturas"]:
            print(self.__listado_departamentos[departamento]["Asignaturas"][asignatura])
            

    def mostrar_miembros_departamento(self, departamento):  #OK
        if not isinstance(departamento, Departamento):
            print("Departamento No válido")
            return
        
        print("Investigadores")
        for investigador in self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Investigador]:
            print(self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Investigador][investigador])

        print("Profesores Titulares")
        for titular in self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Titular]:
            print(self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Titular][titular])

        print("Profesores Asociados")
        for asociado in self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Asociado]:
            print(self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Asociado][asociado])

        

    def eliminar_estudiante(self, identificador):   #OK

        if identificador not in self.__listado_estudiantes: 
            print("Estudiante No encontrado")   
            return                                                                                                          
        del self.__listado_estudiantes[identificador]                                                                   


    def eliminar_miembro(self, identificador):          #OK

        miembro = self.devolver_miembro(identificador)
        if miembro is None:
            return
        
        del self.__listado_departamentos[miembro.devolverDepartamento()]['Miembros'][miembro.tipo][identificador]

    def eliminar_asignatura(self, codigo_asignatura):       #Ok
        asignatura = self.devolver_asignatura(codigo_asignatura)
        if asignatura is None:
            return
        
        del self.__listado_departamentos[asignatura.devolverDepartamento()]['Asignaturas'][codigo_asignatura]

        for numero_expediente in self.__listado_estudiantes:
            estudiante = self.__listado_estudiantes[numero_expediente]
            if asignatura in estudiante.asignaturas():
                estudiante.desmatricular(asignatura)

        for departamento in self.__listado_departamentos:
            for identificacion in self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Titular]:
                profesor = self.devolver_miembro(identificacion)
                if asignatura in profesor.asignaturas():
                    profesor.asignaturas().remove(asignatura)

            for identificacion in self.__listado_departamentos[departamento]['Miembros'][TipoMiembro.Asociado]:
                profesor = self.devolver_miembro(identificacion)
                if asignatura in profesor.asignaturas():
                    profesor.asignaturas().remove(asignatura)



    def cambiarDepartamento(self, identificador_miembro, nuevo_departamento):       #OK

        miembro = self.devolver_miembro(identificador_miembro)
        if miembro is None:
            return

        if miembro.devolverDepartamento() == nuevo_departamento:
            print("El individuo ya se encuentra en el departamento")
            return
        
        del self.__listado_departamentos[miembro.devolverDepartamento()]["Miembros"][miembro.tipo][identificador_miembro]
        miembro.cambioDepartamento(nuevo_departamento)

        #Incluyo al miembro en el nuevo deparatamento 
        self.__listado_departamentos[nuevo_departamento]["Miembros"][miembro.tipo][identificador_miembro] = miembro         

    

#############################################################ESTÁN BIEN ##############################################################################

    def matricular(self, codigo_asignatura, identificador_estudiante):       #OK
        asignatura = self.devolver_asignatura(codigo_asignatura)
        if asignatura is None: 
            return
        
        estudiante = self.devolver_estudiante(identificador_estudiante)
        if estudiante is None:
            return
        
        estudiante.matricular(asignatura)

    
    def desmatricular(self, codigo_asignatura, identificador_estudiante):       #OK
        asignatura = self.devolver_asignatura(codigo_asignatura)
        if asignatura is None:
            return
        
        estudiante = self.devolver_estudiante(identificador_estudiante)
        if estudiante is None:
            return
        
        if asignatura not in estudiante.asignaturas():
            print("El estudiante seleccionado No está matriculado esa asignatura")
            return
        
        estudiante.desmatricular(asignatura)



    def add_asignatura_profesor(self, codigo_asignatura, identificador_profesor):        #Ok

        asignatura = self.devolver_asignatura(codigo_asignatura)
        if asignatura is None:
            return
        
        profesor = self.devolver_miembro(identificador_profesor)
        if profesor is None:
            return
        
        profesor.add_asignatura(asignatura)
        

    def eliminar_asignatura_profesor(self, codigo_asignatura, identificador_profesor):       #Ok

        asignatura = self.devolver_asignatura(codigo_asignatura)
        if asignatura is None:
            return
        
        profesor = self.devolver_miembro(identificador_profesor)
        if profesor is None:
            return
        
        if asignatura not in profesor.asignaturas():
            print("El profesor seleccionado No imparte esa asignatura")
            return
        
        profesor.eliminar_asignatura(asignatura)


    def cambiarIdentificador(self, identificador, nuevo_identificador):
        miembro = self.devolver_miembro(identificador)
        if miembro is None:
            return
        miembro.ID = nuevo_identificador
        self.eliminar_miembro(identificador)
        self.__listado_departamentos[miembro.devolverDepartamento()]["Miembros"][miembro.tipo][nuevo_identificador] = miembro
    
    def cambiarNumeroExpediente(self, numero_expediente, nuevo_numero_expediente):
        estudiante = self.devolver_estudiante(numero_expediente)
        if estudiante is None:
            return
        
        estudiante.numero_expediente = nuevo_numero_expediente
        self.eliminar_estudiante(numero_expediente)
        self.__listado_estudiantes[nuevo_numero_expediente] = estudiante
        


    def cambiarCodigoAsignatura(self, codigo, codigo_nuevo):
        asignatura = self.devolver_asignatura(codigo)
        if asignatura is None:
            return 
        
        asignatura.codigo_asignatura = codigo_nuevo
        self.eliminar_asignatura(codigo)
        self.__listado_departamentos[asignatura.devolverDepartamento()]['Asignaturas'][codigo_nuevo] = asignatura
def test_incorporar_estudiante():
    universidad = Universidad("Nombre Universidad", "Dirección Universidad")
    sexo = Sexo.Masculino
    universidad.add_estudiante("Nombre Estudiante", "Dirección Estudiante", "12345678A", "123", sexo)
    estudiante = universidad.devolver_estudiante("123")
    assert estudiante is not None
    assert estudiante.nombre == "Nombre Estudiante"

def test_incorporar_profesor():
    universidad = Universidad("Nombre Universidad", "Dirección Universidad")
    sexo = Sexo.Masculino
    tipo = TipoMiembro.Asociado
    departamento = Departamento.DIIC
    universidad.add_profesor("Jorge Larrey", "Calle Olmo", "54328-B", "a-4356", sexo, tipo, departamento)
    profesor = universidad.devolver_miembro("a-4356")
    assert profesor is not None
    assert profesor.nombre == "Jorge Larrey"

def test_incorporar_investigador():
    universidad = Universidad("Nombre Universidad", "Dirección Universidad")
    sexo = Sexo.Masculino
    departamento = Departamento.DIS
    area_investigacion = AreaInvestigacion.InvestigacionOperativa
    universidad.add_investigador("Nombre Investigador", "Dirección Investigador", "55555555X", "789", sexo, departamento, area_investigacion)
    investigador = universidad.devolver_miembro("789")
    assert investigador is not None
    assert investigador.nombre == "Nombre Investigador"

def test_incorporar_asignatura():
    universidad = Universidad("Nombre Universidad", "Dirección Universidad")
    universidad.add_asignatura("Nombre Asignatura", "COD123", 6, "Carrera", 2, Departamento.DIIC)
    asignatura = universidad.devolver_asignatura("COD123")
    assert asignatura is not None
    assert asignatura.nombre == "Nombre Asignatura"

def test_mostrar_asignaturas_departamento(capfd):
    universidad = Universidad("Nombre Universidad", "Dirección Universidad")
    universidad.add_asignatura("Nombre Asignatura", "COD123", 6, "Carrera", 2, Departamento.DIIC)
    universidad.mostrar_asignaturas_departamento(Departamento.DIIC)
    out, _ = capfd.readouterr()
    assert "Nombre Asignatura" in out

def test_matricular():
    universidad = Universidad("Nombre Universidad", "Dirección Universidad")
    universidad.add_estudiante("Nombre Estudiante", "Dirección Estudiante", "12345678A", "123", Sexo.Masculino)
    universidad.add_asignatura("Nombre Asignatura", "COD123", 6, "Carrera", 2, Departamento.DIIC)
    universidad.matricular("COD123", "123")
    estudiante = universidad.devolver_estudiante("123")
    assert len(estudiante.asignaturas()) == 1

def test_desmatricular():
    universidad = Universidad("Nombre Universidad", "Dirección Universidad")
    universidad.add_estudiante("Nombre Estudiante", "Dirección Estudiante", "12345678A", "123", Sexo.Masculino)
    universidad.add_asignatura("Nombre Asignatura", "COD123", 6, "Carrera", 2, Departamento.DIIC)
    universidad.matricular("COD123", "123")
    universidad.desmatricular("COD123", "123")
    estudiante = universidad.devolver_estudiante("123")
    assert len(estudiante.asignaturas()) == 0

def test_vincular_profesor_asignatura():
    universidad = Universidad("Nombre Universidad", "Dirección Universidad")
    universidad.add_profesor("Jorge Larrey", "Calle Olmo", "54328-B", "a-4356", Sexo.Masculino, TipoMiembro.Asociado, Departamento.DIIC)
    universidad.add_asignatura("Nombre Asignatura", "COD123", 6, "Carrera", 2, Departamento.DIIC)
    universidad.add_asignatura_profesor("COD123", "a-4356")
    profesor = universidad.devolver_miembro("a-4356")
    assert len(profesor.asignaturas()) == 1

def test_desvincular_profesor_asignatura():
    universidad = Universidad("Nombre Universidad", "Dirección Universidad")
    universidad.add_profesor("Jorge Larrey", "Calle Olmo", "54328-B", "a-4356", Sexo.Masculino, TipoMiembro.Asociado, Departamento.DIIC)
    universidad.add_asignatura("Nombre Asignatura", "COD123", 6, "Carrera", 2, Departamento.DIIC)
    universidad.add_asignatura_profesor("COD123", "a-4356")
    universidad.eliminar_asignatura_profesor("COD123", "a-4356")
    profesor = universidad.devolver_miembro("a-4356")
    assert len(profesor.asignaturas()) == 0

def test_cambiar_identificador():
    universidad = Universidad("Nombre Universidad", "Dirección Universidad")
    universidad.add_profesor("Jorge Larrey", "Calle Olmo", "54328-B", "a-4356", Sexo.Masculino, TipoMiembro.Asociado, Departamento.DIIC)
    universidad.cambiarIdentificador("a-4356", "nuevo-identificador")
    profesor = universidad.devolver_miembro("nuevo-identificador")
    assert profesor is not None

def test_cambiar_numero_expediente():
    universidad = Universidad("Nombre Universidad", "Dirección Universidad")
    sexo = Sexo.Masculino
    universidad.add_estudiante("Nombre Estudiante", "Dirección Estudiante", "12345678A", "123", sexo)
    universidad.cambiarNumeroExpediente("123", "456")
    estudiante = universidad.devolver_estudiante("456")
    assert estudiante is not None

def test_cambiar_codigo_asignatura():
    universidad = Universidad("Nombre Universidad", "Dirección Universidad")
    universidad.add_asignatura("Nombre Asignatura", "COD123", 6, "Carrera", 2, Departamento.DIIC)
    universidad.cambiarCodigoAsignatura("COD123", "COD456")
    asignatura = universidad.devolver_asignatura("COD456")
    assert asignatura is not None

if __name__ == "__main__":
    e1 = Estudiante('Juan', 'Aurora, 8', '54673', 'e-9987',Sexo.Masculino)
    print(e1)

    p1 = ProfesorTitular('juan', 'Alcala', '44594', 'a-8889',Sexo.Masculino, TipoMiembro.Titular, Departamento.DIS, AreaInvestigacion.Software)
    print(p1)

    u = Universidad('Umu', 'Espinardo 6')

    u.add_estudiante('Maria','Murcia 4','567845','e-33245',Sexo.Femenino)
    u.add_estudiante('Marta', 'Murcia 12', '5644845', 'e-3324879', Sexo.Femenino)
    u.add_estudiante('Juan', 'Calle 34', '5644846', 'e-3324880', Sexo.Masculino)
    u.add_estudiante('Alicia', 'Avenida 56', '5644847', 'e-3324881', Sexo.Femenino)
    u.add_estudiante('Pedro', 'Plaza 78', '5644848', 'e-3324882', Sexo.Masculino)
    u.add_estudiante('Ana', 'Carrera 90', '5644849', 'e-3324883', Sexo.Femenino)
    u.add_estudiante('Luis', 'Paseo 112', '5644850', 'e-3324884', Sexo.Masculino)

    u.add_profesor('Jorge Larrey', 'Calle Olmo', '54328-B', 'a-4356',Sexo.Masculino, TipoMiembro.Asociado, Departamento.DIIC)
    u.add_profesor('Ana Martínez', 'Calle del Bosque', '54321-A', 'a-9876', Sexo.Femenino, TipoMiembro.Titular, Departamento.DIIC, AreaInvestigacion.Software)
    u.add_profesor('Pedro Sánchez', 'Avenida del Rio', '98765-B', 'b-5432', Sexo.Masculino, TipoMiembro.Asociado, Departamento.DIS)
    u.add_profesor('Laura Fernández', 'Calle de la Luna', '13579-C', 'c-2468', Sexo.Femenino, TipoMiembro.Titular, Departamento.DITEC, AreaInvestigacion.AprendizajeProfundo)
    u.add_profesor('Luis Rodríguez', 'Carrera del Sol', '24680-D', 'd-1357', Sexo.Masculino, TipoMiembro.Asociado, Departamento.DIIC)
    u.add_profesor('María García', 'Avenida de las Flores', '98765-E', 'e-8642', Sexo.Femenino, TipoMiembro.Titular, Departamento.DIIC, AreaInvestigacion.ComputacionAltasPrestaciones)
    u.add_profesor('Juan Pérez', 'Calle de los Pinos', '54321-F', 'f-7293', Sexo.Masculino, TipoMiembro.Asociado, Departamento.DITEC)
    u.add_profesor('Sofía Martín', 'Avenida de las Palmeras', '13579-G', 'g-5312', Sexo.Femenino, TipoMiembro.Titular, Departamento.DIS, AreaInvestigacion.InvestigacionOperativa)

    u.add_investigador('Manuel Molina', 'Plaza de la Libertad', '53453-A', 'i-9998653', Sexo.Masculino, Departamento.DITEC, AreaInvestigacion.ComputacionAltasPrestaciones )
    u.add_investigador('Laura González', 'Calle del Sol', '54321-C', 'i-9876543', Sexo.Femenino, Departamento.DIIC, AreaInvestigacion.InvestigacionOperativa)
    u.add_investigador('Carlos Martínez', 'Avenida de las Flores', '98765-D', 'i-1234567', Sexo.Masculino, Departamento.DIS, AreaInvestigacion.Software)
    u.add_investigador('Ana García', 'Calle de los Pinos', '13579-E', 'i-2468101', Sexo.Femenino, Departamento.DITEC, AreaInvestigacion.AprendizajeMaquina)
    u.add_investigador('David Sánchez', 'Avenida de las Palmeras', '98765-F', 'i-987654', Sexo.Masculino, Departamento.DIIC, AreaInvestigacion.AprendizajeProfundo)
    u.add_investigador('María Rodríguez', 'Calle de la Luna', '54321-G', 'i-123456', Sexo.Femenino, Departamento.DIS, AreaInvestigacion.ArquitecturaDeComputadores)
    u.add_investigador('Juan Pérez', 'Calle del Bosque', '13579-H', 'i-246810', Sexo.Masculino, Departamento.DITEC, AreaInvestigacion.ComputacionAltasPrestaciones)
    u.add_investigador('Sofía Martín', 'Avenida del Rio', '98765-I', 'i-9876545', Sexo.Femenino, Departamento.DIIC, AreaInvestigacion.InvestigacionOperativa)
    u.add_investigador('Pedro López', 'Plaza de la Libertad', '54321-J', 'i-1234563', Sexo.Masculino, Departamento.DIS, AreaInvestigacion.Software)
    u.add_investigador('Laura Ruiz', 'Calle de las Rosas', '13579-K', 'i-2468108', Sexo.Femenino, Departamento.DITEC, AreaInvestigacion.AprendizajeMaquina)
    u.add_investigador('Antonio González', 'Avenida de los Olivos', '98765-L', 'i-9876546', Sexo.Masculino, Departamento.DIIC, AreaInvestigacion.AprendizajeProfundo)
    u.add_investigador('María Martínez', 'Calle de las Palmeras', '54321-M', 'i-1234562', Sexo.Femenino, Departamento.DIS, AreaInvestigacion.ArquitecturaDeComputadores)

    u.add_asignatura('Mecánica de Fluidos', '5000001', 6, 'Ing. Mecánica', 2, Departamento.DIIC)
    u.add_asignatura('Termodinámica', '5000002', 6, 'Ing. Mecánica', 2, Departamento.DIIC)
    u.add_asignatura('Electromagnetismo', '5000003', 6, 'Ing. Electrónica', 2,  Departamento.DIIC)
    u.add_asignatura('Programación Avanzada', '5000004', 6, 'Ing. Informática', 3, Departamento.DITEC)
    u.add_asignatura('Diseño de Circuitos', '5000005', 6, 'Ing. Electrónica', 3,  Departamento.DIIC)
    u.add_asignatura('Algoritmos Genéticos', '5000006', 6, 'Ing. Informática', 3,  Departamento.DITEC)
    u.add_asignatura('Diseño de Sistemas', '5000007', 6, 'Ing. de Sistemas', 3, Departamento.DIS)
    u.add_asignatura('Análisis Estructural', '5000008', 6, 'Ing. Civil', 2,  Departamento.DIIC)
    u.add_asignatura('Control de Procesos', '5000009', 6, 'Ing. Química', 3,  Departamento.DIIC)
    u.add_asignatura('Termodinámica', '5000010', 6, 'Ing. Mecánica', 2, Departamento.DIIC)
    u.add_asignatura('Electromagnetismo', '5000011', 6, 'Ing. Electrónica', 2,  Departamento.DIIC)
    u.add_asignatura('Programación Avanzada', '5000012', 6, 'Ing. Informática', 3,  Departamento.DITEC)
    u.add_asignatura('Diseño de Circuitos', '5000013', 6, 'Ing. Electrónica', 3,  Departamento.DIIC)
    u.add_asignatura('Algoritmos Genéticos', '5000014', 6, 'Ing. Informática', 3,  Departamento.DITEC)
    u.add_asignatura('Diseño de Sistemas', '5000015', 6, 'Ing. de Sistemas', 3, Departamento.DIS)
    u.add_asignatura('Análisis Estructural', '5000016', 6, 'Ing. Civil', 2,  Departamento.DIIC)
    u.add_asignatura('Control de Procesos', '5000017', 6, 'Ing. Química', 3,  Departamento.DIIC)

    a = u.devolver_miembro('i-246810')
    print(a)
    u.mostrar_estudiantes()
    print("\n")
    u.mostrar_investigadores()
    print("\n")
    u.mostrar_profesores()
    print("\n")
    u.mostrar_asignaturas_departamento(Departamento.DITEC)
    print("\n")
    u.mostrar_miembros_departamento(Departamento.DIS)
    print("\n")

    