facturado = 0



ventaspinza = 0



ventastenaza = 0



ventasmotosierra = 0



clientemayorfacturacion = 152805212



mayorfacturacion = 152805212



menorcantidadvendida = 152805212



nfacturamenorcantidad = 152805212



porcentajeventaspinza = 0



porcentajeventastenaza = 0



porcentajeventasmotosierra = 0



totalventas = 0



pinza = 0



tenaza = 0



motosierra = 0



maximo=0



minimo=0



nommax=""





nfactura = int(input("Ingrese número de factura: "))



while nfactura <0:



 nfactura = int(input("Ingrese número de factura: "))





while nfactura != 0:



 cantidad_vendida = int(input("Ingrese la cantidad vendida: "))



 while cantidad_vendida < 1:



 cantidad_vendida = int(input("Ingrese la cantidad vendida: "))



 producto = (input("Ingrese el producto vendido (Pinza, Tenaza o Motosierra): ")).upper()



 while producto!="PINZA" and producto!="TENAZA" and producto!="MOTOSIERRA":



 producto = (input("Ingrese el producto vendido (Pinza, Tenaza o Motosierra): ")).upper()



 cliente = (input("Ingrese el nombre del cliente: "))



 if producto == "PINZA": 



 facturado +=500*cantidad_vendida



 ventaspinza += cantidad_vendida



 if producto == "TENAZA":



 facturado += 752*cantidad_vendida



 ventastenaza += cantidad_vendida



 if producto == "MOTOSIERRA":



 facturado +=1360*cantidad_vendida



 ventasmotosierra += cantidad_vendida



 if (maximo==0):



  maximo=facturado

  nommax=cliente





 if(minimo==0):



  minimo=cantidad_vendida

  nfacturamenorcantidad=nfactura





 if (maximo<facturado):



  maximo=facturado

  nommax=cliente



 if (minimo>cantidad_vendida):





  minimo=cantidad_vendida

  nfacturamenorcantidad=nfactura



 totalventas = ventaspinza + ventasmotosierra + ventastenaza



 nfactura = int(input("Ingrese número de factura: "))



 while nfactura <0:



 nfactura = int(input("Ingrese número de factura: "))





if totalventas > 0:



 porcentajeventaspinza = (ventaspinza/totalventas)*100



 porcentajeventastenaza = (ventastenaza/totalventas)*100



 porcentajeventasmotosierra = (ventasmotosierra/totalventas)*100





print (f"Total facturado: $ {facturado}")



print (f"Cantidad vendida de pinzas: {ventaspinza}")



print (f"Cantidad vendida de tenazas: {ventastenaza}")



print (f"Cantidad vendida de motosierras: {ventasmotosierra}")



print (f"El cliente con mayor facturaciòn individual fue: {nommax}")



print (f"El número de factura de menor cantidad vendida fue: {nfacturamenorcantidad}")



print (f"El porcentaje de ventas de pinzas fue de: {porcentajeventaspinza} %")



print (f"El porcentaje de ventas de tenazas fue de: {porcentajeventastenaza} %")



print (f"El porcentaje de ventas de motosierras fue de: {porcentajeventasmotosierra} %")