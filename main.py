from CuentaBancaria import CuentaBancaria

cuenta1 = CuentaBancaria(.05,1000)
cuenta2 = CuentaBancaria(.02,5000)

cuenta1.deposito(10).deposito(20).deposito(40).retiro(600).generar_interés().mostrar_info_cuenta()

cuenta2.deposito(100).deposito(200).deposito(400).retiro(60).generar_interés().mostrar_info_cuenta()

CuentaBancaria.imprimir_cuentas()