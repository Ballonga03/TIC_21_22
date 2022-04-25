package MiCodigo;

public class ManejaVehiculo {
	public static void main(String[] args) {
		//TODO Auto-generated method stud
		Vehiculo miBarquito;
		coche miCoche;
		CocheElectrico miCochePilas;
		miBarquito=new Vehiculo("Titanic2", "acuatico");
		miCoche=new Coche("Bugatti", "terrestre");
		miCochePilas=new CocheElectrico("Tesla", "terrestre");
		System.out.println("Mi coche es un "+miCochePilas.getIdentificador());
	}
}
